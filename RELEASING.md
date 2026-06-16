# Releasing

Releases are automated with [release-please](https://github.com/googleapis/release-please).
You never create tags or GitHub Releases by hand — that manual step is exactly
what previously let a tag drift from the code it was supposed to point at.

## How it works

1. **You merge PRs to `main` using [Conventional Commits](https://www.conventionalcommits.org/).**
   - `fix: …` → patch bump · `feat: …` → minor bump · `feat!:` / `BREAKING CHANGE:` → major bump.
   - Prefix the commit/PR title with the package scope when it's package-specific,
     e.g. `fix(typescript): …` or `feat(python): …`. release-please attributes a
     commit to a package by the files it touches, so a change under `typescript/`
     bumps the TS package and a change under `python/` bumps the Python one.

2. **release-please opens a "Release PR" per package** (see `.github/workflows/release-please.yaml`).
   Each Release PR bumps the version file and updates that package's `CHANGELOG.md`.
   It keeps updating as more commits land.

3. **You merge the Release PR.** That single action:
   - bumps the version (`typescript/package.json` / `python/pyproject.toml`),
   - creates the tag (`typescript-vX.Y.Z` / `python-vX.Y.Z`) **on the merge commit**,
   - creates the GitHub Release.

   The tag and the version are produced together, so they cannot disagree.

4. **Publishing runs automatically.** "Create release" then calls the reusable
   `publish.yaml` for the released package, checking out the freshly-created tag
   and publishing to npm / PyPI. Each publish step skips if that version is
   already on the registry, so re-runs are safe.

## Config

- `release-please-config.json` — package definitions, release types, tag components.
- `.release-please-manifest.json` — the **last released** version per package
  (release-please reads/writes this; don't hand-edit unless correcting drift).

## Manual / recovery publish

If an automated publish fails, re-run it without touching versions:

> Actions → **Publish packages** → Run workflow → enter the tag
> (e.g. `python-v1.2.0`).

## Notes

- `uv.lock` records the package version too, but the published wheel's version
  comes from `pyproject.toml` (hatchling), so a stale `uv.lock` version line does
  not affect releases. Refresh it with `uv lock` when convenient.
- The `release.ts` / `release.py` scripts remain for **regenerating** the SDK
  from a new OpenAPI spec. With release-please owning versioning and publishing,
  prefer using them only to regenerate code; let release-please cut the release.
- `version_map.json` still maps the SDK major version to the npm dist-tag /
  Factorial API version and is consumed by `publish.yaml`.
