# F::CustomFieldsOptionApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**custom_fields_options_get**](CustomFieldsOptionApi.md#custom_fields_options_get) | **GET** /api/2026-07-01/resources/custom_fields/options | Reads all Options |
| [**custom_fields_options_id_get**](CustomFieldsOptionApi.md#custom_fields_options_id_get) | **GET** /api/2026-07-01/resources/custom_fields/options/{id} | Reads a single Option |
| [**custom_fields_options_post**](CustomFieldsOptionApi.md#custom_fields_options_post) | **POST** /api/2026-07-01/resources/custom_fields/options | Creates an Option |


## custom_fields_options_get

> <CustomFieldsOptionsGet200Response> custom_fields_options_get(opts)

Reads all Options

Reads all Options

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

api_instance = F::CustomFieldsOptionApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Options identifiers
  field_ids: ['inner_example'] # Array<String> | Identifiers for the fields where the options belong to
}

begin
  # Reads all Options
  result = api_instance.custom_fields_options_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomFieldsOptionApi->custom_fields_options_get: #{e}"
end
```

#### Using the custom_fields_options_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomFieldsOptionsGet200Response>, Integer, Hash)> custom_fields_options_get_with_http_info(opts)

```ruby
begin
  # Reads all Options
  data, status_code, headers = api_instance.custom_fields_options_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomFieldsOptionsGet200Response>
rescue F::ApiError => e
  puts "Error when calling CustomFieldsOptionApi->custom_fields_options_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Options identifiers | [optional] |
| **field_ids** | [**Array&lt;String&gt;**](String.md) | Identifiers for the fields where the options belong to | [optional] |

### Return type

[**CustomFieldsOptionsGet200Response**](CustomFieldsOptionsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## custom_fields_options_id_get

> <CustomFieldsOption> custom_fields_options_id_get(id)

Reads a single Option

Reads a single Option

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

api_instance = F::CustomFieldsOptionApi.new
id = '1' # String | Options identifiers

begin
  # Reads a single Option
  result = api_instance.custom_fields_options_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomFieldsOptionApi->custom_fields_options_id_get: #{e}"
end
```

#### Using the custom_fields_options_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomFieldsOption>, Integer, Hash)> custom_fields_options_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Option
  data, status_code, headers = api_instance.custom_fields_options_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomFieldsOption>
rescue F::ApiError => e
  puts "Error when calling CustomFieldsOptionApi->custom_fields_options_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Options identifiers |  |

### Return type

[**CustomFieldsOption**](CustomFieldsOption.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## custom_fields_options_post

> <CustomFieldsOption> custom_fields_options_post(opts)

Creates an Option

Creates an Option

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

api_instance = F::CustomFieldsOptionApi.new
opts = {
  custom_fields_options_post_request: F::CustomFieldsOptionsPostRequest.new({label: 'T-shirt size', field_id: '2'}) # CustomFieldsOptionsPostRequest | 
}

begin
  # Creates an Option
  result = api_instance.custom_fields_options_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomFieldsOptionApi->custom_fields_options_post: #{e}"
end
```

#### Using the custom_fields_options_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomFieldsOption>, Integer, Hash)> custom_fields_options_post_with_http_info(opts)

```ruby
begin
  # Creates an Option
  data, status_code, headers = api_instance.custom_fields_options_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomFieldsOption>
rescue F::ApiError => e
  puts "Error when calling CustomFieldsOptionApi->custom_fields_options_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **custom_fields_options_post_request** | [**CustomFieldsOptionsPostRequest**](CustomFieldsOptionsPostRequest.md) |  | [optional] |

### Return type

[**CustomFieldsOption**](CustomFieldsOption.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

