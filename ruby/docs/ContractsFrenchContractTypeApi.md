# F::ContractsFrenchContractTypeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**contracts_french_contract_types_get**](ContractsFrenchContractTypeApi.md#contracts_french_contract_types_get) | **GET** /api/2026-07-01/resources/contracts/french_contract_types | Reads all French contract types |
| [**contracts_french_contract_types_id_get**](ContractsFrenchContractTypeApi.md#contracts_french_contract_types_id_get) | **GET** /api/2026-07-01/resources/contracts/french_contract_types/{id} | Reads a single French contract type |


## contracts_french_contract_types_get

> <ContractsFrenchContractTypesGet200Response> contracts_french_contract_types_get(opts)

Reads all French contract types

Reads all French contract types

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

api_instance = F::ContractsFrenchContractTypeApi.new
opts = {
  ids: ['inner_example'], # Array<String> | list of contract type identifiers.
  archived: false # Boolean | whether to show archived types or not.
}

begin
  # Reads all French contract types
  result = api_instance.contracts_french_contract_types_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsFrenchContractTypeApi->contracts_french_contract_types_get: #{e}"
end
```

#### Using the contracts_french_contract_types_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsFrenchContractTypesGet200Response>, Integer, Hash)> contracts_french_contract_types_get_with_http_info(opts)

```ruby
begin
  # Reads all French contract types
  data, status_code, headers = api_instance.contracts_french_contract_types_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsFrenchContractTypesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ContractsFrenchContractTypeApi->contracts_french_contract_types_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | list of contract type identifiers. | [optional] |
| **archived** | **Boolean** | whether to show archived types or not. | [optional] |

### Return type

[**ContractsFrenchContractTypesGet200Response**](ContractsFrenchContractTypesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_french_contract_types_id_get

> <ContractsFrenchContractType> contracts_french_contract_types_id_get(id)

Reads a single French contract type

Reads a single French contract type

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

api_instance = F::ContractsFrenchContractTypeApi.new
id = '1' # String | list of contract type identifiers.

begin
  # Reads a single French contract type
  result = api_instance.contracts_french_contract_types_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsFrenchContractTypeApi->contracts_french_contract_types_id_get: #{e}"
end
```

#### Using the contracts_french_contract_types_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsFrenchContractType>, Integer, Hash)> contracts_french_contract_types_id_get_with_http_info(id)

```ruby
begin
  # Reads a single French contract type
  data, status_code, headers = api_instance.contracts_french_contract_types_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsFrenchContractType>
rescue F::ApiError => e
  puts "Error when calling ContractsFrenchContractTypeApi->contracts_french_contract_types_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | list of contract type identifiers. |  |

### Return type

[**ContractsFrenchContractType**](ContractsFrenchContractType.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

