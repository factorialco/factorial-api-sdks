import { defineConfig } from "@hey-api/openapi-ts";

const SPEC_URL =
  process.env.OPENAPI_SPEC_URL ?? "https://api.factorialhr.com/oas";

export default defineConfig({
  input: SPEC_URL,
  output: {
    path: "src/generated",
    format: "prettier",
    lint: "eslint",
  },
  plugins: [
    "@hey-api/typescript",
    {
      name: "@hey-api/sdk",
      // Flat tree-shakeable functions — we wrap them in the hand-written
      // FactorialClient class with domain namespaces (see src/sdk.ts)
      operations: {
        strategy: "flat",
      },
      auth: true,
    },
    {
      name: "@hey-api/client-fetch",
      runtimeConfigPath: "../client-config",
    },
  ],
});
