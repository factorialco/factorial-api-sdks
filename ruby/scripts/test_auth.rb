#!/usr/bin/env ruby
# frozen_string_literal: true

# Manual authentication check for the Factorial Ruby SDK.
#
# Phase 1 — wire check (always, offline, no credentials needed):
#   boots a throwaway HTTP server on localhost, points the SDK at it with
#   fake credentials, and asserts on the EXACT auth headers that arrive on
#   the socket for every credential mode. This is the definitive proof of
#   what the SDK sends, exercising the full stack (facade -> generated
#   client -> Faraday -> TCP). The same checks run automatically in
#   spec/factorial_api/api_spec.rb; this script exists to run them by hand.
#
# Phase 2 — live check (only if credentials are present in the env):
#   makes one real request per credential against FACTORIAL_BASE_URL
#   (default: production) and reports how the server judged it:
#     2xx -> credential accepted
#     401 -> credential REJECTED
#     403 -> auth OK, missing scope
#     404 -> auth OK but the resource did not resolve (e.g. on a local
#            instance, an OAuth app not yet installed for the company)
#
# Usage:
#   bundle exec ruby scripts/test_auth.rb
#   FACTORIAL_API_KEY=... bundle exec ruby scripts/test_auth.rb
#   FACTORIAL_TOKEN=... FACTORIAL_BASE_URL=https://api.local.factorial.dev \
#     bundle exec ruby scripts/test_auth.rb

require "socket"
require_relative "../lib/factorial_api"

failures = []

# ---------------------------------------------------------------------------
# Phase 1 — wire check against a local fake server
# ---------------------------------------------------------------------------
puts "== Phase 1: wire check (local fake server) =="

server = TCPServer.new("127.0.0.1", 0)
base_url = "http://127.0.0.1:#{server.addr[1]}"
captured = Queue.new

Thread.new do
  loop do
    sock = server.accept
    sock.gets # request line
    headers = {}
    while (line = sock.gets) && line != "\r\n"
      key, value = line.chomp.split(": ", 2)
      headers[key.downcase] = value
    end
    captured << headers
    body = '{"data":[],"meta":{"has_next_page":false,"has_previous_page":false,"limit":100,"total":0}}'
    sock.write("HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n" \
               "Content-Length: #{body.bytesize}\r\nConnection: close\r\n\r\n#{body}")
    sock.close
  end
rescue IOError, Errno::EBADF
  # server closed
end

wire_cases = [
  {
    name: "api_key only",
    args: { api_key: "FAKE_KEY", token: nil },
    expect: { "x-api-key" => "FAKE_KEY" },
    forbid: ["authorization"]
  },
  {
    name: "token only",
    args: { api_key: nil, token: "FAKE_TOKEN" },
    expect: { "authorization" => "Bearer FAKE_TOKEN" },
    forbid: ["x-api-key"]
  },
  {
    name: "both credentials",
    args: { api_key: "FAKE_KEY", token: "FAKE_TOKEN" },
    expect: { "x-api-key" => "FAKE_KEY", "authorization" => "Bearer FAKE_TOKEN" },
    forbid: []
  },
  {
    name: "no credentials (current behaviour: request goes out unauthenticated)",
    args: { api_key: nil, token: nil },
    expect: {},
    forbid: ["authorization", "x-api-key"]
  }
]

wire_cases.each do |c|
  F::Api.new(base_url: base_url, **c[:args]).teams_team.teams_teams_get
  headers = captured.pop

  wrong = c[:expect].reject { |k, v| headers[k] == v }.keys +
          c[:forbid].select { |k| headers.key?(k) }

  if wrong.empty?
    puts "  PASS  #{c[:name]}"
  else
    failures << "wire: #{c[:name]}"
    puts "  FAIL  #{c[:name]} — problematic headers: #{wrong.join(", ")}"
    puts "        sent: #{headers.slice("x-api-key", "authorization").inspect}"
  end
end

server.close

# ---------------------------------------------------------------------------
# Phase 2 — live check against a real Factorial instance
# ---------------------------------------------------------------------------
# Treat unset and empty-string env vars the same.
api_key  = ENV["FACTORIAL_API_KEY"]
token    = ENV["FACTORIAL_TOKEN"]
api_key  = nil if api_key&.empty?
token    = nil if token&.empty?
live_url = ENV["FACTORIAL_BASE_URL"]
live_url = nil if live_url&.empty?

puts "\n== Phase 2: live check (#{live_url || "https://api.factorialhr.com"}) =="

if api_key.nil? && token.nil?
  puts "  SKIPPED — set FACTORIAL_API_KEY and/or FACTORIAL_TOKEN to test real credentials"
else
  live_cases = []
  live_cases << ["api_key", { api_key: api_key, token: nil }] if api_key
  live_cases << ["token",   { api_key: nil, token: token }]   if token

  live_cases.each do |name, args|
    api = F::Api.new(**args)
    # Cheapest possible call: describes the credential itself, minimal scope.
    api.api_public_credential.api_public_credentials_get
    puts "  PASS  #{name}: credential accepted (2xx)"
  rescue F::ApiError => e
    case e.code
    when 401
      failures << "live: #{name} rejected (401)"
      puts "  FAIL  #{name}: credential REJECTED (401). Body: #{e.response_body}"
    when 403
      puts "  PASS* #{name}: auth OK, but missing scope for this endpoint (403)"
    when 404
      puts "  PASS* #{name}: auth OK (not a 401), but resource did not resolve (404)."
      puts "        On a local instance this usually means the OAuth app is not" \
           " installed for the company yet. Body: #{e.response_body}"
    else
      failures << "live: #{name} unexpected HTTP #{e.code}"
      puts "  FAIL  #{name}: unexpected HTTP #{e.code}. Body: #{e.response_body}"
    end
  rescue StandardError => e
    failures << "live: #{name} connection error"
    puts "  FAIL  #{name}: connection/client error — #{e.class}: #{e.message}"
  end
end

# ---------------------------------------------------------------------------
puts failures.empty? ? "\nAUTH OK — all checks passed" : "\nFAILURES: #{failures.inspect}"
exit(failures.empty? ? 0 : 1)
