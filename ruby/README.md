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

response = api.teams_team.teams_teams_get
response.data.each { |team| puts team.name }
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

### Custom base URL

Point the client at another environment with `base_url:` (a full http(s)
URL). It falls back to the `FACTORIAL_BASE_URL` environment variable and
defaults to `https://api.factorialhr.com`:

```ruby
api = F::Api.new(api_key: "YOUR_KEY", base_url: "http://localhost:3000")
```

## SDK structure

`F::Api` exposes one accessor per API resource, named after the underlying
generated class in snake_case:

| Generated class           | Accessor                 |
|---------------------------|--------------------------|
| `F::TeamsTeamApi`         | `api.teams_team`         |
| `F::EmployeesEmployeeApi` | `api.employees_employee` |
| `F::TimeoffLeaveApi`      | `api.timeoff_leave`      |

The full list is available at runtime via `F::Api::API_CLASSES.keys`. For
the per-endpoint reference, see the
[Factorial API docs](https://apidoc.factorialhr.com).

## Pagination

The Factorial API uses **cursor-based pagination**. Every list endpoint
returns an object with `data` (the items) and `meta` (`has_next_page`,
`end_cursor`, `total`, …). The pagination params (`after_id`, `limit`) are
passed via `query_params:`.

Note: query params the spec marks as *required* are generated as positional
arguments — for employees, `only_active` and `only_managers` below.

### Single page

```ruby
page = api.employees_employee.employees_employees_get(true, false, query_params: { limit: 50 })

# Fetch the next page manually
if page.meta.has_next_page
  next_page = api.employees_employee.employees_employees_get(
    true, false,
    query_params: { limit: 50, after_id: page.meta.end_cursor }
  )
end
```

### Stream all pages (lazy Enumerator)

`F.paginate` follows cursors automatically. Give it a block that performs
the list call with the pagination params it hands you; it returns a lazy
`Enumerator`, so pages are only fetched as items are consumed:

```ruby
employees = F.paginate do |page|
  api.employees_employee.employees_employees_get(true, false, query_params: page)
end

employees.each { |employee| puts employee.full_name }
employees.first(10)   # fetches a single page
```

### Collect all into an array

```ruby
# Optional safety caps: limit (page size, max 100) and max_items (total)
pages = F.paginate(limit: 100, max_items: 500) do |page|
  api.employees_employee.employees_employees_get(true, false, query_params: page)
end

all_employees = pages.to_a
```

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

Standard semver (`MAJOR.MINOR.PATCH`), same model as the TypeScript and
Python SDKs:

- **Major** tracks the Factorial API version — the mapping lives in the
  repo-root
  [`version_map.json`](https://github.com/factorialco/factorial-api-sdks/blob/main/version_map.json)
  (e.g. `2.x.y` targets `2026-07-01`). **A new dated API version is a
  breaking change** and ships as a new major.
- **Minor/patch** — features/fixes of the handwritten SDK layer, always
  backwards compatible within the same major.
- Prereleases are tagged `MAJOR.MINOR.PATCH.beta.N`. Bundler and
  `gem install` ignore them unless you ask for them explicitly.

Pick your update policy in the `Gemfile`:

```ruby
gem "factorial_api", "~> 2.0"    # stay on this API version, receive every compatible update
gem "factorial_api", "~> 2.1.3"  # fixes only
gem "factorial_api"              # always the newest API version
```

## License

MIT