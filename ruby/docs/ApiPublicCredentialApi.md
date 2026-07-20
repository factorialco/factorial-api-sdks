# F::ApiPublicCredentialApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**api_public_credentials_get**](ApiPublicCredentialApi.md#api_public_credentials_get) | **GET** /api/2026-07-01/resources/api_public/credentials | Reads all Credentials |


## api_public_credentials_get

> <ApiPublicCredentialsGet200Response> api_public_credentials_get

Reads all Credentials

Reads all Credentials

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

api_instance = F::ApiPublicCredentialApi.new

begin
  # Reads all Credentials
  result = api_instance.api_public_credentials_get
  p result
rescue F::ApiError => e
  puts "Error when calling ApiPublicCredentialApi->api_public_credentials_get: #{e}"
end
```

#### Using the api_public_credentials_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ApiPublicCredentialsGet200Response>, Integer, Hash)> api_public_credentials_get_with_http_info

```ruby
begin
  # Reads all Credentials
  data, status_code, headers = api_instance.api_public_credentials_get_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ApiPublicCredentialsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ApiPublicCredentialApi->api_public_credentials_get_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiPublicCredentialsGet200Response**](ApiPublicCredentialsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

