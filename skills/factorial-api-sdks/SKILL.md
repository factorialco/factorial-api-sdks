---
name: factorial-api-sdks
description: >-
  Build integrations with the Factorial HR API using the official TypeScript
  (@factorialco/api-client) and Python (factorial-api-client) SDKs. Use when
  authenticating, calling endpoints, paginating list results, subscribing to
  webhooks, or typing webhook handler payloads against the Factorial API.
---

# Factorial API SDKs

Official SDKs that wrap the Factorial public API with a domain-namespaced client,
pagination helpers, and clean auth. This skill teaches an agent how to use them
and how to work with Factorial webhooks. Generated reference data lives in
`reference/` (see [References](#references)).

- **TypeScript**: `@factorialco/api-client` (npm)
- **Python**: `factorial-api-client` (PyPI)

## Install

```bash
npm install @factorialco/api-client     # TypeScript
pip install factorial-api-client          # Python
```

## Authentication

Provide **either** an API key **or** an OAuth token (or both):

| Option   | Header sent                  |
| -------- | ---------------------------- |
| `apiKey` | `x-api-key: <value>`         |
| `token`  | `Authorization: Bearer <value>` |

> The Factorial API key is JWT-formatted but is sent as `x-api-key`, **not** as a bearer token.

Credentials can be passed explicitly or read from the environment
(`FACTORIAL_API_KEY`, `FACTORIAL_TOKEN`, optional `FACTORIAL_BASE_URL`).

```ts
import { FactorialClient } from "@factorialco/api-client";
const client = new FactorialClient({ apiKey: process.env.FACTORIAL_API_KEY });
```

```python
from factorial_api_client import FactorialClient
client = FactorialClient(api_key="YOUR_KEY")   # or token="...", or from env
```

## Calling endpoints

The client is organized as `client.<namespace>.<resource>.<method>`. Namespaces and
resources mirror the REST path `/api/<version>/resources/<namespace>/<resource>`.

Method naming is deterministic:

| HTTP / shape                | SDK method                          |
| --------------------------- | ----------------------------------- |
| `GET` collection            | `list()` / `paginate()` / `all()`   |
| `GET` by id                 | `get(id)`                           |
| `POST` collection           | `create(body)`                      |
| `PUT`/`PATCH` by id         | `update(id, body)`                  |
| `DELETE` by id              | `delete(id)`                        |
| Custom action (e.g. `apply`)| camelCased action, e.g. `apply()`   |

```ts
const { data } = await client.employees.employees.list();
const created = await client.apiPublic.webhookSubscriptions.create({ /* body */ });
```

```python
employees = client.employees.employee.list()
sub = client.api_public.webhook_subscription.create(body={...})
```

To discover the exact namespace/resource/method for any endpoint, consult
`reference/sdk-methods.md` (every endpoint, grouped) or the
[online API reference](https://apidoc.factorialhr.com/reference).

## Pagination

List endpoints return `{ data: T[], meta: { end_cursor?, has_next_page, ... } }`.

- `list()` — one raw page
- `paginate()` — async iterator (TS) / sync or async generator (Python)
- `all()` (TS) / `collect_all()` (Python) — fetch every page into one array/list

```ts
for await (const emp of client.employees.employees.paginate()) { /* ... */ }
const everyone = await client.employees.employees.all({ maxItems: 500 });
```

```python
for emp in client.employees.employee.paginate(max_items=50): ...
everyone = client.employees.employee.all()
```

### High-volume retrieval

Pages are capped at **100 items** — a server-side hard max, not a default
(see the [pagination docs](https://apidoc.factorialhr.com/docs/pagination)).
Passing a larger `limit` has no effect. Cursor pagination is sequential (page
N+1 needs page N's `end_cursor`), so `all()` on a big dataset (e.g. a full
company-month of `attendance/worked_times`) means dozens of sequential
requests. To keep request counts and latency sane:

- **Filter first.** Use the endpoint's query params (date ranges, `ids`,
  `employee_ids`, …) instead of pulling everything and filtering locally.
- **Sync incrementally.** Where an endpoint supports `updated_at`-style
  filters, fetch only what changed since your last run and cache locally —
  don't re-pull the full dataset per report.
- **Shard big pulls.** Split one large query into filtered sub-queries (by
  date window or id chunks) and run those concurrently — each sub-query still
  paginates sequentially, but wall-clock time drops. Total request count is
  unchanged, so watch rate limits.
- **Cap defensively.** Pass `max_items` / `maxItems` so a bug or unexpected
  data volume can't turn into an unbounded crawl.

There is no server-side aggregation endpoint; totals (e.g. hours per employee
per period) must be computed client-side from the raw records.

## Errors

The client throws on any non-2xx response (bad/expired token, wrong base URL,
server errors) instead of silently returning empty data. Wrap calls in
try/catch (TS) or try/except (Python).

## API versioning

The SDK targets a specific Factorial API date version (e.g. `2026-04-01`), pinned
by the SDK's major version. Newer API versions ship as new SDK majors.

## Webhooks

Webhooks are HTTP POSTs Factorial sends to your `target_url` when an event happens.

**How delivery works**

- You create a **webhook subscription** for a `subscription_type` (e.g.
  `ats/application/create`), pointing at a `target_url`, with your `company_id`.
- When the event fires, Factorial sends a `POST` to `target_url`. **The payload is
  the resource object at the top level** — it is *not* wrapped in a `{ type, data }`
  envelope. Use a distinct URL per event if you need to tell them apart easily.
- If you set a `challenge` when subscribing, Factorial echoes it back in the
  `x-factorial-wh-challenge` request header so you can verify the source.
- Optional author headers `x-factorial-author-id` / `x-factorial-author-type`
  (`employee` or `company`) identify who triggered the event, when safe to expose.
- **Retry policy**: up to 20 retries over 48h; after that the subscription is
  disabled and you are emailed. Re-enable with a `PUT { enabled: true }`.

**Manage subscriptions via the SDK**

```ts
await client.apiPublic.webhookSubscriptions.create({
  subscription_type: "ats/application/create",
  target_url: "https://example.com/webhooks/factorial",
  challenge: "a-secret-you-choose",
  company_id: 55,
});
```

```python
client.api_public.webhook_subscription.create(body={
    "subscription_type": "ats/application/create",
    "target_url": "https://example.com/webhooks/factorial",
    "challenge": "a-secret-you-choose",
    "company_id": 55,
})
```

**Type the handler payload** with the exported webhook types:

```ts
import type { AtsApplicationCreateWebhook, WebhookPayloadMap, WebhookSubscriptionType }
  from "@factorialco/api-client";

// Direct alias
function onApplicationCreated(payload: AtsApplicationCreateWebhook) { /* ... */ }

// Typed dispatch keyed on the runtime subscription_type
function handle<T extends WebhookSubscriptionType>(type: T, payload: WebhookPayloadMap[T]) { /* ... */ }
```

```python
from factorial_api_client import AtsApplicationCreateWebhook, WEBHOOK_PAYLOAD_TYPES

def on_application_created(payload: AtsApplicationCreateWebhook) -> None: ...

# Runtime lookup of the model class for a subscription_type
model_cls = WEBHOOK_PAYLOAD_TYPES["ats/application/create"]
```

The full list of events, their `subscription_type`, and payload fields is in
`reference/webhooks.md`.

## References

Generated, SDK-specific lookup tables (consult these for exact names/shapes):

- `reference/webhooks.md` — every webhook event, its `subscription_type`, and payload fields.
- `reference/sdk-methods.md` — every REST endpoint grouped by namespace/resource, with the SDK call.

For prose guides (OAuth flows, API keys, versioning, webhook policies, etc.), use the
live docs — always current, not vendored here:

- Getting started: <https://apidoc.factorialhr.com/docs/getting-started>
- Full API reference: <https://apidoc.factorialhr.com/reference>
