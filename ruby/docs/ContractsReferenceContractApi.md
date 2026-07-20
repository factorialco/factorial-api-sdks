# F::ContractsReferenceContractApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**contracts_reference_contracts_get**](ContractsReferenceContractApi.md#contracts_reference_contracts_get) | **GET** /api/2026-07-01/resources/contracts/reference_contracts | Reads all Reference contracts |


## contracts_reference_contracts_get

> <ContractsContractVersionsGet200Response> contracts_reference_contracts_get(job_catalog_tree_node_uuids, opts)

Reads all Reference contracts

Reads all Reference Contracts. The reference contract is the contract that applies today. If no contract applies today, we will return the nearest upcoming contract. If there are no upcoming contracts, we will provide the most recent past contract.

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

api_instance = F::ContractsReferenceContractApi.new
job_catalog_tree_node_uuids = ['inner_example'] # Array<String> | the uuid of nodes in the job catalog tree.
opts = {
  employee_ids: ['inner_example'] # Array<String> | filter by employee ids.
}

begin
  # Reads all Reference contracts
  result = api_instance.contracts_reference_contracts_get(job_catalog_tree_node_uuids, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsReferenceContractApi->contracts_reference_contracts_get: #{e}"
end
```

#### Using the contracts_reference_contracts_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsContractVersionsGet200Response>, Integer, Hash)> contracts_reference_contracts_get_with_http_info(job_catalog_tree_node_uuids, opts)

```ruby
begin
  # Reads all Reference contracts
  data, status_code, headers = api_instance.contracts_reference_contracts_get_with_http_info(job_catalog_tree_node_uuids, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsContractVersionsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ContractsReferenceContractApi->contracts_reference_contracts_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **job_catalog_tree_node_uuids** | [**Array&lt;String&gt;**](String.md) | the uuid of nodes in the job catalog tree. |  |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | filter by employee ids. | [optional] |

### Return type

[**ContractsContractVersionsGet200Response**](ContractsContractVersionsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

