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
   - bumps the version (`typescript/package.json` / `python/pyproject.toml` /
     `ruby/lib/factorial_api/version.rb`),
   - creates the tag (`typescript-vX.Y.Z` / `python-vX.Y.Z` / `ruby-vX.Y.Z`)
     **on the merge commit**,
   - creates the GitHub Release.

   The tag and the version are produced together, so they cannot disagree.

4. **Publishing runs automatically.** "Create release" then calls the reusable
   `publish.yaml` for the released package, checking out the freshly-created tag
   and publishing to npm / PyPI / RubyGems. Each publish step skips if that version is
   already on the registry, so re-runs are safe.

## Config

- `release-please-config.json` — package definitions, release types, tag components.
- `.release-please-manifest.json` — the **last released** version per package
  (release-please reads/writes this; don't hand-edit unless correcting drift).

## Backporting fixes to previous majors

Each SDK major tracks a dated Factorial API version (`version_map.json`), so
previous majors stay supported. Patch releases for them use release-please's
maintenance branches: the workflow also runs on `N.x` branches
(`.github/workflows/release-please.yaml`), and release-please reads the config
and manifest from the branch it runs on, so each branch carries its own
version state.

To ship e.g. `python 1.3.1`:

1. **Create the maintenance branch once** (skip if it exists), at the commit
   of the last 1.x tag:

   ```bash
   git branch 1.x python-v1.3.0   # or typescript-v1.3.0 — same commit line
   git push origin 1.x
   ```

2. **Backport the fix via a PR into `1.x`** with a conventional-commit title
   (`fix: …`, or `fix(python): …` if package-specific) and squash-merge it.
   The same title/path rules as `main` apply.

3. **release-please does the rest**: it opens a Release PR against `1.x`;
   merging it bumps the version, creates the `python-v1.3.1` tag and GitHub
   Release, and publishes. The npm package keeps its dated API-version
   dist-tag from `version_map.json`; `latest` stays on the newest major.

**Caveat: don't cherry-pick generated files blindly.** `python/factorial_api_client/client.py`,
`typescript/src/sdk.ts`, `webhooks.*` and `generated/` are produced from the
spec of *that* major's API version. If the fix touches a generator, apply the
generator change on `1.x` and re-run the stage-2/3 generators there
(`npm run generate-sdk`, `python scripts/generate_python_sdk.py`, …) so the
output matches the 1.x spec.

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
