# F::AttendanceOpenShiftApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**attendance_open_shifts_get**](AttendanceOpenShiftApi.md#attendance_open_shifts_get) | **GET** /api/2026-07-01/resources/attendance/open_shifts | Reads all Open shifts |


## attendance_open_shifts_get

> <AttendanceOpenShiftsGet200Response> attendance_open_shifts_get(opts)

Reads all Open shifts

This endpoint retrieves the current open shifts for the specified employee_ids.

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

api_instance = F::AttendanceOpenShiftApi.new
opts = {
  employee_ids: ['inner_example'] # Array<String> | Employee ids to filter the open shifts by.
}

begin
  # Reads all Open shifts
  result = api_instance.attendance_open_shifts_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceOpenShiftApi->attendance_open_shifts_get: #{e}"
end
```

#### Using the attendance_open_shifts_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceOpenShiftsGet200Response>, Integer, Hash)> attendance_open_shifts_get_with_http_info(opts)

```ruby
begin
  # Reads all Open shifts
  data, status_code, headers = api_instance.attendance_open_shifts_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceOpenShiftsGet200Response>
rescue F::ApiError => e
  puts "Error when calling AttendanceOpenShiftApi->attendance_open_shifts_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Employee ids to filter the open shifts by. | [optional] |

### Return type

[**AttendanceOpenShiftsGet200Response**](AttendanceOpenShiftsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

