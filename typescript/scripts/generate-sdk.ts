#!/usr/bin/env tsx
/**
 * Stage-2 generator for src/sdk.ts  (the FactorialClient wrapper).
 *
 * Reads all exported function names from src/generated/sdk.gen.ts (stage-1
 * output) and produces a fully-typed, domain-namespaced FactorialClient with
 * resource classes, namespace classes, and pagination helpers.
 *
 * Run manually after updating src/generated/:
 *   npx tsx scripts/generate-sdk.ts
 *   npm run generate-sdk
 *
 * Also called automatically by scripts/release.ts (step 4b) after
 * regenerating src/generated/.
 *
 * Output: src/sdk.ts  (fully overwritten — never edit that file by hand)
 */

import { readFileSync, writeFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, "..");
const SDK_GEN = join(ROOT, "src/generated/sdk.gen.ts");
const OUT = join(ROOT, "src/sdk.ts");

// ─── Parse all exported function names from sdk.gen.ts ──────────────────────

const genSource = readFileSync(SDK_GEN, "utf-8");
const fnNames: string[] = [];
for (const m of genSource.matchAll(/^export const (\w+) = /gm)) {
  fnNames.push(m[1]);
}
console.log(`Found ${fnNames.length} generated functions.`);

// ─── Parse each function name into its parts ────────────────────────────────

// Naming pattern: {verb}Api{Version}Resources{Namespace}{Resource}[{Action}]
// verb: get | post | put | delete
// version: e.g. 20260401
// namespace + resource + optional action are PascalCase segments

type ParsedFn = {
  fnName: string;
  verb: "get" | "post" | "put" | "delete";
  version: string;
  /** e.g. "Ats" */
  namespace: string;
  /** e.g. "Applications" */
  resource: string;
  /** e.g. "Apply", "ById", "" */
  action: string;
};

/**
 * Split a PascalCase string into its component words.
 * e.g. "AtsJobPostings" → ["Ats", "Job", "Postings"]
 */
function splitPascal(s: string): string[] {
  return s.match(/[A-Z][a-z0-9]*/g) ?? [];
}

/**
 * Try to split "NamespaceResource[Action]" into namespace, resource, action.
 *
 * Strategy: try every 1..N prefix lengths as namespace, then try matching the
 * remaining words against known resource patterns. We pick the split where the
 * namespace is the shortest prefix that, when we remove it, leaves a non-empty
 * resource. Because namespaces are always 1-3 PascalCase words, this is safe.
 *
 * Edge cases handled:
 *  - Single-word namespace ("Ats", "Attendance", "Finance" …)
 *  - Multi-word namespace ("ApiPublic", "BookkeepersManagement",
 *    "PayrollEmployees", "PayrollIntegrationsBase", "ProjectManagement", …)
 *  - "ById" suffix always becomes the action
 *  - A trailing sequence of words that doesn't repeat the namespace/resource
 *    prefix is treated as the action
 */
function parseResourcePath(
  body: string
): { namespace: string; resource: string; action: string } | null {
  // body = everything after "Api{Version}Resources" — e.g. "AtsApplicationsApply"
  const words = splitPascal(body);
  if (words.length === 0) return null;

  // Known multi-word namespaces (order matters — longer first)
  const KNOWN_NAMESPACES = [
    ["Bookkeepers", "Management"],
    ["Api", "Public"],
    ["Employee", "Updates"],
    ["Custom", "Fields"],
    ["Custom", "Resources"],
    ["It", "Management"],
    ["Job", "Catalog"],
    ["Payroll", "Employees"],
    ["Payroll", "Integrations", "Base"],
    ["Project", "Management"],
    ["Shift", "Management"],
    ["Time", "Planning"],
    ["Time", "Settings"],
    ["Work", "Schedule"],
  ];

  // Try to match a known multi-word namespace prefix
  for (const ns of KNOWN_NAMESPACES) {
    if (
      words.length > ns.length &&
      ns.every((w, i) => words[i] === w)
    ) {
      const namespace = ns.join("");
      const remaining = words.slice(ns.length);
      // The resource is the next word(s). Try to find where the resource ends
      // and the action begins by looking for "ById" or resource-boundary heuristic.
      const { resource, action } = splitResourceAction(namespace, remaining);
      return { namespace, resource, action };
    }
  }

  // Single-word namespace: first word
  const namespace = words[0];
  const remaining = words.slice(1);
  const { resource, action } = splitResourceAction(namespace, remaining);
  return { namespace, resource, action };
}

/**
 * Given remaining words after the namespace, split into resource name and action.
 *
 * Heuristic: the resource is the longest prefix of words that, when PascalCased,
 * does NOT include known action words. "ById" is always an action.
 *
 * We try all prefix lengths from longest to shortest, stopping when the remaining
 * suffix (action words) is either empty or starts with an action indicator.
 */
