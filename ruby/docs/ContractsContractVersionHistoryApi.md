# F::ContractsContractVersionHistoryApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**contracts_contract_version_histories_get**](ContractsContractVersionHistoryApi.md#contracts_contract_version_histories_get) | **GET** /api/2026-07-01/resources/contracts/contract_version_histories | Reads all Contract version histories |
| [**contracts_contract_version_histories_id_get**](ContractsContractVersionHistoryApi.md#contracts_contract_version_histories_id_get) | **GET** /api/2026-07-01/resources/contracts/contract_version_histories/{id} | Reads a single Contract version history |


## contracts_contract_version_histories_get

> <ContractsContractVersionHistoriesGet200Response> contracts_contract_version_histories_get(opts)

Reads all Contract version histories

Reads all Contract version histories

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

api_instance = F::ContractsContractVersionHistoryApi.new
opts = {
  ids: ['inner_example'], # Array<String> | the ids of the contract versions.
  contract_version_ids: ['inner_example'], # Array<String> | the ids of the contract versions.
  employee_ids: ['inner_example'], # Array<String> | the ids of the employees.
  current_on: '2024-10-06', # String | the date to filter the contract version histories.
  changes_lteq: '2024-10-07', # String | the date to filter the contract version histories.
  changes_gteq: '2024-10-05' # String | the date to filter the contract version histories.
}

begin
  # Reads all Contract version histories
  result = api_instance.contracts_contract_version_histories_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionHistoryApi->contracts_contract_version_histories_get: #{e}"
end
```

#### Using the contracts_contract_version_histories_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsContractVersionHistoriesGet200Response>, Integer, Hash)> contracts_contract_version_histories_get_with_http_info(opts)

```ruby
begin
  # Reads all Contract version histories
  data, status_code, headers = api_instance.contracts_contract_version_histories_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsContractVersionHistoriesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionHistoryApi->contracts_contract_version_histories_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | the ids of the contract versions. | [optional] |
| **contract_version_ids** | [**Array&lt;String&gt;**](String.md) | the ids of the contract versions. | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | the ids of the employees. | [optional] |
| **current_on** | **String** | the date to filter the contract version histories. | [optional] |
| **changes_lteq** | **String** | the date to filter the contract version histories. | [optional] |
| **changes_gteq** | **String** | the date to filter the contract version histories. | [optional] |

### Return type

[**ContractsContractVersionHistoriesGet200Response**](ContractsContractVersionHistoriesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_contract_version_histories_id_get

> <ContractsContractVersionHistory> contracts_contract_version_histories_id_get(id)

Reads a single Contract version history

Reads a single Contract version history

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

api_instance = F::ContractsContractVersionHistoryApi.new
id = '1' # String | the ids of the contract versions.

begin
  # Reads a single Contract version history
  result = api_instance.contracts_contract_version_histories_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionHistoryApi->contracts_contract_version_histories_id_get: #{e}"
end
```

#### Using the contracts_contract_version_histories_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsContractVersionHistory>, Integer, Hash)> contracts_contract_version_histories_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Contract version history
  data, status_code, headers = api_instance.contracts_contract_version_histories_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsContractVersionHistory>
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionHistoryApi->contracts_contract_version_histories_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | the ids of the contract versions. |  |

### Return type

[**ContractsContractVersionHistory**](ContractsContractVersionHistory.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

