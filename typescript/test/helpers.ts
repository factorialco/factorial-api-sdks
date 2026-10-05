import { FactorialClient } from "../src/index.js";

/** Base URL used by every test, so assertions never depend on the real host. */
export const TEST_BASE_URL = "https://api.example.test";

/** Query params required by the employees list endpoint's spec. */
export const EMPLOYEE_LIST_QUERY = {
  only_active: true,
  only_managers: false,
} as const;

type Handler = (request: Request) => Response | Promise<Response>;

/**
 * Builds a `FactorialClient` backed by a fake `fetch`, plus the list of requests
 * it received. The client passes unknown config through to the underlying fetch
 * client, so `fetch` is injectable without touching globals.
 */
export function makeClient(handler: Handler): {
  client: FactorialClient;
  calls: Request[];
} {
  const calls: Request[] = [];
  const fetch = async (
    input: RequestInfo | URL,
    init?: RequestInit,
  ): Promise<Response> => {
    const request = input instanceof Request ? input : new Request(input, init);
    calls.push(request);
    return handler(request);
  };

  const client = new FactorialClient({
    apiKey: "test-key",
    baseUrl: TEST_BASE_URL,
    fetch: fetch as typeof globalThis.fetch,
  });

  return { client, calls };
}

/** Builds a JSON response with an optional reason phrase. */
export function jsonResponse(
  status: number,
  body: unknown,
  statusText = "",
): Response {
  return new Response(JSON.stringify(body), {
    status,
    statusText,
    headers: { "content-type": "application/json" },
  });
}

/** Builds a single page of a cursor-paginated list response. */
export function pageResponse(
  items: unknown[],
  meta: { has_next_page: boolean; end_cursor?: string; total?: number },
): Response {
  return jsonResponse(200, {
    data: items,
    meta: {
      has_previous_page: false,
      has_next_page: meta.has_next_page,
      end_cursor: meta.end_cursor,
      limit: items.length,
      total: meta.total ?? items.length,
    },
  });
}
