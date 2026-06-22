#!/usr/bin/env node
// Beta-detection for the daily beta-publish workflow.
//
// Decides whether a new BETA SDK should be published for an intermediate
// Factorial API version, and computes the prerelease versions. Detection is
// stateless except for beta_state.json, which is only used to detect a spec
// RE-ISSUE for an already-published date (so the iteration counter can bump).
//
// Outputs (written to $GITHUB_OUTPUT when set, always printed as JSON):
//   should_publish  "true" | "false"
//   target_date     yyyy-mm-dd                (the intermediate API version)
//   next_major      e.g. "2"
//   npm_version     e.g. "2.0.0-beta.2026070100"
//   pypi_version    e.g. "2.0.0b2026070100"
//   iteration       re-issue counter for target_date
//   spec_sha256     hash of the target spec (recorded on the beta-state branch on success)
//   reason          human-readable explanation
//
// Env:
//   OPENAPI_SPEC_BASE   default https://api.factorialhr.com/oas/
//   TARGET_DATE         optional override (workflow_dispatch input)
//   FORCE               "true" to republish even if the spec is unchanged
//
// Exit codes: 0 = ran (check should_publish); 1 = hard error (never publish).

import { readFileSync, existsSync, appendFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const SPEC_BASE = process.env.OPENAPI_SPEC_BASE ?? "https://api.factorialhr.com/oas/";
const NPM_PKG = "@factorialco/api-client";
const PYPI_PKG = "factorial-api-client";
const DATE_RE = /^\d{4}-\d{2}-\d{2}$/;

function fail(msg) {
  console.error(`::error::${msg}`);
  process.exit(1);
}

async function fetchJson(url, { allow404 = false } = {}) {
  const res = await fetch(url, { headers: { "User-Agent": "factorial-sdk-beta-detect/1.0" } });
  if (res.status === 404 && allow404) return null;
  if (!res.ok) throw new Error(`GET ${url} → ${res.status} ${res.statusText}`);
  return res.json();
}

// Fetch a version spec, returning null on any failure (bad status, HTML error
// page, invalid JSON). Used to probe whether a candidate date is a real,
// servable API version.
async function fetchSpecOrNull(url) {
  try {
    const res = await fetch(url, { headers: { "User-Agent": "factorial-sdk-beta-detect/1.0" } });
    if (!res.ok) return null;
    return await res.json();
  } catch {
    return null;
  }
}

// Quarterly version dates (months 01/04/07/10, day 01) strictly after `afterISO`.
function nextQuarters(afterISO, count) {
  let [y, m] = afterISO.split("-").map(Number);
  const out = [];
  for (let i = 0; i < count; i++) {
    m += 3;
    if (m > 12) { m -= 12; y += 1; }
    out.push(`${y}-${String(m).padStart(2, "0")}-01`);
  }
  return out;
}

// Stable stringify (sorted keys) so the hash is deterministic across runs.
function stableStringify(value) {
  if (Array.isArray(value)) return `[${value.map(stableStringify).join(",")}]`;
  if (value && typeof value === "object") {
    return `{${Object.keys(value)
      .sort()
      .map((k) => `${JSON.stringify(k)}:${stableStringify(value[k])}`)
      .join(",")}}`;
  }
  return JSON.stringify(value);
}

// Collect every enum under a key named "api_version" anywhere in the spec.
function collectApiVersionEnum(node, parentKey, out) {
  if (Array.isArray(node)) {
    for (const item of node) collectApiVersionEnum(item, parentKey, out);
  } else if (node && typeof node === "object") {
    if (parentKey === "api_version" && Array.isArray(node.enum)) {
      for (const v of node.enum) if (typeof v === "string") out.add(v);
    }
    for (const [k, v] of Object.entries(node)) collectApiVersionEnum(v, k, out);
  }
}

function emit(outputs) {
  console.log(JSON.stringify(outputs, null, 2));
  if (process.env.GITHUB_OUTPUT) {
    appendFileSync(
      process.env.GITHUB_OUTPUT,
      Object.entries(outputs).map(([k, v]) => `${k}=${v}`).join("\n") + "\n"
    );
  }
}

function done(should, extra, reason) {
  emit({
    should_publish: should ? "true" : "false",
    target_date: extra.target_date ?? "",
    next_major: extra.next_major ?? "",
    npm_version: extra.npm_version ?? "",
    pypi_version: extra.pypi_version ?? "",
    iteration: extra.iteration ?? "",
    spec_sha256: extra.spec_sha256 ?? "",
    reason,
  });
  process.exit(0);
}

async function main() {
  const versionMap = JSON.parse(readFileSync(join(ROOT, "version_map.json"), "utf-8"));
  const stableMajor = String(versionMap.latest);
  const stableDate = versionMap.versions[stableMajor];
  if (!stableDate) fail(`version_map.json has no date for latest major "${stableMajor}"`);
  const nextMajor = String(Number(stableMajor) + 1);

  const specUrl = (d) => `${SPEC_BASE}${SPEC_BASE.includes("?") ? "&" : "?"}version=${d}`;
  const override = process.env.TARGET_DATE?.trim();
  if (override && !DATE_RE.test(override)) fail(`Invalid TARGET_DATE "${override}" (want yyyy-mm-dd)`);

  let targetDate;
  let targetSpec;

  if (override) {
    // 1a. Explicit override: validate just it.
    targetSpec = await fetchSpecOrNull(specUrl(override));
    if (targetSpec?.info?.version !== override) {
      fail(`Override ${override} is not a servable API version (spec reports "${targetSpec?.info?.version}").`);
    }
    targetDate = override;
  } else {
    // 1b. Build candidate dates from quarterly probing (primary — the spec's
    //     api_version enum lags behind servable versions) unioned with the enum,
    //     keeping only dates beyond the current stable. Validate each by the
    //     authoritative confirm-fetch (info.version must echo the request) and
    //     pick the newest that checks out.
    const baseSpec = await fetchJson(SPEC_BASE);
    const enumDates = new Set();
    collectApiVersionEnum(baseSpec, null, enumDates);
    const candidates = [
      ...new Set([
        ...[...enumDates].filter((d) => DATE_RE.test(d)),
        ...nextQuarters(stableDate, 4),
      ]),
    ]
      .filter((d) => d > stableDate)
      .sort();

    for (const d of candidates.reverse()) {
      const spec = await fetchSpecOrNull(specUrl(d));
      if (spec?.info?.version === d) {
        targetDate = d;
        targetSpec = spec;
        break;
      }
    }

    // 2. Nothing intermediate beyond the current stable → no-op.
    if (!targetDate) {
      done(false, { target_date: stableDate, next_major: nextMajor },
        `No intermediate version newer than stable ${stableDate}. ` +
        `(If a "beta" dist-tag exists on npm it should be cleaned up — see workflow.)`);
    }
  }

  // 4. Graduation guard: if the next-major FINAL already exists, stable has taken
  //    over — stop publishing betas for this line.
  const npmMeta = await fetchJson(`https://registry.npmjs.org/${NPM_PKG.replace("/", "%2F")}`, { allow404: true });
  const pypiMeta = await fetchJson(`https://pypi.org/pypi/${PYPI_PKG}/json`, { allow404: true });
  const finalVer = `${nextMajor}.0.0`;
  const npmHasFinal = npmMeta?.versions && npmMeta.versions[finalVer];
  const pypiHasFinal = pypiMeta?.releases && pypiMeta.releases[finalVer];
  if (npmHasFinal || pypiHasFinal) {
    done(false, { target_date: targetDate, next_major: nextMajor },
      `Stable ${finalVer} already published — beta line has graduated; nothing to do.`);
  }

  // 5. First-publish precondition: both packages must already exist with a
  //    stable/latest so a beta can never become the default install.
  const npmLatest = npmMeta?.["dist-tags"]?.latest;
  const pypiHasStable = pypiMeta?.releases &&
    Object.keys(pypiMeta.releases).some((v) => /^\d+\.\d+\.\d+$/.test(v));
  if (!npmLatest) fail(`${NPM_PKG} has no published "latest" on npm — refusing first-publish as a beta.`);
  if (!pypiHasStable) fail(`${PYPI_PKG} has no stable release on PyPI — refusing first-publish as a beta.`);

  // 6. Re-issue detection via beta_state.json → iteration counter.
  const specSha = createHash("sha256").update(stableStringify(targetSpec)).digest("hex");
  const statePath = join(ROOT, "beta_state.json");
  const state = existsSync(statePath) ? JSON.parse(readFileSync(statePath, "utf-8")) : {};
  const force = process.env.FORCE === "true";

  let iteration;
  if (state.target_date !== targetDate) {
    iteration = 0;
  } else if (state.spec_sha256 === specSha && !force) {
    done(false, { target_date: targetDate, next_major: nextMajor, spec_sha256: specSha,
                  iteration: String(state.iteration ?? 0) },
      `Beta for ${targetDate} is already current (spec unchanged) — nothing to do.`);
  } else {
    iteration = Number(state.iteration ?? 0) + 1;
  }

  // 7. Compute prerelease versions. N = YYYYMMDD*100 + iteration (fixed width
  //    keeps cross-date ordering correct, e.g. 2026070100 < 2026070101 < 2026080100).
  const n = Number(targetDate.replaceAll("-", "")) * 100 + iteration;
  done(true, {
    target_date: targetDate,
    next_major: nextMajor,
    npm_version: `${nextMajor}.0.0-beta.${n}`,
    pypi_version: `${nextMajor}.0.0b${n}`,
    iteration: String(iteration),
    spec_sha256: specSha,
  }, `Publish beta for intermediate API ${targetDate} (iteration ${iteration}).`);
}

main().catch((err) => fail(err.message));
