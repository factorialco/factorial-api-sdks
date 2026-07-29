#!/usr/bin/env ruby
# frozen_string_literal: true

# Smoke test against the real Factorial API.
#
# Usage:
#   bundle exec ruby scripts/test_api.rb [--debug]
#
# Auth (pick one):
#   FACTORIAL_API_KEY=...   API key, sent as x-api-key header
#   FACTORIAL_TOKEN=...     OAuth2 token, sent as Authorization: Bearer
#
# --debug prints full request/response traces, including headers.
# WARNING: debug output contains your credentials. Never paste it
# anywhere without redacting them first.

require_relative '../lib/factorial_api'

# Treat unset and empty-string env vars the same.
api_key = ENV.fetch('FACTORIAL_API_KEY', nil)
token   = ENV.fetch('FACTORIAL_TOKEN', nil)
api_key = nil if api_key && api_key.empty?
token   = nil if token && token.empty?

abort('ERROR: set FACTORIAL_API_KEY or FACTORIAL_TOKEN before running') unless api_key || token
warn('NOTE: both credentials set; both auth headers will be sent') if api_key && token

api = F::Api.new(api_key: api_key, token: token)
api.client.config.debugging = true if ARGV.include?('--debug')

puts "Host: #{api.client.config.host}"
puts "Auth: #{token ? 'OAuth2 token' : 'API key'}"

begin
  response = api.teams_team.teams_teams_get
  data = response.respond_to?(:data) ? Array(response.data) : []
  puts "OK: teams endpoint responded (#{data.size} teams)"
  puts "First team: #{data.first.name}" if !data.empty? && data.first.respond_to?(:name)
rescue F::ApiError => e
  warn "API ERROR: HTTP #{e.code}"
  warn "Response body: #{e.response_body}"
  exit 1
rescue StandardError => e
  warn "CONNECTION/CLIENT ERROR: #{e.class}: #{e.message}"
  exit 1
end
