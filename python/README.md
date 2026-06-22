# factorial-api-client (Python)

Official Python SDK for the [Factorial API](https://apidoc.factorialhr.com).


## Versioning

The SDK uses standard semver (`MAJOR.MINOR.PATCH`), independent of the Factorial API version date.

| SDK version | Factorial API version |
|-------------|----------------------|
| `1.x.y`     | `2026-04-01`         |

Factorial releases new API versions quarterly (Jan/Apr/Jul/Oct).

See the [Factorial API versioning docs](https://apidoc.factorialhr.com/docs/api-versioning) for details.

## Installation

```bash
pip install factorial-api-client
```

## Quick start

```python
from factorial_api_client import FactorialClient

client = FactorialClient(api_key="YOUR_KEY")

# First page only
result = client.employees.employee.list()
employees = result.data

# Cursor-paginated iterator (sync)
for emp in client.employees.employee.paginate(max_items=100):
    print(emp.full_name)

# Collect all pages into a list
all_employees = client.employees.employee.all()

# Async iterator
import asyncio

async def main():
    async for emp in await client.employees.employee.paginate_async(max_items=100):
        print(emp.full_name)

asyncio.run(main())
```

## Authentication

Pass your API key via `api_key=` or an OAuth2 bearer token via `token=`:

```python
# API key (sent as x-api-key header)
client = FactorialClient(api_key="YOUR_KEY")

# OAuth2 bearer token
client = FactorialClient(token="YOUR_BEARER_TOKEN")
```

### Environment variables

When an argument is omitted, the client falls back to environment variables.
Explicit arguments always take precedence.

| Variable | Maps to | Sent as |
|----------|---------|---------|
| `FACTORIAL_API_KEY` | `api_key` | `x-api-key` header |
| `FACTORIAL_TOKEN` | `token` | `Authorization: Bearer` |
| `FACTORIAL_BASE_URL` | `base_url` | — (defaults to `https://api.factorialhr.com`) |

```python
# No arguments needed — reads FACTORIAL_API_KEY / FACTORIAL_TOKEN / FACTORIAL_BASE_URL
client = FactorialClient()
```

## Error handling

The client fails loudly on non-2xx responses (bad/expired token, wrong base
URL, `4xx`/`5xx`) instead of silently returning `None`. These raise
`UnexpectedStatus`:

```python
from factorial_api_client.generated.errors import UnexpectedStatus

try:
    employees = client.employees.employee.list()
except UnexpectedStatus as e:
    print(e.status_code)  # e.g. 401
    print(e.content)      # raw response body (bytes)
```

## Domain namespaces

The client is organised as `client.{domain}.{resource}.{method}()`.

| Domain | Example |
|--------|---------|
| `employees` | `client.employees.employee.list()` |
| `ats` | `client.ats.application.list()` |
| `attendance` | `client.attendance.shift.list()` |
| `timeoff` | `client.timeoff.leave.list()` |
| `contracts` | `client.contracts.contract_version.list()` |
| `payroll` | `client.payroll.supplement.list()` |
| `documents` | `client.documents.document.list()` |
| `performance` | `client.performance.review_process.list()` |
| ... | 36 domains total |

Available methods per resource: `list`, `get`, `create`, `update`, `delete`,
`paginate`, `paginate_async`, `all`, plus any custom action endpoints.

## Pagination

All list endpoints support cursor-based pagination via `paginate()` / `paginate_async()` / `all()`:

```python
# Stop after 50 items
for emp in client.employees.employee.paginate(max_items=50):
    ...

# Collect everything (use carefully on large datasets)
all_leaves = client.timeoff.leave.all()
```

## Webhooks

Manage subscriptions through the client, and type your handler payloads with the
generated webhook catalog (re-exported from the package root).

```python
from factorial_api_client import (
    FactorialClient,
    AtsApplicationCreateWebhook,
    WEBHOOK_CATALOG,
    WEBHOOK_PAYLOAD_TYPES,
)

client = FactorialClient(api_key="YOUR_KEY")

# Subscribe to an event. The `challenge` is a secret you choose; Factorial echoes
# it back in the `x-factorial-wh-challenge` header on every delivery so you can
# verify the request really came from Factorial.
client.api_public.webhook_subscription.create(body={
    "subscription_type": "ats/application/create",
    "target_url": "https://example.com/webhooks/factorial",
    "company_id": 55,
    "challenge": "a-random-secret-you-generate",
})

# Type a handler directly
def on_application_created(payload: AtsApplicationCreateWebhook) -> None:
    print(payload.id)

# Look up the payload model class for a subscription_type at runtime
model_cls = WEBHOOK_PAYLOAD_TYPES["ats/application/create"]
print(len(WEBHOOK_CATALOG), "webhook events available")
```

Factorial delivers the resource object at the **top level** of the POST body (no
`{type, data}` envelope). A full event→payload reference and an SDK usage guide
for coding agents are available as a skill:

```bash
npx skills add https://github.com/factorialco/factorial-api-sdks --skill factorial-api-sdks
```
