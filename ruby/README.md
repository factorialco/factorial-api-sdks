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

When **no credential is passed at all**, the client falls back to the
`FACTORIAL_API_KEY` / `FACTORIAL_TOKEN` environment variables. Passing any
credential explicitly disables the env fallback entirely, so a leftover
exported variable can never ride along with (or veto) the credential you
actually chose.

### Inspecting a token

Factorial credentials are opaque strings that happen to be JWTs. `F::Api::Token`
decodes one — **without verifying its signature**; verification is the
server's job — so you can read its claims and plan refreshes:

```ruby
token = F::Api::Token.new(ENV["FACTORIAL_TOKEN"])

token.claims                       # => {"exp" => 1767225600, "cid" => "42", ...}
token[:cid]                        # => "42"
token.expires_at                   # => 2026-01-01 00:00:00 UTC
token.expired?                     # => false
token.expiring_soon?(margin: 120)  # => true within 2 minutes of expiry
```

A credential that isn't a decodable JWT is handled gracefully: `claims` is
empty, `expires_at` is `nil`, and `expired?` never reports true — the API
remains the authority on whether it works.

### OAuth (managed token lifecycle)

For OAuth2 integrations, `F::Api::OAuth` covers the whole lifecycle: authorize
URL, code exchange, decoding, proactive and reactive refresh, and rotation:

```ruby
oauth = F::Api::OAuth.new(client_id: "...", client_secret: "...")
# Falls back to FACTORIAL_OAUTH_CLIENT_ID / FACTORIAL_OAUTH_CLIENT_SECRET.

# 1. Send the user to authorize (browser step, by design):
oauth.authorize_url(redirect_uri: "https://myapp.com/callback")

# 2. Exchange the code your callback receives (single-use, ~10 min):
tokens = oauth.exchange_code(params[:code], redirect_uri: "https://myapp.com/callback")

# 3. Wrap the tokens in a self-refreshing session:
session = oauth.session(tokens) do |rotated|
  # Refresh tokens are SINGLE-USE: each refresh invalidates the previous
  # one. Persist the new one here, or the chain breaks.
  save_refresh_token!(rotated.refresh_token)
end

api = F::Api.new(oauth: session)
api.employees_employee.employees_employees_get(true, false) # required params are positional
```

The session checks the access token before every request and refreshes it
when it is within `margin:` seconds of expiry (default 60, configurable via
`oauth.session(tokens, margin: 120)`), judged by the token endpoint's
`expires_in` — so it works even if the access token is not a JWT. Expiry is
only an upper bound (a token can be revoked at any time), so if the API
still rejects the bearer with a 401, the client refreshes reactively and
retries that request once. Token endpoint failures raise `F::Api::OAuthError`,
which carries the HTTP `code` and parsed `body`.

### Bring your own token source

`oauth:` is duck-typed: any object that responds to `access_token` and
returns the bearer string works — the built-in session is just the
batteries-included implementation. This is the composition seam for other
token sources (your own cache or vault, or another Factorial gem's token
client) without coupling them to this gem:

```ruby
class MyTokenSource
  def access_token = fetch_current_token_from_somewhere
end

api = F::Api.new(oauth: MyTokenSource.new)
```

A source that also responds to `refresh_after_reject!(rejected_bearer)` —
returning whether it now holds a different bearer — opts into the built-in
401 refresh-and-retry.

For the common "forward the caller's token" case there is a shortcut:
`access_token:` takes any callable, so one shared client can act on behalf
of whoever is making the current request:

```ruby
api = F::Api.new(access_token: -> { Current.factorial_token })
```

Both forms are consulted on every request — sometimes more than once per
request — so keep them cheap, idempotent, and thread-safe. `token:`,
`oauth:` and `access_token:` are mutually exclusive: each is a different
way of supplying the same `Authorization: Bearer` header.

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
| `F::Api::TeamsTeamApi`         | `api.teams_team`         |
| `F::Api::EmployeesEmployeeApi` | `api.employees_employee` |
| `F::Api::TimeoffLeaveApi`      | `api.timeoff_leave`      |

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

`F::Api.paginate` follows cursors automatically. Give it a block that performs
the list call with the pagination params it hands you; it returns a lazy
`Enumerator`, so pages are only fetched as items are consumed:

```ruby
employees = F::Api.paginate do |page|
  api.employees_employee.employees_employees_get(true, false, query_params: page)
end

employees.each { |employee| puts employee.full_name }
employees.first(10)   # fetches a single page
```

### Collect all into an array

```ruby
# Optional safety caps: limit (page size, max 100) and max_items (total)
pages = F::Api.paginate(limit: 100, max_items: 500) do |page|
  api.employees_employee.employees_employees_get(true, false, query_params: page)
end

all_employees = pages.to_a
```

## Webhooks

Manage subscriptions through the client, and use the generated webhook
catalog to type your handler payloads. Factorial delivers the resource
object **at the top level** of the POST body (no `{type, data}` envelope);
the `challenge` you choose when subscribing is echoed back in the
`x-factorial-wh-challenge` header of every delivery so you can verify the
sender.

```ruby
# Discover events and their payload types
F::Api::WEBHOOK_SUBSCRIPTION_TYPES        # every valid subscription_type
F::Api::WEBHOOK_CATALOG                   # runtime list of every event

# In your receiver: parse the delivered body into a typed model
payload = F::Api::WEBHOOK_PAYLOAD_TYPES
          .fetch('ats/application/create')
          .build_from_hash(JSON.parse(request.body.read))
payload.id

# Or reference payload types directly — one alias per event
payload.is_a?(F::Api::AtsApplicationCreateWebhook)  # => true
```

## Error handling

Non-2xx responses raise `F::Api::ApiError`:

```ruby
begin
  api.teams_team.teams_teams_get
rescue F::Api::ApiError => e
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

Pick your update policy in the `Gemfile`:

```ruby
gem "factorial_api", "~> 2.0"    # stay on this API version, receive every compatible update
gem "factorial_api", "~> 2.1.3"  # fixes only
gem "factorial_api"              # always the newest API version
```

## License

MIT