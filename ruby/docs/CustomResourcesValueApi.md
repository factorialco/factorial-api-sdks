# F::CustomResourcesValueApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**custom_resources_values_get**](CustomResourcesValueApi.md#custom_resources_values_get) | **GET** /api/2026-07-01/resources/custom_resources/values | Reads all Values |
| [**custom_resources_values_id_get**](CustomResourcesValueApi.md#custom_resources_values_id_get) | **GET** /api/2026-07-01/resources/custom_resources/values/{id} | Reads a single Value |
| [**custom_resources_values_post**](CustomResourcesValueApi.md#custom_resources_values_post) | **POST** /api/2026-07-01/resources/custom_resources/values | Creates a Value |


## custom_resources_values_get

> <CustomResourcesValuesGet200Response> custom_resources_values_get(opts)

Reads all Values

Reads all Values

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

api_instance = F::CustomResourcesValueApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Values identifiers
  employee_ids: ['inner_example'] # Array<String> | Employee identifiers
}

begin
  # Reads all Values
  result = api_instance.custom_resources_values_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomResourcesValueApi->custom_resources_values_get: #{e}"
end
```

#### Using the custom_resources_values_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomResourcesValuesGet200Response>, Integer, Hash)> custom_resources_values_get_with_http_info(opts)

```ruby
begin
  # Reads all Values
  data, status_code, headers = api_instance.custom_resources_values_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomResourcesValuesGet200Response>
rescue F::ApiError => e
  puts "Error when calling CustomResourcesValueApi->custom_resources_values_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Values identifiers | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Employee identifiers | [optional] |

### Return type

[**CustomResourcesValuesGet200Response**](CustomResourcesValuesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## custom_resources_values_id_get

> <CustomResourcesValue> custom_resources_values_id_get(id)

Reads a single Value

Reads a single Value

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

api_instance = F::CustomResourcesValueApi.new
id = '1' # String | Values identifiers

begin
  # Reads a single Value
  result = api_instance.custom_resources_values_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomResourcesValueApi->custom_resources_values_id_get: #{e}"
end
```

#### Using the custom_resources_values_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomResourcesValue>, Integer, Hash)> custom_resources_values_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Value
  data, status_code, headers = api_instance.custom_resources_values_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomResourcesValue>
rescue F::ApiError => e
  puts "Error when calling CustomResourcesValueApi->custom_resources_values_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Values identifiers |  |

### Return type

[**CustomResourcesValue**](CustomResourcesValue.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## custom_resources_values_post

> <CustomResourcesValue> custom_resources_values_post(opts)

Creates a Value

Creates a Value

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

api_instance = F::CustomResourcesValueApi.new
opts = {
  custom_resources_values_post_request: F::CustomResourcesValuesPostRequest.new({schema_id: '1', employee_id: '1', field_id: '2', value: 'This is an example value for a custom field'}) # CustomResourcesValuesPostRequest | 
}

begin
  # Creates a Value
  result = api_instance.custom_resources_values_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomResourcesValueApi->custom_resources_values_post: #{e}"
end
```

#### Using the custom_resources_values_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomResourcesValue>, Integer, Hash)> custom_resources_values_post_with_http_info(opts)

```ruby
begin
  # Creates a Value
  data, status_code, headers = api_instance.custom_resources_values_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomResourcesValue>
rescue F::ApiError => e
  puts "Error when calling CustomResourcesValueApi->custom_resources_values_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **custom_resources_values_post_request** | [**CustomResourcesValuesPostRequest**](CustomResourcesValuesPostRequest.md) |  | [optional] |

### Return type

[**CustomResourcesValue**](CustomResourcesValue.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

