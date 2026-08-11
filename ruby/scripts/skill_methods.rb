#!/usr/bin/env ruby
# frozen_string_literal: true

# Emits the Ruby SDK call for every REST endpoint, as JSON on stdout:
#
#   { "GET /api/.../teams/teams": "api.teams_team.teams_teams_get", ... }
#
# Consumed by scripts/generate_skill.py to fill the Ruby column of the skill's
# reference/sdk-methods.md. Method names are never derived here: the
# operationIds come from normalize_oas.rb (the same normalization the real
# pipeline runs) and the owning accessor comes from reflecting on the loaded
# gem — so the table can only ever show calls that actually exist.
#
# Usage: bundle exec ruby scripts/skill_methods.rb <spec.(yaml|json)>

require 'fileutils'
require 'json'
require 'tmpdir'
require 'yaml'
require_relative '../lib/factorial_api'

VERBS = %w[get post put patch delete].freeze

spec_path = ARGV.fetch(0) { abort('Usage: skill_methods.rb <spec.(yaml|json)>') }
abort("ERROR: spec not found: #{spec_path}") unless File.exist?(spec_path)

# normalize_oas.rb names its output from a .yaml input; go through a temp copy
# so any input name (or a .json download) works and nothing is overwritten.
normalized = Dir.mktmpdir do |dir|
  tmp_spec = File.join(dir, 'spec.yaml')
  FileUtils.cp(spec_path, tmp_spec)
  system('ruby', File.expand_path('normalize_oas.rb', __dir__), tmp_spec, out: File::NULL) or
    abort('ERROR: normalize_oas.rb failed')
  YAML.unsafe_load_file(File.join(dir, 'spec.normalized.yaml'))
end

# operation_id => accessor, from the gem itself.
accessor_by_method = {}
F::Api::API_CLASSES.each do |accessor, const|
  F::Api.const_get(const).instance_methods(false).each do |method|
    next if method.to_s.end_with?('_with_http_info') || method.to_s.start_with?('api_client')

    accessor_by_method[method.to_s] = accessor
  end
end

calls = {}
normalized.fetch('paths').each do |route, item|
  VERBS.each do |verb|
    operation = item[verb] or next
    operation_id = operation.fetch('operationId')
    accessor = accessor_by_method.fetch(operation_id) do
      abort("ERROR: the gem exposes no method #{operation_id} (#{verb.upcase} #{route}) — regenerate it first")
    end
    calls["#{verb.upcase} #{route}"] = "api.#{accessor}.#{operation_id}"
  end
end

puts JSON.generate(calls)
