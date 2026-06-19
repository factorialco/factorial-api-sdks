#!/usr/bin/env tsx
/**
 * Stage-3 generator for src/webhooks.ts  (the typed webhook catalog).
 *
 * Reads the OpenAPI spec's top-level `webhooks` object and emits clean,
 * importable webhook payload types plus a runtime catalog:
 *
 *   - One clean alias per event, aliasing the existing generated payload type
 *     (e.g. `AtsApplicationCreateWebhook = AtsApplication`), so a handler can do
 *     `import { AtsApplicationCreateWebhook } from "@factorialco/api-client"`.
 *   - `WebhookSubscriptionType` — string-literal union of every subscription_type.
 *   - `WebhookPayloadMap` — subscription_type → payload type, for typed dispatch:
 *       function handle<T extends WebhookSubscriptionType>(t: T, p: WebhookPayloadMap[T])
 *   - `WEBHOOK_CATALOG` — runtime array describing every event (for discovery).
 *
 * Each spec webhook entry looks like:
 *   "Webhooks > Ats > Application > Creates": {
 *     post: {
 *       description: "Subscription_type: `ats/application/create`",
 *       requestBody: { content: { "application/json": {
 *         schema: { $ref: "#/components/schemas/ats_application" } } } }
 *     }
 *   }
 *
 * Run manually:
 *   npx tsx scripts/generate-webhooks.ts [specPathOrUrl]
 *   npm run generate-webhooks
 *
 * Also called automatically by scripts/release.ts (stage 3) after regenerating
 * src/generated/.
 *
 * Output: src/webhooks.ts  (fully overwritten — never edit that file by hand)
 */

import { readFileSync, writeFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, "..");
const OUT = join(ROOT, "src/webhooks.ts");
const TYPES_GEN = join(ROOT, "src/generated/types.gen.ts");

const DEFAULT_SPEC_URL =
  process.env.OPENAPI_SPEC_URL ?? "https://api.factorialhr.com/oas/?version=2026-04-01";

// ─── Spec loading (file path or URL) ─────────────────────────────────────────

type Spec = {
  webhooks?: Record<string, WebhookItem>;
};

type WebhookItem = {
  post?: {
    description?: string;
    summary?: string;
    requestBody?: {
      content?: {
        "application/json"?: { schema?: { $ref?: string } };
      };
    };
  };
};

async function loadSpec(arg: string | undefined): Promise<Spec> {
  const src = arg ?? DEFAULT_SPEC_URL;
  if (/^https?:\/\//.test(src)) {
    const res = await fetch(src);
    if (!res.ok) throw new Error(`Failed to fetch spec: ${res.status} ${res.statusText}`);
    return (await res.json()) as Spec;
  }
  return JSON.parse(readFileSync(src, "utf-8")) as Spec;
}

// ─── Name helpers ────────────────────────────────────────────────────────────

/** snake_case → PascalCase  (matches openapi-ts schema → type naming). */
function pascal(snake: string): string {
  return snake
    .split("_")
    .map((p) => (p ? p[0].toUpperCase() + p.slice(1) : ""))
    .join("");
}

/** subscription_type → clean alias, e.g. "ats/application/create" → "AtsApplicationCreateWebhook". */
function aliasName(subscriptionType: string): string {
  return (
    subscriptionType
      .split("/")
      .map(pascal)
      .join("") + "Webhook"
  );
}

/** "#/components/schemas/ats_application" → "AtsApplication" (the exported type name). */
function payloadTypeName(ref: string): string {
  return pascal(ref.split("/").pop()!);
}

// ─── Parse the spec's webhooks ───────────────────────────────────────────────

type Entry = {
  key: string;
  subscriptionType: string;
  namespace: string;
  resource: string;
  event: string;
  summary: string;
  payloadSchema: string; // raw schema name, e.g. "ats_application"
  payloadType: string; // exported TS type, e.g. "AtsApplication"
  alias: string; // clean alias, e.g. "AtsApplicationCreateWebhook"
};

const spec = await loadSpec(process.argv[2]);
const webhooks = spec.webhooks ?? {};

