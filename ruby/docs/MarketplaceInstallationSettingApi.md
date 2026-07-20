# F::MarketplaceInstallationSettingApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**marketplace_installation_settings_get**](MarketplaceInstallationSettingApi.md#marketplace_installation_settings_get) | **GET** /api/2026-07-01/resources/marketplace/installation_settings | Reads all Installation settings |


## marketplace_installation_settings_get

> <MarketplaceInstallationSettingsGet200Response> marketplace_installation_settings_get(company_id, integration_id)

Reads all Installation settings

Reads all Installation settings

### Examples

```ruby
require 'time'
require 'factorial_api'
# setup authorization
F.configure do |config|
  # Configure API key authorization: apikey
  config.api_key['x-api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x-api-key'] = 'Bearer'

  # Configure OAuth2 access token for authorization: oauth2
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = F::MarketplaceInstallationSettingApi.new
company_id = '1' # String | Identifier of the company
integration_id = 'Y0h_Sh7pRxCWpl0DySn_uQ' # String | ID of the integration

begin
  # Reads all Installation settings
  result = api_instance.marketplace_installation_settings_get(company_id, integration_id)
  p result
rescue F::ApiError => e
  puts "Error when calling MarketplaceInstallationSettingApi->marketplace_installation_settings_get: #{e}"
end
```

#### Using the marketplace_installation_settings_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<MarketplaceInstallationSettingsGet200Response>, Integer, Hash)> marketplace_installation_settings_get_with_http_info(company_id, integration_id)

```ruby
begin
  # Reads all Installation settings
  data, status_code, headers = api_instance.marketplace_installation_settings_get_with_http_info(company_id, integration_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <MarketplaceInstallationSettingsGet200Response>
rescue F::ApiError => e
  puts "Error when calling MarketplaceInstallationSettingApi->marketplace_installation_settings_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **company_id** | **String** | Identifier of the company |  |
| **integration_id** | **String** | ID of the integration |  |

### Return type

[**MarketplaceInstallationSettingsGet200Response**](MarketplaceInstallationSettingsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

