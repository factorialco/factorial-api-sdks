# @factorialco/api-client

Official TypeScript SDK for the [Factorial API](https://apidoc.factorialhr.com).

## Versioning

The SDK uses standard semver (`MAJOR.MINOR.PATCH`), independent of the Factorial API version date.

| SDK version | Factorial API version |
|-------------|----------------------|
| `1.x.y`     | `2026-04-01`         |

Factorial releases new API versions quarterly (Jan/Apr/Jul/Oct).

See the [Factorial API versioning docs](https://apidoc.factorialhr.com/docs/api-versioning) for details.

## Installation

```sh
npm install @factorialco/api-client
```

## Quick start

```ts
import { FactorialClient } from "@factorialco/api-client";

const client = new FactorialClient({
  apiKey: process.env.FACTORIAL_API_KEY,
});

const { data: { data: { data, meta } = {}, error } = {}, error } = await client.employees.employees.list();
console.log(`${meta.total} employees total`);
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
const { data: { data, meta } = {}, error } = await client.employees.employees.list({
  query: { only_active: true },
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
await client.attendance.shifts.clockIn({ body: { employee_id: 1, , now: new Date().toISOString().slice(0, 19) } });
```

## Pagination

The Factorial API uses **cursor-based pagination**. All list endpoints return
`{ data: { data, meta } = {}, error }` where `meta` contains `has_next_page`, `end_cursor`, and `total`.

### Single page

```ts
const { data: { data, meta } = {}, error } = await client.employees.employees.list({ query: { limit: 50 } });

// Fetch next page manually
if (meta.has_next_page) {
  const page2 = await client.employees.employees.list({
    query: { limit: 50, after_id: meta.end_cursor },
  });
}
```

### Stream all pages (async iterator)

```ts
for await (const employee of client.employees.employees.paginate()) {
  console.log(employee.full_name);
}
```

### Collect all into array

```ts
// Optional safety cap via maxItems
const all = await client.employees.employees.all({ maxItems: 500 });
```

Both `paginate()` and `all()` are available on every list endpoint.

## Error handling

```ts
const { data, error } = await client.employees.employees.list();

if (error) {
  console.error("API error:", error);
} else {
  console.log(data);
}
```

## Custom base URL

```ts
const client = new FactorialClient({
  apiKey: process.env.FACTORIAL_API_KEY,
  baseUrl: "https://api.factorialhr.com", // default
});
```
