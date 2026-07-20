# F::ProcurementTypeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**procurement_types_get**](ProcurementTypeApi.md#procurement_types_get) | **GET** /api/2026-07-01/resources/procurement/types | Reads all Types |
| [**procurement_types_id_get**](ProcurementTypeApi.md#procurement_types_id_get) | **GET** /api/2026-07-01/resources/procurement/types/{id} | Reads a single Type |


## procurement_types_get

> <ProcurementTypesGet200Response> procurement_types_get(opts)

Reads all Types

Fetch one or all procurement types for the company.

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

api_instance = F::ProcurementTypeApi.new
opts = {
  ids: ['inner_example'] # Array<String> | An array of procurement type IDs to filter by.
}

begin
  # Reads all Types
  result = api_instance.procurement_types_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProcurementTypeApi->procurement_types_get: #{e}"
end
```

#### Using the procurement_types_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProcurementTypesGet200Response>, Integer, Hash)> procurement_types_get_with_http_info(opts)

```ruby
begin
  # Reads all Types
  data, status_code, headers = api_instance.procurement_types_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProcurementTypesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ProcurementTypeApi->procurement_types_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | An array of procurement type IDs to filter by. | [optional] |

### Return type

[**ProcurementTypesGet200Response**](ProcurementTypesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## procurement_types_id_get

> <ProcurementType> procurement_types_id_get(id)

Reads a single Type

Fetch one or all procurement types for the company.

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

api_instance = F::ProcurementTypeApi.new
id = '1' # String | An array of procurement type IDs to filter by.

begin
  # Reads a single Type
  result = api_instance.procurement_types_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProcurementTypeApi->procurement_types_id_get: #{e}"
end
```

#### Using the procurement_types_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProcurementType>, Integer, Hash)> procurement_types_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Type
  data, status_code, headers = api_instance.procurement_types_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProcurementType>
rescue F::ApiError => e
  puts "Error when calling ProcurementTypeApi->procurement_types_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | An array of procurement type IDs to filter by. |  |

### Return type

[**ProcurementType**](ProcurementType.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

