import { describe, expect, expectTypeOf, it } from "vitest";
import { FactorialApiError, isFactorialApiError } from "../src/index.js";
import {
  EMPLOYEE_LIST_QUERY,
  jsonResponse,
  makeClient,
  pageResponse,
  TEST_BASE_URL,
} from "./helpers.js";

describe("HTTP errors", () => {
  it("throws a FactorialApiError with the parsed body for a 401", async () => {
    const { client } = makeClient(() =>
      jsonResponse(401, { errors: null }, "Unauthorized"),
    );

    const error = await client.employees.employees
      .list({ query: EMPLOYEE_LIST_QUERY })
      .catch((err: unknown) => err);

    expect(error).toBeInstanceOf(FactorialApiError);
    expect(isFactorialApiError(error)).toBe(true);

    const apiError = error as FactorialApiError;
    expect(apiError.name).toBe("FactorialApiError");
    expect(apiError.status).toBe(401);
    expect(apiError.statusText).toBe("Unauthorized");
    expect(apiError.method).toBe("GET");
    expect(apiError.url).toContain("/resources/employees/employees");
    expect(apiError.body).toEqual({ errors: null });
    expect(apiError.headers.get("content-type")).toBe("application/json");
    expect(apiError.message).toBe(
      `Factorial API 401 Unauthorized: GET ${apiError.url} — {"errors":null}`,
    );
  });

  it("reports an empty error body as undefined and omits the excerpt", async () => {
    const { client } = makeClient(() => new Response(null, { status: 500 }));

    const error = await client.employees.employees
      .get({ path: { id: "1" } })
      .catch((err: unknown) => err);

    expect(error).toBeInstanceOf(FactorialApiError);
    const apiError = error as FactorialApiError;
    expect(apiError.status).toBe(500);
    expect(apiError.body).toBeUndefined();
    expect(apiError.message).toBe(
      `Factorial API 500: GET ${TEST_BASE_URL}/api/2026-07-01/resources/employees/employees/1`,
    );
  });

  it("keeps a non-JSON error body as a raw string", async () => {
    const { client } = makeClient(
      () =>
        new Response("<html>Bad Gateway</html>", {
          status: 502,
          headers: { "content-type": "text/html" },
        }),
    );

    const error = await client.timeoff.leaves
      .approve({ body: { id: "9" } })
      .catch((err: unknown) => err);

    expect(error).toBeInstanceOf(FactorialApiError);
    const apiError = error as FactorialApiError;
    expect(apiError.status).toBe(502);
    expect(apiError.method).toBe("POST");
    expect(apiError.body).toBe("<html>Bad Gateway</html>");
  });

  it("keeps a plain-text body raw even when the response claims JSON", async () => {
    // Observed on the live API: a 400 answers `Invalid parameters` under
    // `content-type: application/json`, so JSON.parse fails and the raw text
    // must survive onto the error rather than being lost.
    const { client } = makeClient(
      () =>
        new Response("Invalid parameters", {
          status: 400,
          statusText: "Bad Request",
          headers: { "content-type": "application/json; charset=utf-8" },
        }),
    );

    const error = (await client.employees.employees
      .list({ query: EMPLOYEE_LIST_QUERY })
      .catch((err: unknown) => err)) as FactorialApiError;

    expect(error).toBeInstanceOf(FactorialApiError);
    expect(error.status).toBe(400);
    expect(error.body).toBe("Invalid parameters");
    expect(error.message).toContain("Invalid parameters");
  });

  it("exposes the status so callers can branch without parsing the body", async () => {
    const statuses = [400, 401, 404, 429, 500];

    for (const status of statuses) {
      const { client } = makeClient(() => jsonResponse(status, { errors: null }));
      const error = (await client.employees.employees
        .get({ path: { id: "1" } })
        .catch((err: unknown) => err)) as FactorialApiError;

      expect(error).toBeInstanceOf(FactorialApiError);
      expect(error.status).toBe(status);
    }
  });

  it("truncates a long error body in the message but keeps it whole on the error", async () => {
    const detail = "x".repeat(500);
    const { client } = makeClient(() => jsonResponse(422, { detail }));

    const error = (await client.employees.employees
      .get({ path: { id: "1" } })
      .catch((err: unknown) => err)) as FactorialApiError;

    expect(error.message).toMatch(/…$/);
    expect(error.message.length).toBeLessThan(400);
    expect(error.body).toEqual({ detail });
  });

  it("keeps headers and response accessible but out of logged output", async () => {
    const { client } = makeClient(() => jsonResponse(429, { retry: true }));

    const error = (await client.employees.employees
      .get({ path: { id: "1" } })
      .catch((err: unknown) => err)) as FactorialApiError;

    // Accessible for callers that need them...
    expect(error.headers.get("content-type")).toBe("application/json");
    expect(error.response?.status).toBe(429);

    // ...but hidden from console.error / JSON.stringify, which would otherwise
    // bury the useful fields under the whole Response object.
    expect(Object.keys(error)).not.toContain("response");
    expect(Object.keys(error)).not.toContain("headers");
    expect(JSON.parse(JSON.stringify(error))).toMatchObject({
      status: 429,
      method: "GET",
      body: { retry: true },
    });
  });

  it("passes transport failures through unwrapped", async () => {
    const { client } = makeClient(() => {
      throw new TypeError("fetch failed");
    });

    const error = await client.employees.employees
      .get({ path: { id: "1" } })
      .catch((err: unknown) => err);

    expect(error).toBeInstanceOf(TypeError);
    expect(error).not.toBeInstanceOf(FactorialApiError);
    expect((error as TypeError).message).toBe("fetch failed");
  });

  it("rejects from all() with a FactorialApiError", async () => {
    const { client } = makeClient(() => jsonResponse(401, { errors: null }));

    await expect(client.employees.employees.all()).rejects.toBeInstanceOf(
      FactorialApiError,
    );
  });

  it("rejects from paginate() on a later page", async () => {
    const responses = [
      pageResponse([{ id: 1 }], { has_next_page: true, end_cursor: "c1" }),
      jsonResponse(500, { errors: ["boom"] }),
    ];
    const { client } = makeClient(() => responses.shift()!);

    const seen: unknown[] = [];
    const consume = async () => {
      for await (const item of client.employees.employees.paginate()) {
        seen.push(item);
      }
    };

    await expect(consume()).rejects.toBeInstanceOf(FactorialApiError);
    expect(seen).toHaveLength(1);
  });
});

