#!/usr/bin/env tsx
/**
 * Live API test script for @factorialco/api-client.
 *
 * Demonstrates:
 *   1. list()     — fetch a single page of employees
 *   2. paginate() — stream all employees one-by-one via async iterator
 *   3. all()      — collect all employees into an array (with a safety cap)
 *
 * Any non-2xx response throws a FactorialApiError, reported by the handler at
 * the bottom of this file.
 *
 * Usage:
 *   FACTORIAL_API_KEY=your_key npm run test:api
 *
 * Or with OAuth token:
 *   FACTORIAL_TOKEN=your_token npm run test:api
 *
 * Optional overrides:
 *   FACTORIAL_BASE_URL=https://api.factorialhr.com  (default)
 */

import { FactorialApiError, FactorialClient } from "../src/index.js";

// ─── Auth ────────────────────────────────────────────────────────────────────

const apiKey = process.env.FACTORIAL_API_KEY;
const oauthToken = process.env.FACTORIAL_TOKEN;
const token = apiKey ?? oauthToken;

if (!token) {
  console.error(
    "❌  No auth token found.\n" +
      "    Set FACTORIAL_API_KEY or FACTORIAL_TOKEN environment variable.\n" +
      "    Example: FACTORIAL_API_KEY=your_key npm run test:api",
  );
  process.exit(1);
}

// ─── Client ──────────────────────────────────────────────────────────────────

const client = new FactorialClient({
  baseUrl: process.env.FACTORIAL_BASE_URL ?? "https://api.factorialhr.com",
  ...(apiKey ? { apiKey } : { token: oauthToken! }),
});

console.log("🔑  Authenticated via", apiKey ? "API key" : "OAuth token");
console.log("🌐  Base URL:", process.env.FACTORIAL_BASE_URL ?? "https://api.factorialhr.com");
console.log();

// ─── Failure reporting ───────────────────────────────────────────────────────

// Every non-2xx response rejects with a FactorialApiError. Report it compactly
// instead of letting Node dump a stack trace for an expected API failure.
const reportFailure = (reason: unknown) => {
  if (reason instanceof FactorialApiError) {
    console.error(`❌  ${reason.message}`);
    console.error(`    status: ${reason.status}  method: ${reason.method}`);
    console.error(`    url:    ${reason.url}`);
    console.error(`    body:   ${JSON.stringify(reason.body)}`);
  } else {
    console.error("❌  Request failed:", reason);
  }
  process.exit(1);
};

// A rejected top-level await surfaces as an uncaught exception, not an
// unhandled rejection, so both are wired to the same reporter.
process.on("uncaughtException", reportFailure);
process.on("unhandledRejection", reportFailure);

// ─── 1. list() — single page ─────────────────────────────────────────────────

console.log("─────────────────────────────────────────────────");
console.log("1️⃣   list()  — fetch first page (up to 100 items)");
console.log("─────────────────────────────────────────────────");

const listQuery = { only_active: true, only_managers: false } as const;

const page1 = await client.employees.employees.list({ query: listQuery });

const { data: employees, meta } = page1.data;

console.log(`✅  Received ${employees.length} employees`);
console.log(`    Total employees: ${meta.total}`);
console.log(`    Has next page:   ${meta.has_next_page}`);
console.log(`    End cursor:      ${meta.end_cursor ?? "n/a"}`);
console.log();

if (employees.length > 0) {
  const first = employees[0]!;
  console.log("    First employee:");
  console.log(`      id:         ${first.id}`);
  console.log(`      full_name:  ${(first as Record<string, unknown>).full_name ?? "n/a"}`);
  console.log(`      email:      ${(first as Record<string, unknown>).email ?? "n/a"}`);
}

// ─── 2. paginate() — async iterator ─────────────────────────────────────────

console.log();
console.log("─────────────────────────────────────────────────");
console.log("2️⃣   paginate()  — stream first 5 employees via async iterator");
console.log("─────────────────────────────────────────────────");

let count = 0;
for await (const employee of client.employees.employees.paginate({ query: listQuery, maxItems: 5 })) {
  count++;
  console.log(
    `    [${count}] id=${employee.id}  name=${(employee as Record<string, unknown>).full_name ?? "n/a"}`,
  );
}
console.log(`✅  Streamed ${count} employees`);

// ─── 3. all() — collect into array ───────────────────────────────────────────

console.log();
console.log("─────────────────────────────────────────────────");
console.log("3️⃣   all()  — collect up to 10 employees into an array");
console.log("─────────────────────────────────────────────────");

const allEmployees = await client.employees.employees.all({ query: listQuery, maxItems: 10 });

console.log(`✅  Collected ${allEmployees.length} employees`);
console.log();
console.log("    Sample (first 3):");
allEmployees.slice(0, 3).forEach((e, i) => {
  console.log(
    `      [${i + 1}] id=${e.id}  name=${(e as Record<string, unknown>).full_name ?? "n/a"}`,
  );
});

console.log();
console.log("🎉  All tests passed!");
