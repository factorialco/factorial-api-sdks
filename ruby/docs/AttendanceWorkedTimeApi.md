# F::AttendanceWorkedTimeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**attendance_worked_times_get**](AttendanceWorkedTimeApi.md#attendance_worked_times_get) | **GET** /api/2026-07-01/resources/attendance/worked_times | Reads all Worked times |


## attendance_worked_times_get

> <AttendanceWorkedTimesGet200Response> attendance_worked_times_get(include_time_range_category, include_non_attendable_employees, opts)

Reads all Worked times

Reads all Worked times

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

api_instance = F::AttendanceWorkedTimeApi.new
include_time_range_category = true # Boolean | 
include_non_attendable_employees = true # Boolean | 
opts = {
  start_on: 'start_on_example', # String | 
  end_on: 'end_on_example', # String | 
  employee_ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Worked times
  result = api_instance.attendance_worked_times_get(include_time_range_category, include_non_attendable_employees, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceWorkedTimeApi->attendance_worked_times_get: #{e}"
end
```

#### Using the attendance_worked_times_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceWorkedTimesGet200Response>, Integer, Hash)> attendance_worked_times_get_with_http_info(include_time_range_category, include_non_attendable_employees, opts)

```ruby
begin
  # Reads all Worked times
  data, status_code, headers = api_instance.attendance_worked_times_get_with_http_info(include_time_range_category, include_non_attendable_employees, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceWorkedTimesGet200Response>
rescue F::ApiError => e
  puts "Error when calling AttendanceWorkedTimeApi->attendance_worked_times_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include_time_range_category** | **Boolean** |  |  |
| **include_non_attendable_employees** | **Boolean** |  |  |
| **start_on** | **String** |  | [optional] |
| **end_on** | **String** |  | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**AttendanceWorkedTimesGet200Response**](AttendanceWorkedTimesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

