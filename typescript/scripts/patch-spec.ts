/**
 * Spec fixes applied before openapi-ts parses the Factorial OpenAPI document
 * (wired in via `parser.patch.input` in openapi-ts.config.ts).
 *
 * The Factorial spec declares some array schemas with the `enum` on the array
 * itself instead of on its items:
 *
 *   { "type": "array", "enum": ["a3innuva", "a3nom"], "items": { "type": "string" } }
 *
 * openapi-ts reads that `enum` as the type of the whole value, so the generated
 * type is a single literal union and the array is lost (see issue #43, the
 * `integrations[]` query parameter). The values are clearly item values, so we
 * move the enum onto `items`, which generates `Array<"a3innuva" | "a3nom">`.
 */

type JsonObject = Record<string, unknown>;

const isObject = (value: unknown): value is JsonObject =>
  typeof value === "object" && value !== null && !Array.isArray(value);

const isArraySchema = (schema: JsonObject): boolean =>
  schema.type === "array" ||
  (Array.isArray(schema.type) && schema.type.includes("array"));

const isPrimitive = (value: unknown): boolean =>
  value === null || ["string", "number", "boolean"].includes(typeof value);

/**
 * Walks the whole spec and moves array-level enums of primitive values onto the
 * array's inline `items` schema. Leaves alone enums whose members are arrays,
 * items that are `$ref`s, and items that already declare their own enum.
 * Mutates `spec` in place and returns the number of schemas changed.
 */
export function moveArrayEnumsToItems(spec: unknown): number {
  let changed = 0;
  const seen = new Set<unknown>();

  const visit = (node: unknown): void => {
    if (typeof node !== "object" || node === null || seen.has(node)) return;
    seen.add(node);

    if (Array.isArray(node)) {
      node.forEach(visit);
      return;
    }

    const schema = node as JsonObject;
    const items = schema.items;
    if (
      isArraySchema(schema) &&
      Array.isArray(schema.enum) &&
      schema.enum.every(isPrimitive) &&
      isObject(items) &&
      items.$ref === undefined &&
      items.enum === undefined
    ) {
      items.enum = schema.enum;
      delete schema.enum;
      changed += 1;
    }

    Object.values(schema).forEach(visit);
  };

  visit(spec);
  return changed;
}
