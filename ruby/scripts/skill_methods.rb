#!/usr/bin/env ruby
# frozen_string_literal: true

# Regenerates skills/factorial-api-sdks/reference/ruby-methods.json: the Ruby
# SDK call for every REST endpoint, keyed date-agnostically ("GET teams/teams").
#
# scripts/generate_skill.py reads that committed file to fill the Ruby column
# of reference/sdk-methods.md, so the TS/Python release flows never need a Ruby
# toolchain. Method names are never derived here: operationIds come from the
# normalized spec (scripts/normalize_oas.rb) and the owning accessor from
# reflecting on the loaded gem, so the map can only contain calls that exist.
#
# Usage: bundle exec ruby scripts/skill_methods.rb <normalized-spec.yaml>

require 'json'
require 'yaml'
require_relative '../lib/factorial_api'

VERBS  = %w[get post put patch delete].freeze
PREFIX = %r{\A/api/\d{4}-\d{2}-\d{2}/resources/}
OUT    = File.expand_path('../../skills/factorial-api-sdks/reference/ruby-methods.json', __dir__)

spec_path = ARGV.fetch(0) { abort('Usage: skill_methods.rb <normalized-spec.yaml>') }
abort("ERROR: spec not found: #{spec_path}") unless File.exist?(spec_path)
spec = YAML.unsafe_load_file(spec_path)

# operation_id => accessor, from the gem itself.
accessor_by_method = {}
F::Api::API_CLASSES.each do |accessor, const|
  F::Api.const_get(const).instance_methods(false).each do |method|
    next if method.to_s.end_with?('_with_http_info') || method.to_s.start_with?('api_client')

    accessor_by_method[method.to_s] = accessor
  end
end

calls = {}
spec.fetch('paths').each do |route, item|
  VERBS.each do |verb|
    operation = item[verb] or next
    operation_id = operation['operationId'] ||
                   abort("ERROR: #{verb.upcase} #{route} has no operationId " \
                         '- pass the NORMALIZED spec (see scripts/normalize_oas.rb)')
    accessor = accessor_by_method.fetch(operation_id) do
      abort("ERROR: the gem exposes no method #{operation_id} (#{verb.upcase} #{route}) " \
            '- regenerate the gem first')
    end
    calls["#{verb.upcase} #{route.sub(PREFIX, '')}"] = "api.#{accessor}.#{operation_id}"
  end
end

File.write(OUT, "#{JSON.pretty_generate(calls)}\n")
puts "Wrote #{OUT} (#{calls.size} endpoints)"
