# frozen_string_literal: true

require 'yaml'
require_relative '../lib/factorial_api'

# The endpoint table shared by generate_sdk_layer.rb (which emits the
# ergonomic layer from it) and skill_methods.rb (which documents that layer in
# the skill's ruby-methods.json): one row per route×verb of the normalized
# spec, carrying the ergonomic classification and the owning raw method.
# Nothing is guessed: routes and operationIds come from the spec, and the
# owning accessor plus the required argument names come from reflecting on
# the loaded gem, so the table can only describe calls that exist with their
# real signature.
module EndpointTable
  VERBS  = %w[get post put patch delete].freeze
  PREFIX = %r{\A/api/\d{4}-\d{2}-\d{2}/resources/}

  # Verb → method name on a bare collection route and on a member ({id})
  # route; same classification table as the TS generator
  # (scripts/generate-sdk.ts). Any other non-parameter segment turns the
  # endpoint into a custom action named after those segments.
  COLLECTION_KIND = { 'get' => 'list', 'post' => 'create', 'put' => 'update',
                      'patch' => 'update', 'delete' => 'delete' }.freeze
  MEMBER_KIND = { 'get' => 'get', 'post' => 'create', 'put' => 'update',
                  'patch' => 'update', 'delete' => 'delete' }.freeze
  KIND_ORDER = %w[list get create update delete action].freeze

  Endpoint = Struct.new(:namespace, :resource, :name, :kind, :verb, :route,
                        :accessor, :raw_method, :required, keyword_init: true)

  module_function

  def camelize(snake) = snake.split('_').map(&:capitalize).join

  # Crosses the normalized spec's routes with the gem: returns the table plus
  # the structural anomalies no consumer may work past.
  def build(spec)
    owner_map = owners
    anomalies = []
    endpoints = []
    spec.fetch('paths').each do |full_route, item|
      VERBS.each do |verb|
        operation = item[verb] or next
        endpoints << row(full_route, verb, operation, owner_map, anomalies)
      end
    end
    integrity_checks(endpoints, owner_map, anomalies)
    [endpoints, anomalies]
  end

  # operationId → owning accessor, raw method and required positionals, from
  # the gem itself.
  def owners
    map = {}
    F::Api::API_CLASSES.each do |accessor, const|
      klass = F::Api.const_get(const)
      klass.instance_methods(false).each do |method|
        next if method.to_s.end_with?('_with_http_info') || method.to_s.start_with?('api_client')

        required = klass.instance_method(method).parameters.filter_map { |kind, name| name if kind == :req }
        map[method.to_s] = { accessor: accessor.to_s, method: method, required: required }
      end
    end
    map
  end

  def row(full_route, verb, operation, owner_map, anomalies)
    operation_id = operation['operationId'] ||
                   abort("ERROR: #{verb.upcase} #{full_route} has no operationId " \
                         '— pass the NORMALIZED spec (see scripts/normalize_oas.rb)')
    owner = owner_map.fetch(operation_id) do
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
    Endpoint.new(namespace:, resource:, kind:, verb:, route:,
                 name: action_parts.any? ? action_parts.join('_') : kind,
                 accessor: owner[:accessor], raw_method: owner[:method], required: owner[:required])
  end

  def integrity_checks(endpoints, owner_map, anomalies)
    orphans = owner_map.keys - endpoints.map { |e| e.raw_method.to_s }
    anomalies << "gem methods reachable from no endpoint: #{orphans.join(', ')}" if orphans.any?

    endpoints.group_by { |e| [e.namespace, e.resource] }.each do |(namespace, resource), rows|
      accessors = rows.map(&:accessor).uniq
      anomalies << "#{namespace}.#{resource} built from several classes: #{accessors.join(' + ')}" if accessors.size > 1
    end
  end
end
