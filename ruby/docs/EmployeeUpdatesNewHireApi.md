# F::EmployeeUpdatesNewHireApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**employee_updates_new_hires_get**](EmployeeUpdatesNewHireApi.md#employee_updates_new_hires_get) | **GET** /api/2026-07-01/resources/employee_updates/new_hires | Reads all New hires |
| [**employee_updates_new_hires_id_get**](EmployeeUpdatesNewHireApi.md#employee_updates_new_hires_id_get) | **GET** /api/2026-07-01/resources/employee_updates/new_hires/{id} | Reads a single New hire |


## employee_updates_new_hires_get

> <EmployeeUpdatesNewHiresGet200Response> employee_updates_new_hires_get(opts)

Reads all New hires

This endpoint can be used to retrieve a detail of new hire `employee updates`.

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

api_instance = F::EmployeeUpdatesNewHireApi.new
opts = {
  ids: ['inner_example'] # Array<String> | filter by new hire incidence ids.
}

begin
  # Reads all New hires
  result = api_instance.employee_updates_new_hires_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesNewHireApi->employee_updates_new_hires_get: #{e}"
end
```

#### Using the employee_updates_new_hires_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeeUpdatesNewHiresGet200Response>, Integer, Hash)> employee_updates_new_hires_get_with_http_info(opts)

```ruby
begin
  # Reads all New hires
  data, status_code, headers = api_instance.employee_updates_new_hires_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeeUpdatesNewHiresGet200Response>
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesNewHireApi->employee_updates_new_hires_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | filter by new hire incidence ids. | [optional] |

### Return type

[**EmployeeUpdatesNewHiresGet200Response**](EmployeeUpdatesNewHiresGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## employee_updates_new_hires_id_get

> <EmployeeUpdatesNewHire> employee_updates_new_hires_id_get(id)

Reads a single New hire

This endpoint can be used to retrieve a detail of new hire `employee updates`.

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

api_instance = F::EmployeeUpdatesNewHireApi.new
id = '1' # String | filter by new hire incidence ids.

begin
  # Reads a single New hire
  result = api_instance.employee_updates_new_hires_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesNewHireApi->employee_updates_new_hires_id_get: #{e}"
end
```

#### Using the employee_updates_new_hires_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeeUpdatesNewHire>, Integer, Hash)> employee_updates_new_hires_id_get_with_http_info(id)

```ruby
begin
  # Reads a single New hire
  data, status_code, headers = api_instance.employee_updates_new_hires_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeeUpdatesNewHire>
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesNewHireApi->employee_updates_new_hires_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | filter by new hire incidence ids. |  |

### Return type

[**EmployeeUpdatesNewHire**](EmployeeUpdatesNewHire.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

