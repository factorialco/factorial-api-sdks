# frozen_string_literal: true

# Handwritten specs for the F::Api facade (auth, base_url, accessors) and
# F::Api.paginate. Unlike the generated placeholder specs, these exercise the SDK
# end-to-end: every request goes through the full stack (facade -> generated
# client -> Faraday -> real TCP socket) against a local fake server, and the
# assertions inspect what actually went over the wire.

require 'spec_helper'
require_relative '../support/fake_factorial_server'

RSpec.describe F::Api do
  let(:server) { FakeFactorialServer.new }

  after { server.stop }

  # Keep the facade's env fallbacks out of the picture: values leaking in
  # from the developer's shell would silently change what these examples
  # exercise (and the env-fallback examples below set their own).
  around do |example|
    saved = %w[FACTORIAL_BASE_URL FACTORIAL_API_KEY FACTORIAL_TOKEN]
            .to_h { |name| [name, ENV.delete(name)] }
    example.run
  ensure
    saved.each { |name, value| value ? ENV[name] = value : ENV.delete(name) }
  end

  def build_api(**options)
    described_class.new(base_url: server.base_url, **options)
  end

  def last_request
    server.requests.last
  end

  describe 'authentication headers' do
    it 'sends only x-api-key when constructed with an api_key' do
      build_api(api_key: 'KEY', token: nil).teams_team.teams_teams_get

      expect(last_request[:headers]).to include('x-api-key' => 'KEY')
      expect(last_request[:headers]).not_to have_key('authorization')
    end

    it 'sends only a bearer token when constructed with a token' do
      build_api(api_key: nil, token: 'TOKEN').teams_team.teams_teams_get

      expect(last_request[:headers]).to include('authorization' => 'Bearer TOKEN')
      expect(last_request[:headers]).not_to have_key('x-api-key')
    end

    it 'sends both headers when both credentials are given' do
      build_api(api_key: 'KEY', token: 'TOKEN').teams_team.teams_teams_get

      expect(last_request[:headers]).to include(
        'x-api-key' => 'KEY',
        'authorization' => 'Bearer TOKEN'
      )
    end

    # Validation-only examples construct directly: no request is ever sent,
    # so there is no server to boot.
    it 'fails fast when constructed without credentials' do
      expect { described_class.new }
        .to raise_error(ArgumentError,
                        /provide api_key, token, oauth, or access_token \(or set FACTORIAL_API_KEY/)
    end

    it 'treats empty-string credentials (unset-but-exported env vars) as absent' do
      expect { described_class.new(api_key: '', token: '  ') }
        .to raise_error(ArgumentError, /provide api_key/)
    end
  end

  describe 'env credential fallback' do
    it 'falls back to env credentials only when none are passed' do
      ENV['FACTORIAL_API_KEY'] = 'ENV_KEY'

      build_api.teams_team.teams_teams_get

      expect(last_request[:headers]).to include('x-api-key' => 'ENV_KEY')
    end

    it 'ignores env credentials once any credential is passed explicitly' do
      ENV['FACTORIAL_TOKEN'] = 'ENV_LEFTOVER'
      ENV['FACTORIAL_API_KEY'] = 'ENV_KEY'
      session = instance_double(F::Api::OAuth::Session)
      allow(session).to receive(:access_token).and_return('SESSION')

      # Neither a "mutually exclusive" veto from the env token, nor an
      # x-api-key riding along from the env key.
      build_api(oauth: session).teams_team.teams_teams_get

      expect(last_request[:headers]['authorization']).to eq('Bearer SESSION')
      expect(last_request[:headers]).not_to have_key('x-api-key')
    end
  end

  describe 'oauth session integration' do
    it 'consults the session on every request: a token swap needs no client rebuild' do
      session = instance_double(F::Api::OAuth::Session)
      current_token = 'FIRST'
      allow(session).to receive(:access_token) { current_token }
      api = build_api(api_key: nil, token: nil, oauth: session)

      api.teams_team.teams_teams_get
      current_token = 'SECOND'
      api.teams_team.teams_teams_get

      bearers = server.requests.map { |r| r[:headers]['authorization'] }
      expect(bearers).to eq(['Bearer FIRST', 'Bearer SECOND'])
      expect(server.requests.last[:headers]).not_to have_key('x-api-key')
    end

    it 'rejects token and oauth together' do
      session = instance_double(F::Api::OAuth::Session, access_token: 'X')

      expect { described_class.new(token: 'T', oauth: session) }
        .to raise_error(ArgumentError, /mutually exclusive/)
    end

    it 'rejects an oauth source that does not respond to #access_token' do
      expect { described_class.new(oauth: 'a-raw-token-string') }
        .to raise_error(ArgumentError, /oauth must respond to #access_token/)
    end

    # The composition seam: `oauth:` is duck-typed on purpose, so any token
    # source can plug in without depending on this gem's Session class.
    it 'accepts any token source that responds to #access_token' do
      source = Class.new { def access_token = 'PLUGGED' }.new
      api = build_api(oauth: source)

      api.teams_team.teams_teams_get

      expect(last_request[:headers]['authorization']).to eq('Bearer PLUGGED')
    end

    it 'refuses to send a request when the token source yields no token' do
      api = build_api(access_token: -> {})

      expect { api.teams_team.teams_teams_get }
        .to raise_error(RuntimeError, /returned no token/)
      expect(server.requests).to be_empty
    end
  end

  describe 'access_token callable' do
    it 'evaluates the callable on every request, so one client can serve many callers' do
      current = 'FIRST'
      api = build_api(api_key: nil, token: nil, access_token: -> { current })

      api.teams_team.teams_teams_get
      current = 'SECOND'
      api.teams_team.teams_teams_get

      bearers = server.requests.map { |r| r[:headers]['authorization'] }
      expect(bearers).to eq(['Bearer FIRST', 'Bearer SECOND'])
    end

    it 'rejects a non-callable access_token, pointing at token: instead' do
      expect { described_class.new(access_token: 'A-STRING') }
        .to raise_error(ArgumentError, /must be callable.*use token:/)
    end

    it 'rejects access_token combined with another bearer source' do
      expect { described_class.new(token: 'T', access_token: -> { 'X' }) }
        .to raise_error(ArgumentError, /token and access_token are mutually exclusive/)

      session = instance_double(F::Api::OAuth::Session, access_token: 'X')
      expect { described_class.new(oauth: session, access_token: -> { 'X' }) }
        .to raise_error(ArgumentError, /oauth and access_token are mutually exclusive/)
    end
  end

  describe 'base_url' do
    it 'defaults to production over https' do
      config = described_class.new(api_key: 'k').client.config

      expect(config.scheme).to eq('https')
      expect(config.host).to eq('api.factorialhr.com')
    end

    it 'applies scheme, host, non-default port and base path from a full URL' do
      config = described_class
               .new(api_key: 'k', base_url: 'https://staging.example.com:8443/subpath')
               .client.config

      expect(config.scheme).to eq('https')
      expect(config.host).to eq('staging.example.com:8443')
      expect(config.base_path).to eq('/subpath')
    end

    it 'omits the port when it is the scheme default' do
      config = described_class
               .new(api_key: 'k', base_url: 'https://example.com:443')
               .client.config

      expect(config.host).to eq('example.com')
    end

    it 'rejects URLs without an http(s) scheme' do
      expect { described_class.new(api_key: 'k', base_url: 'localhost:3000') }
        .to raise_error(ArgumentError, /full http\(s\) URL/)
    end

    it 'falls back to the FACTORIAL_BASE_URL environment variable' do
      ENV['FACTORIAL_BASE_URL'] = 'http://fallback.example.com'

      config = described_class.new(api_key: 'k').client.config

      expect(config.scheme).to eq('http')
      expect(config.host).to eq('fallback.example.com')
    end
  end

  describe 'resource accessors' do
    it 'exposes one snake_case accessor per generated *Api class' do
      api = build_api(api_key: 'k')

      expect(described_class::API_CLASSES).to include(teams_team: :TeamsTeamApi)
      expect(api.teams_team).to be_a(F::Api::TeamsTeamApi)
    end

    it 'memoizes resource instances and shares one ApiClient' do
      api = build_api(api_key: 'k')

      expect(api.teams_team).to equal(api.teams_team)
      expect(api.teams_team.api_client).to equal(api.employees_employee.api_client)
    end
  end

  describe 'F::Api.paginate' do
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
    let(:api) { build_api(api_key: 'k') }

    def paginate(**options)
      F::Api.paginate(limit: 2, **options) do |page|
        api.teams_team.teams_teams_get(query_params: page)
      end
    end

    it 'follows cursors across pages via the query_params passthrough' do
      names = paginate.map(&:name)

      expect(names).to eq(%w[A B C])
      expect(server.requests.size).to eq(2)
      expect(server.requests.last[:line]).to include('after_id=2')
    end

    it 'is lazy: only fetches the pages the consumer actually needs' do
      first_team = paginate.first

      expect(first_team.name).to eq('A')
      expect(server.requests.size).to eq(1)
    end

    it 'stops at max_items without fetching further pages' do
      names = paginate(max_items: 2).map(&:name)

      expect(names).to eq(%w[A B])
      expect(server.requests.size).to eq(1)
    end
  end
end
