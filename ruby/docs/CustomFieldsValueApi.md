# F::CustomFieldsValueApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**custom_fields_values_get**](CustomFieldsValueApi.md#custom_fields_values_get) | **GET** /api/2026-07-01/resources/custom_fields/values | Reads all Values |
| [**custom_fields_values_id_get**](CustomFieldsValueApi.md#custom_fields_values_id_get) | **GET** /api/2026-07-01/resources/custom_fields/values/{id} | Reads a single Value |
| [**custom_fields_values_id_put**](CustomFieldsValueApi.md#custom_fields_values_id_put) | **PUT** /api/2026-07-01/resources/custom_fields/values/{id} | Updates a Value |
| [**custom_fields_values_post**](CustomFieldsValueApi.md#custom_fields_values_post) | **POST** /api/2026-07-01/resources/custom_fields/values | Creates a Value |


## custom_fields_values_get

> <CustomFieldsValuesGet200Response> custom_fields_values_get(opts)

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

api_instance = F::CustomFieldsValueApi.new
opts = {
  employee_ids: ['inner_example'], # Array<String> | Employee identifiers to filter custom field values by
  identifiers: ['inner_example'], # Array<String> | Custom field to filter by identifier
  ids: ['inner_example'], # Array<String> | Custom field value identifiers to filter by
  instance_id: '18', # String | Identifier of the instance that the custom field value is attached to
  value: '1235436', # String | Custom field value to filter by
  slug: 'matricule', # String | Custom field slug to filter by
  field_id: '75', # String | Custom field identifier to filter by
  updated_at_gteq: '2024-10-06' # String | Filter values updated on or after this date (ISO 8601 format).
}

begin
  # Reads all Values
  result = api_instance.custom_fields_values_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomFieldsValueApi->custom_fields_values_get: #{e}"
end
```

#### Using the custom_fields_values_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomFieldsValuesGet200Response>, Integer, Hash)> custom_fields_values_get_with_http_info(opts)

```ruby
begin
  # Reads all Values
  data, status_code, headers = api_instance.custom_fields_values_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomFieldsValuesGet200Response>
rescue F::ApiError => e
  puts "Error when calling CustomFieldsValueApi->custom_fields_values_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Employee identifiers to filter custom field values by | [optional] |
| **identifiers** | [**Array&lt;String&gt;**](String.md) | Custom field to filter by identifier | [optional] |
| **ids** | [**Array&lt;String&gt;**](String.md) | Custom field value identifiers to filter by | [optional] |
| **instance_id** | **String** | Identifier of the instance that the custom field value is attached to | [optional] |
| **value** | **String** | Custom field value to filter by | [optional] |
| **slug** | **String** | Custom field slug to filter by | [optional] |
| **field_id** | **String** | Custom field identifier to filter by | [optional] |
| **updated_at_gteq** | **String** | Filter values updated on or after this date (ISO 8601 format). | [optional] |

### Return type

[**CustomFieldsValuesGet200Response**](CustomFieldsValuesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## custom_fields_values_id_get

> <CustomFieldsValue> custom_fields_values_id_get(id)

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

api_instance = F::CustomFieldsValueApi.new
id = '73' # String | Custom field value identifiers to filter by

begin
  # Reads a single Value
  result = api_instance.custom_fields_values_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomFieldsValueApi->custom_fields_values_id_get: #{e}"
end
```

#### Using the custom_fields_values_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomFieldsValue>, Integer, Hash)> custom_fields_values_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Value
  data, status_code, headers = api_instance.custom_fields_values_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomFieldsValue>
rescue F::ApiError => e
  puts "Error when calling CustomFieldsValueApi->custom_fields_values_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Custom field value identifiers to filter by |  |

### Return type

[**CustomFieldsValue**](CustomFieldsValue.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## custom_fields_values_id_put

> <CustomFieldsValue> custom_fields_values_id_put(id, opts)

Updates a Value

Updates a Value

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

api_instance = F::CustomFieldsValueApi.new
id = '1' # String | 
opts = {
  custom_fields_values_id_put_request: F::CustomFieldsValuesIdPutRequest.new # CustomFieldsValuesIdPutRequest | 
}

begin
  # Updates a Value
  result = api_instance.custom_fields_values_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomFieldsValueApi->custom_fields_values_id_put: #{e}"
end
```

#### Using the custom_fields_values_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomFieldsValue>, Integer, Hash)> custom_fields_values_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Value
  data, status_code, headers = api_instance.custom_fields_values_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomFieldsValue>
rescue F::ApiError => e
  puts "Error when calling CustomFieldsValueApi->custom_fields_values_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **custom_fields_values_id_put_request** | [**CustomFieldsValuesIdPutRequest**](CustomFieldsValuesIdPutRequest.md) |  | [optional] |

### Return type

[**CustomFieldsValue**](CustomFieldsValue.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## custom_fields_values_post

> <CustomFieldsValue> custom_fields_values_post(opts)

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

api_instance = F::CustomFieldsValueApi.new
opts = {
  custom_fields_values_post_request: F::CustomFieldsValuesPostRequest.new({field_id: '1', valuable_type: 'Employee', valuable_id: '1', value: 'This is an example value for a custom field'}) # CustomFieldsValuesPostRequest | 
}

begin
  # Creates a Value
  result = api_instance.custom_fields_values_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomFieldsValueApi->custom_fields_values_post: #{e}"
end
```

#### Using the custom_fields_values_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomFieldsValue>, Integer, Hash)> custom_fields_values_post_with_http_info(opts)

```ruby
begin
  # Creates a Value
  data, status_code, headers = api_instance.custom_fields_values_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomFieldsValue>
rescue F::ApiError => e
  puts "Error when calling CustomFieldsValueApi->custom_fields_values_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **custom_fields_values_post_request** | [**CustomFieldsValuesPostRequest**](CustomFieldsValuesPostRequest.md) |  | [optional] |

### Return type

[**CustomFieldsValue**](CustomFieldsValue.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

