# Factorial API SDKs

Official auto-generated SDKs for the [Factorial API](https://apidoc.factorialhr.com), available for TypeScript and Python.

Both SDKs are generated from the OpenAPI spec and wrapped with a hand-written `FactorialClient` providing clean domain-namespaced access and cursor pagination helpers.

## SDKs

### TypeScript · `@factorial/api-client`

```bash
npm install @factorial/api-client
```

```ts
import { FactorialClient } from "@factorial/api-client";

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

SDK versions mirror the Factorial API version date using the format `YYYY.M.D`:

| API version | SDK version |
|-------------|-------------|
| `2026-04-01` | `2026.4.1` |
| `2026-07-01` | `2026.7.1` |

Factorial releases new API versions quarterly (Jan/Apr/Jul/Oct). To release a new SDK version:

1. Run the release script in the relevant SDK directory.
2. Enter the API version date (`yyyy-mm-dd`) when prompted.
3. The script fetches the spec from `https://api.factorialhr.com/oas/?version=<date>`, regenerates all generated code, and sets the SDK version automatically.
4. After building, it asks whether to publish — answer `y` to push to npm/PyPI or `n` to skip.

See the per-SDK READMEs for full instructions: [TypeScript](typescript/README.md) · [Python](python/README.md)

## Authentication

Both SDKs support:

- **API key** — via `apiKey:` / `api_key=` (sent as `x-api-key` header)
- **OAuth2 bearer token** — via `token:` / `token=` (sent as `Authorization: Bearer`)
