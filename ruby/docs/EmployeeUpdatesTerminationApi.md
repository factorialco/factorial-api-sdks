# F::EmployeeUpdatesTerminationApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**employee_updates_terminations_get**](EmployeeUpdatesTerminationApi.md#employee_updates_terminations_get) | **GET** /api/2026-07-01/resources/employee_updates/terminations | Reads all Terminations |
| [**employee_updates_terminations_id_get**](EmployeeUpdatesTerminationApi.md#employee_updates_terminations_id_get) | **GET** /api/2026-07-01/resources/employee_updates/terminations/{id} | Reads a single Termination |


## employee_updates_terminations_get

> <EmployeeUpdatesTerminationsGet200Response> employee_updates_terminations_get(opts)

Reads all Terminations

This endpoint can be used to retrieve a list of termination `employee updates`.

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

api_instance = F::EmployeeUpdatesTerminationApi.new
opts = {
  ids: ['inner_example'] # Array<String> | filter by termination incidence ids.
}

begin
  # Reads all Terminations
  result = api_instance.employee_updates_terminations_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesTerminationApi->employee_updates_terminations_get: #{e}"
end
```

#### Using the employee_updates_terminations_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeeUpdatesTerminationsGet200Response>, Integer, Hash)> employee_updates_terminations_get_with_http_info(opts)

```ruby
begin
  # Reads all Terminations
  data, status_code, headers = api_instance.employee_updates_terminations_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeeUpdatesTerminationsGet200Response>
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesTerminationApi->employee_updates_terminations_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | filter by termination incidence ids. | [optional] |

### Return type

[**EmployeeUpdatesTerminationsGet200Response**](EmployeeUpdatesTerminationsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## employee_updates_terminations_id_get

> <EmployeeUpdatesTermination> employee_updates_terminations_id_get(id)

Reads a single Termination

This endpoint can be used to retrieve a list of termination `employee updates`.

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

api_instance = F::EmployeeUpdatesTerminationApi.new
id = '1' # String | filter by termination incidence ids.

begin
  # Reads a single Termination
  result = api_instance.employee_updates_terminations_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesTerminationApi->employee_updates_terminations_id_get: #{e}"
end
```

#### Using the employee_updates_terminations_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeeUpdatesTermination>, Integer, Hash)> employee_updates_terminations_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Termination
  data, status_code, headers = api_instance.employee_updates_terminations_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeeUpdatesTermination>
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesTerminationApi->employee_updates_terminations_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | filter by termination incidence ids. |  |

### Return type

[**EmployeeUpdatesTermination**](EmployeeUpdatesTermination.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

