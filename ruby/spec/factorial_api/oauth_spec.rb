# frozen_string_literal: true

# Handwritten specs for F::Api::OAuth: the /oauth/token operations, the
# self-refreshing Session, and the end-to-end integration with F::Api.
# Like api_spec, everything goes over a real TCP socket against a fake
# server, and the assertions inspect the wire.

require 'spec_helper'
require_relative '../support/fake_factorial_server'
require_relative '../support/jwt_fixtures'

RSpec.describe F::Api::OAuth do
  include JwtFixtures

  let(:server) { FakeFactorialServer.new }

  after { server.stop }

  # Keep the OAuth-related env vars out of the picture, same rationale as the
  # FACTORIAL_BASE_URL scrub in api_spec.
  around do |example|
    saved = %w[FACTORIAL_OAUTH_CLIENT_ID FACTORIAL_OAUTH_CLIENT_SECRET FACTORIAL_BASE_URL]
            .to_h { |name| [name, ENV.delete(name)] }
    example.run
  ensure
    saved.each { |name, value| value ? ENV[name] = value : ENV.delete(name) }
  end

  def build_oauth(**options)
    described_class.new(client_id: 'CLIENT', client_secret: 'SECRET', base_url: server.base_url,
                        **options)
  end

  def token_response(access_token:, refresh_token: 'REFRESH-2', expires_in: 3600)
    JSON.generate('access_token' => access_token, 'refresh_token' => refresh_token,
                  'token_type' => 'Bearer', 'expires_in' => expires_in, 'scope' => 'read')
  end

  def form_params(request)
    URI.decode_www_form(request[:body].to_s).to_h
  end

  describe '#initialize' do
    it 'requires client_id and client_secret, treating empty strings as absent' do
      expect { described_class.new(client_id: nil, client_secret: 'S') }
        .to raise_error(ArgumentError, /provide client_id and client_secret/)
      expect { described_class.new(client_id: 'ID', client_secret: ' ') }
        .to raise_error(ArgumentError, /FACTORIAL_OAUTH_CLIENT_SECRET/)
    end

    it 'falls back to the FACTORIAL_OAUTH_* and FACTORIAL_BASE_URL env vars' do
      ENV['FACTORIAL_OAUTH_CLIENT_ID'] = 'ENV_ID'
      ENV['FACTORIAL_OAUTH_CLIENT_SECRET'] = 'ENV_SECRET'
      ENV['FACTORIAL_BASE_URL'] = 'http://env.example.com/'

      oauth = described_class.new

      expect(oauth.client_id).to eq('ENV_ID')
      expect(oauth.base_url).to eq('http://env.example.com') # trailing slash trimmed
    end

    it 'defaults the base URL to production' do
      expect(described_class.new(client_id: 'ID', client_secret: 'S').base_url)
        .to eq('https://api.factorialhr.com')
    end
  end

  describe '#authorize_url' do
    it 'points at /oauth/authorize with the client_id and encoded redirect_uri' do
      url = build_oauth.authorize_url(redirect_uri: 'https://myapp.com/cb?x=1')

      expect(url).to start_with("#{server.base_url}/oauth/authorize?")
      expect(url).to include('client_id=CLIENT')
      expect(url).to include('response_type=code')
      expect(url).to include('redirect_uri=https%3A%2F%2Fmyapp.com%2Fcb%3Fx%3D1')
    end
  end

  describe '#exchange_code' do
    it 'POSTs the authorization_code grant form-encoded and returns Tokens' do
      jwt = build_jwt('exp' => Time.now.to_i + 3600, 'cid' => '42')
      server.responder = ->(_line, _body) { token_response(access_token: jwt) }

      tokens = build_oauth.exchange_code('THE-CODE', redirect_uri: 'https://myapp.com/cb')

      request = server.requests.last
      expect(request[:line]).to start_with('POST /oauth/token')
      expect(form_params(request)).to eq(
        'grant_type' => 'authorization_code', 'code' => 'THE-CODE',
        'redirect_uri' => 'https://myapp.com/cb',
        'client_id' => 'CLIENT', 'client_secret' => 'SECRET'
      )
      expect(tokens.access_token).to be_a(F::Api::Token)
      expect(tokens.access_token[:cid]).to eq('42')
      expect(tokens.refresh_token).to eq('REFRESH-2')
      expect(tokens.expires_in).to eq(3600)
      expect(tokens.expires_at).to be_within(5).of(Time.now + 3600)
      expect(tokens.scope).to eq('read')
      expect(tokens.token_type).to eq('Bearer')
    end
  end

  describe '#refresh' do
    it 'POSTs the refresh_token grant' do
      server.responder = ->(_line, _body) { token_response(access_token: 'NEW') }

      tokens = build_oauth.refresh('REFRESH-1')

      expect(form_params(server.requests.last)).to include(
        'grant_type' => 'refresh_token', 'refresh_token' => 'REFRESH-1'
      )
      expect(tokens.access_token.raw).to eq('NEW')
    end
  end

  describe 'base URL with a path prefix' do
    it 'keeps the prefix on the token endpoint, like authorize_url does' do
      server.responder = ->(_l, _b) { token_response(access_token: 'NEW') }
      oauth = build_oauth(base_url: "#{server.base_url}/sub")

      oauth.refresh('R')

      expect(server.requests.last[:line]).to start_with('POST /sub/oauth/token')
      expect(oauth.authorize_url(redirect_uri: 'https://x.dev/cb'))
        .to start_with("#{server.base_url}/sub/oauth/authorize?")
    end
  end

  describe 'error handling' do
    it 'raises F::Api::OAuthError with code, body, and the OAuth error id on non-2xx' do
      server.responder = lambda do |_line, _body|
        [400, '{"error":"invalid_grant","error_description":"code expired"}']
      end

      expect { build_oauth.refresh('STALE') }.to raise_error(F::Api::OAuthError) do |error|
        expect(error.code).to eq(400)
        expect(error.error).to eq('invalid_grant')
        expect(error.body).to include('error_description' => 'code expired')
        expect(error.message).to include('HTTP 400 (invalid_grant): code expired')
      end
    end

    it 'keeps the raw body when the error response is not JSON' do
      server.responder = ->(_line, _body) { [502, 'Bad Gateway', 'text/plain'] }

      expect { build_oauth.refresh('R') }.to raise_error(F::Api::OAuthError) do |error|
        expect(error.code).to eq(502)
        expect(error.body).to eq('Bad Gateway')
        expect(error.error).to be_nil
      end
    end

    it 'rejects a 2xx whose body is not a JSON object' do
      server.responder = ->(_line, _body) { '"unexpected"' }

      expect { build_oauth.refresh('R') }.to raise_error(F::Api::OAuthError) { |e| expect(e.code).to eq(200) }
    end

    it 'rejects a 2xx JSON object that carries no access_token' do
      server.responder = ->(_line, _body) { '{"error":"try_again_later"}' }

      expect { build_oauth.refresh('R') }.to raise_error(F::Api::OAuthError) do |error|
        expect(error.code).to eq(200)
      end
    end

    it 'wraps an unparseable JSON body instead of leaking JSON::ParserError' do
      server.responder = ->(_line, _body) { [400, 'not-json'] } # Content-Type: application/json

      expect { build_oauth.refresh('R') }.to raise_error(F::Api::OAuthError) do |error|
        expect(error.code).to be_nil
        expect(error.message).to include('unparseable')
      end
    end
  end

  describe 'F::Api::OAuth::Session' do
    let(:fresh_jwt)  { build_jwt('exp' => Time.now.to_i + 3600) }
    let(:stale_jwt)  { build_jwt('exp' => Time.now.to_i + 5) }
    let(:rotations)  { [] }

    def tokens_with(access_token, refresh_token: 'REFRESH-1', **extra)
      F::Api::OAuth::Tokens.new({ 'access_token' => access_token,
                                  'refresh_token' => refresh_token }.merge(extra))
    end

    def build_session(oauth, tokens, **options)
      oauth.session(tokens, **options) { |rotated| rotations << rotated }
    end

    it 'requires the rotation block' do
      expect { build_oauth.session(tokens_with(fresh_jwt)) }
        .to raise_error(ArgumentError, /rotation block/)
    end

    it 'returns a fresh token as-is, without calling the token endpoint' do
      session = build_session(build_oauth, tokens_with(fresh_jwt))

      expect(session.access_token).to eq(fresh_jwt)
      expect(server.requests).to be_empty
    end

    # tokens_with builds sets without expires_in, so the refresh examples
    # exercise the JWT-exp fallback path.
    it 'refreshes a token inside the margin, rotates, and keeps the new set' do
      server.responder = ->(_l, _b) { token_response(access_token: fresh_jwt) }
      session = build_session(build_oauth, tokens_with(stale_jwt))

      expect(session.access_token).to eq(fresh_jwt)
      expect(form_params(server.requests.last)).to include('refresh_token' => 'REFRESH-1')
      expect(rotations.map(&:refresh_token)).to eq(['REFRESH-2'])
      expect(session.tokens.refresh_token).to eq('REFRESH-2')

      # The refreshed token is fresh, so the next call goes straight through.
      expect { session.access_token }.not_to(change { server.requests.size })
    end

    it 'honours a custom margin' do
      soonish = build_jwt('exp' => Time.now.to_i + 100)
      server.responder = ->(_l, _b) { token_response(access_token: 'NEW') }

      expect(build_session(build_oauth, tokens_with(soonish)).access_token).to eq(soonish)
      expect(build_session(build_oauth, tokens_with(soonish), margin: 200).access_token).to eq('NEW')
    end

    it 'refreshes at the earliest known expiry, whichever clock says sooner' do
      server.responder = ->(_l, _b) { token_response(access_token: fresh_jwt) }
      oauth = build_oauth

      # The JWT looks fresh, but the endpoint said it dies in 10s: refresh.
      build_session(oauth, tokens_with(fresh_jwt, 'expires_in' => 10)).access_token
      expect(server.requests.size).to eq(1)

      # The endpoint granted an hour, but the JWT exp is in 5s: refresh too —
      # serving a token past its exp is never right, whatever expires_in said.
      build_session(oauth, tokens_with(stale_jwt, 'expires_in' => 3600)).access_token
      expect(server.requests.size).to eq(2)

      # Both clocks fresh: no refresh.
      sound = build_session(oauth, tokens_with(fresh_jwt, 'expires_in' => 3600))
      expect(sound.access_token).to eq(fresh_jwt)
      expect(server.requests.size).to eq(2)
    end

    it 'keeps the previous refresh token when the endpoint does not rotate it' do
      server.responder = ->(_l, _b) { token_response(access_token: fresh_jwt, refresh_token: nil) }
      session = build_session(build_oauth, tokens_with(stale_jwt))

      session.access_token

      expect(session.tokens.refresh_token).to eq('REFRESH-1')
      expect(rotations.map(&:refresh_token)).to eq(['REFRESH-1'])
    end

    it 'has no expires_at when the endpoint sent no expires_in' do
      expect(tokens_with(fresh_jwt).expires_at).to be_nil
    end

    it 'returns a stale token as-is when there is no refresh token' do
      session = build_session(build_oauth, tokens_with(stale_jwt, refresh_token: nil))

      expect(session.access_token).to eq(stale_jwt)
      expect(server.requests).to be_empty
    end

    it 'never refreshes an opaque (non-JWT) token' do
      session = build_session(build_oauth, tokens_with('opaque-token'))

      expect(session.access_token).to eq('opaque-token')
      expect(server.requests).to be_empty
    end

    it 'propagates refresh failures as F::Api::OAuthError' do
      server.responder = ->(_l, _b) { [400, '{"error":"invalid_grant"}'] }
      session = build_session(build_oauth, tokens_with(stale_jwt))

      expect { session.access_token }.to raise_error(F::Api::OAuthError, /invalid_grant/)
      expect(rotations).to be_empty
    end
  end

  describe 'end-to-end with F::Api' do
    it 'refreshes mid-flight: the API request carries the rotated bearer' do
      fresh_jwt = build_jwt('exp' => Time.now.to_i + 3600)
      stale_jwt = build_jwt('exp' => Time.now.to_i + 5)
      server.responder = lambda do |line, _body|
        if line.start_with?('POST /oauth/token')
          token_response(access_token: fresh_jwt)
        else
          FakeFactorialServer::EMPTY_PAGE
        end
      end
      rotations = []
      session = build_oauth.session(F::Api::OAuth::Tokens.new('access_token' => stale_jwt,
                                                              'refresh_token' => 'REFRESH-1')) do |t|
        rotations << t.refresh_token
      end

      F::Api.new(oauth: session, base_url: server.base_url)
            .teams_team.teams_teams_get

      token_request, api_request = server.requests
      expect(token_request[:line]).to start_with('POST /oauth/token')
      expect(api_request[:headers]['authorization']).to eq("Bearer #{fresh_jwt}")
      expect(api_request[:headers]).not_to have_key('x-api-key')
      expect(rotations).to eq(['REFRESH-2'])
    end
  end
end
