#!/usr/bin/env ruby
# frozen_string_literal: true

# Injects short operationIds into the OpenAPI spec before generation.
#
# Why: the source spec has no operationIds and defines many request/response
# schemas inline, so openapi-generator derives model names from the full
# route, producing file names like:
#
#   api20260701_resources_performance_review_questionnaire_by_strategies_
#   update_default_rating_scale_post_request.rb   (112 chars)
#
# A .gem package is a tar archive in ustar format, which caps each path
# component at 100 characters — `gem build` fails with
# Gem::Package::TooLongFileName on names like the one above.
#
# Fix: give every operation an operationId derived from its route minus the
# constant `/api/<date>/resources/` prefix. The worst name drops to 96 chars,
# and generated method names lose the noise too (`teams_teams_get` instead
# of `api20260701_resources_teams_teams_get`).
#
# NOTE: the remaining margin is only 4 characters. A future endpoint with a
# longer route will hit the limit again. The proper long-term fix is short
# operationIds (or named schemas) in the source spec — raised with the API
# team.
#
# Usage: ruby scripts/normalize_spec.rb oas-2026-07-01.yaml

require "yaml"

VERBS  = %w[get post put patch delete head options trace].freeze
PREFIX = %r{\A/api/\d{4}-\d{2}-\d{2}/resources/}

input  = ARGV.fetch(0)
output = input.sub(/\.yaml\z/, ".normalized.yaml")

spec = YAML.unsafe_load_file(input)

spec.fetch("paths").each do |route, item|
  VERBS.each do |verb|
    op = item[verb]
    next unless op
    next if op["operationId"]

    base = route.sub(PREFIX, "")
                .gsub(/[^a-zA-Z0-9]+/, "_")
                .delete_prefix("_")
                .delete_suffix("_")
    op["operationId"] = "#{base}_#{verb}"
  end
end

spec.delete("webhooks")
File.write(output, spec.to_yaml)
puts "Output file: #{output}"
