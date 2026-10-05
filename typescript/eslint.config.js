import tseslint from "typescript-eslint";

export default tseslint.config(
  {
    files: ["src/**/*.ts", "test/**/*.ts"],
    extends: [tseslint.configs.recommended],
  },
  {
    files: ["src/generated/**/*.ts"],
    // Generated files — suppress rules that fire on auto-generated code. The
    // generator emits some disable directives that are vacuous here, so don't
    // report those either: they can only be fixed upstream in openapi-ts.
    linterOptions: {
      reportUnusedDisableDirectives: "off",
    },
    rules: {
      "@typescript-eslint/no-explicit-any": "off",
      "@typescript-eslint/no-unused-vars": "off",
      "@typescript-eslint/ban-ts-comment": "off",
    },
  },
);
