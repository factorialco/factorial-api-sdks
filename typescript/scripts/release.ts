#!/usr/bin/env tsx
/**
 * Release script for @factorialco/api-client.
 *
 * Steps:
 *   0. Prompt for the API version date (yyyy-mm-dd) to generate
 *   1. Fetch the OpenAPI spec from https://api.factorialhr.com/oas/?version=<date>
 *   2. Bump SDK semver (--bump major|minor|patch, default: patch)
 *   3. Regenerate all *.gen.ts files via openapi-ts  (stage 1)
 *   3b. Regenerate src/sdk.ts via generate-sdk.ts    (stage 2)
 *   4. Update package.json version
 *   5. Publish to npm  (skipped with --dry-run)
 *
 * Usage:
 *   npm run release                    # patch bump
 *   npm run release -- --bump minor    # minor bump
 *   npm run release -- --bump major    # major bump
 *   npm run release:dry-run            # preview only, no writes / publish
 */

import { execSync } from "child_process";
import { readFileSync, writeFileSync } from "fs";
import { createInterface } from "readline";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, "..");

function resolveNpmTag(sdkVersion: string): string {
  const major = sdkVersion.split(".")[0];
  const { latest, versions } = JSON.parse(
    readFileSync(join(ROOT, "../version_map.json"), "utf-8")
  ) as { latest: string; versions: Record<string, string> };
  const tag = versions[major];
  if (!tag) {
    throw new Error(
      `No Factorial API version found for SDK major version ${major} in version_map.json`
    );
  }
  return major === latest ? `${tag} latest` : tag;
}

const isDryRun = process.argv.includes("--dry-run");

const bumpArgIdx = process.argv.indexOf("--bump");
const bumpType: "major" | "minor" | "patch" =
  bumpArgIdx !== -1 ? (process.argv[bumpArgIdx + 1] as "major" | "minor" | "patch") : "patch";

if (!["major", "minor", "patch"].includes(bumpType)) {
  throw new Error(`Invalid --bump value: "${bumpType}". Expected major, minor, or patch.`);
}

// CI/beta mode (used by the daily beta-publish workflow):
//   --set-version <ver>  use this exact version instead of bumping semver
//                        (e.g. a prerelease like 2.0.0-beta.2026070100)
//   --no-publish         regenerate + write the version, then stop (no build,
//                        no publish, no prompt). CI publishes via the composite
//                        actions instead.
//   --no-git             accepted for symmetry with release.py; this script
//                        issues no git commands, so it is a no-op.
const setVersionIdx = process.argv.indexOf("--set-version");
const setVersion = setVersionIdx !== -1 ? process.argv[setVersionIdx + 1] : undefined;
const noPublish = process.argv.includes("--no-publish");

function bumpSemver(version: string, bump: "major" | "minor" | "patch"): string {
  const [major, minor, patch] = version.split(".").map(Number);
  if (bump === "major") return `${major + 1}.0.0`;
  if (bump === "minor") return `${major}.${minor + 1}.0`;
  return `${major}.${minor}.${patch + 1}`;
}

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

// ─── Step 2: Bump SDK semver ─────────────────────────────────────────────────

const pkgPath = join(ROOT, "package.json");
const pkg = readJson<{ version: string; name: string }>(pkgPath);
const newSdkVersion = setVersion ?? bumpSemver(pkg.version, bumpType);

log(`\n🔖  Version:`);
log(
  setVersion
    ? `    SDK:  ${pkg.version} → ${newSdkVersion}  (explicit --set-version)`
    : `    SDK:  ${pkg.version} → ${newSdkVersion}  (${bumpType} bump)`
);
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

if (noPublish) {
  log(`\n⏭️   --no-publish: regenerated and set version to ${newSdkVersion}; stopping before build/publish.\n`);
  process.exit(0);
}

// ─── Step 5: Publish ────────────────────────────────────────────────────────

log(`\n🏗️   Building …`);
run(`npm run build`);

const shouldPublish = (await prompt("Publish @factorialco/api-client@" + newSdkVersion + " to npm? [y/N] ")).toLowerCase() === "y";

if (shouldPublish) {
  const [primaryTag, ...extraTags] = resolveNpmTag(newSdkVersion).split(" ");
  const allTags = [primaryTag, ...extraTags].join(", ");
  log(`\n🚀  Publishing @factorialco/api-client@${newSdkVersion} to npm (tags: ${allTags}) …`);
  run(`npm publish --access public --tag ${primaryTag}`);
  for (const tag of extraTags) {
    run(`npm dist-tag add @factorialco/api-client@${newSdkVersion} ${tag}`);
  }
  log(`\n✅  Released @factorialco/api-client@${newSdkVersion} (tags: ${allTags}) successfully!\n`);
} else {
  log(`\n⏭️   Skipped publish. Package built and version bumped to ${newSdkVersion}.\n`);
}
