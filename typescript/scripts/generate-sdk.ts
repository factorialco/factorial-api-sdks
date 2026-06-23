#!/usr/bin/env tsx
/**
 * Stage-2 generator for src/sdk.ts  (the FactorialClient wrapper).
 *
 * Structure is derived from the REST URL of each generated function
 * (`/api/<ver>/resources/<namespace>/<resource>/[<id>|<action>]`), which is the
 * single source of truth shared with the Python generator — so both SDKs expose
 * the same namespaces, resources and methods, differing only in case convention
 * (camelCase here, snake_case in Python).
 *
 * Method naming:
 *   - collection            GET → list, POST → create
 *   - by-id (/{id})         GET → get, PUT → update, DELETE → delete
 *   - custom action (/foo)  → the action verb, camelCase (e.g. approveResource,
 *                             clockIn, bulkCreateUpdate)
 *
 * Run manually after updating src/generated/:
 *   npm run generate-sdk
 *
 * Also called automatically by scripts/release.ts after regenerating
 * src/generated/. Output: src/sdk.ts  (fully overwritten — never edit by hand).
 */

import { readFileSync, writeFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, "..");
const SDK_GEN = join(ROOT, "src/generated/sdk.gen.ts");
const OUT = join(ROOT, "src/sdk.ts");

// ─── Parse functions (name + HTTP method + url) from sdk.gen.ts ──────────────

type Verb = "get" | "post" | "put" | "delete";
type Kind = "list" | "get" | "create" | "update" | "delete" | "custom";

type Endpoint = {
  fnName: string;
  verb: Verb;
  ns: string;
  resource: string;
  kind: Kind;
  method: string;
};

const genSource = readFileSync(SDK_GEN, "utf-8");

// Each function is `export const <name> = ... (client).<verb><...>({ ... url: '<url>' ... })`.
// Split on the export boundary and read name/verb from the head and url from the body.
const rawBlocks = genSource.split(/^export const /m).slice(1);

const COLLECTION: Record<Verb, Kind> = { get: "list", post: "create", put: "update", delete: "delete" };
const BY_ID: Record<Verb, Kind> = { get: "get", put: "update", delete: "delete", post: "create" };

function capitalize(s: string): string {
  return s ? s[0].toUpperCase() + s.slice(1) : s;
}
/** snake_case → camelCase */
function camel(snake: string): string {
  const [first, ...rest] = snake.split("_");
  return first + rest.map(capitalize).join("");
}
/** snake_case → PascalCase */
function pascal(snake: string): string {
  return snake.split("_").map(capitalize).join("");
}

const endpoints: Endpoint[] = [];
for (const block of rawBlocks) {
  const nameMatch = block.match(/^(\w+) =/);
  const verbMatch = block.match(/\)\.(get|post|put|delete)</);
  const urlMatch = block.match(/url: '(\/api\/[^']+)'/);
  if (!nameMatch || !verbMatch || !urlMatch) continue;

  const fnName = nameMatch[1];
  const verb = verbMatch[1] as Verb;
  // /api/<ver>/resources/<ns>/<resource>/<rest...>
  const parts = urlMatch[1].split("/api/")[1].split("/");
  const ns = parts[2];
  const resource = parts[3];
  const rest = parts.slice(4);

  let kind: Kind;
  let method: string;
  if (rest.length === 0) {
    kind = COLLECTION[verb];
    method = kind;
  } else if (rest[0].startsWith("{")) {
    kind = BY_ID[verb];
    method = kind;
  } else {
    kind = "custom";
    method = camel(rest[0]);
  }
  endpoints.push({ fnName, verb, ns, resource, kind, method });
}

console.log(`Parsed ${endpoints.length} endpoints from sdk.gen.ts.`);

// ─── Group by namespace → resource ───────────────────────────────────────────

type ResourceMap = Map<string, Map<string, Endpoint[]>>; // ns → resource → endpoints[]
const resourceMap: ResourceMap = new Map();
for (const e of endpoints) {
  if (!resourceMap.has(e.ns)) resourceMap.set(e.ns, new Map());
  const nsMap = resourceMap.get(e.ns)!;
  if (!nsMap.has(e.resource)) nsMap.set(e.resource, []);
  nsMap.get(e.resource)!.push(e);
}

// Deduplicate method names within a resource (rare — only when two endpoints map
// to the same name, e.g. a custom action colliding with a CRUD verb).
for (const nsMap of resourceMap.values()) {
  for (const entries of nsMap.values()) {
    const seen = new Map<string, number>();
    for (const e of entries.sort((a, b) => a.fnName.localeCompare(b.fnName))) {
      const n = seen.get(e.method) ?? 0;
      seen.set(e.method, n + 1);
      if (n > 0) e.method = `${e.method}${n}`;
    }
  }
}

// ─── Code generators ─────────────────────────────────────────────────────────

