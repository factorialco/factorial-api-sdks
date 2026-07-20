# F::ContractsContractVersionApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**contracts_contract_versions_get**](ContractsContractVersionApi.md#contracts_contract_versions_get) | **GET** /api/2026-07-01/resources/contracts/contract_versions | Reads all Contract versions |
| [**contracts_contract_versions_id_delete**](ContractsContractVersionApi.md#contracts_contract_versions_id_delete) | **DELETE** /api/2026-07-01/resources/contracts/contract_versions/{id} | Deletes a Contract version |
| [**contracts_contract_versions_id_get**](ContractsContractVersionApi.md#contracts_contract_versions_id_get) | **GET** /api/2026-07-01/resources/contracts/contract_versions/{id} | Reads a single Contract version |
| [**contracts_contract_versions_id_put**](ContractsContractVersionApi.md#contracts_contract_versions_id_put) | **PUT** /api/2026-07-01/resources/contracts/contract_versions/{id} | Updates a Contract version |
| [**contracts_contract_versions_post**](ContractsContractVersionApi.md#contracts_contract_versions_post) | **POST** /api/2026-07-01/resources/contracts/contract_versions | Creates a Contract version |


## contracts_contract_versions_get

> <ContractsContractVersionsGet200Response> contracts_contract_versions_get(job_catalog_tree_node_uuids, opts)

Reads all Contract versions

Reads all Contract versions

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

api_instance = F::ContractsContractVersionApi.new
job_catalog_tree_node_uuids = ['inner_example'] # Array<String> | the uuid of nodes in the job catalog tree. As only level nodes are accepted and persisted, so filtering with other node types will return no results. Refer to job_catalog/tree_nodes endpoint.
opts = {
  ids: ['inner_example'], # Array<String> | list of contract version identifiers.
  employee_ids: ['inner_example'], # Array<String> | list of employee identifiers, refers to /employees/employees endpoint.
  date: '2024-10-06', # String | filters contracts of employees with effective_on date less or equal than the given date.
  updated_at_gteq: '2024-01-01T00:00:00.000Z', # String | Filter contract versions updated on or after this timestamp (ISO 8601). 
  updated_at_lteq: '2024-12-31T23:59:59.999Z' # String | Filter contract versions updated on or before this timestamp (ISO 8601). 
}

begin
  # Reads all Contract versions
  result = api_instance.contracts_contract_versions_get(job_catalog_tree_node_uuids, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionApi->contracts_contract_versions_get: #{e}"
end
```

#### Using the contracts_contract_versions_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsContractVersionsGet200Response>, Integer, Hash)> contracts_contract_versions_get_with_http_info(job_catalog_tree_node_uuids, opts)

```ruby
begin
  # Reads all Contract versions
  data, status_code, headers = api_instance.contracts_contract_versions_get_with_http_info(job_catalog_tree_node_uuids, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsContractVersionsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionApi->contracts_contract_versions_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **job_catalog_tree_node_uuids** | [**Array&lt;String&gt;**](String.md) | the uuid of nodes in the job catalog tree. As only level nodes are accepted and persisted, so filtering with other node types will return no results. Refer to job_catalog/tree_nodes endpoint. |  |
| **ids** | [**Array&lt;String&gt;**](String.md) | list of contract version identifiers. | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | list of employee identifiers, refers to /employees/employees endpoint. | [optional] |
| **date** | **String** | filters contracts of employees with effective_on date less or equal than the given date. | [optional] |
| **updated_at_gteq** | **String** | Filter contract versions updated on or after this timestamp (ISO 8601).  | [optional] |
| **updated_at_lteq** | **String** | Filter contract versions updated on or before this timestamp (ISO 8601).  | [optional] |

### Return type

[**ContractsContractVersionsGet200Response**](ContractsContractVersionsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_contract_versions_id_delete

> <ContractsContractVersion> contracts_contract_versions_id_delete(id)

Deletes a Contract version

Deletes a Contract version

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

api_instance = F::ContractsContractVersionApi.new
id = '1' # String | contract version identifier.

begin
  # Deletes a Contract version
  result = api_instance.contracts_contract_versions_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionApi->contracts_contract_versions_id_delete: #{e}"
end
```

#### Using the contracts_contract_versions_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsContractVersion>, Integer, Hash)> contracts_contract_versions_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Contract version
  data, status_code, headers = api_instance.contracts_contract_versions_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsContractVersion>
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionApi->contracts_contract_versions_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | contract version identifier. |  |

### Return type

[**ContractsContractVersion**](ContractsContractVersion.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_contract_versions_id_get

> <ContractsContractVersion> contracts_contract_versions_id_get(id)

Reads a single Contract version

Reads a single Contract version

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

api_instance = F::ContractsContractVersionApi.new
id = '1' # String | list of contract version identifiers.

begin
  # Reads a single Contract version
  result = api_instance.contracts_contract_versions_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionApi->contracts_contract_versions_id_get: #{e}"
end
```

#### Using the contracts_contract_versions_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsContractVersion>, Integer, Hash)> contracts_contract_versions_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Contract version
  data, status_code, headers = api_instance.contracts_contract_versions_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsContractVersion>
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionApi->contracts_contract_versions_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | list of contract version identifiers. |  |

### Return type

[**ContractsContractVersion**](ContractsContractVersion.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_contract_versions_id_put

> <ContractsContractVersion> contracts_contract_versions_id_put(id, opts)

Updates a Contract version

Updates a Contract version

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

api_instance = F::ContractsContractVersionApi.new
id = '1' # String | contract version identifier.
opts = {
  contracts_contract_versions_id_put_request: F::ContractsContractVersionsIdPutRequest.new({id: '1'}) # ContractsContractVersionsIdPutRequest | 
}

begin
  # Updates a Contract version
  result = api_instance.contracts_contract_versions_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionApi->contracts_contract_versions_id_put: #{e}"
end
```

#### Using the contracts_contract_versions_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsContractVersion>, Integer, Hash)> contracts_contract_versions_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Contract version
  data, status_code, headers = api_instance.contracts_contract_versions_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsContractVersion>
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionApi->contracts_contract_versions_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | contract version identifier. |  |
| **contracts_contract_versions_id_put_request** | [**ContractsContractVersionsIdPutRequest**](ContractsContractVersionsIdPutRequest.md) |  | [optional] |

### Return type

[**ContractsContractVersion**](ContractsContractVersion.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contracts_contract_versions_post

> <ContractsContractVersion> contracts_contract_versions_post(opts)

Creates a Contract version

Creates a Contract version

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

api_instance = F::ContractsContractVersionApi.new
opts = {
  contracts_contract_versions_post_request: F::ContractsContractVersionsPostRequest.new({employee_id: '1', effective_on: '2024-10-06', starts_on: '2024-10-06'}) # ContractsContractVersionsPostRequest | 
}

begin
  # Creates a Contract version
  result = api_instance.contracts_contract_versions_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionApi->contracts_contract_versions_post: #{e}"
end
```

#### Using the contracts_contract_versions_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsContractVersion>, Integer, Hash)> contracts_contract_versions_post_with_http_info(opts)

```ruby
begin
  # Creates a Contract version
  data, status_code, headers = api_instance.contracts_contract_versions_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsContractVersion>
rescue F::ApiError => e
  puts "Error when calling ContractsContractVersionApi->contracts_contract_versions_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **contracts_contract_versions_post_request** | [**ContractsContractVersionsPostRequest**](ContractsContractVersionsPostRequest.md) |  | [optional] |

### Return type

[**ContractsContractVersion**](ContractsContractVersion.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

