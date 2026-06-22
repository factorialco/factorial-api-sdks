#!/usr/bin/env python3
"""Generator for the factorial-api-sdks skill reference/ content.

Reads the OpenAPI spec and writes the generated, refreshable parts of
skills/factorial-api-sdks/reference/:

  - webhooks.md      — every webhook event, its subscription_type, and payload fields
  - sdk-methods.md   — every REST endpoint grouped by namespace, with the TS SDK call

These are SDK-specific lookup tables that don't exist elsewhere. The skill does
NOT vendor copies of the public human-oriented docs — those live (and stay
current) at https://apidoc.factorialhr.com; SKILL.md links to them directly.

SKILL.md itself is hand-written and is NOT touched by this script.

Run manually (spec source optional — pass a path/URL or set OPENAPI_SPEC_URL;
defaults to the unversioned endpoint, which serves the latest spec)::

    python scripts/generate_skill.py [specPathOrUrl]

Wired into both release pipelines (typescript/scripts/release.ts and
python/scripts/release.py) so the skill stays in sync with each release.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = REPO_ROOT / "skills" / "factorial-api-sdks"
REFERENCE_DIR = SKILL_DIR / "reference"

DOCS_BASE = "https://apidoc.factorialhr.com"

# No version is pinned in code. Pass a spec path/URL or set OPENAPI_SPEC_URL; if
# neither is given, fall back to the unversioned endpoint, which serves latest.
LATEST_SPEC_URL = "https://api.factorialhr.com/oas"


# ── helpers ──────────────────────────────────────────────────────────────────


def fetch(url: str) -> str:
    # The docs host rejects the default urllib user-agent with a 403.
    req = urllib.request.Request(url, headers={"User-Agent": "factorial-api-sdks-skill-generator"})
    with urllib.request.urlopen(req) as resp:  # noqa: S310 - trusted Factorial host
        return resp.read().decode("utf-8")


def load_spec(arg: str | None) -> dict:
    src = arg or os.environ.get("OPENAPI_SPEC_URL") or LATEST_SPEC_URL
    print(f"Loading OpenAPI spec from {src}")
    if re.match(r"^https?://", src):
        spec = json.loads(fetch(src))
    else:
        spec = json.loads(Path(src).read_text())
    print(f"Spec version: {spec.get('info', {}).get('version', '<unknown>')}")
    return spec


def camel(snake: str) -> str:
    parts = [p for p in snake.split("_") if p]
    if not parts:
        return snake
    return parts[0] + "".join(p[:1].upper() + p[1:] for p in parts[1:])


def resolve_ref(spec: dict, ref: str) -> dict:
    node: object = spec
    for seg in ref.lstrip("#/").split("/"):
        node = node[seg]  # type: ignore[index]
    return node  # type: ignore[return-value]


def render_type(spec: dict, prop: dict) -> str:
    """Render a property schema as a short human-readable type string."""
    if "$ref" in prop:
        return prop["$ref"].split("/")[-1]
    for combiner in ("anyOf", "oneOf", "allOf"):
        if combiner in prop:
            subs = [render_type(spec, s) for s in prop[combiner] if s.get("type") != "null"]
            nullable = any(s.get("type") == "null" for s in prop[combiner])
            joined = " | ".join(dict.fromkeys(subs)) or "object"
            return f"{joined} | null" if nullable else joined
    t = prop.get("type")
    if isinstance(t, list):
        return " | ".join(t)
    if t == "array":
        items = prop.get("items", {})
        return f"array<{render_type(spec, items)}>"
    if t:
        fmt = prop.get("format")
        return f"{t} ({fmt})" if fmt else t
    return "object"


def md_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


# ── webhooks.md ────────────────────────────────────────────────────────────────


def gen_webhooks(spec: dict) -> str:
    webhooks = spec.get("webhooks", {})
    schemas = spec.get("components", {}).get("schemas", {})

    # Parse events grouped by namespace; collect the payload schemas in use.
    by_ns: dict[str, list[dict]] = {}
    used_schemas: dict[str, None] = {}
    for key, item in webhooks.items():
        post = item["post"]
        stype = re.search(r"`([^`]+)`", post.get("description", "")).group(1)
        ref = post["requestBody"]["content"]["application/json"]["schema"]["$ref"]
        schema_name = ref.split("/")[-1]
        used_schemas[schema_name] = None
        _, ns, resource, event = ([s.strip() for s in key.split(">")] + ["", "", "", ""])[:4]
        by_ns.setdefault(ns, []).append(
            {
                "subscription_type": stype,
                "summary": post.get("summary", key),
                "event": event,
                "resource": resource,
                "schema": schema_name,
            }
        )

    total = sum(len(v) for v in by_ns.values())
    out: list[str] = []
    out.append("# Factorial webhook events\n")
    out.append(
        "Auto-generated from the OpenAPI spec. "
        f"{total} events across {len(by_ns)} namespaces, "
        f"{len(used_schemas)} distinct payload schemas.\n"
    )
    out.append(
        "Factorial POSTs the payload (the resource object) to your `target_url` at the "
        "**top level** — it is not wrapped in a `{ type, data }` envelope. Subscribe with "
        "the `subscription_type` value shown below. See `../SKILL.md` for delivery, "
        "verification, and retry details.\n"
    )

    out.append("## Events by namespace\n")
    for ns in sorted(by_ns):
        out.append(f"### {ns}\n")
        out.append("| subscription_type | event | payload schema | summary |")
        out.append("| --- | --- | --- | --- |")
        for e in sorted(by_ns[ns], key=lambda x: x["subscription_type"]):
            out.append(
                # GitHub heading anchors lowercase and keep underscores; the schema
                # name is already lowercase with no spaces, so the anchor == the name.
                f"| `{e['subscription_type']}` | {md_escape(e['event'])} "
                f"| [`{e['schema']}`](#{e['schema']}) "
                f"| {md_escape(e['summary'])} |"
            )
        out.append("")

    out.append("## Payload schemas\n")
    out.append(
        "Top-level fields of each payload. Nested object types reference other schemas "
        "by name; see the [full OpenAPI reference]"
        f"({DOCS_BASE}/reference) for their fields.\n"
    )
    for name in sorted(used_schemas):
        schema = schemas.get(name, {})
        out.append(f"### {name}\n")
        desc = schema.get("description")
        if desc:
            out.append(f"{md_escape(desc)}\n")
        props = schema.get("properties", {})
        required = set(schema.get("required", []))
        if not props:
            out.append("_No documented properties._\n")
            continue
        out.append("| field | type | required | description |")
        out.append("| --- | --- | --- | --- |")
        for fname, prop in props.items():
            out.append(
                f"| `{fname}` | {md_escape(render_type(spec, prop))} "
                f"| {'yes' if fname in required else 'no'} "
                f"| {md_escape(prop.get('description', ''))} |"
            )
        out.append("")

    return "\n".join(out)


# ── sdk-methods.md ──────────────────────────────────────────────────────────────


def derive_method(http: str, rest_segments: list[str]) -> str:
    """Best-effort SDK method name from the HTTP verb and trailing path segments."""
    action_segs = [s for s in rest_segments if not (s.startswith("{") and s.endswith("}"))]
    has_id = any(s.startswith("{") and s.endswith("}") for s in rest_segments)
    if action_segs:
        return camel("_".join(action_segs))
    if http == "get":
        return "get(id)" if has_id else "list()"
    if http == "post":
        return "create(body)"
    if http in ("put", "patch"):
        return "update(id, body)" if has_id else "update(body)"
    if http == "delete":
        return "delete(id)" if has_id else "delete()"
    return http


def gen_sdk_methods(spec: dict) -> str:
    paths = spec.get("paths", {})
    by_ns: dict[str, list[dict]] = {}
    for path, ops in paths.items():
        # /api/<version>/resources/<namespace>/<resource>/<rest...>
        segs = [s for s in path.split("/") if s]
        if "resources" not in segs:
            continue
        i = segs.index("resources")
        rest = segs[i + 1 :]
        if len(rest) < 2:
            continue
        namespace, resource, *tail = rest
        for http, op in ops.items():
            if http not in ("get", "post", "put", "patch", "delete"):
                continue
            method = derive_method(http, tail)
            by_ns.setdefault(namespace, []).append(
                {
                    "resource": resource,
                    "call": f"client.{camel(namespace)}.{camel(resource)}.{method}",
                    "http": http.upper(),
                    "path": path,
                    "summary": op.get("summary", ""),
                }
            )

    total = sum(len(v) for v in by_ns.values())
    out: list[str] = []
    out.append("# Factorial API endpoints → SDK calls\n")
    out.append(
        f"Auto-generated from the OpenAPI spec. {total} endpoints across "
        f"{len(by_ns)} namespaces.\n"
    )
    out.append(
        "The SDK call column shows the **TypeScript** accessor "
        "(`client.<namespace>.<resource>.<method>`). The Python SDK uses the same "
        "namespaces/resources in `snake_case` (and `collect_all()` instead of `all()`). "
        "`id`/`body` args are illustrative; see the [online reference]"
        f"({DOCS_BASE}/reference) for exact request shapes.\n"
    )
    for ns in sorted(by_ns):
        out.append(f"## {ns}\n")
        out.append("| SDK call | HTTP | path | summary |")
        out.append("| --- | --- | --- | --- |")
        for e in sorted(by_ns[ns], key=lambda x: (x["resource"], x["path"], x["http"])):
            out.append(
                f"| `{e['call']}` | {e['http']} | `{e['path']}` | {md_escape(e['summary'])} |"
            )
        out.append("")
    return "\n".join(out)


# ── main ───────────────────────────────────────────────────────────────────────


def main() -> None:
    spec = load_spec(sys.argv[1] if len(sys.argv) > 1 else None)
    REFERENCE_DIR.mkdir(parents=True, exist_ok=True)

    (REFERENCE_DIR / "webhooks.md").write_text(gen_webhooks(spec))
    print("  Wrote reference/webhooks.md")

    (REFERENCE_DIR / "sdk-methods.md").write_text(gen_sdk_methods(spec))
    print("  Wrote reference/sdk-methods.md")


if __name__ == "__main__":
    main()
