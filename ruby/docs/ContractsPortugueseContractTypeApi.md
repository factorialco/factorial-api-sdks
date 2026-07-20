# F::ContractsPortugueseContractTypeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**contracts_portuguese_contract_types_get**](ContractsPortugueseContractTypeApi.md#contracts_portuguese_contract_types_get) | **GET** /api/2026-07-01/resources/contracts/portuguese_contract_types | Reads all Portuguese contract types |
| [**contracts_portuguese_contract_types_id_get**](ContractsPortugueseContractTypeApi.md#contracts_portuguese_contract_types_id_get) | **GET** /api/2026-07-01/resources/contracts/portuguese_contract_types/{id} | Reads a single Portuguese contract type |


## contracts_portuguese_contract_types_get

> <ContractsPortugueseContractTypesGet200Response> contracts_portuguese_contract_types_get(opts)

Reads all Portuguese contract types

Reads all Portuguese contract types

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

api_instance = F::ContractsPortugueseContractTypeApi.new
opts = {
  ids: ['inner_example'], # Array<String> | list of contract type identifiers.
  archived: false # Boolean | whether to show archived types or not.
}

begin
  # Reads all Portuguese contract types
  result = api_instance.contracts_portuguese_contract_types_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsPortugueseContractTypeApi->contracts_portuguese_contract_types_get: #{e}"
end
```

#### Using the contracts_portuguese_contract_types_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsPortugueseContractTypesGet200Response>, Integer, Hash)> contracts_portuguese_contract_types_get_with_http_info(opts)

```ruby
begin
  # Reads all Portuguese contract types
  data, status_code, headers = api_instance.contracts_portuguese_contract_types_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsPortugueseContractTypesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ContractsPortugueseContractTypeApi->contracts_portuguese_contract_types_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | list of contract type identifiers. | [optional] |
| **archived** | **Boolean** | whether to show archived types or not. | [optional] |

### Return type

[**ContractsPortugueseContractTypesGet200Response**](ContractsPortugueseContractTypesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_portuguese_contract_types_id_get

> <ContractsPortugueseContractType> contracts_portuguese_contract_types_id_get(id)

Reads a single Portuguese contract type

Reads a single Portuguese contract type

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

api_instance = F::ContractsPortugueseContractTypeApi.new
id = '1' # String | list of contract type identifiers.

begin
  # Reads a single Portuguese contract type
  result = api_instance.contracts_portuguese_contract_types_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsPortugueseContractTypeApi->contracts_portuguese_contract_types_id_get: #{e}"
end
```

#### Using the contracts_portuguese_contract_types_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsPortugueseContractType>, Integer, Hash)> contracts_portuguese_contract_types_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Portuguese contract type
  data, status_code, headers = api_instance.contracts_portuguese_contract_types_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsPortugueseContractType>
rescue F::ApiError => e
  puts "Error when calling ContractsPortugueseContractTypeApi->contracts_portuguese_contract_types_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | list of contract type identifiers. |  |

### Return type

[**ContractsPortugueseContractType**](ContractsPortugueseContractType.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

