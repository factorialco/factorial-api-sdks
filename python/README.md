# factorial-api-client (Python)

Official Python SDK for the [Factorial API](https://apidoc.factorialhr.com).

Auto-generated from the OpenAPI spec with a hand-written `FactorialClient` wrapper
providing clean domain-namespaced access, cursor pagination helpers, and both sync
and async support.

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

## API version & versioning

SDK versions mirror the Factorial API version date using the format `YYYY.M.D`
(e.g. `2026-04-01` → `2026.4.1`).

Factorial releases new API versions quarterly (Jan/Apr/Jul/Oct). Each version is supported for one year.

## Release

```bash
# Dry run (shows what would change, no writes)
uv run python scripts/release.py --dry-run

# Full release — prompts for version date and whether to publish
uv run python scripts/release.py

# Supply version non-interactively
uv run python scripts/release.py --version 2026-07-01
```

The release script:
1. Prompts for the API version date (`yyyy-mm-dd`).
2. Fetches and patches the spec from `https://api.factorialhr.com/oas/?version=<date>`.
3. Regenerates `factorial_api_client/generated/` and `client.py`.
4. Sets the SDK version to match the API date (e.g. `2026-07-01` → `2026.7.1`).
5. Builds the package, then asks whether to publish to PyPI.

## Smoke test

```bash
FACTORIAL_API_KEY=xxx uv run python scripts/test_api.py
```

## Development

```bash
# Install dependencies
uv sync

# Type check
uv run mypy factorial_api_client --ignore-missing-imports

# Lint
uv run ruff check factorial_api_client
```
