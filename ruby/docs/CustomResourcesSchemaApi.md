# F::CustomResourcesSchemaApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**custom_resources_schemas_get**](CustomResourcesSchemaApi.md#custom_resources_schemas_get) | **GET** /api/2026-07-01/resources/custom_resources/schemas | Reads all Schemas |
| [**custom_resources_schemas_id_get**](CustomResourcesSchemaApi.md#custom_resources_schemas_id_get) | **GET** /api/2026-07-01/resources/custom_resources/schemas/{id} | Reads a single Schema |
| [**custom_resources_schemas_post**](CustomResourcesSchemaApi.md#custom_resources_schemas_post) | **POST** /api/2026-07-01/resources/custom_resources/schemas | Creates a Schema |


## custom_resources_schemas_get

> <CustomResourcesSchemasGet200Response> custom_resources_schemas_get(opts)

Reads all Schemas

Reads all Schemas

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

api_instance = F::CustomResourcesSchemaApi.new
opts = {
  ids: ['inner_example'] # Array<String> | Schemas identifiers
}

begin
  # Reads all Schemas
  result = api_instance.custom_resources_schemas_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomResourcesSchemaApi->custom_resources_schemas_get: #{e}"
end
```

#### Using the custom_resources_schemas_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomResourcesSchemasGet200Response>, Integer, Hash)> custom_resources_schemas_get_with_http_info(opts)

```ruby
begin
  # Reads all Schemas
  data, status_code, headers = api_instance.custom_resources_schemas_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomResourcesSchemasGet200Response>
rescue F::ApiError => e
  puts "Error when calling CustomResourcesSchemaApi->custom_resources_schemas_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Schemas identifiers | [optional] |

### Return type

[**CustomResourcesSchemasGet200Response**](CustomResourcesSchemasGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## custom_resources_schemas_id_get

> <CustomResourcesSchema> custom_resources_schemas_id_get(id)

Reads a single Schema

Reads a single Schema

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

api_instance = F::CustomResourcesSchemaApi.new
id = '1' # String | Schemas identifiers

begin
  # Reads a single Schema
  result = api_instance.custom_resources_schemas_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomResourcesSchemaApi->custom_resources_schemas_id_get: #{e}"
end
```

#### Using the custom_resources_schemas_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomResourcesSchema>, Integer, Hash)> custom_resources_schemas_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Schema
  data, status_code, headers = api_instance.custom_resources_schemas_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomResourcesSchema>
rescue F::ApiError => e
  puts "Error when calling CustomResourcesSchemaApi->custom_resources_schemas_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Schemas identifiers |  |

### Return type

[**CustomResourcesSchema**](CustomResourcesSchema.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## custom_resources_schemas_post

> <CustomResourcesSchema> custom_resources_schemas_post(opts)

Creates a Schema

Creates a Schema

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

api_instance = F::CustomResourcesSchemaApi.new
opts = {
  custom_resources_schemas_post_request: F::CustomResourcesSchemasPostRequest.new({name: 'Company Offsite', company_id: '2', hidden: false}) # CustomResourcesSchemasPostRequest | 
}

begin
  # Creates a Schema
  result = api_instance.custom_resources_schemas_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomResourcesSchemaApi->custom_resources_schemas_post: #{e}"
end
```

#### Using the custom_resources_schemas_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomResourcesSchema>, Integer, Hash)> custom_resources_schemas_post_with_http_info(opts)

```ruby
begin
  # Creates a Schema
  data, status_code, headers = api_instance.custom_resources_schemas_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomResourcesSchema>
rescue F::ApiError => e
  puts "Error when calling CustomResourcesSchemaApi->custom_resources_schemas_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **custom_resources_schemas_post_request** | [**CustomResourcesSchemasPostRequest**](CustomResourcesSchemasPostRequest.md) |  | [optional] |

### Return type

[**CustomResourcesSchema**](CustomResourcesSchema.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

