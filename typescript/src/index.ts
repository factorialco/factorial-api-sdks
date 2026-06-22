// Public entry point for @factorialco/api-client.
// Import FactorialClient to get started:
//   import { FactorialClient } from "@factorialco/api-client";
export { FactorialClient } from "./sdk.js";
export type { FactorialClientConfig } from "./sdk.js";
export type { PagedMeta, PaginateOptions } from "./pagination.js";
export * from "./generated/types.gen.js";
// Typed webhook catalog: per-event payload aliases, WebhookSubscriptionType,
// WebhookPayloadMap, and the runtime WEBHOOK_CATALOG.
export * from "./webhooks.js";