function generateResourceClass(ns: string, resource: string, entries: Endpoint[]): string {
  const className = `${pascal(ns)}${pascal(resource)}Resource`;
  const list = entries.find((e) => e.kind === "list");
  const getOne = entries.find((e) => e.kind === "get");
  const create = entries.find((e) => e.kind === "create");
  const update = entries.find((e) => e.kind === "update");
  const del = entries.find((e) => e.kind === "delete");
  const custom = entries.filter((e) => e.kind === "custom");

  const lines: string[] = [];
  lines.push(`/** Methods for the ${ns} > ${resource} resource */`);
  lines.push(`export class ${className} {`);
  lines.push(`  constructor(private readonly _client: ReturnType<typeof createClient>) {}`);
  lines.push("");

  if (list) {
    lines.push(`  /** Lists all ${resource} */`);
    lines.push(`  list: typeof ${list.fnName} = (options?: any) => ${list.fnName}({ client: this._client, ...options });`);
    lines.push("");
    lines.push(`  /**`);
    lines.push(`   * Auto-paginate through all ${resource}, yielding one item at a time.`);
    lines.push(`   * @example for await (const item of client.${camel(ns)}.${camel(resource)}.paginate()) { ... }`);
    lines.push(`   */`);
    lines.push(`  paginate(options?: Parameters<typeof ${list.fnName}>[0] & { limit?: number; maxItems?: number }) {`);
    lines.push(`    const { maxItems, ...rest } = options ?? {};`);
    lines.push(`    return paginate(`);
    lines.push(`      (params) => ${list.fnName}({ client: this._client, ...rest, query: { ...(rest as any)?.query, ...params } } as any),`);
    lines.push(`      { maxItems },`);
    lines.push(`    );`);
    lines.push(`  }`);
    lines.push("");
    lines.push(`  /**`);
    lines.push(`   * Fetch all ${resource} across all pages into a single array.`);
    lines.push(`   * @example const all = await client.${camel(ns)}.${camel(resource)}.all()`);
    lines.push(`   */`);
    lines.push(`  all(options?: Parameters<typeof ${list.fnName}>[0] & { limit?: number; maxItems?: number }) {`);
    lines.push(`    return collectAll(this.paginate(options));`);
    lines.push(`  }`);
    lines.push("");
  }

  if (create) {
    lines.push(`  /** Creates a ${resource} record */`);
    lines.push(`  create: typeof ${create.fnName} = (options?: any) => ${create.fnName}({ client: this._client, ...options });`);
    lines.push("");
  }
  if (getOne) {
    lines.push(`  /** Reads a single ${resource} record */`);
    lines.push(`  get: typeof ${getOne.fnName} = (options?: any) => ${getOne.fnName}({ client: this._client, ...options });`);
    lines.push("");
  }
  if (update) {
    lines.push(`  /** Updates a ${resource} record */`);
    lines.push(`  update: typeof ${update.fnName} = (options?: any) => ${update.fnName}({ client: this._client, ...options });`);
    lines.push("");
  }
  if (del) {
    lines.push(`  /** Deletes a ${resource} record */`);
    lines.push(`  delete: typeof ${del.fnName} = (options?: any) => ${del.fnName}({ client: this._client, ...options });`);
    lines.push("");
  }
  for (const ca of custom) {
    lines.push(`  /** ${ca.method} */`);
    lines.push(`  ${ca.method}: typeof ${ca.fnName} = (options?: any) => ${ca.fnName}({ client: this._client, ...options });`);
    lines.push("");
  }

  lines.push(`}`);
  lines.push("");
  return lines.join("\n");
}

function generateNamespaceClass(ns: string, resources: Map<string, Endpoint[]>): string {
  const className = `${pascal(ns)}Namespace`;
  const names = [...resources.keys()].sort();
  const lines: string[] = [];
  lines.push(`/** Namespace for all ${ns} resources */`);
  lines.push(`export class ${className} {`);
  for (const resource of names) {
    lines.push(`  readonly ${camel(resource)}: ${pascal(ns)}${pascal(resource)}Resource;`);
  }
  lines.push(`  constructor(client: ReturnType<typeof createClient>) {`);
  for (const resource of names) {
    lines.push(`    this.${camel(resource)} = new ${pascal(ns)}${pascal(resource)}Resource(client);`);
  }
  lines.push(`  }`);
  lines.push(`}`);
  lines.push("");
  return lines.join("\n");
}

// ─── Build the file ──────────────────────────────────────────────────────────

const allFnNames = endpoints.map((e) => e.fnName).sort();
const namespaces = [...resourceMap.keys()].sort();
const parts: string[] = [];

parts.push(`// This file is auto-generated by scripts/generate-sdk.ts
// DO NOT edit manually — run \`npm run generate-sdk\` to regenerate.
// Generated from src/generated/sdk.gen.ts

import type { Config } from "./generated/client/index.js";
import { createClient, createConfig } from "./generated/client/index.js";
import type { ClientOptions } from "./generated/types.gen.js";
import {
`);

