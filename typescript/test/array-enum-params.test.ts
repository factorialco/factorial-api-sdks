import { describe, expect, it } from "vitest";
import { moveArrayEnumsToItems } from "../scripts/patch-spec.js";
import { makeClient, pageResponse } from "./helpers.js";

describe("array-of-enum query params (#43)", () => {
  it("accepts and sends several values for integrations[]", async () => {
    const { client, calls } = makeClient(() =>
      pageResponse([], { has_next_page: false }),
    );

    await client.payrollIntegrationsBase.codes.list({
      query: { "integrations[]": ["a3innuva", "a3nom"] },
    });

    expect(calls).toHaveLength(1);
    const url = new URL(calls[0].url);
    expect(url.searchParams.getAll("integrations[]")).toEqual([
      "a3innuva",
      "a3nom",
    ]);
  });

  it("still rejects values outside the enum at compile time", async () => {
    const { client } = makeClient(() =>
      pageResponse([], { has_next_page: false }),
    );

    await client.payrollIntegrationsBase.codes.list({
      // @ts-expect-error "not_an_integration" is not a payroll integration
      query: { "integrations[]": ["not_an_integration"] },
    });
  });
});

describe("moveArrayEnumsToItems", () => {
  it("moves an array-level enum onto the items of a parameter schema", () => {
    const spec = {
      openapi: "3.0.3",
      paths: {
        "/codes": {
          get: {
            parameters: [
              {
                name: "integrations[]",
                in: "query",
                schema: {
                  type: "array",
                  enum: ["a3innuva", "a3nom"],
                  items: { type: "string" },
                },
              },
            ],
          },
        },
      },
    };

    expect(moveArrayEnumsToItems(spec)).toBe(1);
    expect(spec.paths["/codes"].get.parameters[0].schema).toEqual({
      type: "array",
      items: { type: "string", enum: ["a3innuva", "a3nom"] },
    });
  });

  it("handles OpenAPI 3.1 type arrays in component properties", () => {
    const spec = {
      openapi: "3.1.0",
      components: {
        schemas: {
          process: {
            type: "object",
            properties: {
              reviewer_strategies: {
                type: ["array", "null"],
                enum: ["self", "manager"],
                items: { type: "string" },
              },
            },
          },
        },
      },
    };

    expect(moveArrayEnumsToItems(spec)).toBe(1);
    expect(
      spec.components.schemas.process.properties.reviewer_strategies,
    ).toEqual({
      type: ["array", "null"],
      items: { type: "string", enum: ["self", "manager"] },
    });
  });

  it("leaves schemas it cannot safely rewrite untouched", () => {
    const untouched = {
      // enum of whole arrays: the enum really describes the array value
      wholeArrays: {
        type: "array",
        enum: [["a", "b"]],
        items: { type: "string" },
      },
      // items is a $ref: the enum cannot be merged into a reference
      refItems: {
        type: "array",
        enum: ["a"],
        items: { $ref: "#/components/schemas/x" },
      },
      // items already has its own enum
      itemEnum: {
        type: "array",
        enum: ["a"],
        items: { type: "string", enum: ["a", "b"] },
      },
      // a plain string enum is not an array schema
      plainEnum: { type: "string", enum: ["a", "b"] },
    };
    const before = structuredClone(untouched);

    expect(moveArrayEnumsToItems(untouched)).toBe(0);
    expect(untouched).toEqual(before);
  });
});
