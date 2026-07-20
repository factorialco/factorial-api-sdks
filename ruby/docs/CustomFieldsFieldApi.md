# F::CustomFieldsFieldApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**custom_fields_fields_get**](CustomFieldsFieldApi.md#custom_fields_fields_get) | **GET** /api/2026-07-01/resources/custom_fields/fields | Reads all Fields |
| [**custom_fields_fields_id_delete**](CustomFieldsFieldApi.md#custom_fields_fields_id_delete) | **DELETE** /api/2026-07-01/resources/custom_fields/fields/{id} | Deletes a Field |
| [**custom_fields_fields_id_get**](CustomFieldsFieldApi.md#custom_fields_fields_id_get) | **GET** /api/2026-07-01/resources/custom_fields/fields/{id} | Reads a single Field |
| [**custom_fields_fields_post**](CustomFieldsFieldApi.md#custom_fields_fields_post) | **POST** /api/2026-07-01/resources/custom_fields/fields | Creates a Field |


## custom_fields_fields_get

> <CustomFieldsFieldsGet200Response> custom_fields_fields_get(opts)

Reads all Fields

Reads all Fields

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

api_instance = F::CustomFieldsFieldApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Field identifiers
  field_type: 'text', # String | Filter fields by type
  label: 'T-Shirt Size', # String | Field label
  slug: 'tshirt_size', # String | Custom field slug
  company_id: '3' # String | Company identifier where this field belongs
}

begin
  # Reads all Fields
  result = api_instance.custom_fields_fields_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomFieldsFieldApi->custom_fields_fields_get: #{e}"
end
```

#### Using the custom_fields_fields_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomFieldsFieldsGet200Response>, Integer, Hash)> custom_fields_fields_get_with_http_info(opts)

```ruby
begin
  # Reads all Fields
  data, status_code, headers = api_instance.custom_fields_fields_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomFieldsFieldsGet200Response>
rescue F::ApiError => e
  puts "Error when calling CustomFieldsFieldApi->custom_fields_fields_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Field identifiers | [optional] |
| **field_type** | **String** | Filter fields by type | [optional] |
| **label** | **String** | Field label | [optional] |
| **slug** | **String** | Custom field slug | [optional] |
| **company_id** | **String** | Company identifier where this field belongs | [optional] |

### Return type

[**CustomFieldsFieldsGet200Response**](CustomFieldsFieldsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## custom_fields_fields_id_delete

> <CustomFieldsField> custom_fields_fields_id_delete(id)

Deletes a Field

Deletes a Field

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

api_instance = F::CustomFieldsFieldApi.new
id = '1' # String | 

begin
  # Deletes a Field
  result = api_instance.custom_fields_fields_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomFieldsFieldApi->custom_fields_fields_id_delete: #{e}"
end
```

#### Using the custom_fields_fields_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomFieldsField>, Integer, Hash)> custom_fields_fields_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Field
  data, status_code, headers = api_instance.custom_fields_fields_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomFieldsField>
rescue F::ApiError => e
  puts "Error when calling CustomFieldsFieldApi->custom_fields_fields_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**CustomFieldsField**](CustomFieldsField.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## custom_fields_fields_id_get

> <CustomFieldsField> custom_fields_fields_id_get(id)

Reads a single Field

Reads a single Field

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

api_instance = F::CustomFieldsFieldApi.new
id = '1' # String | Field identifiers

begin
  # Reads a single Field
  result = api_instance.custom_fields_fields_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomFieldsFieldApi->custom_fields_fields_id_get: #{e}"
end
```

#### Using the custom_fields_fields_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomFieldsField>, Integer, Hash)> custom_fields_fields_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Field
  data, status_code, headers = api_instance.custom_fields_fields_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomFieldsField>
rescue F::ApiError => e
  puts "Error when calling CustomFieldsFieldApi->custom_fields_fields_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Field identifiers |  |

### Return type

[**CustomFieldsField**](CustomFieldsField.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## custom_fields_fields_post

> <CustomFieldsField> custom_fields_fields_post(opts)

Creates a Field

Creates a Field

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

api_instance = F::CustomFieldsFieldApi.new
opts = {
  custom_fields_fields_post_request: F::CustomFieldsFieldsPostRequest.new({company_id: '3', field_type: 'text'}) # CustomFieldsFieldsPostRequest | 
}

begin
  # Creates a Field
  result = api_instance.custom_fields_fields_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CustomFieldsFieldApi->custom_fields_fields_post: #{e}"
end
```

#### Using the custom_fields_fields_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CustomFieldsField>, Integer, Hash)> custom_fields_fields_post_with_http_info(opts)

```ruby
begin
  # Creates a Field
  data, status_code, headers = api_instance.custom_fields_fields_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CustomFieldsField>
rescue F::ApiError => e
  puts "Error when calling CustomFieldsFieldApi->custom_fields_fields_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **custom_fields_fields_post_request** | [**CustomFieldsFieldsPostRequest**](CustomFieldsFieldsPostRequest.md) |  | [optional] |

### Return type

[**CustomFieldsField**](CustomFieldsField.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

