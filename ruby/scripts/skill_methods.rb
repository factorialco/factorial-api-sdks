#!/usr/bin/env ruby
# frozen_string_literal: true

# Regenerates skills/factorial-api-sdks/reference/ruby-methods.json: the Ruby
# SDK call for every REST endpoint, keyed date-agnostically ("GET teams/teams").
#
# scripts/generate_skill.py reads that committed file to fill the Ruby column
# of reference/sdk-methods.md, so the TS/Python release flows never need a Ruby
# toolchain. The documented call is the ergonomic one (api.teams.team.get(id:),
# from the endpoint table shared with generate_sdk_layer.rb), and every row is
# verified by reflection against the emitted layer, so the map can only
# describe calls that exist with the signature they actually have. Optional
# query params and bodies travel in the trailing opts keywords, which the
# skill documents once rather than per row.
#
# Usage: bundle exec ruby scripts/skill_methods.rb <normalized-spec.yaml>

require 'json'
require 'yaml'
require_relative 'endpoint_table'

OUT = File.expand_path('../../skills/factorial-api-sdks/reference/ruby-methods.json', __dir__)

spec_path = ARGV.fetch(0) { abort('Usage: skill_methods.rb <normalized-spec.yaml>') }
abort("ERROR: spec not found: #{spec_path}") unless File.exist?(spec_path)
spec = YAML.unsafe_load_file(spec_path)

abort('ERROR: the ergonomic layer is not loaded — run scripts/generate_sdk_layer.rb first') unless
  defined?(F::Api::SDK)

endpoints, anomalies = EndpointTable.build(spec)
if anomalies.any?
  anomalies.each { |anomaly| warn "  - #{anomaly}" }
  abort("ERROR: #{anomalies.size} anomalies in the endpoint table")
end

calls = endpoints.to_h do |e|
  # The documented call must exist on the emitted layer with these exact
  # keywords — a stale lib/factorial_api/sdk.rb fails here, pointing at the
  # regeneration step instead of silently documenting a call that isn't there.
  begin
    resource = F::Api::SDK.const_get("#{EndpointTable.camelize(e.accessor)}Resource")
    keyreqs = resource.instance_method(e.name).parameters.filter_map { |kind, name| name if kind == :keyreq }
  rescue NameError
    abort("ERROR: sdk.rb has no #{e.namespace}.#{e.resource}.#{e.name} — re-run scripts/generate_sdk_layer.rb")
  end
  unless keyreqs == e.required
    abort("ERROR: sdk.rb is stale: #{e.namespace}.#{e.resource}.#{e.name} takes #{keyreqs.inspect} " \
          "but the gem requires #{e.required.inspect} — re-run scripts/generate_sdk_layer.rb")
  end

  signature = e.required.empty? ? '' : "(#{e.required.map { |name| "#{name}:" }.join(', ')})"
  ["#{e.verb.upcase} #{e.route}", "api.#{e.namespace}.#{e.resource}.#{e.name}#{signature}"]
end

File.write(OUT, "#{JSON.pretty_generate(calls)}\n")
puts "Wrote #{OUT} (#{calls.size} endpoints)"
