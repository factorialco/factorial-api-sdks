# frozen_string_literal: true

require 'uri'
require 'factorial_api/oauth'
require 'factorial_api/pagination'
require 'factorial_api/token'
require 'factorial_api/webhooks'

module F
  # The gem's single namespace on the shared F:: root. The root belongs to
  # all Factorial gems — each claims exactly one constant under it, and ours
  # is Api: every class, module and constant this gem defines lives inside.
  module Api
    # One entry per generated *Api class: snake_case accessor => class name.
    # Evaluated when this file loads, which the entrypoint does last — after
    # every generated class exists.
    API_CLASSES = constants.grep(/Api$/).to_h do |const|
      method_name = const.to_s
                         .delete_suffix('Api')
                         .gsub(/([a-z\d])([A-Z])/, '\1_\2')
                         .downcase
      [method_name.to_sym, const]
    end.freeze

    # Keeps `F::Api.new(...)` as the package's front door even though Api is
    # a module (the namespace) rather than a class: it builds the facade.
    def self.new(...)
      Client.new(...)
    end

    # Entry point of the SDK: exposes one accessor per API resource over a
    # single shared ApiClient, and handles credentials and base URL.
    #
    #   api = F::Api.new(api_key: "...")
    #   api.teams_team.teams_teams_get
    class Client
      # Drops auth schemes without a credential, so a request never carries an
      # empty `Authorization: Bearer` alongside a valid `x-api-key`.
      class Config < Configuration
        def auth_settings
          super.reject do |_name, setting|
            setting[:value].nil? || setting[:value].strip == 'Bearer'
          end
        end
      end

      # Every generated method funnels through ApiClient#call_api, which makes
      # this override the SDK's request wrapper: the one seat for cross-cutting
      # transport behavior. Today that is reauthentication — expiry-based
      # refresh cannot see revocation, so a 401 (the API's authoritative "this
      # bearer is dead") triggers one reactive refresh and one retry when the
      # credential source can mint a replacement. Safe even for writes: a 401
      # is rejected at authentication, before the action runs. Static
      # credentials fail exactly as before.
      class RefreshingClient < ApiClient
        def initialize(config, session:)
          super(config)
          @session = session
        end

        def call_api(http_method, path, opts = {})
          sent = @session&.access_token
          super
        rescue ApiError => e
          # A rescue clause does not cover its own body: a second 401 (or a
          # failed refresh) propagates instead of looping.
          raise unless e.code == 401 && @session&.refresh_after_reject!(sent)

          super
        end
      end

      attr_reader :client

      def initialize(api_key: nil, token: nil, base_url: ENV.fetch('FACTORIAL_BASE_URL', nil),
                     oauth: nil, access_token: nil)
        api_key = presence(api_key)
        token = presence(token)
        # Env credentials are a zero-config convenience, not a supplement:
        # passing any credential explicitly disables them, so an exported
        # FACTORIAL_TOKEN can neither veto nor ride along with an
        # oauth:/access_token: the caller actually chose.
        if [api_key, token, oauth, access_token].compact.empty?
          api_key = presence(ENV.fetch('FACTORIAL_API_KEY', nil))
          token = presence(ENV.fetch('FACTORIAL_TOKEN', nil))
        end
        validate_credentials!(api_key, token, oauth, access_token)
        @client = build_client(build_config(api_key, token, oauth, access_token, presence(base_url)), oauth)
        @apis = {}
      end

      API_CLASSES.each do |method_name, const|
        define_method(method_name) do
          @apis[method_name] ||= Api.const_get(const).new(client)
        end
      end

      private

      def presence(value)
        value unless value.nil? || value.to_s.strip.empty?
      end

      def validate_credentials!(api_key, token, oauth, access_token)
        validate_bearer_sources!(oauth, access_token)
        bearers = { token: token, oauth: oauth, access_token: access_token }.compact.keys
        if bearers.size > 1
          raise ArgumentError, "#{bearers.join(' and ')} are mutually exclusive — each supplies the bearer"
        end
        return if api_key || bearers.any?

        raise ArgumentError,
              'provide api_key, token, oauth, or access_token (or set FACTORIAL_API_KEY / FACTORIAL_TOKEN)'
      end

      # Misuse of the duck-typed sources fails here, at the constructor,
      # instead of as a NoMethodError buried mid-request.
      def validate_bearer_sources!(oauth, access_token)
        if oauth && !oauth.respond_to?(:access_token)
          raise ArgumentError,
                'oauth must respond to #access_token — for a static string use token:, for a callable use access_token:'
        end
        return unless access_token && !access_token.respond_to?(:call)

        raise ArgumentError, 'access_token must be callable — for a static string use token:'
      end

      # Only a source that can mint a replacement bearer opts into the 401
      # retry; the contract is duck-typed like `oauth:` itself.
      def build_client(config, oauth)
        session = oauth if oauth.respond_to?(:refresh_after_reject!)
        RefreshingClient.new(config, session: session)
      end

      def build_config(api_key, token, oauth, access_token, base_url)
        config = Config.new
        config.api_key['x-api-key'] = api_key
        config.access_token = token if token
        bearer_source = oauth || access_token
        config.access_token_getter = bearer_getter(bearer_source) if bearer_source
        apply_base_url(config, base_url) if base_url
        config
      end

      # Consulted by the generated client on EVERY request (via
      # Configuration#access_token_with_refresh) — what lets an oauth session
      # refresh mid-flight and an access_token callable forward the caller's
      # token. May fire more than once per request (auth_settings is rebuilt
      # per auth scheme), so sources must stay cheap and idempotent. A source
      # that yields no token raises rather than letting the request leave
      # unauthenticated (the empty Bearer header would be dropped silently).
      def bearer_getter(source)
        lambda do
          value = (source.respond_to?(:call) ? source.call : source.access_token).to_s
          if value.strip.empty?
            raise 'F::Api: the oauth/access_token source returned no token — ' \
                  'refusing to send an unauthenticated request'
          end

          value
        end
      end

      def apply_base_url(config, base_url)
        uri = parse_base_url(base_url)

        config.scheme = uri.scheme
        config.host = uri.port == uri.default_port ? uri.host : "#{uri.host}:#{uri.port}"
        config.base_path = uri.path unless uri.path.empty?
      end

      def parse_base_url(base_url)
        uri = URI.parse(base_url)
        return uri if uri.is_a?(URI::HTTP) && uri.host

        raise ArgumentError,
              'base_url must be a full http(s) URL, e.g. https://api.factorialhr.com ' \
              "(got #{base_url.inspect})"
      end
    end
  end
end
