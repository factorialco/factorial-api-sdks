# Development

Maintainer notes for the Ruby SDK. Users: see [README.md](README.md).

## Regenerating the SDK

```bash
ruby scripts/generate_sdk.rb            # uses the latest oas-*.yaml
ruby scripts/generate_sdk.rb oas-2026-08-01.yaml
```

The script normalizes the spec, computes the gem version (bumping the build
counter when regenerating for the same spec date), cleans and regenerates
the client, patches the generated models (see below), re-attaches the
handwritten facade, verifies the gem loads and runs the handwritten facade
specs (`spec/factorial_api/`) against the freshly generated code.

## Why the generated models are patched

The spec marks many fields as required, but the live API returns `null` for
some of them (e.g. `ApiPublicCredential.employee_id` is null for
company-level API keys). The generated attribute writers raise
`ArgumentError: <field> cannot be nil` unconditionally, crashing the
deserialization of valid responses. `scripts/patch_models.rb` rewrites those
guards to tolerate nil; `generate_sdk.rb` runs it after every regeneration.
(The Python SDK post-patches its generated code for the same reason.)

To bump `MAJOR.MINOR`, edit `sdkMajorMinor` in `openapi-ruby-client.yaml`.

## Why the spec is normalized first

The source spec has no operationIds, so the generator derives model file
names from full routes — some exceed the 100-character path limit of the
tar format used by `.gem` packages, breaking `gem build`.
`scripts/normalize_oas.rb` injects short operationIds to keep names under
the limit. Full story in that script's header comment.

## Handwritten vs generated files

Handwritten files are listed in `.openapi-generator-ignore` and survive
regeneration. Everything else under `lib/`, `docs/` and `spec/` is
generated — do not edit it by hand.

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