# F::EmployeeUpdatesSummaryApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**employee_updates_summaries_get**](EmployeeUpdatesSummaryApi.md#employee_updates_summaries_get) | **GET** /api/2026-07-01/resources/employee_updates/summaries | Reads all Summaries |
| [**employee_updates_summaries_id_get**](EmployeeUpdatesSummaryApi.md#employee_updates_summaries_id_get) | **GET** /api/2026-07-01/resources/employee_updates/summaries/{id} | Reads a single Summary |


## employee_updates_summaries_get

> <EmployeeUpdatesSummariesGet200Response> employee_updates_summaries_get(opts)

Reads all Summaries

This endpoint can be used to retrieve a list of `employee updates`.

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

api_instance = F::EmployeeUpdatesSummaryApi.new
opts = {
  ids: ['inner_example'], # Array<String> | retrieve only the `employee updates` that matches the `ids` passed in the request.
  employee_ids: ['inner_example'], # Array<String> | retrieve only the `employee updates` assigned to any `employee` specified in the request.
  legal_entities_ids: ['inner_example'], # Array<String> | retrieve only the `employee updates` assigned to any `legal entity` specified in the request.
  type: ['inner_example'], # Array<String> | filter `employee updates` that have the given type. The supported types are: sick, parental, name, id, address, irpf, bank, residence, nationality, gender, hiring, custom-leave, termination, contract, workplace, manual_incidence, legal_entity
  starts_on: '2024-06-06', # String | filter `employee updates` that started **later** the given param.
  ends_on: '2024-06-06' # String | filter `employee updates` that started **before** the given param.
}

begin
  # Reads all Summaries
  result = api_instance.employee_updates_summaries_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesSummaryApi->employee_updates_summaries_get: #{e}"
end
```

#### Using the employee_updates_summaries_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeeUpdatesSummariesGet200Response>, Integer, Hash)> employee_updates_summaries_get_with_http_info(opts)

```ruby
begin
  # Reads all Summaries
  data, status_code, headers = api_instance.employee_updates_summaries_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeeUpdatesSummariesGet200Response>
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesSummaryApi->employee_updates_summaries_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | retrieve only the &#x60;employee updates&#x60; that matches the &#x60;ids&#x60; passed in the request. | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | retrieve only the &#x60;employee updates&#x60; assigned to any &#x60;employee&#x60; specified in the request. | [optional] |
| **legal_entities_ids** | [**Array&lt;String&gt;**](String.md) | retrieve only the &#x60;employee updates&#x60; assigned to any &#x60;legal entity&#x60; specified in the request. | [optional] |
| **type** | [**Array&lt;String&gt;**](String.md) | filter &#x60;employee updates&#x60; that have the given type. The supported types are: sick, parental, name, id, address, irpf, bank, residence, nationality, gender, hiring, custom-leave, termination, contract, workplace, manual_incidence, legal_entity | [optional] |
| **starts_on** | **String** | filter &#x60;employee updates&#x60; that started **later** the given param. | [optional] |
| **ends_on** | **String** | filter &#x60;employee updates&#x60; that started **before** the given param. | [optional] |

### Return type

[**EmployeeUpdatesSummariesGet200Response**](EmployeeUpdatesSummariesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## employee_updates_summaries_id_get

> <EmployeeUpdatesSummary> employee_updates_summaries_id_get(id)

Reads a single Summary

This endpoint can be used to retrieve a list of `employee updates`.

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

api_instance = F::EmployeeUpdatesSummaryApi.new
id = '1' # String | retrieve only the `employee updates` that matches the `ids` passed in the request.

begin
  # Reads a single Summary
  result = api_instance.employee_updates_summaries_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesSummaryApi->employee_updates_summaries_id_get: #{e}"
end
```

#### Using the employee_updates_summaries_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeeUpdatesSummary>, Integer, Hash)> employee_updates_summaries_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Summary
  data, status_code, headers = api_instance.employee_updates_summaries_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeeUpdatesSummary>
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesSummaryApi->employee_updates_summaries_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | retrieve only the &#x60;employee updates&#x60; that matches the &#x60;ids&#x60; passed in the request. |  |

### Return type

[**EmployeeUpdatesSummary**](EmployeeUpdatesSummary.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

