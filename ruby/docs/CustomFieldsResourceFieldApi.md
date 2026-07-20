# F::CustomFieldsResourceFieldApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**custom_fields_resource_fields_get**](CustomFieldsResourceFieldApi.md#custom_fields_resource_fields_get) | **GET** /api/2026-07-01/resources/custom_fields/resource_fields | Reads all Resource fields |
| [**custom_fields_resource_fields_id_get**](CustomFieldsResourceFieldApi.md#custom_fields_resource_fields_id_get) | **GET** /api/2026-07-01/resources/custom_fields/resource_fields/{id} | Reads a single Resource field |
| [**custom_fields_resource_fields_post**](CustomFieldsResourceFieldApi.md#custom_fields_resource_fields_post) | **POST** /api/2026-07-01/resources/custom_fields/resource_fields | Creates a Resource field |


## custom_fields_resource_fields_get

> <CustomFieldsResourceFieldsGet200Response> custom_fields_resource_fields_get(opts)

Reads all Resource fields

Reads schema custom fields

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

api_instance = F::CustomFieldsResourceFieldApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Resource field identifiers
  field_ids: ['inner_example'], # Array<String> | Custom Field identifiers
  schema_ids: ['inner_example'] # Array<String> | Custom Resources Schema identifiers
}

begin
  # Reads all Resource fields
  result = api_instance.custom_fields_resource_fields_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomFieldsResourceFieldApi->custom_fields_resource_fields_get: #{e}"
end
```

#### Using the custom_fields_resource_fields_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomFieldsResourceFieldsGet200Response>, Integer, Hash)> custom_fields_resource_fields_get_with_http_info(opts)

```ruby
begin
  # Reads all Resource fields
  data, status_code, headers = api_instance.custom_fields_resource_fields_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomFieldsResourceFieldsGet200Response>
rescue F::ApiError => e
  puts "Error when calling CustomFieldsResourceFieldApi->custom_fields_resource_fields_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Resource field identifiers | [optional] |
| **field_ids** | [**Array&lt;String&gt;**](String.md) | Custom Field identifiers | [optional] |
| **schema_ids** | [**Array&lt;String&gt;**](String.md) | Custom Resources Schema identifiers | [optional] |

### Return type

[**CustomFieldsResourceFieldsGet200Response**](CustomFieldsResourceFieldsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## custom_fields_resource_fields_id_get

> <CustomFieldsResourceField> custom_fields_resource_fields_id_get(id)

Reads a single Resource field

Reads schema custom fields

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

api_instance = F::CustomFieldsResourceFieldApi.new
id = '1' # String | Resource field identifiers

begin
  # Reads a single Resource field
  result = api_instance.custom_fields_resource_fields_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomFieldsResourceFieldApi->custom_fields_resource_fields_id_get: #{e}"
end
```

#### Using the custom_fields_resource_fields_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomFieldsResourceField>, Integer, Hash)> custom_fields_resource_fields_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Resource field
  data, status_code, headers = api_instance.custom_fields_resource_fields_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomFieldsResourceField>
rescue F::ApiError => e
  puts "Error when calling CustomFieldsResourceFieldApi->custom_fields_resource_fields_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Resource field identifiers |  |

### Return type

[**CustomFieldsResourceField**](CustomFieldsResourceField.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## custom_fields_resource_fields_post

> <CustomFieldsResourceField> custom_fields_resource_fields_post(opts)

Creates a Resource field

Creates an schema custom field

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

api_instance = F::CustomFieldsResourceFieldApi.new
opts = {
  custom_fields_resource_fields_post_request: F::CustomFieldsResourceFieldsPostRequest.new({schema_id: '1', company_id: '1', field_type: 'text', required: true, editable: 'owned', visible: 'owned'}) # CustomFieldsResourceFieldsPostRequest | 
}

begin
  # Creates a Resource field
  result = api_instance.custom_fields_resource_fields_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomFieldsResourceFieldApi->custom_fields_resource_fields_post: #{e}"
end
```

#### Using the custom_fields_resource_fields_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomFieldsResourceField>, Integer, Hash)> custom_fields_resource_fields_post_with_http_info(opts)

```ruby
begin
  # Creates a Resource field
  data, status_code, headers = api_instance.custom_fields_resource_fields_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomFieldsResourceField>
rescue F::ApiError => e
  puts "Error when calling CustomFieldsResourceFieldApi->custom_fields_resource_fields_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **custom_fields_resource_fields_post_request** | [**CustomFieldsResourceFieldsPostRequest**](CustomFieldsResourceFieldsPostRequest.md) |  | [optional] |

### Return type

[**CustomFieldsResourceField**](CustomFieldsResourceField.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

