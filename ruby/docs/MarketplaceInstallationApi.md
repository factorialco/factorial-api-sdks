# F::MarketplaceInstallationApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**marketplace_installations_post**](MarketplaceInstallationApi.md#marketplace_installations_post) | **POST** /api/2026-07-01/resources/marketplace/installations | Creates an Installation |


## marketplace_installations_post

> <MarketplaceInstallation> marketplace_installations_post(opts)

Creates an Installation

Creates an Installation

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

api_instance = F::MarketplaceInstallationApi.new
opts = {
  marketplace_installations_post_request: F::MarketplaceInstallationsPostRequest.new({company_id: '1', integration_uuid: '123e4567-e89b-12d3-a456-426614174000'}) # MarketplaceInstallationsPostRequest | 
}

begin
  # Creates an Installation
  result = api_instance.marketplace_installations_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling MarketplaceInstallationApi->marketplace_installations_post: #{e}"
end
```

#### Using the marketplace_installations_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<MarketplaceInstallation>, Integer, Hash)> marketplace_installations_post_with_http_info(opts)

```ruby
begin
  # Creates an Installation
  data, status_code, headers = api_instance.marketplace_installations_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <MarketplaceInstallation>
rescue F::ApiError => e
  puts "Error when calling MarketplaceInstallationApi->marketplace_installations_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **marketplace_installations_post_request** | [**MarketplaceInstallationsPostRequest**](MarketplaceInstallationsPostRequest.md) |  | [optional] |

### Return type

[**MarketplaceInstallation**](MarketplaceInstallation.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

