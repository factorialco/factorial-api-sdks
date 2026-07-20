# F::ContractsSpanishWorkingDayTypeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**contracts_spanish_working_day_types_get**](ContractsSpanishWorkingDayTypeApi.md#contracts_spanish_working_day_types_get) | **GET** /api/2026-07-01/resources/contracts/spanish_working_day_types | Reads all Spanish working day types |
| [**contracts_spanish_working_day_types_id_get**](ContractsSpanishWorkingDayTypeApi.md#contracts_spanish_working_day_types_id_get) | **GET** /api/2026-07-01/resources/contracts/spanish_working_day_types/{id} | Reads a single Spanish working day type |
| [**contracts_spanish_working_day_types_post**](ContractsSpanishWorkingDayTypeApi.md#contracts_spanish_working_day_types_post) | **POST** /api/2026-07-01/resources/contracts/spanish_working_day_types | Creates a Spanish working day type |


## contracts_spanish_working_day_types_get

> <ContractsSpanishWorkingDayTypesGet200Response> contracts_spanish_working_day_types_get(opts)

Reads all Spanish working day types

Reads all Spanish working day types

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

api_instance = F::ContractsSpanishWorkingDayTypeApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Working day type ids
  contract_template_id: '1' # String | Contract template identifier, refers to contracts/contract_templates
}

begin
  # Reads all Spanish working day types
  result = api_instance.contracts_spanish_working_day_types_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishWorkingDayTypeApi->contracts_spanish_working_day_types_get: #{e}"
end
```

#### Using the contracts_spanish_working_day_types_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsSpanishWorkingDayTypesGet200Response>, Integer, Hash)> contracts_spanish_working_day_types_get_with_http_info(opts)

```ruby
begin
  # Reads all Spanish working day types
  data, status_code, headers = api_instance.contracts_spanish_working_day_types_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsSpanishWorkingDayTypesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishWorkingDayTypeApi->contracts_spanish_working_day_types_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Working day type ids | [optional] |
| **contract_template_id** | **String** | Contract template identifier, refers to contracts/contract_templates | [optional] |

### Return type

[**ContractsSpanishWorkingDayTypesGet200Response**](ContractsSpanishWorkingDayTypesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_spanish_working_day_types_id_get

> <ContractsSpanishWorkingDayType> contracts_spanish_working_day_types_id_get(id)

Reads a single Spanish working day type

Reads a single Spanish working day type

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

api_instance = F::ContractsSpanishWorkingDayTypeApi.new
id = '1' # String | Working day type ids

begin
  # Reads a single Spanish working day type
  result = api_instance.contracts_spanish_working_day_types_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishWorkingDayTypeApi->contracts_spanish_working_day_types_id_get: #{e}"
end
```

#### Using the contracts_spanish_working_day_types_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsSpanishWorkingDayType>, Integer, Hash)> contracts_spanish_working_day_types_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Spanish working day type
  data, status_code, headers = api_instance.contracts_spanish_working_day_types_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsSpanishWorkingDayType>
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishWorkingDayTypeApi->contracts_spanish_working_day_types_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Working day type ids |  |

### Return type

[**ContractsSpanishWorkingDayType**](ContractsSpanishWorkingDayType.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_spanish_working_day_types_post

> <ContractsSpanishWorkingDayType> contracts_spanish_working_day_types_post(opts)

Creates a Spanish working day type

Creates a Spanish working day type

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

api_instance = F::ContractsSpanishWorkingDayTypeApi.new
opts = {
  contracts_spanish_working_day_types_post_request: F::ContractsSpanishWorkingDayTypesPostRequest.new({name: 'Fulltime'}) # ContractsSpanishWorkingDayTypesPostRequest | 
}

begin
  # Creates a Spanish working day type
  result = api_instance.contracts_spanish_working_day_types_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishWorkingDayTypeApi->contracts_spanish_working_day_types_post: #{e}"
end
```

#### Using the contracts_spanish_working_day_types_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsSpanishWorkingDayType>, Integer, Hash)> contracts_spanish_working_day_types_post_with_http_info(opts)

```ruby
begin
  # Creates a Spanish working day type
  data, status_code, headers = api_instance.contracts_spanish_working_day_types_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsSpanishWorkingDayType>
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishWorkingDayTypeApi->contracts_spanish_working_day_types_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **contracts_spanish_working_day_types_post_request** | [**ContractsSpanishWorkingDayTypesPostRequest**](ContractsSpanishWorkingDayTypesPostRequest.md) |  | [optional] |

### Return type

[**ContractsSpanishWorkingDayType**](ContractsSpanishWorkingDayType.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

