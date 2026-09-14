# @factorialco/api-client

Official TypeScript SDK for the [Factorial API](https://apidoc.factorialhr.com).

## Versioning

The SDK uses standard semver (`MAJOR.MINOR.PATCH`), independent of the Factorial API version date.

| SDK version | Factorial API version |
|-------------|----------------------|
| `1.x.y`     | `2026-04-01`         |
| `2.x.y`     | `2026-07-01`         |
| `3.x.y`     | `2026-07-01`         |

Factorial releases new API versions quarterly (Jan/Apr/Jul/Oct). A new major is
usually cut for a new API version, but can also be cut for a breaking change to
the SDK itself — which is why `2.x` and `3.x` target the same API version.

See the [Factorial API versioning docs](https://apidoc.factorialhr.com/docs/api-versioning) for details.

## Installation

```sh
npm install @factorialco/api-client@2026-07-01
```

## Quick start

```ts
import { FactorialClient } from "@factorialco/api-client";

const client = new FactorialClient({
  apiKey: process.env.FACTORIAL_API_KEY,
});

const { data: page } = await client.employees.employees.list({
  query: { only_active: true, only_managers: false },
});
console.log(`${page.meta?.total} employees total`);
```

## Authentication

The SDK supports both **API keys** and **OAuth2 bearer tokens**:

```ts
// API key — sent as x-api-key header
const client = new FactorialClient({
  apiKey: process.env.FACTORIAL_API_KEY,
});

// OAuth2 bearer token — sent as Authorization: Bearer
const client = new FactorialClient({
  token: getAccessToken(), // your token refresh logic
});
```

### Environment variables

When an option is omitted, the client falls back to environment variables.
Explicit options always take precedence.

| Variable | Maps to option | Sent as |
|----------|----------------|---------|
| `FACTORIAL_API_KEY` | `apiKey` | `x-api-key` header |
| `FACTORIAL_TOKEN` | `token` | `Authorization: Bearer` |
| `FACTORIAL_BASE_URL` | `baseUrl` | — (defaults to `https://api.factorialhr.com`) |

```ts
// No options needed — reads FACTORIAL_API_KEY / FACTORIAL_TOKEN / FACTORIAL_BASE_URL
const client = new FactorialClient();
```

The fallback reads `process.env`, so it applies in Node-like runtimes. In the
browser there is no `process.env` — pass credentials explicitly.

## SDK structure

All resources are grouped by domain, mirroring the Factorial API hierarchy:

```
client.employees.employees
client.ats.applications
client.ats.candidates
client.attendance.shifts
client.timeoff.leaves
client.contracts.contractVersions
client.performance.reviewProcesses
// … 30+ domain namespaces, 100+ resources
```

## CRUD operations

Every resource exposes the standard methods available in the API:

```ts
// List (single page, up to 100 items)
const { data: page } = await client.employees.employees.list({
  query: { only_active: true, only_managers: false },
});

// Get by ID
const { data: employee } = await client.employees.employees.get({
  path: { id: 42 },
});

// Create
const { data: leave } = await client.timeoff.leaves.create({
  body: { employee_id: 1, leave_type_id: 2, start_on: "2026-06-01", finish_on: "2026-06-05" },
});

// Update
const { data: updated } = await client.timeoff.leaves.update({
  path: { id: 99 },
  body: { finish_on: "2026-06-10" },
});

// Delete
await client.timeoff.leaves.delete({ path: { id: 99 } });

// Named actions
await client.timeoff.leaves.approve({ body: { id: 99 } });
await client.attendance.shifts.clockIn({
  body: { employee_id: 1, now: new Date().toISOString().slice(0, 19) },
});
```

## Pagination

The Factorial API uses **cursor-based pagination**. Every list endpoint resolves
to `{ data: { data, meta }, request, response }`, where `meta` carries
`has_next_page`, `end_cursor`, and `total`. The spec marks `data` and `meta`
optional, so access them with `?.`. A non-2xx response throws — see
[Error handling](#error-handling).

### Single page

```ts
const { data: page } = await client.employees.employees.list({
  query: { only_active: true, only_managers: false },
});
console.log(page.data?.length, page.meta?.has_next_page);
```

`limit` and `after_id` work at runtime but are absent from the OpenAPI spec, so
they are not part of the typed `query`. Prefer `paginate({ limit })` below; to
cursor by hand, cast the query.

### Stream all pages (async iterator)

```ts
for await (const employee of client.employees.employees.paginate({
  query: { only_active: true, only_managers: false },
})) {
  console.log(employee.full_name);
}
```

`paginate()` and `all()` accept `limit` (items per request, max 100) and
`maxItems` (a cap on the total fetched) alongside the endpoint's own options.

### Collect all into array

```ts
// Optional safety cap via maxItems
const all = await client.employees.employees.all({
  query: { only_active: true, only_managers: false },
  maxItems: 500,
});
```

Both `paginate()` and `all()` are available on every list endpoint.

### High-volume retrieval

Pages are capped at **100 items** — a server-side hard max
([pagination docs](https://apidoc.factorialhr.com/docs/pagination)); a larger
`limit` has no effect. Cursor pagination is sequential, so `all()` on a large
dataset issues one request per 100 records. For big pulls:

- Filter with the endpoint's query params (date ranges, `ids`, `employee_ids`, …)
  instead of pulling everything.
- Sync incrementally where `updated_at`-style filters exist, and cache locally.
- Split one large query into filtered sub-queries (date windows, id chunks) and
  run them concurrently with `Promise.all` — faster wall-clock, same total
  request count, so mind rate limits.
- Pass `maxItems` as a safety cap.

There is no server-side aggregation endpoint; compute totals client-side.

## Error handling

Any non-2xx response (bad/expired token, wrong base URL, `4xx`/`5xx`) **throws a
`FactorialApiError`** rather than resolving to empty data. Results carry no
`error` field — wrap calls in `try`/`catch`:

```ts
import { FactorialApiError, FactorialClient } from "@factorialco/api-client";

try {
  const { data } = await client.employees.employees.get({ path: { id: "42" } });
  console.log(data);
} catch (err) {
  if (err instanceof FactorialApiError) {
    console.error(err.status);     // 404
    console.error(err.method);     // "GET"
    console.error(err.url);        // full request URL
    console.error(err.body);       // parsed error body from the API
    console.error(err.message);    // "Factorial API 404 Not Found: GET https://… — {…}"
  } else {
    // Transport failure (DNS, connection reset, abort) — not an HTTP response.
    throw err;
  }
}
```

`FactorialApiError` fields:

| Field | Type | Notes |
|-------|------|-------|
| `status` | `number` | HTTP status code |
| `statusText` | `string` | Reason phrase; empty over HTTP/2 |
| `method` | `string` | Request method |
| `url` | `string` | Full request URL, including the query string |
| `body` | `unknown` | Parsed JSON, the raw string for non-JSON, `undefined` when empty |
| `headers` | `Headers` | Response headers; non-enumerable |
| `response` | `Response` | Raw response; non-enumerable, body already consumed |

`headers` and `response` are non-enumerable so `console.error(err)` stays
readable — they are still accessible directly.

Across package copies (the ESM + CJS dual-package hazard) `instanceof` can fail;
`isFactorialApiError(err)` is a name-based fallback for that case.

## Webhooks

Manage subscriptions through the client, and type your handler payloads with the
generated webhook catalog (re-exported from the package root).

```ts
import {
  FactorialClient,
  WEBHOOK_CATALOG,
} from "@factorialco/api-client";
import type {
  AtsApplicationCreateWebhook,
  WebhookSubscriptionType,
  WebhookPayloadMap,
} from "@factorialco/api-client";

const client = new FactorialClient({ apiKey: process.env.FACTORIAL_API_KEY });

// Subscribe to an event. The `challenge` is a secret you choose; Factorial echoes
// it back in the `x-factorial-wh-challenge` header on every delivery so you can
// verify the request really came from Factorial.
await client.apiPublic.webhookSubscriptions.create({
  subscription_type: "ats/application/create",
  target_url: "https://example.com/webhooks/factorial",
  company_id: 55,
  challenge: "a-random-secret-you-generate",
});

// Type a handler directly…
function onApplicationCreated(payload: AtsApplicationCreateWebhook) {
  console.log(payload.id);
}

// …or dispatch on the runtime subscription_type with full type safety
function handle<T extends WebhookSubscriptionType>(type: T, payload: WebhookPayloadMap[T]) {
  /* payload is narrowed to the right type for `type` */
}

// Discover every event at runtime
console.log(WEBHOOK_CATALOG.length, "webhook events available");
```

Factorial delivers the resource object at the **top level** of the POST body (no
`{ type, data }` envelope). A full event→payload reference and an SDK usage guide
for coding agents are available as a skill:

```bash
npx skills add https://github.com/factorialco/factorial-api-sdks --skill factorial-api-sdks
```

## Custom base URL

```ts
const client = new FactorialClient({
  apiKey: process.env.FACTORIAL_API_KEY,
  baseUrl: "https://api.factorialhr.com", // default; or set FACTORIAL_BASE_URL
});
```
