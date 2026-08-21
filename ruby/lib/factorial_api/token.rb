# frozen_string_literal: true

require 'json'

module F
  module Api
    # Read-only view over a bearer credential that may be a JWT: exposes its
    # claims and expiry with no dependencies beyond the standard library.
    #
    #   token = F::Api::Token.new(ENV["FACTORIAL_TOKEN"])
    #   token.claims                      # => {"exp" => 1767225600, ...}
    #   token.expires_at                  # => 2026-01-01 00:00:00 UTC
    #   token.expiring_soon?(margin: 120) # => false
    #
    # **Decoding is NOT verifying.** The payload is base64url-decoded without
    # checking the signature — enough for a client to introspect its own
    # credential (when to refresh, which company it belongs to), never enough
    # to trust a token somebody else presents. Verifying signatures is the
    # server's job.
    #
    # Non-JWT input is fine: Factorial credentials are opaque strings that
    # just happen to be JWTs today, so anything that doesn't parse yields
    # empty claims and no expiry instead of raising.
    class Token
      # Seconds before `exp` at which #expiring_soon? starts reporting true by
      # default: refreshing this early absorbs clock skew and in-flight time.
      DEFAULT_MARGIN = 60

      # @return [String] the credential exactly as given (what goes on the wire)
      attr_reader :raw

      # @return [Hash] decoded JWT payload, string-keyed and frozen; empty when
      #   the credential is not a decodable JWT
      attr_reader :claims

      def initialize(raw)
        @raw = raw.to_s
        @claims = decode_claims.freeze
        freeze
      end

      # Whether the credential parsed as a JWT (three dot-separated segments
      # whose payload is a JSON object).
      def jwt?
        !claims.empty?
      end

      # @return [Time, nil] the `exp` claim as a UTC Time, nil when absent
      def expires_at
        exp = claims['exp']
        Time.at(exp).utc if exp.is_a?(Numeric)
      end

      # True once `now` reaches the `exp` claim. A credential without a
      # readable expiry never reports itself expired: the API is the authority.
      def expired?(now: Time.now)
        exp = expires_at
        !exp.nil? && now >= exp
      end

      # Like #expired?, but `margin` seconds early — the natural trigger for a
      # proactive refresh.
      def expiring_soon?(margin: DEFAULT_MARGIN, now: Time.now)
        exp = expires_at
        !exp.nil? && (now + margin) >= exp
      end

      # Claim shorthand, indifferent to symbol/string keys:
      #   token[:cid]   # == token.claims["cid"]
      def [](name)
        claims[name.to_s]
      end

      def to_s
        raw
      end

      # The raw value is a live credential — show the claims, never the token.
      def inspect
        "#<F::Api::Token jwt?=#{jwt?} claims=#{claims.inspect}>"
      end

      private

      def decode_claims
        segments = raw.split('.')
        return {} unless segments.size == 3

        payload = JSON.parse(base64url_decode(segments[1]))
        payload.is_a?(Hash) ? payload : {}
      rescue StandardError
        {}
      end

      # base64url (RFC 7515: `-_` alphabet, padding stripped) via unpack —
      # the base64 gem is no longer a default gem as of Ruby 3.4.
      def base64url_decode(segment)
        padded = segment.tr('-_', '+/')
        padded += '=' * ((4 - (padded.length % 4)) % 4)
        padded.unpack1('m')
      end
    end
  end
end
