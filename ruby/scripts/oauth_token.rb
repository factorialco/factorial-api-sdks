#!/usr/bin/env ruby
# frozen_string_literal: true

# Obtain (and refresh) an OAuth access token — a JWT — from a Factorial
# instance, replicating the authorization_code flow step by step. Dev helper
# for testing token acquisition against local/demo instances; feed the token
# it prints to FACTORIAL_TOKEN / scripts/test_auth.rb.
#
# The authorize step needs a browser (user consent, by design): the script
# prints the URL, you approve there, and paste back the code (or the whole
# redirect URL — both work). Codes are single-use and expire in ~10 minutes.
#
# Usage:
#   FACTORIAL_OAUTH_CLIENT_ID=... FACTORIAL_OAUTH_CLIENT_SECRET=... \
#   FACTORIAL_BASE_URL=https://api.local.factorial.dev \
#     bundle exec ruby scripts/oauth_token.rb                       # full flow
#
#   ... bundle exec ruby scripts/oauth_token.rb --refresh REFRESH_TOKEN
#
# WARNING: tokens and secrets are printed to stdout for convenience — do not
# paste the output anywhere public.

require 'json'
require 'net/http'
require 'uri'

BASE_URL = ENV['FACTORIAL_BASE_URL'].to_s.empty? ? 'https://api.factorialhr.com' : ENV.fetch('FACTORIAL_BASE_URL', nil)
CLIENT_ID = ENV.fetch('FACTORIAL_OAUTH_CLIENT_ID', nil)
CLIENT_SECRET = ENV.fetch('FACTORIAL_OAUTH_CLIENT_SECRET', nil)
REDIRECT_URI = if ENV['FACTORIAL_OAUTH_REDIRECT_URI'].to_s.empty?
                 BASE_URL
               else
                 ENV.fetch('FACTORIAL_OAUTH_REDIRECT_URI',
                           nil)
               end

if CLIENT_ID.to_s.empty? || CLIENT_SECRET.to_s.empty?
  abort('ERROR: set FACTORIAL_OAUTH_CLIENT_ID and FACTORIAL_OAUTH_CLIENT_SECRET ' \
        '(from your OAuth application in Factorial)')
end

def post_token(**params)
  uri = URI("#{BASE_URL}/oauth/token")
  response = Net::HTTP.post_form(uri, params.transform_keys(&:to_s))
  body = begin
    JSON.parse(response.body)
  rescue StandardError
    { 'raw' => response.body[0, 300] }
  end

  abort("ERROR: token endpoint returned HTTP #{response.code}: #{body.inspect}") unless response.is_a?(Net::HTTPSuccess)

  body
end

def decode_claims(jwt)
  segments = jwt.to_s.split('.')
  return nil unless segments.size == 3

  # base64url decode without the base64 gem (no longer a default gem in 3.4)
  payload = segments[1].tr('-_', '+/')
  payload += '=' * ((4 - (payload.length % 4)) % 4)
  JSON.parse(payload.unpack1('m'))
rescue StandardError
  nil
end

def show(token_response)
  access_token = token_response['access_token']

  puts "\n== Token response =="
  puts "  token_type:    #{token_response['token_type']}"
  puts "  expires_in:    #{token_response['expires_in']}s"
  puts "  scope:         #{token_response['scope']}"
  puts "  access_token:  #{access_token}"
  puts "  refresh_token: #{token_response['refresh_token']}"

  if (claims = decode_claims(access_token))
    puts "\n== JWT claims (decoded, unverified) =="
    claims.each { |k, v| puts "  #{k.ljust(12)} #{v.to_s[0, 80]}" }
    if claims['exp'] && claims['iat']
      puts "  (lifetime: #{claims['exp'] - claims['iat']}s, " \
           "expires at #{Time.at(claims['exp']).utc})"
    end
  else
    puts "\n(access_token is not a JWT — opaque token)"
  end

  puts "\n== Next steps =="
  puts "  export FACTORIAL_TOKEN=#{access_token}"
  puts "  export FACTORIAL_BASE_URL=#{BASE_URL}"
  puts '  bundle exec ruby scripts/test_auth.rb   # verify it against the API'
  puts "\n  To renew when it expires (rotates the refresh token — save the new one!):"
  puts "  bundle exec ruby scripts/oauth_token.rb --refresh #{token_response['refresh_token']}"
end

if ARGV[0] == '--refresh'
  refresh_token = ARGV[1] or abort('Usage: oauth_token.rb --refresh REFRESH_TOKEN')

  puts "Refreshing access token against #{BASE_URL} ..."
  show(post_token(
         grant_type: 'refresh_token',
         refresh_token: refresh_token,
         client_id: CLIENT_ID,
         client_secret: CLIENT_SECRET
       ))
else
  authorize_url = "#{BASE_URL}/oauth/authorize" \
                  "?client_id=#{CLIENT_ID}" \
                  "&redirect_uri=#{URI.encode_uri_component(REDIRECT_URI)}" \
                  '&response_type=code'

  puts '1. Open this URL in a browser with an active Factorial session:'
  puts "\n   #{authorize_url}\n\n"
  puts '2. Authorize the app. You will be redirected to:'
  puts "   #{REDIRECT_URI}/?code=XXXX"
  print "\n3. Paste the code (or the full redirect URL): "

  input = $stdin.gets.to_s.strip
  code = input[/code=([^&\s]+)/, 1] || input
  abort('ERROR: no code provided') if code.empty?

  puts "\nExchanging code for tokens ..."
  show(post_token(
         grant_type: 'authorization_code',
         code: code,
         client_id: CLIENT_ID,
         client_secret: CLIENT_SECRET,
         redirect_uri: REDIRECT_URI
       ))
end
