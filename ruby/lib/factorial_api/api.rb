# frozen_string_literal: true

require 'uri'
require 'factorial_api/pagination'
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

      attr_reader :client

      def initialize(api_key: ENV.fetch('FACTORIAL_API_KEY', nil), token: ENV.fetch('FACTORIAL_TOKEN', nil),
                     base_url: ENV.fetch('FACTORIAL_BASE_URL', nil))
        config = Config.new
        config.api_key['x-api-key'] = api_key
        config.access_token = token if token
        apply_base_url(config, base_url) if base_url
        @client = ApiClient.new(config)
        @apis = {}
      end

      API_CLASSES.each do |method_name, const|
        define_method(method_name) do
          @apis[method_name] ||= Api.const_get(const).new(client)
        end
      end

      private

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
