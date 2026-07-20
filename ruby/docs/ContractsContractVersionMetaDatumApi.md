# F::ContractsContractVersionMetaDatumApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**contracts_contract_version_meta_data_get**](ContractsContractVersionMetaDatumApi.md#contracts_contract_version_meta_data_get) | **GET** /api/2026-07-01/resources/contracts/contract_version_meta_data | Reads all Contract version meta data |


## contracts_contract_version_meta_data_get

> <ContractsContractVersionMetaDataGet200Response> contracts_contract_version_meta_data_get(contract_version_ids)

Reads all Contract version meta data

Reads all Contract version meta data

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

api_instance = F::ContractsContractVersionMetaDatumApi.new
contract_version_ids = ['inner_example'] # Array<String> | list of contract version ids identifiers.

begin
  # Reads all Contract version meta data
  result = api_instance.contracts_contract_version_meta_data_get(contract_version_ids)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionMetaDatumApi->contracts_contract_version_meta_data_get: #{e}"
end
```

#### Using the contracts_contract_version_meta_data_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsContractVersionMetaDataGet200Response>, Integer, Hash)> contracts_contract_version_meta_data_get_with_http_info(contract_version_ids)

```ruby
begin
  # Reads all Contract version meta data
  data, status_code, headers = api_instance.contracts_contract_version_meta_data_get_with_http_info(contract_version_ids)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsContractVersionMetaDataGet200Response>
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionMetaDatumApi->contracts_contract_version_meta_data_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **contract_version_ids** | [**Array&lt;String&gt;**](String.md) | list of contract version ids identifiers. |  |

### Return type

[**ContractsContractVersionMetaDataGet200Response**](ContractsContractVersionMetaDataGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

