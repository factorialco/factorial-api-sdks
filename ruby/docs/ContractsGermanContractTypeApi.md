# F::ContractsGermanContractTypeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**contracts_german_contract_types_get**](ContractsGermanContractTypeApi.md#contracts_german_contract_types_get) | **GET** /api/2026-07-01/resources/contracts/german_contract_types | Reads all German contract types |
| [**contracts_german_contract_types_id_get**](ContractsGermanContractTypeApi.md#contracts_german_contract_types_id_get) | **GET** /api/2026-07-01/resources/contracts/german_contract_types/{id} | Reads a single German contract type |


## contracts_german_contract_types_get

> <ContractsGermanContractTypesGet200Response> contracts_german_contract_types_get(opts)

Reads all German contract types

Reads all German contract types

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

api_instance = F::ContractsGermanContractTypeApi.new
opts = {
  ids: ['inner_example'], # Array<String> | list of contract type identifiers.
  archived: false # Boolean | whether to show archived types or not.
}

begin
  # Reads all German contract types
  result = api_instance.contracts_german_contract_types_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsGermanContractTypeApi->contracts_german_contract_types_get: #{e}"
end
```

#### Using the contracts_german_contract_types_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsGermanContractTypesGet200Response>, Integer, Hash)> contracts_german_contract_types_get_with_http_info(opts)

```ruby
begin
  # Reads all German contract types
  data, status_code, headers = api_instance.contracts_german_contract_types_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsGermanContractTypesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ContractsGermanContractTypeApi->contracts_german_contract_types_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | list of contract type identifiers. | [optional] |
| **archived** | **Boolean** | whether to show archived types or not. | [optional] |

### Return type

[**ContractsGermanContractTypesGet200Response**](ContractsGermanContractTypesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_german_contract_types_id_get

> <ContractsGermanContractType> contracts_german_contract_types_id_get(id)

Reads a single German contract type

Reads a single German contract type

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

api_instance = F::ContractsGermanContractTypeApi.new
id = '1' # String | list of contract type identifiers.

begin
  # Reads a single German contract type
  result = api_instance.contracts_german_contract_types_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsGermanContractTypeApi->contracts_german_contract_types_id_get: #{e}"
end
```

#### Using the contracts_german_contract_types_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsGermanContractType>, Integer, Hash)> contracts_german_contract_types_id_get_with_http_info(id)

```ruby
begin
  # Reads a single German contract type
  data, status_code, headers = api_instance.contracts_german_contract_types_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsGermanContractType>
rescue F::ApiError => e
  puts "Error when calling ContractsGermanContractTypeApi->contracts_german_contract_types_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | list of contract type identifiers. |  |

### Return type

[**ContractsGermanContractType**](ContractsGermanContractType.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

