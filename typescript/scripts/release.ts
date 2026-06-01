#!/usr/bin/env tsx
/**
 * Release script for @factorial/api-client.
 *
 * Steps:
 *   0. Prompt for the API version date (yyyy-mm-dd) to generate
 *   1. Fetch the OpenAPI spec from https://api.factorialhr.com/oas/?version=<date>
 *   2. Derive SDK version from API date (yyyy-mm-dd → YYYY.M.D)
 *   3. Regenerate all *.gen.ts files via openapi-ts  (stage 1)
 *   3b. Regenerate src/sdk.ts via generate-sdk.ts    (stage 2)
 *   4. Update package.json version
 *   5. Publish to npm  (skipped with --dry-run)
 *
 * Usage:
 *   npm run release             # full release
 *   npm run release:dry-run     # preview only, no writes / publish
 */

import { execSync } from "child_process";
import { readFileSync, writeFileSync } from "fs";
import { createInterface } from "readline";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, "..");

const isDryRun = process.argv.includes("--dry-run");

// ─── Helpers ────────────────────────────────────────────────────────────────

function log(msg: string) {
  console.log(msg);
}

function run(cmd: string, cwd = ROOT) {
  if (isDryRun && (cmd.includes("npm publish") || cmd.includes("git "))) {
    log(`  [dry-run] skipping: ${cmd}`);
    return "";
  }
  return execSync(cmd, { cwd, stdio: "pipe" }).toString().trim();
}

function readJson<T>(path: string): T {
  return JSON.parse(readFileSync(path, "utf-8")) as T;
}

function writeJson(path: string, data: unknown) {
  if (isDryRun) {
    log(`  [dry-run] would write: ${path}`);
    return;
  }
  writeFileSync(path, JSON.stringify(data, null, 2) + "\n");
}

function prompt(question: string): Promise<string> {
  const rl = createInterface({ input: process.stdin, output: process.stdout });
  return new Promise((resolve) => {
    rl.question(question, (answer) => {
      rl.close();
      resolve(answer.trim());
    });
  });
}

// ─── Step 0: Prompt for API version ─────────────────────────────────────────

const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
let apiVersion = process.env.OPENAPI_VERSION ?? "";

if (!apiVersion) {
  apiVersion = await prompt("Enter the API version to generate (yyyy-mm-dd): ");
}

if (!dateRegex.test(apiVersion)) {
  throw new Error(`Invalid version format: "${apiVersion}". Expected yyyy-mm-dd.`);
}

const SPEC_URL =
  process.env.OPENAPI_SPEC_URL ?? `https://api.factorialhr.com/oas/?version=${apiVersion}`;

// ─── Step 1: Fetch spec ──────────────────────────────────────────────────────

log(`\n🔍  Fetching spec from ${SPEC_URL} …`);

const specResponse = await fetch(SPEC_URL);
if (!specResponse.ok) {
  throw new Error(`Failed to fetch spec: ${specResponse.status} ${specResponse.statusText}`);
}
const newSpec = (await specResponse.json()) as Record<string, unknown>;
const specVersion = (newSpec.info as Record<string, string>).version;
log(`    API version in spec: ${specVersion}`);

// ─── Step 2: Derive SDK version from API date ───────────────────────────────

// Convert yyyy-mm-dd → YYYY.M.D (valid semver with large major)
const [year, month, day] = apiVersion.split("-").map(Number);
const newSdkVersion = `${year}.${month}.${day}`;

const pkgPath = join(ROOT, "package.json");
const pkg = readJson<{ version: string; name: string }>(pkgPath);

log(`\n🔖  Version:`);
log(`    SDK:  ${pkg.version} → ${newSdkVersion}`);
log(`    API version: ${apiVersion}`);

if (isDryRun) {
  log(`\n🌵  Dry run — stopping before any writes or publish.\n`);
  process.exit(0);
}

// ─── Step 3: Regenerate *.gen.ts ────────────────────────────────────────────

log(`\n⚙️   Regenerating SDK from spec …`);
run(`npx openapi-ts --input "${SPEC_URL}" --output src/generated --plugins @hey-api/typescript @hey-api/sdk @hey-api/client-fetch`);
log(`    Done.`);

// ─── Step 3b: Regenerate src/sdk.ts from generated functions ────────────────

log(`\n⚙️   Regenerating src/sdk.ts …`);
run(`npx tsx scripts/generate-sdk.ts`);
log(`    Done.`);

// ─── Step 4: Update package.json version ────────────────────────────────────

log(`\n📝  Updating package.json to ${newSdkVersion} …`);
(pkg as Record<string, unknown>).version = newSdkVersion;
writeJson(pkgPath, pkg);

// ─── Step 5: Publish ────────────────────────────────────────────────────────

log(`\n🏗️   Building …`);
run(`npm run build`);

const shouldPublish = (await prompt("Publish @factorial/api-client@" + newSdkVersion + " to npm? [y/N] ")).toLowerCase() === "y";

if (shouldPublish) {
  log(`\n🚀  Publishing @factorial/api-client@${newSdkVersion} to npm …`);
  run(`npm publish --access public`);
  log(`\n✅  Released @factorial/api-client@${newSdkVersion} successfully!\n`);
} else {
  log(`\n⏭️   Skipped publish. Package built and version bumped to ${newSdkVersion}.\n`);
}
