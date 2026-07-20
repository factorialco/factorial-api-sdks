# Factorial Ruby SDK

Official Ruby client for the [Factorial API](https://apidoc.factorialhr.com).

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

api = F::Api.new(api_key: "YOUR_KEY")

teams = api.teams_team.teams_teams_get
```

## Authentication

The SDK supports both **API keys** and **OAuth2 bearer tokens**:

```ruby
# API key — sent as x-api-key header
api = F::Api.new(api_key: "YOUR_KEY")

# OAuth2 bearer token — sent as Authorization: Bearer
api = F::Api.new(token: "YOUR_BEARER_TOKEN")
```

When an argument is omitted, the client falls back to environment variables:
`FACTORIAL_API_KEY` for the API key, `FACTORIAL_TOKEN` for the token.

## SDK structure

`F::Api` exposes one accessor per API resource, named after the underlying
generated class in snake_case:

| Generated class           | Accessor                 |
|---------------------------|--------------------------|
| `F::TeamsTeamApi`         | `api.teams_team`         |
| `F::EmployeesEmployeeApi` | `api.employees_employee` |
| `F::TimeoffLeaveApi`      | `api.timeoff_leave`      |

The full list is available at runtime via `F::Api::API_CLASSES.keys`. A
detailed per-endpoint reference lives in
[`docs/`](https://github.com/factorialco/factorial-api-sdks/tree/main/ruby/docs).

## Error handling

Non-2xx responses raise `F::ApiError`:

```ruby
begin
  api.teams_team.teams_teams_get
rescue F::ApiError => e
  puts e.code           # e.g. 401
  puts e.response_body
end
```

## Versioning

The gem version follows `MAJOR.MINOR.YEAR.MONTH.DAY.BUILD`:

- `MAJOR.MINOR` — version of the handwritten SDK layer (the `F::Api`
  facade). Bumped manually when the facade changes.
- `YEAR.MONTH.DAY` — date of the OpenAPI spec the client was generated
  from (spec `oas-2026-07-01.yaml` → `2026.7.1`).
- `BUILD` — regeneration counter within the same spec date, starting at 0.

Example: `1.0.2026.7.1.0` is the first build of the 1.0 facade against the
2026-07-01 spec.

## License

MIT