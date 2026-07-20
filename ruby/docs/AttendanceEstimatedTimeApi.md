# F::AttendanceEstimatedTimeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**attendance_estimated_times_get**](AttendanceEstimatedTimeApi.md#attendance_estimated_times_get) | **GET** /api/2026-07-01/resources/attendance/estimated_times | Reads all Estimated times |


## attendance_estimated_times_get

> <AttendanceEstimatedTimesGet200Response> attendance_estimated_times_get(start_on, end_on, employee_ids)

Reads all Estimated times

Get information about estimated data for a given date range and a bunch of employees.

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

api_instance = F::AttendanceEstimatedTimeApi.new
start_on = 'start_on_example' # String | 
end_on = 'end_on_example' # String | 
employee_ids = ['inner_example'] # Array<String> | 

begin
  # Reads all Estimated times
  result = api_instance.attendance_estimated_times_get(start_on, end_on, employee_ids)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceEstimatedTimeApi->attendance_estimated_times_get: #{e}"
end
```

#### Using the attendance_estimated_times_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceEstimatedTimesGet200Response>, Integer, Hash)> attendance_estimated_times_get_with_http_info(start_on, end_on, employee_ids)

```ruby
begin
  # Reads all Estimated times
  data, status_code, headers = api_instance.attendance_estimated_times_get_with_http_info(start_on, end_on, employee_ids)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceEstimatedTimesGet200Response>
rescue F::ApiError => e
  puts "Error when calling AttendanceEstimatedTimeApi->attendance_estimated_times_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **start_on** | **String** |  |  |
| **end_on** | **String** |  |  |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) |  |  |

### Return type

[**AttendanceEstimatedTimesGet200Response**](AttendanceEstimatedTimesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

