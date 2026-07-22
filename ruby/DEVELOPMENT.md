# Development

Maintainer notes for the Ruby SDK. Users: see [README.md](README.md).

## Regenerating the SDK

```bash
ruby scripts/generate_sdk.rb            # uses the latest oas-*.yaml
ruby scripts/generate_sdk.rb oas-2026-08-01.yaml
```

The script normalizes the spec, computes the gem version (bumping the build
counter when regenerating for the same spec date), cleans and regenerates
the client, re-attaches the handwritten facade, verifies the gem loads and
runs the handwritten facade specs (`spec/factorial_api/`) against the
freshly generated code.

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

## Smoke test against the live API

```bash
FACTORIAL_API_KEY=your_key bundle exec ruby scripts/test_api.rb
```