function splitResourceAction(
  _namespace: string,
  words: string[]
): { resource: string; action: string } {
  if (words.length === 0) return { resource: "", action: "" };

  // "ById" is always appended at the end as an action
  if (words[words.length - 1] === "Id" && words[words.length - 2] === "By") {
    const resourceWords = words.slice(0, -2);
    return {
      resource: resourceWords.join(""),
      action: "ById",
    };
  }

  // Everything else: resource is the whole thing, action is empty.
  // We'll separate action suffixes in a second pass after we know all resources.
  // For now just return the full word set as resource.
  return { resource: words.join(""), action: "" };
}

const parsed: ParsedFn[] = fnNames.map((fnName) => {
  // e.g. "getApi20260401ResourcesAtsApplicationsApply"
  const m = fnName.match(
    /^(get|post|put|delete)Api(\d+)Resources([A-Z].*)$/
  );
  if (!m) throw new Error(`Cannot parse function name: ${fnName}`);
  const [, verb, version, body] = m as [string, string, string, string];

  const parsed = parseResourcePath(body);
  if (!parsed) throw new Error(`Cannot parse body: ${body}`);

  return {
    fnName,
    verb: verb as ParsedFn["verb"],
    version,
    ...parsed,
  };
});

// ─── Collect all known resource names per namespace ──────────────────────────

// After initial parse, some functions have an action embedded in the "resource"
// field (e.g. "ApplicationsApply", "ShiftsClockIn"). We need to separate them.
// Strategy: collect all base resources (those with no action, i.e. the bare
// GET collection or POST/PUT/DELETE without suffix). Then for any parsed entry
// whose "resource" starts with a known base resource name but has extra words,
// split those extra words off as the action.

// First pass: collect definite base resources (GET collection = no ById, no action)
const baseResources = new Map<string, Set<string>>(); // namespace → Set<resourceName>
for (const p of parsed) {
  if (p.verb === "get" && p.action === "" && p.resource !== "") {
    if (!baseResources.has(p.namespace)) baseResources.set(p.namespace, new Set());
    baseResources.get(p.namespace)!.add(p.resource);
  }
}

// Second pass: for entries without a detected action, check if their resource
// starts with a known base resource and has trailing words → those are the action.
for (const p of parsed) {
  if (p.action !== "") continue; // already has an action (ById)
  const bases = baseResources.get(p.namespace);
  if (!bases) continue;

  // Sort bases by length descending so we match longest prefix first
  const sortedBases = [...bases].sort((a, b) => b.length - a.length);
  for (const base of sortedBases) {
    if (p.resource.startsWith(base) && p.resource.length > base.length) {
      const actionPart = p.resource.slice(base.length); // e.g. "Apply", "ClockIn"
      p.resource = base;
      p.action = actionPart;
      break;
    }
  }
}

// Third pass: if we have a resource with no GET collection (action-only resources
// like ApprovalsMaterializedApprovalsFlows), treat the whole thing as resource="" action=resource
// and use the resource name directly. Actually keep them as-is — they just won't get list/paginate.

// ─── Group by namespace → resource ──────────────────────────────────────────

type ResourceEntry = {
  fnName: string;
  verb: ParsedFn["verb"];
  action: string; // "" | "ById" | "Apply" | "ClockIn" | …
};

type ResourceMap = Map<string, Map<string, ResourceEntry[]>>; // namespace → resource → entries[]

const resourceMap: ResourceMap = new Map();

for (const p of parsed) {
  if (!resourceMap.has(p.namespace)) resourceMap.set(p.namespace, new Map());
  const nsMap = resourceMap.get(p.namespace)!;
  if (!nsMap.has(p.resource)) nsMap.set(p.resource, []);
  nsMap.get(p.resource)!.push({ fnName: p.fnName, verb: p.verb, action: p.action });
}

// ─── Helpers ─────────────────────────────────────────────────────────────────

/** PascalCase → camelCase */
function toCamel(s: string): string {
  if (!s) return s;
  return s[0].toLowerCase() + s.slice(1);
}

/**
 * Convert a PascalCase namespace name to camelCase property name.
 * e.g. "ApiPublic" → "apiPublic", "Ats" → "ats"
 */
function namespaceProp(ns: string): string {
  return toCamel(ns);
}

/**
 * Convert a PascalCase resource name to camelCase property name on the namespace.
 * e.g. "Applications" → "applications", "JobPostings" → "jobPostings"
 * Special: strip the namespace prefix if resource starts with it.
 */
function resourceProp(ns: string, resource: string): string {
  // Strip namespace prefix if resource name starts with namespace
  // e.g. namespace="Ats", resource="AtsApplications" — shouldn't happen after parsing
  // but just in case.
  let name = resource;
  if (name.startsWith(ns) && name.length > ns.length) {
    name = name.slice(ns.length);
  }
  return toCamel(name);
}

