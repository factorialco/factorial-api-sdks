#!/usr/bin/env ruby
# frozen_string_literal: true

# Stage-2 generator for the ergonomic layer (api.employees.employee.list).
#
# From the endpoint table (scripts/endpoint_table.rb: the normalized spec's
# routes crossed with reflection on the loaded gem) it emits
# lib/factorial_api/sdk.rb: one Resource class per generated Api class, one
# Namespace class per domain, and the namespace accessors that reopen
# F::Api::Client — api.rb is never touched.
#
#   bundle exec ruby scripts/generate_sdk_layer.rb [normalized-spec]            # emit
#   bundle exec ruby scripts/generate_sdk_layer.rb --dry-run [normalized-spec]  # table only
#
# --dry-run prints the full table (grouped namespace → resource → method).
# Both modes refuse to proceed past name collisions, actions landing on
# reserved names, or structural anomalies, so a spec change that introduces
# one fails loudly instead of silently emitting a broken layer.

require 'yaml'
require_relative 'endpoint_table'

SDK_FILE     = File.expand_path('../lib/factorial_api/sdk.rb', __dir__)
ENTRYPOINT   = File.expand_path('../lib/factorial_api.rb', __dir__)
REQUIRE_LINE = "require 'factorial_api/sdk'"

KIND_ORDER = EndpointTable::KIND_ORDER

# Names the layer itself defines on every listable resource: an action that
# lands on one of these needs a conscious rename before emitting.
RESERVED = %w[all paginate collect_all].freeze

# Required params are re-exposed as keywords and referenced bare inside the
# emitted bodies, so they cannot be Ruby keywords nor collide with the
# emitted machinery (`opts`, and on list: paginate's own parameters).
RUBY_KEYWORDS = %w[alias and begin break case class def do else elsif end ensure false for if in
                   module next nil not or redo rescue retry return self super then true undef
                   unless until when while yield].freeze
FORBIDDEN_PARAMS  = (RUBY_KEYWORDS + %w[opts]).freeze
FORBIDDEN_ON_LIST = %w[limit max_items page].freeze

# Prefixes every non-empty line with `levels` two-space steps.
def indent(text, levels) = text.gsub(/^(?!$)/, '  ' * levels)

def kwargs_signature(required) = (required.map { |name| "#{name}:" } + ['**opts']).join(', ')

def kwargs_forward(required) = (required.map { |name| "#{name}: #{name}" } + ['**opts']).join(', ')

# The paginate/all pair, only emitted when the resource has a list endpoint.
# Cursor params travel per page through the raw method's query_params
# passthrough; the cursor's own keys win over caller-supplied ones.
def pagination_lines(list)
  paginate_signature = (list.required.map { |name| "#{name}:" } +
                        ['limit: nil', 'max_items: nil', '**opts']).join(', ')
  forward = kwargs_forward(list.required)
  ['',
   '  # Lazy Enumerator over every list page (see F::Api.paginate).',
   "  def paginate(#{paginate_signature})",
   '    F::Api.paginate(limit: limit, max_items: max_items) do |page|',
   "      list(#{forward}, query_params: (opts[:query_params] || {}).merge(page))",
   '    end',
   '  end',
   '',
   '  # Fetches every list page into one Array.',
   "  def all(#{kwargs_signature(list.required)})",
   "    paginate(#{forward}).to_a",
   '  end']
end

def emit_resource(rows)
  first = rows.first
  lines = ["# api.#{first.namespace}.#{first.resource} — wraps the raw api.#{first.accessor}.",
           "class #{EndpointTable.camelize(first.accessor)}Resource",
           '  def initialize(client)',
           "    @raw = client.#{first.accessor}",
           '  end']
  sorted = rows.sort_by { |e| [KIND_ORDER.index(e.kind), e.name, e.verb] }
  sorted.each do |e|
    lines << ''
    lines << "  # #{e.verb.upcase} #{e.route}"
    lines << "  def #{e.name}(#{kwargs_signature(e.required)})"
    lines << "    @raw.#{e.raw_method}(#{(e.required.map(&:to_s) + ['opts']).join(', ')})"
    lines << '  end'
  end
  list = sorted.find { |e| e.name == 'list' }
  lines.concat(pagination_lines(list)) if list
  lines << 'end'
  lines.join("\n")
end

def emit_namespace(namespace, resources)
  lines = ["# api.#{namespace}.* — one accessor per resource.",
           "class #{EndpointTable.camelize(namespace)}Namespace",
           '  def initialize(client)',
           '    @client = client',
           '  end']
  resources.sort.each do |resource, resource_class|
    lines << ''
    lines << "  def #{resource}"
    lines << "    @#{resource} ||= #{resource_class}.new(@client)"
    lines << '  end'
  end
  lines << 'end'
  lines.join("\n")
end

def emit_client_reopen(namespaces)
  lines = ['# The ergonomic entry points: one accessor per domain namespace, added',
           '# to the facade without touching the handwritten api.rb (Ruby classes',
           '# are open, so this ADDS methods to the Client defined there).',
           'class Client']
  namespaces.each_with_index do |namespace, index|
    lines << '' if index.positive?
    lines << "  def #{namespace}"
    lines << "    @sdk_#{namespace} ||= SDK::#{EndpointTable.camelize(namespace)}Namespace.new(self)"
    lines << '  end'
  end
  lines << 'end'
  lines.join("\n")
