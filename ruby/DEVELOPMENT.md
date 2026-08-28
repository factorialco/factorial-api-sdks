# Development

Maintainer notes for the Ruby SDK. Users: see [README.md](README.md).

## Regenerating the SDK

```bash
bundle exec rake generate                             # latest spec
bundle exec rake generate VERSION=2026-10-01          # a dated API version
bundle exec rake generate SPEC=path/to/oas.yaml       # local spec file (offline dev)
bundle exec rake generate SET_VERSION=2.1.0           # pin an exact version
# (equivalent: ruby scripts/generate_sdk.rb [spec] [--version=...] [--set-version=...])
```

The spec is fetched from `https://api.factorialhr.com/oas/?version=<date>`
(unversioned = latest) and is **never committed** — downloads land in
gitignored `oas-<date>.yaml` files. Override the source with
`OPENAPI_SPEC_URL` (e.g. `https://api.local.factorial.dev/oas/` to generate
against a local instance), same contract as the TypeScript and Python SDKs.

### Versioning

**release-please owns the version** (same model as the TypeScript and Python
SDKs): it maintains `lib/factorial_api/version.rb` from Conventional Commits,
and the major tracks the Factorial API version (mapped in the repo-root
`version_map.json`). Regenerating never bumps — the pipeline reuses whatever
version.rb says, so there is nothing to revert afterwards. `SET_VERSION` pins
an exact version (reserved for prerelease automation; Ruby has no beta
publishing workflow yet).

The script normalizes the spec, cleans and
regenerates the client, patches the generated models (see below),
regenerates the typed webhook catalog (`lib/factorial_api/webhooks.rb`,
emitted by `scripts/generate_webhooks.rb` from the raw spec's `webhooks`
section), re-attaches the handwritten facade, re-emits the ergonomic layer
(`lib/factorial_api/sdk.rb`, by `scripts/generate_sdk_layer.rb` from the
endpoint table it shares with `scripts/skill_methods.rb` — pass `--dry-run`
to inspect that table), verifies the gem loads, refreshes the skill
reference tables and runs the handwritten facade specs
(`spec/factorial_api/`) against the freshly generated code.

## Why the generated models are patched

The spec marks many fields as required, but the live API returns `null` for
some of them (e.g. `ApiPublicCredential.employee_id` is null for
company-level API keys). The generated attribute writers raise
`ArgumentError: <field> cannot be nil` unconditionally, crashing the
deserialization of valid responses. `scripts/patch_models.rb` rewrites those
guards to tolerate nil; `generate_sdk.rb` runs it after every regeneration.
(The Python SDK post-patches its generated code for the same reason.)

## Why the spec is normalized first

The source spec has no operationIds, so the generator derives model file
names from full routes — some exceed the 100-character path limit of the
tar format used by `.gem` packages, breaking `gem build`.
`scripts/normalize_oas.rb` injects short operationIds to keep names under
the limit. Full story in that script's header comment.

## Handwritten vs generated files

Handwritten files are listed in `.openapi-generator-ignore` and survive
regeneration. Everything else under `lib/` and `spec/` is generated — do
not edit it by hand. The generator's per-class markdown docs are disabled
(`globalProperties` in `openapi-ruby-client.yaml`): they are not shipped in
the gem, and rubydoc.info renders docs from the YARD comments once the gem
is published.

The facade specs live in `spec/factorial_api/` (outside the regenerated
`spec/api/` and `spec/models/` trees). Run them alone with:

```bash
bundle exec rspec spec/factorial_api
```

## Verifying auth and tokens manually

Three dev scripts cover the full cycle (none are shipped in the gem):

```bash
# 1. Obtain an OAuth access token (guides you through the authorization
#    code flow; also supports --refresh REFRESH_TOKEN to renew)
FACTORIAL_OAUTH_CLIENT_ID=... FACTORIAL_OAUTH_CLIENT_SECRET=... \
FACTORIAL_BASE_URL=... bundle exec ruby scripts/oauth_token.rb

# 2. Verify authentication: asserts the exact auth headers sent on the
#    wire (offline), then checks real credentials against the API if
#    FACTORIAL_API_KEY / FACTORIAL_TOKEN are set
bundle exec ruby scripts/test_auth.rb

# 3. Smoke test the SDK against the live API
FACTORIAL_API_KEY=your_key bundle exec ruby scripts/test_api.rb
```