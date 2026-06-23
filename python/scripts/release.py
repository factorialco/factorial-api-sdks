#!/usr/bin/env python3
"""
release.py — Factorial Python SDK release script.

Steps:
  0. Prompt for the API version date (yyyy-mm-dd) to generate.
  1. Fetch the OpenAPI spec from https://api.factorialhr.com/oas/?version=<date>
     (or use --spec-path for a local file).
  2. Patch invalid `type: "unknown"` fields to `type: "string"`.
  3. Bump SDK semver (--bump major|minor|patch, default: patch).
  4. Regenerate the generated layer:
       - openapi-python-client generate → factorial_api_client/generated/
       - Re-run scripts/generate_python_sdk.py → factorial_api_client/client.py
  5. Bump version in pyproject.toml.
  6. Build and publish: uv build && uv publish (requires PyPI token in env).

Usage:
    uv run python scripts/release.py [--dry-run] [--version yyyy-mm-dd] [--spec-path PATH] [--bump major|minor|patch]

    --bump defaults to patch. Use minor for new API features, major for breaking changes.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PYTHON_DIR = Path(__file__).resolve().parent.parent
PYPROJECT_PATH = PYTHON_DIR / "pyproject.toml"
GENERATED_DIR = PYTHON_DIR / "factorial_api_client" / "generated"
GENERATE_SCRIPT = Path(__file__).resolve().parent / "generate_python_sdk.py"


# ── helpers ──────────────────────────────────────────────────────────────────

def run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    print(f"  $ {' '.join(cmd)}")
    result = subprocess.run(cmd, check=True, **kwargs)
    return result


def fetch_spec(spec_path: str | None, spec_url: str) -> dict:
    if spec_path:
        print(f"Loading spec from {spec_path}")
        with open(spec_path) as f:
            return json.load(f)
    print(f"Fetching spec from {spec_url}")
    req = urllib.request.Request(spec_url, headers={"User-Agent": "factorial-sdk-release/1.0"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def patch_spec(spec: dict) -> dict:
    """Replace all type: 'unknown' with type: 'string' recursively."""
    def _fix(obj):
        if isinstance(obj, dict):
            if obj.get("type") == "unknown":
                obj["type"] = "string"
            for v in obj.values():
                _fix(v)
        elif isinstance(obj, list):
            for item in obj:
                _fix(item)
    import copy
    spec = copy.deepcopy(spec)
    _fix(spec)
    return spec


def get_current_version() -> str:
    content = PYPROJECT_PATH.read_text()
    m = re.search(r'^version\s*=\s*"([^"]+)"', content, re.MULTILINE)
    if not m:
        raise ValueError("Could not find version in pyproject.toml")
    return m.group(1)


def bump_version(current: str, bump: str) -> str:
    parts = [int(x) for x in current.split(".")]
    if bump == "major":
        parts = [parts[0] + 1, 0, 0]
    elif bump == "minor":
        parts = [parts[0], parts[1] + 1, 0]
    else:  # patch
        parts = [parts[0], parts[1], parts[2] + 1]
    return ".".join(str(p) for p in parts)


def _patch_enum_none_safety(models_dir: Path) -> None:
    """
    The Factorial API returns null for many enum fields that the spec declares as
    non-nullable. Patch all generated model from_dict methods so that enum
    constructor calls like SomeEnum(value) become SomeEnum(value) if value is not None else None.
    """
    import re as _re

    # Collect all enum class names from the models directory
    enum_classes: set[str] = set()
    for fpath in models_dir.glob("*.py"):
        content = fpath.read_text()
        for m in _re.finditer(r"class (\w+)\(str, Enum\)", content):
            enum_classes.add(m.group(1))

    patched_files = 0
    for fpath in models_dir.glob("*.py"):
        content = fpath.read_text()
        original = content
        for enum_cls in enum_classes:
            pattern = rf"({_re.escape(enum_cls)})\((\w+)\)"
            def _repl(m: _re.Match) -> str:
                cls_name, var_name = m.group(1), m.group(2)
                return f"{cls_name}({var_name}) if {var_name} is not None else None"
            content = _re.sub(pattern, _repl, content)
        if content != original:
            fpath.write_text(content)
            patched_files += 1

    print(f"  Patched {patched_files} model files for enum None-safety")


def _patch_raise_on_unexpected_status(client_py: Path) -> None:
    """
    The stage-2 generator builds the AuthenticatedClient without
    raise_on_unexpected_status, which defaults to False. That makes the
    generated sync/asyncio helpers return None on any undocumented status
    (bad/expired token, wrong base URL, server errors) — the SDK fails
    silently. Inject raise_on_unexpected_status=True so it fails loudly.
    """
    if not client_py.exists():
        print(f"  WARNING: {client_py} not found — skipping raise_on_unexpected_status patch")
        return

    content = client_py.read_text()
    if "raise_on_unexpected_status=True" in content:
        print("  client.py already raises on unexpected status — nothing to patch")
        return

    patched = content.replace(
        '            auth_header_name="x-api-key",\n        )',
        '            auth_header_name="x-api-key",\n'
        '            raise_on_unexpected_status=True,\n        )',
        1,
    )
    if patched == content:
        print("  WARNING: could not locate AuthenticatedClient(...) call to patch")
        return

    client_py.write_text(patched)
    print("  Patched client.py to raise on unexpected status")


def _patch_env_var_support(client_py: Path) -> None:
    """
    The stage-2 generator builds FactorialClient.__init__ to read credentials
    only from its arguments. Patch it so that, when an argument is omitted, the
    client falls back to environment variables — FACTORIAL_API_KEY,
    FACTORIAL_TOKEN and FACTORIAL_BASE_URL — so consumers don't have to
    wire them up by hand. Explicit arguments still take precedence.
    """
    if not client_py.exists():
        print(f"  WARNING: {client_py} not found — skipping env var patch")
        return

    content = client_py.read_text()
    if 'os.environ.get("FACTORIAL_API_KEY")' in content:
        print("  client.py already reads env vars — nothing to patch")
        return

    original = content

    # Ensure `import os` is present (placed just above the typing import).
    if "\nimport os\n" not in content:
        content = content.replace(
            "\nfrom typing import Any, List\n",
            "\nimport os\nfrom typing import Any, List\n",
            1,
        )

    # Make base_url optional and add the env-var fallbacks + clearer error.
    content = content.replace(
        '        base_url: str = "https://api.factorialhr.com",\n'
        "    ) -> None:\n"
        "        auth_token = api_key or token\n"
        "        if not auth_token:\n"
        '            raise ValueError("Provide api_key or token")',
        "        base_url: str | None = None,\n"
        "    ) -> None:\n"
        '        api_key = api_key or os.environ.get("FACTORIAL_API_KEY")\n'
        '        token = token or os.environ.get("FACTORIAL_TOKEN")\n'
        '        base_url = base_url or os.environ.get("FACTORIAL_BASE_URL") or "https://api.factorialhr.com"\n'
        "        auth_token = api_key or token\n"
        "        if not auth_token:\n"
        "            raise ValueError(\n"
        '                "Provide api_key or token (or set FACTORIAL_API_KEY / FACTORIAL_TOKEN)"\n'
        "            )",
        1,
    )

    if content == original:
        print("  WARNING: could not locate FactorialClient.__init__ to patch for env vars")
        return

    client_py.write_text(content)
    print("  Patched client.py to read credentials from environment variables")


def set_version(new_version: str) -> None:
    content = PYPROJECT_PATH.read_text()
    content = re.sub(
        r'^(version\s*=\s*)"[^"]+"',
        f'\\1"{new_version}"',
        content,
        flags=re.MULTILINE,
    )
    PYPROJECT_PATH.write_text(content)


def determine_bump(forced: str | None) -> str:
    # Kept for potential future use; not called in normal flow
    return forced or "minor"


# ── main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Release the Factorial Python SDK")
    parser.add_argument("--dry-run", action="store_true", help="Skip publish and file writes")
    parser.add_argument("--version", help="API version date to generate (yyyy-mm-dd)")
    parser.add_argument("--spec-path", help="Local spec file instead of fetching")
    parser.add_argument("--bump", choices=["major", "minor", "patch"], default="patch",
                        help="Semver bump type (default: patch)")
    # CI/beta mode (used by the daily beta-publish workflow):
    parser.add_argument("--set-version",
                        help="Use this exact version instead of bumping semver "
                             "(e.g. a prerelease like 2.0.0b2026070100)")
    parser.add_argument("--no-publish", action="store_true",
                        help="Regenerate + write the version, then stop (no build, "
                             "no publish, no prompt). CI publishes separately.")
    args = parser.parse_args()

    print("=== Factorial Python SDK Release ===\n")

    # 0. Prompt for API version
    api_version = args.version or os.environ.get("OPENAPI_VERSION", "")
    if not api_version:
        api_version = input("Enter the API version to generate (yyyy-mm-dd): ").strip()

    import re as _re
    if not _re.fullmatch(r"\d{4}-\d{2}-\d{2}", api_version):
        print(f'Error: Invalid version format "{api_version}". Expected yyyy-mm-dd.', file=sys.stderr)
        sys.exit(1)

    spec_url = os.environ.get("OPENAPI_SPEC_URL", f"https://api.factorialhr.com/oas/?version={api_version}")

    # 1. Fetch spec
    print("Step 1: Fetch spec")
    new_spec = fetch_spec(args.spec_path, spec_url)

    # 2. Patch
    print("Step 2: Patch spec (type: unknown → string)")
    patched_spec = patch_spec(new_spec)

    # 3. Bump SDK semver (or use an explicit --set-version)
    print("Step 3: Bump SDK version")
    current_version = get_current_version()
    if args.set_version:
        new_version = args.set_version
        print(f"  Version: {current_version} → {new_version}  (explicit --set-version)")
    else:
        new_version = bump_version(current_version, args.bump)
        print(f"  Version: {current_version} → {new_version}  ({args.bump} bump)")

    if args.dry_run:
        print("\n[DRY RUN] Stopping before making changes.")
        return

    # 4. Regenerate    print("\nStep 4: Regenerate SDK")
    with tempfile.NamedTemporaryFile(suffix=".json", mode="w", delete=False) as tf:
        json.dump(patched_spec, tf)
        patched_path = tf.name

    try:
        run(
            [
                "uv", "run", "openapi-python-client", "generate",
                "--path", patched_path,
                "--config", str(PYTHON_DIR / "openapi-python-client.yaml"),
                "--output-path", str(GENERATED_DIR),
                "--overwrite",
                "--meta", "none",
            ],
            cwd=PYTHON_DIR,
        )
    finally:
        os.unlink(patched_path)

    # Post-generation patches to fix spec inaccuracies
    print("  Post-processing generated models...")
    _patch_enum_none_safety(GENERATED_DIR / "models")

    if GENERATE_SCRIPT.exists():
        run(["python3", str(GENERATE_SCRIPT)])
    else:
        print(f"  WARNING: {GENERATE_SCRIPT} not found — skipping client.py regeneration")

    # Stage 3: regenerate the typed webhook catalog (factorial_api_client/webhooks.py)
    # and refresh the factorial-api-sdks skill reference content.
    print("  Regenerating webhooks.py and the factorial-api-sdks skill...")
    with tempfile.NamedTemporaryFile(suffix=".json", mode="w", delete=False) as wf:
        json.dump(patched_spec, wf)
        webhook_spec_path = wf.name
    try:
        run(["python3", str(PYTHON_DIR / "scripts" / "generate_webhooks.py"), webhook_spec_path])
        run(["python3", str(REPO_ROOT / "scripts" / "generate_skill.py"), webhook_spec_path])
    finally:
        os.unlink(webhook_spec_path)

    # Make the high-level client fail loudly on undocumented HTTP statuses.
    _patch_raise_on_unexpected_status(PYTHON_DIR / "factorial_api_client" / "client.py")

    # Let the high-level client read credentials from environment variables.
    _patch_env_var_support(PYTHON_DIR / "factorial_api_client" / "client.py")

    # 5. Bump version
    print(f"\nStep 5: Bump version to {new_version}")
    set_version(new_version)

    if args.no_publish:
        print(f"\n⏭  --no-publish: regenerated and set version to {new_version}; "
              "stopping before build/publish.")
        return

    # 6. Build & publish
    print("\nStep 6: Build and publish")
    run(["uv", "build"], cwd=PYTHON_DIR)

    answer = input(f"Publish factorial-api-client {new_version} to PyPI? [y/N] ").strip().lower()
    if answer == "y":
        run(["uv", "publish"], cwd=PYTHON_DIR)
        print(f"\n✓ Released factorial-api-client {new_version}")
    else:
        print(f"\n⏭  Skipped publish. Package built and version bumped to {new_version}.")


if __name__ == "__main__":
    main()
