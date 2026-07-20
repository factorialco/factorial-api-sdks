#!/usr/bin/env ruby
# frozen_string_literal: true

# Injects short operationIds (path without the /api/<date>/resources/ prefix)
# so that the generator produces filenames < 100 chars
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