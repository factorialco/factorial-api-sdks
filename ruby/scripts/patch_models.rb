#!/usr/bin/env ruby
# frozen_string_literal: true

# Post-generation patch for the generated models (stage 1.5).
#
# The OpenAPI spec marks many fields as required, but the live API returns
# `null` for some of them (e.g. ApiPublicCredential.employee_id is null for
# company-level credentials). openapi-generator emits attribute writers that
# unconditionally raise on nil:
#
#     def employee_id=(employee_id)
#       if employee_id.nil?
#         fail ArgumentError, 'employee_id cannot be nil'
#       end
#       @employee_id = employee_id
#     end
#
# ...which crashes the deserialization of otherwise valid API responses.
# This script rewrites those guards to tolerate nil (assign and return),
# leaving `valid?` / `list_invalid_properties` as the advisory validation
# layer. Same spirit as the Python SDK's enum null-safety post-patch in
# release.py (see the repo-level CLAUDE.md, "Known gotchas").
#
# Idempotent: a second run finds nothing left to patch.
# generate_sdk.rb must run this after every regeneration (the generator
# rewrites the models and reintroduces the raises).
#
# Usage: ruby scripts/patch_models.rb

MODELS_GLOB = File.expand_path('../lib/factorial_api/models/*.rb', __dir__)

NIL_GUARD = /
  if\ (\w+)\.nil\?\n
  (\s+)fail\ ArgumentError,\ '\1\ cannot\ be\ nil'\n
  (\s+)end
/x

patched_files = 0
patched_setters = 0

Dir.glob(MODELS_GLOB).each do |path|
  content = File.read(path, encoding: 'UTF-8')
  count = 0

  patched = content.gsub(NIL_GUARD) do
    count += 1
    name = Regexp.last_match(1)
    body_indent = Regexp.last_match(2)
    end_indent = Regexp.last_match(3)
    "if #{name}.nil?\n#{body_indent}@#{name} = nil\n#{body_indent}return\n#{end_indent}end"
  end

  next if count.zero?

  File.write(path, patched)
  patched_files += 1
  patched_setters += count
end

puts "Patched #{patched_setters} nil-raising setters across #{patched_files} model files"
