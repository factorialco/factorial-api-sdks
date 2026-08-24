#!/usr/bin/env ruby
# frozen_string_literal: true

# Stage-2 generator for the ergonomic layer (api.employees.employee.list).
#
# Phase 1: builds the endpoint table the emitter will consume — namespace,
# resource, CRUD-or-action classification, owning raw accessor + method and
# required parameters — by crossing the normalized spec's routes with
# reflection on the loaded gem, the same technique as scripts/skill_methods.rb.
# Nothing is guessed: routes and operationIds come from the spec, and the
# owning accessor plus the required argument names come from the gem itself,
# so the table can only describe calls that exist with their real signature.
#
#   bundle exec ruby scripts/generate_sdk_layer.rb --dry-run [normalized-spec]
#
# --dry-run prints the full table (grouped namespace → resource → method)
# plus everything worth eyeballing before emitting code: name collisions,
# actions landing on reserved names, and structural anomalies. Code emission
# (lib/factorial_api/sdk.rb) arrives in a later phase.

require 'yaml'
require_relative '../lib/factorial_api'

VERBS  = %w[get post put patch delete].freeze
PREFIX = %r{\A/api/\d{4}-\d{2}-\d{2}/resources/}

# Verb → method name on a bare collection route and on a member ({id}) route;
# same classification table as the TS generator (scripts/generate-sdk.ts).
# Any other non-parameter segment turns the endpoint into a custom action
# named after those segments.
COLLECTION_KIND = { 'get' => 'list', 'post' => 'create', 'put' => 'update',
                    'patch' => 'update', 'delete' => 'delete' }.freeze
MEMBER_KIND = { 'get' => 'get', 'post' => 'create', 'put' => 'update',
                'patch' => 'update', 'delete' => 'delete' }.freeze
KIND_ORDER = %w[list get create update delete action].freeze

# Names the layer itself defines on every resource: an action that lands on
# one of these must be resolved by the collision strategy (phase 2).
RESERVED = %w[all paginate collect_all].freeze

Endpoint = Struct.new(:namespace, :resource, :name, :kind, :verb, :route,
                      :accessor, :raw_method, :required, keyword_init: true)

dry_run   = ARGV.delete('--dry-run')
spec_path = ARGV.fetch(0) { Dir.glob('oas-*.normalized.yaml').max }
abort('ERROR: no normalized spec found — pass one or run scripts/normalize_oas.rb first') unless spec_path
abort("ERROR: spec not found: #{spec_path}") unless File.exist?(spec_path)
abort('ERROR: only --dry-run is implemented (emission arrives in phase 2)') unless dry_run

spec = YAML.unsafe_load_file(spec_path)

# --- 1. Reflect on the gem: operationId → owning accessor, method, requireds
owners = {}
F::Api::API_CLASSES.each do |accessor, const|
  klass = F::Api.const_get(const)
  klass.instance_methods(false).each do |method|
    next if method.to_s.end_with?('_with_http_info') || method.to_s.start_with?('api_client')

    required = klass.instance_method(method).parameters.filter_map { |kind, name| name if kind == :req }
    owners[method.to_s] = { accessor: accessor.to_s, method: method, required: required }
  end
end

