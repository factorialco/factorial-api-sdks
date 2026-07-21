# frozen_string_literal: true

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
    
    def initialize(api_key: ENV["FACTORIAL_API_KEY"], token: ENV["FACTORIAL_TOKEN"], host: nil)
      config = Config.new
      config.api_key["x-api-key"] = api_key
      config.access_token = token if token
      config.host = host if host
      @client = ApiClient.new(config)
      @apis = {}
    end


    API_CLASSES.each do |method_name, const|
      define_method(method_name) do
        @apis[method_name] ||= F.const_get(const).new(client)
      end
    end
  end
end