end

dry_run   = ARGV.delete('--dry-run')
spec_path = ARGV.fetch(0) { Dir.glob('oas-*.normalized.yaml').max }
abort('ERROR: no normalized spec found — pass one or run scripts/normalize_oas.rb first') unless spec_path
abort("ERROR: spec not found: #{spec_path}") unless File.exist?(spec_path)

spec = YAML.unsafe_load_file(spec_path)
spec_date = spec.dig('info', 'version')

# --- 1. Build the endpoint table (shared with skill_methods.rb)
endpoints, anomalies = EndpointTable.build(spec)

# --- 2. Emission-policy checks on top of the table's structural ones
namespaces = endpoints.map(&:namespace).uniq.sort
# Ignore accessors a previously emitted sdk.rb already put on Client (the
# script loads the gem, so its own output is visible on re-runs).
taken = F::Api::Client.instance_methods.reject do |method|
  F::Api::Client.instance_method(method).source_location&.first&.end_with?('lib/factorial_api/sdk.rb')
end.map(&:to_s)
clashes = namespaces & taken
anomalies << "namespace accessor(s) would collide on Client: #{clashes.join(', ')}" if clashes.any?

object_methods = Object.instance_methods.map(&:to_s)
shadowed = (endpoints.map(&:resource).uniq + endpoints.map(&:name).uniq).uniq & object_methods
anomalies << "emitted names would shadow Object methods: #{shadowed.join(', ')}" if shadowed.any?

endpoints.each do |e|
  bad = e.required.map(&:to_s) & FORBIDDEN_PARAMS
  anomalies << "#{e.namespace}.#{e.resource}.#{e.name}: required param(s) unusable as keywords: #{bad.join(', ')}" if
    bad.any?
  next unless e.name == 'list'

  clash = e.required.map(&:to_s) & FORBIDDEN_ON_LIST
  anomalies << "#{e.namespace}.#{e.resource}.list: required #{clash.join(', ')} collide with paginate params" if
    clash.any?
end

collisions = endpoints.group_by { |e| [e.namespace, e.resource, e.name] }
                      .select { |_, rows| rows.size > 1 }
collisions.sort.each do |(namespace, resource, name), rows|
  routes = rows.map { |e| "#{e.verb.upcase} #{e.route}" }.join(' | ')
  anomalies << "duplicate method #{namespace}.#{resource}.#{name}: #{routes}"
end
endpoints.select { |e| e.kind == 'action' && RESERVED.include?(e.name) }.each do |e|
  anomalies << "#{e.namespace}.#{e.resource}: action lands on reserved name '#{e.name}' (#{e.verb.upcase} #{e.route})"
end

# --- 3. Dry-run: dump the table
if dry_run
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
end

if anomalies.any?
  puts "\nANOMALIES:"
  anomalies.each { |anomaly| puts "  - #{anomaly}" }
  abort("ERROR: #{anomalies.size} anomalies — understand them before emitting anything")
end

if dry_run
  puts "\nOK: table is emittable"
  exit
end

# --- 4. Emit lib/factorial_api/sdk.rb
resource_blocks = endpoints.group_by { |e| [e.namespace, e.resource] }.sort
                           .map { |_, rows| emit_resource(rows) }
namespace_blocks = endpoints.group_by(&:namespace).sort.map do |namespace, rows|
  resources = rows.map { |e| [e.resource, "#{EndpointTable.camelize(e.accessor)}Resource"] }.uniq
  emit_namespace(namespace, resources)
end

content = +''
content << <<~HEADER
  # frozen_string_literal: true

  # GENERATED by scripts/generate_sdk_layer.rb from the #{spec_date} spec — DO NOT EDIT.
  #
  # Domain-namespaced ergonomic layer over the generated client:
  #
  #   api = F::Api.new(api_key: '...')
  #   api.employees.employee.list(only_active: true, only_managers: false)
  #   api.teams.team.get(id: 123)
  #   api.timeoff.leave.paginate(max_items: 500).each { |leave| ... }
  #
  # Every call goes through the same shared ApiClient as the raw accessors
  # (api.employees_employee.employees_employees_get), which keep working.

  require 'factorial_api/api'

  module F
    module Api
      # Emitted namespace/resource classes live in their own module so they
      # can never collide with the generated model classes under F::Api.
      module SDK
HEADER
content << indent((resource_blocks + namespace_blocks).join("\n\n"), 3)
content << "\n    end\n\n"
content << indent(emit_client_reopen(namespaces), 2)
content << "\n  end\nend\n"

File.write(SDK_FILE, content)

# Idempotently wire the emitted file into the entrypoint, after the facade's
# own require (same mechanism as generate_sdk.rb step 8).
entry = File.read(ENTRYPOINT)
File.open(ENTRYPOINT, 'a') { |f| f.puts(REQUIRE_LINE) } unless entry.include?(REQUIRE_LINE)

puts "Wrote #{SDK_FILE}"
puts "  #{namespaces.size} namespaces, #{resource_blocks.size} resources, " \
     "#{endpoints.size} endpoint methods (+ paginate/all on #{endpoints.count { |e| e.name == 'list' }} listables)"
