# frozen_string_literal: true

require "uri"
require "factorial_api/pagination"

module F
  class Api
    class Config < Configuration
      def auth_settings
        super.reject do |_name, setting|
          setting[:value].nil? || setting[:value].strip == "Bearer"
        end
      end
    end

    API_CLASSES = (F.constants.grep(/Api$/) - [:Api]).to_h do |const|
      method_name = const.to_s
                         .delete_suffix("Api")
                         .gsub(/([a-z\d])([A-Z])/, '\1_\2')
                         .downcase
      [method_name.to_sym, const]
    end.freeze

    attr_reader :client
    
    def initialize(api_key: ENV["FACTORIAL_API_KEY"], token: ENV["FACTORIAL_TOKEN"],
                   base_url: ENV["FACTORIAL_BASE_URL"])
      config = Config.new
      config.api_key["x-api-key"] = api_key
      config.access_token = token if token
      apply_base_url(config, base_url) if base_url
      @client = ApiClient.new(config)
      @apis = {}
    end

    API_CLASSES.each do |method_name, const|
      define_method(method_name) do
        @apis[method_name] ||= F.const_get(const).new(client)
      end
    end

    private def apply_base_url(config, base_url)
      uri = URI.parse(base_url)
      unless uri.is_a?(URI::HTTP) && uri.host
        raise ArgumentError,
              "base_url must be a full http(s) URL, e.g. https://api.factorialhr.com " \
              "(got #{base_url.inspect})"
      end

      config.scheme = uri.scheme
      config.host = uri.port == uri.default_port ? uri.host : "#{uri.host}:#{uri.port}"
      config.base_path = uri.path unless uri.path.empty?
    end
  end
end
