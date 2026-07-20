# F::CustomResourcesResourceApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**custom_resources_resources_get**](CustomResourcesResourceApi.md#custom_resources_resources_get) | **GET** /api/2026-07-01/resources/custom_resources/resources | Reads all Resources |
| [**custom_resources_resources_id_get**](CustomResourcesResourceApi.md#custom_resources_resources_id_get) | **GET** /api/2026-07-01/resources/custom_resources/resources/{id} | Reads a single Resource |


## custom_resources_resources_get

> <CustomResourcesResourcesGet200Response> custom_resources_resources_get(opts)

Reads all Resources

Reads all Resources

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

api_instance = F::CustomResourcesResourceApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Resource identifiers
  employee_ids: ['inner_example'] # Array<String> | Employee identifiers
}

begin
  # Reads all Resources
  result = api_instance.custom_resources_resources_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomResourcesResourceApi->custom_resources_resources_get: #{e}"
end
```

#### Using the custom_resources_resources_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomResourcesResourcesGet200Response>, Integer, Hash)> custom_resources_resources_get_with_http_info(opts)

```ruby
begin
  # Reads all Resources
  data, status_code, headers = api_instance.custom_resources_resources_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomResourcesResourcesGet200Response>
rescue F::ApiError => e
  puts "Error when calling CustomResourcesResourceApi->custom_resources_resources_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Resource identifiers | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Employee identifiers | [optional] |

### Return type

[**CustomResourcesResourcesGet200Response**](CustomResourcesResourcesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## custom_resources_resources_id_get

> <CustomResourcesResource> custom_resources_resources_id_get(id)

Reads a single Resource

Reads a single Resource

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

api_instance = F::CustomResourcesResourceApi.new
id = '1' # String | Resource identifiers

begin
  # Reads a single Resource
  result = api_instance.custom_resources_resources_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomResourcesResourceApi->custom_resources_resources_id_get: #{e}"
end
```

#### Using the custom_resources_resources_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomResourcesResource>, Integer, Hash)> custom_resources_resources_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Resource
  data, status_code, headers = api_instance.custom_resources_resources_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomResourcesResource>
rescue F::ApiError => e
  puts "Error when calling CustomResourcesResourceApi->custom_resources_resources_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Resource identifiers |  |

### Return type

[**CustomResourcesResource**](CustomResourcesResource.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

