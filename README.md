# Factorial API SDKs

Official auto-generated SDKs for the [Factorial API](https://apidoc.factorialhr.com), available for TypeScript and Python.

Both SDKs are generated from the OpenAPI spec and wrapped with a generated `FactorialClient` providing clean domain-namespaced access and cursor pagination helpers.

## SDKs

### TypeScript · `@factorialco/api-client`

```bash
npm install @factorialco/api-client
```

```ts
import { FactorialClient } from "@factorialco/api-client";

const client = new FactorialClient({ apiKey: process.env.FACTORIAL_API_KEY });

const page = await client.employees.employees.list();
for await (const emp of client.employees.employees.paginate({ maxItems: 50 })) {
  console.log(emp.full_name);
}
```

→ [Full docs](typescript/README.md)

---

### Python · `factorial-api-client`

```bash
pip install factorial-api-client
```

```python
from factorial_api_client import FactorialClient

client = FactorialClient(api_key="YOUR_KEY")

result = client.employees.employee.list()
for emp in client.employees.employee.paginate(max_items=50):
    print(emp.full_name)
```

→ [Full docs](python/README.md)

---

## Versioning

Both SDKs use standard semver (`MAJOR.MINOR.PATCH`), independent of the Factorial API version date.

| SDK version | Factorial API version |
|-------------|----------------------|
| `1.x.y`     | `2026-04-01`         |

Factorial releases new API versions quarterly (Jan/Apr/Jul/Oct).

**Releases are automated with [release-please](https://github.com/googleapis/release-please).**
Land [Conventional Commits](https://www.conventionalcommits.org/) on `main`, then
merge the Release PR it opens — that bumps the version, tags the commit, creates
the GitHub Release, and publishes to npm / PyPI. You never tag or publish by hand.
See **[RELEASING.md](RELEASING.md)** for the full flow.

When opening a PR, two things decide the release:

- **PRs are squash-merged, so the PR _title_ must be a Conventional Commit**
  (`feat:` → minor, `fix:` → patch, `feat!:`/`BREAKING CHANGE:` → major).
- **Which package bumps is decided by file path:** changes under `typescript/`
  bump the npm package, under `python/` the PyPI package. For a change spanning
  **both** SDKs, use a bare `feat:`/`fix:` with **no scope** so both bump together.

The `release.ts` / `release.py` scripts remain for **regenerating** the SDK from a
new OpenAPI spec; see the per-SDK READMEs: [TypeScript](typescript/README.md) · [Python](python/README.md)

## Development

### TypeScript

**Generate SDK from latest spec**

```sh
cd typescript
npm run generate
```

Fetches the OpenAPI spec from `https://api.factorialhr.com/oas/?version=<date>` and regenerates all `src/generated/*.gen.ts` files. Override the URL with:

```sh
OPENAPI_SPEC_URL=./local-spec.json npm run generate
```

**Test against the live API**

```sh
FACTORIAL_API_KEY=your_key npm run test:api
# or with OAuth token:
FACTORIAL_TOKEN=your_token npm run test:api
```

**Release a new version**

```sh
npm run release                    # patch bump (default)
npm run release -- --bump minor    # minor bump
npm run release -- --bump major    # major bump
npm run release:dry-run            # preview only — no writes, no publish
```

The release script:
1. Prompts for the API version date (`yyyy-mm-dd`).
2. Fetches the spec from `https://api.factorialhr.com/oas/?version=<date>`.
3. Regenerates `src/generated/` (stage 1) and `src/sdk.ts` (stage 2).
4. Bumps the SDK semver (`--bump major|minor|patch`, default `patch`).
5. Builds the package, then asks whether to publish to npm.

---

## Authentication

Both SDKs support:

- **API key** — via `apiKey:` / `api_key=` (sent as `x-api-key` header)
- **OAuth2 bearer token** — via `token:` / `token=` (sent as `Authorization: Bearer`)

### Environment variables

If you don't pass credentials (or a base URL) explicitly, the client reads them
from the environment. Explicit arguments always take precedence.

| Variable | Maps to | Sent as |
|----------|---------|---------|
| `FACTORIAL_API_KEY` | API key | `x-api-key` header |
| `FACTORIAL_TOKEN` | OAuth2 token | `Authorization: Bearer` |
| `FACTORIAL_BASE_URL` | Base URL | — (defaults to `https://api.factorialhr.com`) |

```ts
// TypeScript — picks up FACTORIAL_API_KEY / FACTORIAL_TOKEN / FACTORIAL_BASE_URL
const client = new FactorialClient();
```

```python
# Python — same
client = FactorialClient()
```

> The TypeScript client reads `process.env`, so env-var fallback applies in Node-like
> runtimes; in the browser, pass credentials explicitly.

## Error handling

Both SDKs **fail loudly** on non-2xx responses (bad/expired token, wrong base URL,
server errors) instead of silently returning empty data:

- **TypeScript** throws — wrap calls in `try`/`catch`.
- **Python** raises `factorial_api_client.generated.errors.UnexpectedStatus`
  (with `.status_code` and `.content`).