const entries: Entry[] = [];
for (const [key, item] of Object.entries(webhooks)) {
  const post = item.post;
  if (!post) throw new Error(`Webhook "${key}" has no post operation`);

  const m = post.description?.match(/`([^`]+)`/);
  if (!m) throw new Error(`Webhook "${key}" has no subscription_type in description`);
  const subscriptionType = m[1];

  const ref = post.requestBody?.content?.["application/json"]?.schema?.$ref;
  if (!ref) throw new Error(`Webhook "${key}" has no payload $ref`);

  // key = "Webhooks > Ats > Application > Creates"
  const segments = key.split(">").map((s) => s.trim());
  const [, namespace = "", resource = "", event = ""] = segments;

  const payloadSchema = ref.split("/").pop()!;
  entries.push({
    key,
    subscriptionType,
    namespace,
    resource,
    event,
    summary: post.summary ?? key,
    payloadSchema,
    payloadType: payloadTypeName(ref),
    alias: aliasName(subscriptionType),
  });
}

entries.sort((a, b) => a.subscriptionType.localeCompare(b.subscriptionType));

// ─── Sanity guards (fail loudly if the spec shape changes) ───────────────────

const distinctPayloadTypes = [...new Set(entries.map((e) => e.payloadType))].sort();

// Every payload type must actually be exported by the generated types.
const typesSource = readFileSync(TYPES_GEN, "utf-8");
const missingTypes = distinctPayloadTypes.filter(
  (t) => !typesSource.includes(`export type ${t} `) && !typesSource.includes(`export type ${t}=`)
);
if (missingTypes.length) {
  throw new Error(
    `Payload types not exported by generated/types.gen.ts: ${missingTypes.join(", ")}`
  );
}

// Aliases and subscription_types must be unique.
const aliasDupes = entries
  .map((e) => e.alias)
  .filter((a, i, arr) => arr.indexOf(a) !== i);
if (aliasDupes.length) {
  throw new Error(`Duplicate webhook alias names: ${[...new Set(aliasDupes)].join(", ")}`);
}

console.log(
  `Parsed ${entries.length} webhook events, ${distinctPayloadTypes.length} distinct payload types.`
);

// ─── Emit src/webhooks.ts ────────────────────────────────────────────────────

function q(s: string): string {
  return JSON.stringify(s);
}

const parts: string[] = [];

parts.push(`// AUTO-GENERATED by scripts/generate-webhooks.ts — DO NOT EDIT.
//
// Typed catalog of every Factorial webhook event and its delivered payload.
//
// Factorial delivers the resource object at the top level of the POST body (it
// is NOT wrapped in a { type, data } envelope). The subscription_type and the
// author are conveyed out-of-band: subscribe with a subscription_type, and read
// the x-factorial-author-id / x-factorial-author-type headers if you need the
// author. See the factorial-api-sdks skill for details.
//
// @example
// \`\`\`ts
// import type { AtsApplicationCreateWebhook } from "@factorialco/api-client";
//
// function onApplicationCreated(payload: AtsApplicationCreateWebhook) {
//   console.log(payload.id);
// }
// \`\`\`
//
// @example  typed dispatch keyed on the runtime subscription_type
// \`\`\`ts
// import type { WebhookSubscriptionType, WebhookPayloadMap } from "@factorialco/api-client";
//
// function handle<T extends WebhookSubscriptionType>(type: T, payload: WebhookPayloadMap[T]) {
//   // payload is narrowed to the right type for \`type\`
// }
// \`\`\`

import type {
${distinctPayloadTypes.map((t) => `  ${t},`).join("\n")}
} from "./generated/types.gen.js";
`);

// Clean per-event aliases
parts.push(`\n// ─── Per-event payload type aliases ──────────────────────────────────────────\n`);
for (const e of entries) {
  parts.push(`/** Payload for \`${e.subscriptionType}\` (${e.summary}). */\n`);
  parts.push(`export type ${e.alias} = ${e.payloadType};\n`);
}

// Subscription type union
parts.push(`\n// ─── Subscription types ──────────────────────────────────────────────────────\n`);
parts.push(`/** Every subscription_type accepted by the webhook_subscriptions endpoint. */\n`);
parts.push(`export type WebhookSubscriptionType =\n`);
parts.push(entries.map((e) => `  | ${q(e.subscriptionType)}`).join("\n") + ";\n");

// Payload map
parts.push(`\n// ─── subscription_type → payload type ────────────────────────────────────────\n`);
parts.push(
  `/** Maps each subscription_type to the type of payload Factorial delivers for it. */\n`
);
parts.push(`export interface WebhookPayloadMap {\n`);
for (const e of entries) {
  parts.push(`  ${q(e.subscriptionType)}: ${e.payloadType};\n`);
}
parts.push(`}\n`);

// Runtime catalog
parts.push(`\n// ─── Runtime catalog ─────────────────────────────────────────────────────────\n`);
parts.push(`export interface WebhookCatalogEntry {
  /** The value to pass as subscription_type when creating a subscription. */
  subscriptionType: WebhookSubscriptionType;
  /** Domain namespace, e.g. "Ats". */
  namespace: string;
  /** Resource, e.g. "Application". */
  resource: string;
  /** Event, e.g. "Creates". */
  event: string;
  /** Human-readable summary from the spec. */
  summary: string;
  /** Name of the payload schema in the OpenAPI spec, e.g. "ats_application". */
  payloadSchema: string;
}

/** Every webhook event Factorial can deliver. */
export const WEBHOOK_CATALOG: readonly WebhookCatalogEntry[] = [
`);
for (const e of entries) {
  parts.push(
    `  { subscriptionType: ${q(e.subscriptionType)}, namespace: ${q(e.namespace)}, resource: ${q(
      e.resource
    )}, event: ${q(e.event)}, summary: ${q(e.summary)}, payloadSchema: ${q(e.payloadSchema)} },\n`
  );
}
parts.push(`];\n`);

const output = parts.join("");
writeFileSync(OUT, output);
console.log(`Written ${output.split("\n").length} lines to src/webhooks.ts`);
