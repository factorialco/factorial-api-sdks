# frozen_string_literal: true

require 'monitor'
require 'oauth2'
require_relative 'token'

module F
  module Api
    # Raised when the OAuth token endpoint answers with a non-2xx status, a
    # malformed body, or a body without a token. Carries the HTTP `code` and
    # the parsed response `body`, mirroring how F::Api::ApiError exposes API
    # call failures.
    class OAuthError < StandardError
      # @return [Integer, nil] HTTP status returned by the token endpoint;
      #   nil when the response was unparseable before a status was known
      attr_reader :code

      # @return [Hash, String, nil] parsed JSON body, or the raw body when it
      #   wasn't JSON
      attr_reader :body

      def initialize(code:, body:)
        @code = code
        @body = body
        super("OAuth token endpoint returned #{code ? "HTTP #{code}" : 'an unparseable response'}#{detail}")
      end

      # @return [String, nil] the OAuth error identifier ("invalid_grant", ...)
      def error
        body['error'] if body.is_a?(Hash)
      end

      private

      def detail
        return '' unless error

        description = body['error_description']
        description ? " (#{error}): #{description}" : " (#{error})"
      end
    end

    # OAuth2 authorization_code lifecycle against a Factorial instance:
    # building the authorize URL, exchanging the code, refreshing, and — via
    # #session — keeping an F::Api credential fresh automatically.
    #
    #   oauth   = F::Api::OAuth.new(client_id: "...", client_secret: "...")
    #   oauth.authorize_url(redirect_uri: "https://myapp.com/cb") # browser step
    #   tokens  = oauth.exchange_code(code, redirect_uri: "https://myapp.com/cb")
    #   session = oauth.session(tokens) { |t| save(t.refresh_token) }
    #   api     = F::Api.new(oauth: session)
    #
    # Credentials fall back to the FACTORIAL_OAUTH_CLIENT_ID /
    # FACTORIAL_OAUTH_CLIENT_SECRET environment variables, and the base URL
    # to FACTORIAL_BASE_URL (then production), matching F::Api's conventions.
    class OAuth
      DEFAULT_BASE_URL = 'https://api.factorialhr.com'

      attr_reader :client_id, :base_url

      def initialize(client_id: ENV.fetch('FACTORIAL_OAUTH_CLIENT_ID', nil),
                     client_secret: ENV.fetch('FACTORIAL_OAUTH_CLIENT_SECRET', nil),
                     base_url: ENV.fetch('FACTORIAL_BASE_URL', nil))
        @client_id = presence(client_id)
        @client_secret = presence(client_secret)
        @base_url = (presence(base_url) || DEFAULT_BASE_URL).chomp('/')

        unless @client_id && @client_secret
          raise ArgumentError,
                'provide client_id and client_secret (or set FACTORIAL_OAUTH_CLIENT_ID / ' \
                'FACTORIAL_OAUTH_CLIENT_SECRET)'
        end

        @oauth2_client = build_oauth2_client
      end

      # URL where the user grants access in the browser (by design, this step
      # cannot be automated). The redirect back carries the single-use
      # authorization code (?code=...), valid for ~10 minutes.
      def authorize_url(redirect_uri:)
        oauth2_client.auth_code.authorize_url(redirect_uri: redirect_uri)
      end

      # Exchanges an authorization code for tokens. The redirect_uri must be
      # the same one used in the authorize step.
      def exchange_code(code, redirect_uri:)
        request_tokens { oauth2_client.auth_code.get_token(code, redirect_uri: redirect_uri) }
      end

      # Trades a refresh token for a fresh token set. Refresh tokens are
      # usually single-use: the returned set normally carries a replacement —
      # persist it or the chain breaks.
      def refresh(refresh_token)
        request_tokens { oauth2_client.get_token(grant_type: 'refresh_token', refresh_token: refresh_token) }
      end

      # Wraps a token set in a self-refreshing Session for F::Api's `oauth:`.
      # The block is REQUIRED and receives the current Tokens after every
      # refresh.
      def session(tokens, margin: Token::DEFAULT_MARGIN, &)
        Session.new(self, tokens, margin: margin, &)
      end

      private

      attr_reader :oauth2_client

      def presence(value)
        value unless value.nil? || value.to_s.strip.empty?
      end

      # Protocol mechanics live in the oauth2 gem; this wrapper only maps its
      # results back into the SDK's value objects and error type.
      def request_tokens
        Tokens.new(yield.response.parsed)
      rescue OAuth2::Error => e
        raise OAuthError.new(**error_details(e))
      rescue JSON::ParserError => e
        # Raised mid-parse when a body claims to be JSON but isn't — before
        # the gem has built an error object that would carry the status.
        raise OAuthError.new(code: nil, body: e.message)
      end

      # The gem attaches a Response to protocol failures, but raises with
      # only the parsed Hash when a 2xx body lacks the access_token key.
      def error_details(error)
        response = error.response
        if response.respond_to?(:status)
          { code: response.status, body: parsed_body(response) }
        else
          { code: 200, body: response }
        end
      end

      def build_oauth2_client
        # Absolute authorize/token URLs: leading-slash paths would drop any
        # path prefix present in base_url.
        OAuth2::Client.new(
          @client_id, @client_secret,
          site: base_url,
          authorize_url: "#{base_url}/oauth/authorize",
          token_url: "#{base_url}/oauth/token",
          # Doorkeeper expects the client credentials in the form body (the
          # gem's default is HTTP Basic auth).
          auth_scheme: :request_body
        )
      end

      def parsed_body(response)
        response.parsed || response.body
      rescue StandardError
        response.body
      end

      # One response from the token endpoint, as an immutable value. The
      # access token comes pre-wrapped in F::Api::Token, so expiry and claims
      # are a method call away.
      class Tokens
        # @return [F::Api::Token] the access token (decoded, not verified)
        attr_reader :access_token

        # @return [Hash] the raw token endpoint response, frozen
        attr_reader :raw

        # @return [Time, nil] when this set expires — the moment it was
        #   received plus the endpoint's `expires_in`; nil when the endpoint
        #   sent none
        attr_reader :expires_at

        def initialize(payload)
          @raw = payload.dup.freeze
          @access_token = Token.new(raw['access_token'])
          @expires_at = (Time.now + raw['expires_in'] if raw['expires_in'].is_a?(Numeric))
          freeze
        end

        # Whether the set is within `margin` seconds of the earliest KNOWN
        # expiry. Two clocks can speak: the endpoint's `expires_in` (anchored
        # to the local clock at receipt — immune to server clock skew and to
        # non-JWT tokens) and the JWT `exp` claim. Whichever says "sooner"
        # wins: refreshing early is harmless, serving a dead token is not.
        # A set with neither never reports true — the API stays the
        # authority.
        #
        # The expires_in anchor is set at construction: a Tokens rebuilt
        # later from a persisted #to_h restarts it. Persist the
        # refresh_token, not the whole set.
        def expiring_soon?(margin: Token::DEFAULT_MARGIN, now: Time.now)
          earliest = [expires_at, access_token.expires_at].compact.min
          !earliest.nil? && (now + margin) >= earliest
        end

        # Same set carrying a different refresh token; used when a refresh
        # response omits the field (RFC 6749 allows it) and the previous one
        # must carry over.
        def with_refresh_token(refresh_token)
          Tokens.new(raw.merge('refresh_token' => refresh_token))
        end

        # @return [String, nil] the refresh token to persist
        def refresh_token = raw['refresh_token']
        def expires_in = raw['expires_in']
        def scope = raw['scope']
        def token_type = raw['token_type']
        def to_h = raw
      end

      # The one stateful piece: holds the current Tokens and hands out an
      # access token that is refreshed proactively when the set is within
      # `margin` seconds of expiry (see Tokens#expiring_soon?). Thread-safe:
      # a reentrant Monitor guards the swap, and a refresh holds it for the
      # whole token-endpoint round trip — deliberate: it happens once per
      # expiry, and letting a second thread refresh concurrently would burn
      # the (usually single-use) refresh token.
      #
      # Built through F::Api::OAuth#session; F::Api's `oauth:` calls
      # #access_token before every request, so refreshes happen mid-flight,
      # invisibly. A failed refresh raises F::Api::OAuthError from that
      # request's call site.
      class Session
        ROTATION_BLOCK_ERROR = 'F::Api::OAuth session requires a rotation block: each refresh ' \
                               'normally invalidates the previous refresh token, so persist ' \
                               'the new one — oauth.session(tokens) { |t| save(t.refresh_token) }'

        # @return [Integer] seconds before expiry at which refresh kicks in
        attr_reader :margin

        def initialize(oauth, tokens, margin: Token::DEFAULT_MARGIN, &on_rotation)
          raise ArgumentError, ROTATION_BLOCK_ERROR unless on_rotation

          @oauth = oauth
          @tokens = tokens
          @margin = margin
          @on_rotation = on_rotation
          @lock = Monitor.new
        end

        # @return [Tokens] the current token set
        def tokens
          @lock.synchronize { @tokens }
        end

        # The bearer token to put on the wire, refreshed first when needed.
        # Sets without a readable expiry and sets without a refresh token are
        # returned as-is: the API stays the authority on rejection.
        def access_token
          @lock.synchronize do
            refresh! if refreshable? && @tokens.expiring_soon?(margin: margin)
            @tokens.access_token.raw
          end
        end

        private

        def refreshable?
          !@tokens.refresh_token.nil?
        end

        def refresh!
          replacement = @oauth.refresh(@tokens.refresh_token)
          # RFC 6749 §6: a refresh response MAY omit refresh_token, meaning
          # "keep using the previous one" — dropping it here would silently
          # end refreshability and hand the rotation block a nil.
          replacement = replacement.with_refresh_token(@tokens.refresh_token) if replacement.refresh_token.nil?
          @tokens = replacement
          @on_rotation.call(@tokens)
        end
      end
    end
  end
end
