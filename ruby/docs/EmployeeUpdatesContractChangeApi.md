# F::EmployeeUpdatesContractChangeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**employee_updates_contract_changes_get**](EmployeeUpdatesContractChangeApi.md#employee_updates_contract_changes_get) | **GET** /api/2026-07-01/resources/employee_updates/contract_changes | Reads all Contract changes |
| [**employee_updates_contract_changes_id_get**](EmployeeUpdatesContractChangeApi.md#employee_updates_contract_changes_id_get) | **GET** /api/2026-07-01/resources/employee_updates/contract_changes/{id} | Reads a single Contract change |


## employee_updates_contract_changes_get

> <EmployeeUpdatesContractChangesGet200Response> employee_updates_contract_changes_get(opts)

Reads all Contract changes

This endpoint can be used to retrieve a list of contract changes `employee updates` details.

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

api_instance = F::EmployeeUpdatesContractChangeApi.new
opts = {
  ids: ['inner_example'] # Array<String> | filter by contract change incidence ids.
}

begin
  # Reads all Contract changes
  result = api_instance.employee_updates_contract_changes_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesContractChangeApi->employee_updates_contract_changes_get: #{e}"
end
```

#### Using the employee_updates_contract_changes_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeeUpdatesContractChangesGet200Response>, Integer, Hash)> employee_updates_contract_changes_get_with_http_info(opts)

```ruby
begin
  # Reads all Contract changes
  data, status_code, headers = api_instance.employee_updates_contract_changes_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeeUpdatesContractChangesGet200Response>
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesContractChangeApi->employee_updates_contract_changes_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | filter by contract change incidence ids. | [optional] |

### Return type

[**EmployeeUpdatesContractChangesGet200Response**](EmployeeUpdatesContractChangesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## employee_updates_contract_changes_id_get

> <EmployeeUpdatesContractChange> employee_updates_contract_changes_id_get(id)

Reads a single Contract change

This endpoint can be used to retrieve a list of contract changes `employee updates` details.

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

api_instance = F::EmployeeUpdatesContractChangeApi.new
id = '1' # String | filter by contract change incidence ids.

begin
  # Reads a single Contract change
  result = api_instance.employee_updates_contract_changes_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesContractChangeApi->employee_updates_contract_changes_id_get: #{e}"
end
```

#### Using the employee_updates_contract_changes_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeeUpdatesContractChange>, Integer, Hash)> employee_updates_contract_changes_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Contract change
  data, status_code, headers = api_instance.employee_updates_contract_changes_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeeUpdatesContractChange>
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesContractChangeApi->employee_updates_contract_changes_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | filter by contract change incidence ids. |  |

### Return type

[**EmployeeUpdatesContractChange**](EmployeeUpdatesContractChange.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

