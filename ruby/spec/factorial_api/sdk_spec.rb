# frozen_string_literal: true

# Handwritten specs for the emitted ergonomic layer (lib/factorial_api/sdk.rb):
# domain-namespaced accessors (api.teams.team.list) over the generated client.
# The wire examples run the full stack against the local fake server and check
# what the ergonomic names actually put on the wire; the reflection examples
# pin the layer's completeness — every generated endpoint method must stay
# reachable through exactly one emitted resource.

require 'spec_helper'
require_relative '../support/fake_factorial_server'

RSpec.describe F::Api::SDK do
  let(:server) { FakeFactorialServer.new }
  let(:api) { build_api }

  after { server.stop }

  # Keep the facade's env fallbacks out of the picture (same rationale as
  # api_spec: shell leftovers must not change what these examples exercise).
  around do |example|
    saved = %w[FACTORIAL_BASE_URL FACTORIAL_API_KEY FACTORIAL_TOKEN]
            .to_h { |name| [name, ENV.delete(name)] }
    example.run
  ensure
    saved.each { |name, value| value ? ENV[name] = value : ENV.delete(name) }
  end

  def build_api(**options)
    F::Api.new(base_url: server.base_url, api_key: 'k', **options)
  end

  def last_request
    server.requests.last
  end

  describe 'wire classification' do
    # A bare `{}` deserializes into any generated model as all-nil attributes,
    # so one responder serves every verb; these examples only assert requests.
    before { server.responder = ->(_line, _body) { '{}' } }

    it 'sends list as GET on the collection' do
      api.teams.team.list

      expect(last_request[:line]).to match(%r{\AGET /api/\d{4}-\d{2}-\d{2}/resources/teams/teams[ ?]})
    end

    it 'sends get as GET on the member, interpolating the id keyword' do
      api.teams.team.get(id: 42)

      expect(last_request[:line]).to match(%r{\AGET /api/\d{4}-\d{2}-\d{2}/resources/teams/teams/42[ ?]})
    end

    it 'sends create as POST on the collection' do
      api.teams.team.create

      expect(last_request[:line]).to match(%r{\APOST /api/\d{4}-\d{2}-\d{2}/resources/teams/teams[ ?]})
    end

    it 'sends update as PUT on the member' do
      api.teams.team.update(id: 7)

      expect(last_request[:line]).to match(%r{\APUT /api/\d{4}-\d{2}-\d{2}/resources/teams/teams/7[ ?]})
    end

    it 'sends delete as DELETE on the member' do
      api.teams.team.delete(id: 7)

      expect(last_request[:line]).to match(%r{\ADELETE /api/\d{4}-\d{2}-\d{2}/resources/teams/teams/7[ ?]})
    end

    it 'sends a custom action as POST on its own segment' do
      api.employees.employee.terminate

      expect(last_request[:line])
        .to match(%r{\APOST /api/\d{4}-\d{2}-\d{2}/resources/employees/employees/terminate[ ?]})
    end
  end

  describe 'required keywords' do
    it 'fails fast on a missing keyword, before any request leaves' do
      expect { api.teams.team.get }.to raise_error(ArgumentError, /missing keyword.*id/)
      expect(server.requests).to be_empty
    end

    it 'sends required query keywords on the query string' do
      api.employees.employee.list(only_active: true, only_managers: false)

      expect(last_request[:line]).to include('only_active=true', 'only_managers=false')
    end

    it 'forwards extra keywords to the raw opts hash (query_params passthrough)' do
      api.teams.team.list(query_params: { special: 'yes' })

      expect(last_request[:line]).to include('special=yes')
    end
  end

  describe 'pagination' do
    let(:page1) do
      '{"data":[{"id":1,"name":"A","company_id":1},{"id":2,"name":"B","company_id":1}],' \
        '"meta":{"end_cursor":"2","has_next_page":true,"has_previous_page":false,"limit":2,"total":3}}'
    end
    let(:page2) do
      '{"data":[{"id":3,"name":"C","company_id":1}],' \
        '"meta":{"end_cursor":"3","has_next_page":false,"has_previous_page":true,"limit":2,"total":3}}'
    end
    let(:server) do
      FakeFactorialServer.new { |request_line| request_line.include?('after_id=2') ? page2 : page1 }
    end

    it 'paginate follows cursors across pages through the resource' do
      names = api.teams.team.paginate(limit: 2).map(&:name)

      expect(names).to eq(%w[A B C])
      expect(server.requests.size).to eq(2)
      expect(server.requests.last[:line]).to include('after_id=2')
    end

    it 'paginate is lazy: only fetches the pages the consumer needs' do
      first = api.teams.team.paginate(limit: 2).first

      expect(first.name).to eq('A')
      expect(server.requests.size).to eq(1)
    end

    it 'all collects every page into one Array' do
      teams = api.teams.team.all(limit: 2)

      expect(teams).to be_an(Array)
      expect(teams.map(&:name)).to eq(%w[A B C])
    end

    it 'paginate re-requires and forwards the required list keywords' do
      expect { api.employees.employee.paginate }
        .to raise_error(ArgumentError, /missing keyword/)

      api.employees.employee.paginate(only_active: true, only_managers: false).first

      expect(last_request[:line]).to include('only_active=true', 'only_managers=false')
    end
  end

  describe 'namespace accessors' do
    it 'memoizes namespaces and resources' do
      expect(api.teams).to equal(api.teams)
      expect(api.teams.team).to equal(api.teams.team)
    end

    it 'coexists with the raw accessors instead of replacing them' do
      expect(api.teams).to be_a(F::Api::SDK::TeamsNamespace)
      expect(api.teams_team).to be_a(F::Api::TeamsTeamApi)
    end
  end

  describe 'completeness' do
    # The emitted namespace accessors are the Client methods defined in
    # sdk.rb — the same way the generator itself tells them apart.
    def sdk_resources(client)
      namespaces = F::Api::Client.instance_methods.select do |method|
        F::Api::Client.instance_method(method).source_location&.first&.end_with?('lib/factorial_api/sdk.rb')
      end
      namespaces.map { |method| client.public_send(method) }
                .flat_map { |namespace| namespace.class.instance_methods(false).map { |m| namespace.public_send(m) } }
    end

    it 'wraps every generated Api class in exactly one resource' do
      wrapped = sdk_resources(api).map { |resource| resource.instance_variable_get(:@raw).class }

      expect(wrapped.map { |klass| klass.name.split('::').last.to_sym }.sort)
        .to eq(F::Api::API_CLASSES.values.sort)
    end

    it 'keeps every generated endpoint reachable: per-resource method counts match' do
      sdk_resources(api).each do |resource|
        raw_endpoints = resource.instance_variable_get(:@raw).class.instance_methods(false).reject do |method|
          method.to_s.end_with?('_with_http_info') || method.to_s.start_with?('api_client')
        end
        # A name collision would silently overwrite a method and shrink this
        # count, so equality also proves the emitted names are collision-free.
        ergonomic = resource.class.instance_methods(false) - %i[paginate all]

        expect(ergonomic.size).to eq(raw_endpoints.size),
                                  "#{resource.class.name}: #{ergonomic.size} methods " \
                                  "for #{raw_endpoints.size} raw endpoints"
      end
    end

    it 'emits paginate and all exactly on the resources that can list' do
      sdk_resources(api).each do |resource|
        expect(resource.respond_to?(:paginate)).to eq(resource.respond_to?(:list))
        expect(resource.respond_to?(:all)).to eq(resource.respond_to?(:list))
      end
    end
  end
end