/** Convert PascalCase action to camelCase method name */
function actionMethod(action: string): string {
  return toCamel(action);
}

/** Derive a human-readable singular label from PascalCase resource name */
function resourceLabel(resource: string): string {
  // Split by capital letters, lower-case, join with spaces
  const words = splitPascal(resource);
  if (words.length === 0) return resource;
  // Simple singular: if ends in "s" and not "ss", remove trailing "s"
  const last = words[words.length - 1];
  const singular =
    last.endsWith("sses") ? last :
    last.endsWith("ses") ? last.slice(0, -2) :
    last.endsWith("ies") ? last.slice(0, -3) + "y" :
    last.endsWith("s") && !last.endsWith("ss") ? last.slice(0, -1) :
    last;
  words[words.length - 1] = singular;
  return words.join(" ");
}

// ─── Code generators ─────────────────────────────────────────────────────────

function generateResourceClass(
  ns: string,
  resource: string,
  entries: ResourceEntry[]
): string {
  const className = `${ns}${resource}Resource`;
  const prop = resourceProp(ns, resource);
  const label = resourceLabel(resource);

  // Identify standard CRUD methods
  const getList = entries.find((e) => e.verb === "get" && e.action === "");
  const getById = entries.find((e) => e.verb === "get" && e.action === "ById");
  const postCreate = entries.find(
    (e) => e.verb === "post" && e.action === ""
  );
  const putUpdate = entries.find(
    (e) => (e.verb === "put") && e.action === "ById"
  );
  const deleteItem = entries.find(
    (e) => e.verb === "delete" && e.action === "ById"
  );

  // Custom actions = everything else
  const customActions = entries.filter(
    (e) =>
      e !== getList &&
      e !== getById &&
      e !== postCreate &&
      e !== putUpdate &&
      e !== deleteItem
  );

  const lines: string[] = [];
  lines.push(`/** Methods for the ${ns} > ${resource} resource */`);
  lines.push(`export class ${className} {`);
  lines.push(`  constructor(private readonly _client: ReturnType<typeof createClient>) {}`);
  lines.push("");

  if (getList) {
    lines.push(`  /** Reads all ${label}s */`);
    lines.push(
      `  list: typeof ${getList.fnName} = (options?: any) => ${getList.fnName}({ client: this._client, ...options });`
    );
    lines.push("");
    // paginate
    lines.push(`  /**`);
    lines.push(
      `   * Auto-paginate through all ${resource} records, yielding one item at a time.`
    );
    lines.push(`   * Uses cursor-based pagination with \`after_id\` / \`before_id\`.`);
    lines.push(
      `   * @example for await (const item of client.${namespaceProp(ns)}.${prop}.paginate()) { ... }`
    );
    lines.push(`   */`);
    lines.push(
      `  paginate(options?: Parameters<typeof ${getList.fnName}>[0] & { limit?: number; maxItems?: number }) {`
    );
    lines.push(`    const { maxItems, ...rest } = options ?? {};`);
    lines.push(`    return paginate(`);
    lines.push(
      `      (params) => ${getList.fnName}({ client: this._client, ...rest, query: { ...(rest as any)?.query, ...params } } as any),`
    );
    lines.push(`      { maxItems },`);
    lines.push(`    );`);
    lines.push(`  }`);
    lines.push("");
    // all
    lines.push(`  /**`);
    lines.push(
      `   * Fetch all ${resource} records across all pages into a single array.`
    );
    lines.push(
      `   * @param options.maxItems - Safety cap on total items fetched (default: no limit)`
    );
    lines.push(
      `   * @example const all = await client.${namespaceProp(ns)}.${prop}.all()`
    );
    lines.push(`   */`);
    lines.push(
      `  all(options?: Parameters<typeof ${getList.fnName}>[0] & { limit?: number; maxItems?: number }) {`
    );
    lines.push(`    return collectAll(this.paginate(options));`);
    lines.push(`  }`);
    lines.push("");
  }

  if (postCreate) {
    lines.push(`  /** Creates a ${resourceLabel(resource)} */`);
    lines.push(
      `  create: typeof ${postCreate.fnName} = (options?: any) => ${postCreate.fnName}({ client: this._client, ...options });`
    );
    lines.push("");
  }

  if (getById) {
    lines.push(`  /** Reads a single ${resourceLabel(resource)} */`);
    lines.push(
      `  get: typeof ${getById.fnName} = (options?: any) => ${getById.fnName}({ client: this._client, ...options });`
    );
    lines.push("");
  }

  if (putUpdate) {
    lines.push(`  /** Updates a ${resourceLabel(resource)} */`);
    lines.push(
      `  update: typeof ${putUpdate.fnName} = (options?: any) => ${putUpdate.fnName}({ client: this._client, ...options });`
    );
    lines.push("");
  }

  if (deleteItem) {
    lines.push(`  /** Deletes a ${resourceLabel(resource)} */`);
    lines.push(
      `  delete: typeof ${deleteItem.fnName} = (options?: any) => ${deleteItem.fnName}({ client: this._client, ...options });`
    );
    lines.push("");
  }

  for (const ca of customActions) {
    const methodName = actionMethod(ca.action);
    lines.push(`  /** ${pascalToSentence(ca.action)} ${resourceLabel(resource)} */`);
    lines.push(
      `  ${methodName}: typeof ${ca.fnName} = (options?: any) => ${ca.fnName}({ client: this._client, ...options });`
    );
    lines.push("");
  }

  lines.push(`}`);
  lines.push("");
  return lines.join("\n");
}