for (const fn of allFnNames) {
  parts.push(`  ${fn},\n`);
}

parts.push(`} from "./generated/sdk.gen.js";

export type { ClientOptions } from "./generated/types.gen.js";
export * from "./generated/types.gen.js";

import { paginate, collectAll } from "./pagination.js";
export type { PagedMeta, PaginateOptions } from "./pagination.js";

export type FactorialClientConfig = Omit<Partial<Config<ClientOptions>>, "baseUrl" | "auth"> & {
  /**
   * Base URL of the Factorial API.
   * Falls back to the \`FACTORIAL_BASE_URL\` env var, then https://api.factorialhr.com
   */
  baseUrl?: string;
  /**
   * Factorial API key — sent as the \`x-api-key\` header.
   * Obtain one from Settings → API Keys in the Factorial dashboard.
   * Falls back to the \`FACTORIAL_API_KEY\` env var when omitted.
   */
  apiKey?: string;
  /**
   * OAuth2 bearer token — sent as \`Authorization: Bearer <token>\`.
   * Use this when authenticating via OAuth2 instead of an API key.
   * Falls back to the \`FACTORIAL_TOKEN\` env var when omitted.
   */
  token?: string;
};

`);

for (const ns of namespaces) {
  const nsMap = resourceMap.get(ns)!;
  for (const resource of [...nsMap.keys()].sort()) {
    parts.push(generateResourceClass(ns, resource, nsMap.get(resource)!));
  }
}

for (const ns of namespaces) {
  parts.push(generateNamespaceClass(ns, resourceMap.get(ns)!));
}

parts.push(`/**
 * Official Factorial API client.
 *
 * @example
 * \`\`\`ts
 * import { FactorialClient } from "@factorialco/api-client";
 *
 * const client = new FactorialClient({
 *   apiKey: process.env.FACTORIAL_API_KEY,
 * });
 *
 * // List employees (single page, max 100)
 * const { data } = await client.employees.employees.list();
 *
 * // Stream all employees across all pages (cursor pagination)
 * for await (const employee of client.employees.employees.paginate()) {
 *   console.log(employee.full_name);
 * }
 *
 * // Collect all into an array (with optional safety cap)
 * const all = await client.employees.employees.all({ maxItems: 500 });
 * \`\`\`
 */
export class FactorialClient {
`);

for (const ns of namespaces) {
  parts.push(`  /** ${ns} resources */\n`);
  parts.push(`  readonly ${camel(ns)}: ${pascal(ns)}Namespace;\n`);
}

parts.push(`
  constructor(config: FactorialClientConfig = {}) {
    const { apiKey, token, baseUrl, ...rest } = config;

    // Fall back to environment variables when options are omitted. Guarded so
    // the SDK keeps working in non-Node runtimes (e.g. browsers) where
    // \`process\` is undefined.
    const env: Record<string, string | undefined> =
      typeof globalThis !== "undefined" &&
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      (globalThis as any).process &&
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      (globalThis as any).process.env
        ? // eslint-disable-next-line @typescript-eslint/no-explicit-any
          (globalThis as any).process.env
        : {};
    const resolvedApiKey = apiKey ?? env.FACTORIAL_API_KEY;
    const resolvedToken = token ?? env.FACTORIAL_TOKEN;
    const resolvedBaseUrl =
      baseUrl ?? env.FACTORIAL_BASE_URL ?? "https://api.factorialhr.com";

    if (!resolvedApiKey && !resolvedToken) {
      throw new Error(
        "FactorialClient: provide either apiKey or token (or set FACTORIAL_API_KEY / FACTORIAL_TOKEN)"
      );
    }

    // hey-api calls the auth callback once per security scheme in spec order:
    // 1. { type: 'http', scheme: 'bearer' }  → Authorization: Bearer <token>
    // 2. { type: 'apiKey', name: 'x-api-key' } → x-api-key: <key>
    // Return a value only for the matching scheme so the other is skipped.
    const auth = (scheme: { type: string }) => {
      if (scheme.type === "http") return resolvedToken;    // OAuth bearer
      if (scheme.type === "apiKey") return resolvedApiKey;  // API key
      return undefined;
    };

    const client = createClient(
      createConfig<ClientOptions>({
        baseUrl: resolvedBaseUrl,
        throwOnError: true,
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        auth: auth as any,
        ...(rest as any),
      })
    );
`);

for (const ns of namespaces) {
  parts.push(`    this.${camel(ns)} = new ${pascal(ns)}Namespace(client);\n`);
}

parts.push(`  }
}
`);

const output = parts.join("");
writeFileSync(OUT, output);
console.log(`Written ${output.split("\n").length} lines to src/sdk.ts`);
