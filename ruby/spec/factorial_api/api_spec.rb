# frozen_string_literal: true

# Handwritten specs for the F::Api facade (auth, base_url, accessors) and
# F.paginate. Unlike the generated placeholder specs, these exercise the SDK
# end-to-end: every request goes through the full stack (facade -> generated
# client -> Faraday -> real TCP socket) against a local fake server, and the
# assertions inspect what actually went over the wire.

require "spec_helper"
require "socket"

# Minimal single-threaded HTTP server on a random free port. Records every
# request it receives (request line + headers) and answers with the JSON the
# `responder` block returns for the given request line.
class FakeFactorialServer
  EMPTY_PAGE = '{"data":[],"meta":{"end_cursor":null,"has_next_page":false,' \
               '"has_previous_page":false,"limit":100,"total":0}}'

  attr_reader :requests

  def initialize(&responder)
    @server = TCPServer.new("127.0.0.1", 0)
    @responder = responder || ->(_request_line) { EMPTY_PAGE }
    @requests = []
    @thread = Thread.new { serve }
  end

  def base_url
    "http://127.0.0.1:#{@server.addr[1]}"
  end

  def stop
    @server.close
    @thread.join(1)
  end

  private

  def serve
    loop do
      sock = @server.accept
      request_line = sock.gets.to_s.chomp
      headers = {}
      while (line = sock.gets) && line != "\r\n"
        key, value = line.chomp.split(": ", 2)
        headers[key.downcase] = value
      end
      @requests << { line: request_line, headers: headers }
      body = @responder.call(request_line)
      sock.write("HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n" \
                 "Content-Length: #{body.bytesize}\r\nConnection: close\r\n\r\n#{body}")
      sock.close
    end
  rescue IOError, Errno::EBADF
    # server socket closed: shutting down
  end
end

RSpec.describe F::Api do
  let(:server) { FakeFactorialServer.new }

  after { server.stop }

  # Keep FACTORIAL_BASE_URL out of the picture: the facade reads it as a
  # default, so a value leaking in from the developer's shell would silently
  # change what these examples exercise.
  around do |example|
    saved = ENV.delete("FACTORIAL_BASE_URL")
    example.run
  ensure
    saved ? ENV["FACTORIAL_BASE_URL"] = saved : ENV.delete("FACTORIAL_BASE_URL")
  end

  def build_api(**options)
    described_class.new(base_url: server.base_url, **options)
  end

  def last_request
    server.requests.last
  end

  describe "authentication headers" do
    it "sends only x-api-key when constructed with an api_key" do
      build_api(api_key: "KEY", token: nil).teams_team.teams_teams_get

      expect(last_request[:headers]).to include("x-api-key" => "KEY")
      expect(last_request[:headers]).not_to have_key("authorization")
    end

    it "sends only a bearer token when constructed with a token" do
      build_api(api_key: nil, token: "TOKEN").teams_team.teams_teams_get

      expect(last_request[:headers]).to include("authorization" => "Bearer TOKEN")
      expect(last_request[:headers]).not_to have_key("x-api-key")
    end

    it "sends both headers when both credentials are given" do
      build_api(api_key: "KEY", token: "TOKEN").teams_team.teams_teams_get

      expect(last_request[:headers]).to include(
        "x-api-key" => "KEY",
        "authorization" => "Bearer TOKEN"
      )
    end

    # Documents current behaviour. If the facade ever gains fail-fast
    # credential validation, replace this with `expect { ... }.to raise_error`.
    it "sends no auth headers when constructed without credentials" do
      build_api(api_key: nil, token: nil).teams_team.teams_teams_get

      expect(last_request[:headers].keys).not_to include("authorization", "x-api-key")
    end
  end

  describe "base_url" do
    it "defaults to production over https" do
      config = described_class.new(api_key: "k").client.config

      expect(config.scheme).to eq("https")
      expect(config.host).to eq("api.factorialhr.com")
    end

    it "applies scheme, host, non-default port and base path from a full URL" do
      config = described_class
               .new(api_key: "k", base_url: "https://staging.example.com:8443/subpath")
               .client.config

      expect(config.scheme).to eq("https")
      expect(config.host).to eq("staging.example.com:8443")
      expect(config.base_path).to eq("/subpath")
    end

    it "omits the port when it is the scheme default" do
      config = described_class
               .new(api_key: "k", base_url: "https://example.com:443")
               .client.config

      expect(config.host).to eq("example.com")
    end

    it "rejects URLs without an http(s) scheme" do
      expect { described_class.new(api_key: "k", base_url: "localhost:3000") }
        .to raise_error(ArgumentError, /full http\(s\) URL/)
    end

    it "falls back to the FACTORIAL_BASE_URL environment variable" do
      ENV["FACTORIAL_BASE_URL"] = "http://fallback.example.com"

      config = described_class.new(api_key: "k").client.config

      expect(config.scheme).to eq("http")
      expect(config.host).to eq("fallback.example.com")
    end
  end

  describe "resource accessors" do
    it "exposes one snake_case accessor per generated *Api class" do
      api = build_api(api_key: "k")

      expect(described_class::API_CLASSES).to include(teams_team: :TeamsTeamApi)
      expect(api.teams_team).to be_a(F::TeamsTeamApi)
    end

    it "memoizes resource instances and shares one ApiClient" do
      api = build_api(api_key: "k")

      expect(api.teams_team).to equal(api.teams_team)
      expect(api.teams_team.api_client).to equal(api.employees_employee.api_client)
    end
  end

  describe "F.paginate" do
    let(:page1) do
      '{"data":[{"id":1,"name":"A","company_id":1},{"id":2,"name":"B","company_id":1}],' \
        '"meta":{"end_cursor":"2","has_next_page":true,"has_previous_page":false,"limit":2,"total":3}}'
    end
    let(:page2) do
      '{"data":[{"id":3,"name":"C","company_id":1}],' \
        '"meta":{"end_cursor":"3","has_next_page":false,"has_previous_page":true,"limit":2,"total":3}}'
    end
    let(:server) do
      FakeFactorialServer.new { |request_line| request_line.include?("after_id=2") ? page2 : page1 }
    end
    let(:api) { build_api(api_key: "k") }

    def paginate(**options)
      F.paginate(limit: 2, **options) do |page|
        api.teams_team.teams_teams_get(query_params: page)
      end
    end

    it "follows cursors across pages via the query_params passthrough" do
      names = paginate.map(&:name)

      expect(names).to eq(%w[A B C])
      expect(server.requests.size).to eq(2)
      expect(server.requests.last[:line]).to include("after_id=2")
    end

    it "is lazy: only fetches the pages the consumer actually needs" do
      first_team = paginate.first

      expect(first_team.name).to eq("A")
      expect(server.requests.size).to eq(1)
    end

    it "stops at max_items without fetching further pages" do
      names = paginate(max_items: 2).map(&:name)

      expect(names).to eq(%w[A B])
      expect(server.requests.size).to eq(1)
    end
  end
end