function pascalToSentence(s: string): string {
  const words = splitPascal(s);
  if (!words.length) return s;
  return words[0] + (words.length > 1 ? " " + words.slice(1).join(" ").toLowerCase() : "");
}

function generateNamespaceClass(
  ns: string,
  resources: Map<string, ResourceEntry[]>
): string {
  const className = `${ns}Namespace`;
  const entries = [...resources.entries()].filter(([r]) => r !== "");

  const lines: string[] = [];
  lines.push(`/** Namespace for all ${ns} resources */`);
  lines.push(`export class ${className} {`);
  for (const [resource] of entries) {
    lines.push(`  readonly ${resourceProp(ns, resource)}: ${ns}${resource}Resource;`);
  }
  lines.push(`  constructor(client: ReturnType<typeof createClient>) {`);
  for (const [resource] of entries) {
    lines.push(
      `    this.${resourceProp(ns, resource)} = new ${ns}${resource}Resource(client);`
    );
  }
  lines.push(`  }`);
  lines.push(`}`);
  lines.push("");
  return lines.join("\n");
}

// ─── Collect all imports ─────────────────────────────────────────────────────

const allFnNames = fnNames.slice().sort();

// ─── Build the file ──────────────────────────────────────────────────────────

const namespaces = [...resourceMap.keys()].sort();

const parts: string[] = [];

// Header
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
  /** Base URL of the Factorial API. Defaults to https://api.factorialhr.com */
  baseUrl?: string;
  /**
   * Factorial API key — sent as the \`x-api-key\` header.
   * Obtain one from Settings → API Keys in the Factorial dashboard.
   * @example apiKey: process.env.FACTORIAL_API_KEY
   */
  apiKey?: string;
  /**
   * OAuth2 bearer token — sent as \`Authorization: Bearer <token>\`.
   * Use this when authenticating via OAuth2 instead of an API key.
   * @example token: oauthAccessToken
   */
  token?: string;
};

`);

// Resource classes
for (const ns of namespaces) {
  const nsMap = resourceMap.get(ns)!;
  const resources = [...nsMap.keys()].filter((r) => r !== "").sort();
  for (const resource of resources) {
    parts.push(generateResourceClass(ns, resource, nsMap.get(resource)!));
  }
}

// Namespace classes
for (const ns of namespaces) {
  const nsMap = resourceMap.get(ns)!;
  parts.push(generateNamespaceClass(ns, nsMap));
}

// FactorialClient class
parts.push(`/**
 * Official Factorial API client.
 *
 * @example
 * \`\`\`ts
 * import { FactorialClient } from "@factorial/api-client";
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
  parts.push(`  readonly ${namespaceProp(ns)}: ${ns}Namespace;\n`);
}

parts.push(`
  constructor(config: FactorialClientConfig = {}) {
    const { apiKey, token, baseUrl, ...rest } = config;

    if (!apiKey && !token) {
      throw new Error("FactorialClient: provide either apiKey or token");
    }

    // hey-api calls the auth callback once per security scheme in spec order:
    // 1. { type: 'http', scheme: 'bearer' }  → Authorization: Bearer <token>
    // 2. { type: 'apiKey', name: 'x-api-key' } → x-api-key: <key>
    // Return a value only for the matching scheme so the other is skipped.
    const auth = (scheme: { type: string }) => {
      if (scheme.type === "http") return token;       // OAuth bearer
      if (scheme.type === "apiKey") return apiKey;    // API key
      return undefined;
    };

    const client = createClient(
      createConfig<ClientOptions>({
        baseUrl: baseUrl ?? "https://api.factorialhr.com",
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        auth: auth as any,
        ...(rest as any),
      })
    );
`);

for (const ns of namespaces) {
  parts.push(`    this.${namespaceProp(ns)} = new ${ns}Namespace(client);\n`);
}

parts.push(`  }
}
`);

const output = parts.join("");
writeFileSync(OUT, output);
console.log(`Written ${output.split("\n").length} lines to src/sdk.ts`);