# --- 2. Cross with the spec's routes: one table row per endpoint
anomalies = []
endpoints = []
spec.fetch('paths').each do |full_route, item|
  VERBS.each do |verb|
    operation = item[verb] or next
    operation_id = operation['operationId'] ||
                   abort("ERROR: #{verb.upcase} #{full_route} has no operationId " \
                         '— pass the NORMALIZED spec (see scripts/normalize_oas.rb)')
    owner = owners.fetch(operation_id) do
      abort("ERROR: the gem exposes no method #{operation_id} (#{verb.upcase} #{full_route}) " \
            '— regenerate the gem first')
    end

    route = full_route.sub(PREFIX, '')
    segments = route.split('/')
    # Namespace = first route segment; the accessor (from the generated class
    # name) is "<namespace>_<singular resource>", so stripping the namespace
    # prefix yields the resource. Both facts are checked, not assumed.
    namespace = segments.first.to_s.gsub(/[^a-zA-Z0-9]+/, '_')
    resource  = owner[:accessor].delete_prefix("#{namespace}_")
    if resource == owner[:accessor] || resource.empty?
      anomalies << "#{verb.upcase} #{route}: accessor #{owner[:accessor]} does not start with '#{namespace}_'"
    end
    anomalies << "#{verb.upcase} #{route}: route has no collection segment" if segments.size < 2

    tail = segments.drop(2)
    action_parts = tail.reject { |segment| segment.start_with?('{') }
    kind =
      if action_parts.any?
        'action'
      elsif tail.empty?
        COLLECTION_KIND.fetch(verb)
      else
        MEMBER_KIND.fetch(verb)
      end
    endpoints << Endpoint.new(namespace:, resource:, kind:, verb:, route:,
                              name: action_parts.any? ? action_parts.join('_') : kind,
                              accessor: owner[:accessor], raw_method: owner[:method],
                              required: owner[:required])
  end
end

# --- 3. Cross-checks the emitter will rely on
orphans = owners.keys - endpoints.map { |e| e.raw_method.to_s }
anomalies << "gem methods reachable from no endpoint: #{orphans.join(', ')}" if orphans.any?

namespaces = endpoints.map(&:namespace).uniq.sort
clashes = namespaces & F::Api::Client.instance_methods.map(&:to_s)
anomalies << "namespace accessor(s) would collide on Client: #{clashes.join(', ')}" if clashes.any?

endpoints.group_by { |e| [e.namespace, e.resource] }.each do |(namespace, resource), rows|
  accessors = rows.map(&:accessor).uniq
  anomalies << "#{namespace}.#{resource} built from several classes: #{accessors.join(' + ')}" if accessors.size > 1
end

collisions = endpoints.group_by { |e| [e.namespace, e.resource, e.name] }
                      .select { |_, rows| rows.size > 1 }
reserved_hits = endpoints.select { |e| e.kind == 'action' && RESERVED.include?(e.name) }

# --- 4. Dump the table
puts "#{endpoints.size} endpoints → #{namespaces.size} namespaces, " \
     "#{endpoints.map { |e| [e.namespace, e.resource] }.uniq.size} resources (spec: #{spec_path})"

endpoints.group_by(&:namespace).sort.each do |namespace, ns_rows|
  puts "\n#{namespace}"
  ns_rows.group_by(&:resource).sort.each do |resource, rows|
    puts "  .#{resource}  (raw: api.#{rows.first.accessor})"
    rows.sort_by { |e| [KIND_ORDER.index(e.kind), e.name, e.verb] }.each do |e|
      kwargs = e.required.map { |name| "#{name}:" }.join(', ')
      puts "    #{e.name.ljust(32)} #{e.verb.upcase.ljust(6)} #{e.route.ljust(56)} #{kwargs}".rstrip
    end
  end
end

kinds = endpoints.group_by(&:kind).transform_values(&:size)
puts "\nBy kind: #{KIND_ORDER.map { |kind| "#{kind}=#{kinds.fetch(kind, 0)}" }.join(' ')}"

if collisions.any?
  puts "\nName collisions (strategy: the action keeps its name, the collector yields, then numeric suffix):"
  collisions.sort.each do |(namespace, resource, name), rows|
    puts "  #{namespace}.#{resource}.#{name}: #{rows.map { |e| "#{e.verb.upcase} #{e.route}" }.join(' | ')}"
  end
end

if reserved_hits.any?
  puts "\nActions landing on reserved names (#{RESERVED.join('/')}):"
  reserved_hits.each { |e| puts "  #{e.namespace}.#{e.resource}.#{e.name} (#{e.verb.upcase} #{e.route})" }
end

if anomalies.any?
  puts "\nANOMALIES:"
  anomalies.each { |anomaly| puts "  - #{anomaly}" }
  abort("ERROR: #{anomalies.size} anomalies — understand them before emitting anything")
end

puts "\nOK: table is emittable (collisions above are resolved by the phase-2 strategy)"