describe("successful requests", () => {
  it("resolves to { data, request, response } and sends the API key", async () => {
    const { client, calls } = makeClient(() =>
      pageResponse([{ id: 1 }], { has_next_page: false }),
    );

    const result = await client.employees.employees.list({
      query: EMPLOYEE_LIST_QUERY,
    });

    expect(result.data.data).toHaveLength(1);
    expect(result.request).toBeInstanceOf(Request);
    expect(result.response.status).toBe(200);
    expect(calls[0]!.headers.get("x-api-key")).toBe("test-key");

    // The methods are typed as throwing, so the result carries no `error`.
    expectTypeOf(result).not.toHaveProperty("error");
    expectTypeOf(result).toHaveProperty("data");
  });

  it("follows end_cursor and forwards the page size", async () => {
    const responses = [
      pageResponse([{ id: 1 }], {
        has_next_page: true,
        end_cursor: "c1",
        total: 2,
      }),
      pageResponse([{ id: 2 }], { has_next_page: false, total: 2 }),
    ];
    const { client, calls } = makeClient(() => responses.shift()!);

    const all = await client.employees.employees.all({
      query: EMPLOYEE_LIST_QUERY,
      limit: 1,
    });

    expect(all).toHaveLength(2);
    expect(calls).toHaveLength(2);
    expect(new URL(calls[0]!.url).searchParams.get("limit")).toBe("1");
    expect(new URL(calls[1]!.url).searchParams.get("after_id")).toBe("c1");
  });

  it("stops at maxItems without fetching further pages", async () => {
    const { client, calls } = makeClient(() =>
      pageResponse([{ id: 1 }, { id: 2 }], {
        has_next_page: true,
        end_cursor: "c1",
        total: 99,
      }),
    );

    const all = await client.employees.employees.all({
      query: EMPLOYEE_LIST_QUERY,
      maxItems: 2,
    });

    expect(all).toHaveLength(2);
    expect(calls).toHaveLength(1);
  });
});
