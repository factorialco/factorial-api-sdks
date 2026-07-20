# Factorial Ruby SDK

Official Ruby client for the [Factorial](https://factorialhr.com) public API.

## Installation

Add it to your `Gemfile`:

```ruby
gem "factorial_api"
```

Or install it directly:

```bash
gem install factorial_api
```

## Quick start

```ruby
require "factorial_api"

api = F::Api.new(api_key: ENV["FACTORIAL_API_KEY"])

teams = api.teams_team.teams_teams_get
```

## Authentication

Pass your API key to `F::Api.new` and it is sent as the `x-api-key` header
on every request. OAuth2 bearer tokens are also supported through the
generated configuration:

```ruby
F.configure do |config|
  config.access_token = "your-oauth2-token"
end
```

## Finding your way around

`F::Api` exposes one accessor per API resource, named after the underlying
generated class in snake_case:

| Generated class        | Accessor               |
|------------------------|------------------------|
| `F::TeamsTeamApi`      | `api.teams_team`       |
| `F::EmployeesEmployeeApi` | `api.employees_employee` |
| `F::TimeoffLeaveApi`   | `api.timeoff_leave`    |

The full list is available at runtime via `F::Api::API_CLASSES.keys`.
A detailed per-endpoint reference lives in the [`docs/`](docs/) directory.

## Versioning

The gem version follows `MAJOR.MINOR.YEAR.MONTH.DAY.BUILD`:

- `MAJOR.MINOR` — version of the handwritten SDK layer (the `F::Api`
  facade). Bumped manually when the facade changes.
- `YEAR.MONTH.DAY` — date of the OpenAPI spec the client was generated
  from (spec `oas-2026-07-01.yaml` → `2026.7.1`).
- `BUILD` — regeneration counter within the same spec date, starting at 0.

Example: `1.0.2026.7.1.0` is the first build of the 1.0 facade against the
2026-07-01 spec.

## For maintainers

To regenerate the SDK from a new OpenAPI spec:

```bash
ruby scripts/generate_sdk.rb            # uses the latest oas-*.yaml
ruby scripts/generate_sdk.rb oas-2026-08-01.yaml
```

The script normalizes the spec (injecting short operationIds), computes the
gem version (bumping the build counter when regenerating for the same spec
date), regenerates the client, re-attaches the handwritten facade and
verifies the gem loads. To bump `MAJOR.MINOR`, edit `sdkMajorMinor` in
`openapi-ruby-client.yaml`.

Handwritten files are listed in `.openapi-generator-ignore` and survive
regeneration. Everything else under `lib/`, `docs/` and `spec/` is
generated — do not edit it by hand.

## License

MIT