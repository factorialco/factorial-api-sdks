#!/usr/bin/env ruby
# frozen_string_literal: true

# Obtain (and refresh) an OAuth access token — a JWT — from a Factorial
# instance, walking the authorization_code flow step by step over F::Api::OAuth
# (the SDK's own public API — this script is its manual dogfooding). Dev
# helper for testing token acquisition against local/demo instances; feed
# the token it prints to FACTORIAL_TOKEN / scripts/test_auth.rb.
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

require_relative '../lib/factorial_api/oauth'

begin
  OAUTH = F::Api::OAuth.new
rescue ArgumentError => e
  abort("ERROR: #{e.message} (from your OAuth application in Factorial)")
end

REDIRECT_URI = if ENV['FACTORIAL_OAUTH_REDIRECT_URI'].to_s.empty?
                 OAUTH.base_url
               else
                 ENV.fetch('FACTORIAL_OAUTH_REDIRECT_URI', nil)
               end

def show(tokens)
  puts "\n== Token response =="
  puts "  token_type:    #{tokens.token_type}"
  puts "  expires_in:    #{tokens.expires_in}s"
  puts "  scope:         #{tokens.scope}"
  puts "  access_token:  #{tokens.access_token}"
  puts "  refresh_token: #{tokens.refresh_token}"

  token = tokens.access_token
  if token.jwt?
    puts "\n== JWT claims (decoded, unverified) =="
    token.claims.each { |k, v| puts "  #{k.ljust(12)} #{v.to_s[0, 80]}" }
    if token[:exp] && token[:iat]
      puts "  (lifetime: #{token[:exp] - token[:iat]}s, " \
           "expires at #{token.expires_at})"
    end
  else
    puts "\n(access_token is not a JWT — opaque token)"
  end

  puts "\n== Next steps =="
  puts "  export FACTORIAL_TOKEN=#{token.raw}"
  puts "  export FACTORIAL_BASE_URL=#{OAUTH.base_url}"
  puts '  bundle exec ruby scripts/test_auth.rb   # verify it against the API'
  puts "\n  To renew when it expires (rotates the refresh token — save the new one!):"
  puts "  bundle exec ruby scripts/oauth_token.rb --refresh #{tokens.refresh_token}"
end

begin
  if ARGV[0] == '--refresh'
    refresh_token = ARGV[1] or abort('Usage: oauth_token.rb --refresh REFRESH_TOKEN')

    puts "Refreshing access token against #{OAUTH.base_url} ..."
    show(OAUTH.refresh(refresh_token))
  else
    puts '1. Open this URL in a browser with an active Factorial session:'
    puts "\n   #{OAUTH.authorize_url(redirect_uri: REDIRECT_URI)}\n\n"
    puts '2. Authorize the app. You will be redirected to:'
    puts "   #{REDIRECT_URI}/?code=XXXX"
    print "\n3. Paste the code (or the full redirect URL): "

    input = $stdin.gets.to_s.strip
    code = input[/code=([^&\s]+)/, 1] || input
    abort('ERROR: no code provided') if code.empty?

    puts "\nExchanging code for tokens ..."
    show(OAUTH.exchange_code(code, redirect_uri: REDIRECT_URI))
  end
rescue F::Api::OAuthError => e
  detail = case e.body
           when Hash then " — #{e.body.inspect}"
           when String then " — #{e.body[0, 300]}"
           else ''
           end
  abort("ERROR: #{e.message}#{detail}")
end
