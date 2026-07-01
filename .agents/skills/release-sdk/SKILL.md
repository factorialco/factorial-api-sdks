---
name: release-sdk
description: >-
  Regenerate the Factorial TypeScript and Python SDKs against a new dated API
  version and open the release PR. Use when a new Factorial API version ships
  (e.g. "regenerate the SDKs for 2026-07-01", "release the new API version",
  "cut a new SDK release"). Covers the full pipeline: fetch spec, regenerate,
  validate, version_map, READMEs, and the release-please handoff.
---

# Releasing the Factorial API SDKs

Versioning, tagging, and publishing are owned by **release-please**. Your job is
to regenerate the SDK code from a new OpenAPI spec, wire up the version mapping,
and open a Conventional-Commit PR. Merging that PR makes release-please open the
per-package Release PRs that actually cut the tags and publish to npm / PyPI.

**Never** hand-edit versions (`typescript/package.json`, `python/pyproject.toml`,
`.release-please-manifest.json`), create tags, or run `npm publish` / `uv publish`.
See `RELEASING.md` for the publish machinery.

## The convention: one SDK major per dated API version

Factorial ships dated API versions quarterly (Jan/Apr/Jul/Oct). The repo maps
**each dated API version to its own SDK major**, even when the spec change is
purely additive. This is baked into the release infra:

- `version_map.json` maps `major → API date`, and that date **is** the npm
  dist-tag (`.github/workflows/publish.yaml` reads `versions[major]`).
- `scripts/beta-detect.mjs` computes `nextMajor = latest + 1` when a newer API
  date appears.

So a new API date → new major → new `version_map.json` entry → a `feat!:` PR.
Users pin `@2026-04-01` or `@2026-07-01`.

## Steps

Do everything on a feature branch off the latest `main`. Ask the user before the
PR step (title, reviewers) — that's outward-facing.

### 0. Preflight

```bash
git checkout main && git pull
git checkout -b feat/api-<yyyy-mm-dd>
# spec must be servable (expect 200):
curl -sS -o /dev/null -w "%{http_code}\n" "https://api.factorialhr.com/oas/?version=<yyyy-mm-dd>"
```

Diff the new spec against the current one to know what actually changed (new
webhooks, paths, schemas). Most of the generated churn is just the date prefix
in every URL / filename — that's expected, not a red flag.

### 1. Regenerate TypeScript

```bash
cd typescript
OPENAPI_VERSION=<yyyy-mm-dd> npx tsx scripts/release.ts --no-publish
```

`--no-publish` runs stages 1-3 (openapi-ts → `sdk.ts` → `webhooks.ts` → skill)
but stops before build/publish. It **still bumps `package.json`** — revert it,
release-please owns the version:

```bash
cd .. && git checkout typescript/package.json
```

Validate:

```bash
cd typescript && npx tsc --noEmit && npm run build && cd ..
```

### 2. Regenerate Python

```bash
cd python
export PATH="$HOME/.local/bin:$PATH"   # uv lives here
uv run python scripts/release.py --version <yyyy-mm-dd> --no-publish
cd ..
```

Revert the version bump **and** the stale `uv.lock` version line (harmless per
`RELEASING.md`, but keep the diff clean):

```bash
git checkout python/pyproject.toml
git diff --quiet python/uv.lock || git checkout python/uv.lock
```

Validate:

```bash
cd python && export PATH="$HOME/.local/bin:$PATH"
uv run mypy factorial_api_client/ && uv run ruff check factorial_api_client/ && cd ..
```

Note: `uv run` during mypy may re-touch `uv.lock` — revert it again after.

### 3. Update `version_map.json`

Add the new major → date, keep the old majors, bump `latest`:

```json
{
  "latest": "2",
  "versions": {
    "1": "2026-04-01",
    "2": "2026-07-01"
  }
}
```

This must land in the same PR — `publish.yaml` fails if the new major has no
entry.

### 4. Update the READMEs (hand-maintained, NOT regenerated)

Add a `| \`N.x.y\` | \`<yyyy-mm-dd>\` |` row to the version table in all three:
`README.md`, `typescript/README.md`, `python/README.md`. Also bump the TS install
example in `typescript/README.md` to the new date (it's the new `latest` dist-tag):
`npm install @factorialco/api-client@<yyyy-mm-dd>`. The Python install stays
unpinned (PyPI has no dist-tags).

### 5. Sanity-check the diff

```bash
git status --short | grep -vE "generated/(api|models)/"   # the meaningful files
```

Expect: `sdk.ts`/`client.py`, `webhooks.ts`/`webhooks.py`, `types.gen.ts`,
`version_map.json`, the 3 READMEs, and the skill `reference/`. Confirm new
webhook events / schemas actually appear (e.g. `grep -c subscriptionType:
typescript/src/webhooks.ts`).

### 6. Open the PR

- Title: bare **`feat!:`** (no scope) so BOTH packages bump major together.
  A change confined to one package would use a scope (`feat(typescript):`), but
  a regen touches both.
- There is no PR-level CI — the local `tsc`/`build`/`mypy`/`ruff` above is the gate.
- Follow the user's PR conventions (Factorial template, ask for reviewers). If
  `CODEOWNERS` is absent, no reviewer is auto-requested — offer to add one.

Merging the PR → release-please opens two Release PRs (bumping to the new major)
→ merging those cuts tags + publishes. You do not publish anything by hand.

## Gotchas

- The `release.ts` / `release.py` scripts can publish, but with release-please
  owning releases you only ever use them with `--no-publish` to regenerate.
- The webhook generators are count-agnostic (they validate that payload types
  exist and aliases are unique, not a fixed 127/33 total) — a new event just
  works. CLAUDE.md's "guards the known totals" wording is stale.
- Non-breaking API changes still get a **major** bump here — the major tracks the
  API date, not semver breaking-ness. This is intentional (see the convention above).
- READMEs and `version_map.json` are the only hand-edited files; everything under
  `generated/`, plus `sdk.ts`/`client.py`/`webhooks.*` and the skill `reference/`,
  is generated — never edit by hand.
