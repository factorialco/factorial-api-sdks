# F::AttendanceShiftApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**attendance_shifts_autofill_post**](AttendanceShiftApi.md#attendance_shifts_autofill_post) | **POST** /api/2026-07-01/resources/attendance/shifts/autofill | Autofills a Shift |
| [**attendance_shifts_break_end_post**](AttendanceShiftApi.md#attendance_shifts_break_end_post) | **POST** /api/2026-07-01/resources/attendance/shifts/break_end | Break ends a Shift |
| [**attendance_shifts_break_start_post**](AttendanceShiftApi.md#attendance_shifts_break_start_post) | **POST** /api/2026-07-01/resources/attendance/shifts/break_start | Break starts a Shift |
| [**attendance_shifts_clock_in_post**](AttendanceShiftApi.md#attendance_shifts_clock_in_post) | **POST** /api/2026-07-01/resources/attendance/shifts/clock_in | Clocks in a shift |
| [**attendance_shifts_clock_out_post**](AttendanceShiftApi.md#attendance_shifts_clock_out_post) | **POST** /api/2026-07-01/resources/attendance/shifts/clock_out | Clocks out a shift |
| [**attendance_shifts_get**](AttendanceShiftApi.md#attendance_shifts_get) | **GET** /api/2026-07-01/resources/attendance/shifts | Reads all Shifts |
| [**attendance_shifts_id_delete**](AttendanceShiftApi.md#attendance_shifts_id_delete) | **DELETE** /api/2026-07-01/resources/attendance/shifts/{id} | Deletes a Shift |
| [**attendance_shifts_id_get**](AttendanceShiftApi.md#attendance_shifts_id_get) | **GET** /api/2026-07-01/resources/attendance/shifts/{id} | Reads a single Shift |
| [**attendance_shifts_id_put**](AttendanceShiftApi.md#attendance_shifts_id_put) | **PUT** /api/2026-07-01/resources/attendance/shifts/{id} | Updates a Shift |
| [**attendance_shifts_post**](AttendanceShiftApi.md#attendance_shifts_post) | **POST** /api/2026-07-01/resources/attendance/shifts | Creates a shift |
| [**attendance_shifts_toggle_clock_post**](AttendanceShiftApi.md#attendance_shifts_toggle_clock_post) | **POST** /api/2026-07-01/resources/attendance/shifts/toggle_clock | Clock in/out a shift |


## attendance_shifts_autofill_post

> <Array<AttendanceShift>> attendance_shifts_autofill_post(opts)

Autofills a Shift

Autofills a Shift

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

api_instance = F::AttendanceShiftApi.new
opts = {
  attendance_shifts_autofill_post_request: F::AttendanceShiftsAutofillPostRequest.new({employee_ids: ["1", "2", "3"], start_on: '2022-01-01', end_on: '2022-01-01'}) # AttendanceShiftsAutofillPostRequest | 
}

begin
  # Autofills a Shift
  result = api_instance.attendance_shifts_autofill_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_autofill_post: #{e}"
end
```

#### Using the attendance_shifts_autofill_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<AttendanceShift>>, Integer, Hash)> attendance_shifts_autofill_post_with_http_info(opts)

```ruby
begin
  # Autofills a Shift
  data, status_code, headers = api_instance.attendance_shifts_autofill_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<AttendanceShift>>
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_autofill_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_shifts_autofill_post_request** | [**AttendanceShiftsAutofillPostRequest**](AttendanceShiftsAutofillPostRequest.md) |  | [optional] |

### Return type

[**Array&lt;AttendanceShift&gt;**](AttendanceShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attendance_shifts_break_end_post

> <AttendanceShift> attendance_shifts_break_end_post(opts)

Break ends a Shift

Given that attendance breaks are enabled, this endpoint ends a break in an open shift.

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

api_instance = F::AttendanceShiftApi.new
opts = {
  attendance_shifts_break_end_post_request: F::AttendanceShiftsBreakEndPostRequest.new({now: '2022-06-23T11:00:00.000+00:00'}) # AttendanceShiftsBreakEndPostRequest | 
}

begin
  # Break ends a Shift
  result = api_instance.attendance_shifts_break_end_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_break_end_post: #{e}"
end
```

#### Using the attendance_shifts_break_end_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceShift>, Integer, Hash)> attendance_shifts_break_end_post_with_http_info(opts)

```ruby
begin
  # Break ends a Shift
  data, status_code, headers = api_instance.attendance_shifts_break_end_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceShift>
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_break_end_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_shifts_break_end_post_request** | [**AttendanceShiftsBreakEndPostRequest**](AttendanceShiftsBreakEndPostRequest.md) |  | [optional] |

### Return type

[**AttendanceShift**](AttendanceShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attendance_shifts_break_start_post

> <AttendanceShift> attendance_shifts_break_start_post(opts)

Break starts a Shift

Given that attendance breaks are enabled, this endpoint starts a break in an open shift.

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

api_instance = F::AttendanceShiftApi.new
opts = {
  attendance_shifts_break_start_post_request: F::AttendanceShiftsBreakStartPostRequest.new({now: '2022-06-23T11:00:00.000+00:00'}) # AttendanceShiftsBreakStartPostRequest | 
}

begin
  # Break starts a Shift
  result = api_instance.attendance_shifts_break_start_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_break_start_post: #{e}"
end
```

#### Using the attendance_shifts_break_start_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceShift>, Integer, Hash)> attendance_shifts_break_start_post_with_http_info(opts)

```ruby
begin
  # Break starts a Shift
  data, status_code, headers = api_instance.attendance_shifts_break_start_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceShift>
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_break_start_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_shifts_break_start_post_request** | [**AttendanceShiftsBreakStartPostRequest**](AttendanceShiftsBreakStartPostRequest.md) |  | [optional] |

### Return type

[**AttendanceShift**](AttendanceShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attendance_shifts_clock_in_post

> <AttendanceShift> attendance_shifts_clock_in_post(opts)

Clocks in a shift

Records the start of a shift by setting the current time as the clock-in. The shift remains open and will not have a clock-out time until explicitly updated. If you need to clock out directly, consider using or subscribing to the [clock-out endpoint](https://apidoc.factorialhr.com/v2025-01-01/reference/post_api-2025-01-01-resources-attendance-shifts-clock-out)

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

api_instance = F::AttendanceShiftApi.new
opts = {
  attendance_shifts_clock_in_post_request: F::AttendanceShiftsClockInPostRequest.new({now: '2024-06-23T11:00:00.000+00:00'}) # AttendanceShiftsClockInPostRequest | 
}

begin
  # Clocks in a shift
  result = api_instance.attendance_shifts_clock_in_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_clock_in_post: #{e}"
end
```

#### Using the attendance_shifts_clock_in_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceShift>, Integer, Hash)> attendance_shifts_clock_in_post_with_http_info(opts)

```ruby
begin
  # Clocks in a shift
  data, status_code, headers = api_instance.attendance_shifts_clock_in_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceShift>
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_clock_in_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_shifts_clock_in_post_request** | [**AttendanceShiftsClockInPostRequest**](AttendanceShiftsClockInPostRequest.md) |  | [optional] |

### Return type

[**AttendanceShift**](AttendanceShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attendance_shifts_clock_out_post

> <AttendanceShift> attendance_shifts_clock_out_post(opts)

Clocks out a shift

Completes an open shift by setting the current time as the clock-out. This action only applies to shifts that were previously started using clock_in. If you need to clock in directly, consider using or subscribing to the [clock-in endpoint](https://apidoc.factorialhr.com/v2025-01-01/reference/post_api-2025-01-01-resources-attendance-shifts-clock-in)

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

api_instance = F::AttendanceShiftApi.new
opts = {
  attendance_shifts_clock_out_post_request: F::AttendanceShiftsClockOutPostRequest.new({now: '2024-06-23T11:00:00.000+00:00'}) # AttendanceShiftsClockOutPostRequest | 
}

begin
  # Clocks out a shift
  result = api_instance.attendance_shifts_clock_out_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_clock_out_post: #{e}"
end
```

#### Using the attendance_shifts_clock_out_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceShift>, Integer, Hash)> attendance_shifts_clock_out_post_with_http_info(opts)

```ruby
begin
  # Clocks out a shift
  data, status_code, headers = api_instance.attendance_shifts_clock_out_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceShift>
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_clock_out_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_shifts_clock_out_post_request** | [**AttendanceShiftsClockOutPostRequest**](AttendanceShiftsClockOutPostRequest.md) |  | [optional] |

### Return type

[**AttendanceShift**](AttendanceShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attendance_shifts_get

> <AttendanceShiftsGet200Response> attendance_shifts_get(half_day, sort_created_at_asc, opts)

Reads all Shifts

Reads all Shifts

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

api_instance = F::AttendanceShiftApi.new
half_day = false # Boolean | Flag to filter half day shifts
sort_created_at_asc = true # Boolean | Flag to sort by created_at asc
opts = {
  employee_ids: ['inner_example'], # Array<String> | filter by employee ids.
  start_on: '2023-09-30', # String | filter by shift that starts after or including this date.
  end_on: '2023-10-01', # String | filter by shift that ends before or including this date.
  ids: ['inner_example'], # Array<String> | filter by ids.
  workable: true, # Boolean | Flag to filter shifts in workable days
  latest_shift: true, # Boolean | Flag to filter only the latest shift for each employee
  breaks_with_time_configuration: true, # Boolean | Flag to include breaks with time configuration
  last_working_shift: true, # Boolean | Filter by last working shift
  updated_at: '2023-10-01' # String | Filter shifts by the date they were last updated
}

begin
  # Reads all Shifts
  result = api_instance.attendance_shifts_get(half_day, sort_created_at_asc, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_get: #{e}"
end
```

#### Using the attendance_shifts_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceShiftsGet200Response>, Integer, Hash)> attendance_shifts_get_with_http_info(half_day, sort_created_at_asc, opts)

```ruby
begin
  # Reads all Shifts
  data, status_code, headers = api_instance.attendance_shifts_get_with_http_info(half_day, sort_created_at_asc, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceShiftsGet200Response>
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **half_day** | **Boolean** | Flag to filter half day shifts |  |
| **sort_created_at_asc** | **Boolean** | Flag to sort by created_at asc |  |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | filter by employee ids. | [optional] |
| **start_on** | **String** | filter by shift that starts after or including this date. | [optional] |
| **end_on** | **String** | filter by shift that ends before or including this date. | [optional] |
| **ids** | [**Array&lt;String&gt;**](String.md) | filter by ids. | [optional] |
| **workable** | **Boolean** | Flag to filter shifts in workable days | [optional] |
| **latest_shift** | **Boolean** | Flag to filter only the latest shift for each employee | [optional] |
| **breaks_with_time_configuration** | **Boolean** | Flag to include breaks with time configuration | [optional] |
| **last_working_shift** | **Boolean** | Filter by last working shift | [optional] |
| **updated_at** | **String** | Filter shifts by the date they were last updated | [optional] |

### Return type

[**AttendanceShiftsGet200Response**](AttendanceShiftsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attendance_shifts_id_delete

> <AttendanceShift> attendance_shifts_id_delete(id)

Deletes a Shift

Deletes a Shift

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

api_instance = F::AttendanceShiftApi.new
id = '1' # String | 

begin
  # Deletes a Shift
  result = api_instance.attendance_shifts_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_id_delete: #{e}"
end
```

#### Using the attendance_shifts_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceShift>, Integer, Hash)> attendance_shifts_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Shift
  data, status_code, headers = api_instance.attendance_shifts_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceShift>
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**AttendanceShift**](AttendanceShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attendance_shifts_id_get

> <AttendanceShift> attendance_shifts_id_get(id)

Reads a single Shift

Reads a single Shift

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

api_instance = F::AttendanceShiftApi.new
id = '1' # String | filter by ids.

begin
  # Reads a single Shift
  result = api_instance.attendance_shifts_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_id_get: #{e}"
end
```

#### Using the attendance_shifts_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceShift>, Integer, Hash)> attendance_shifts_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Shift
  data, status_code, headers = api_instance.attendance_shifts_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceShift>
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | filter by ids. |  |

### Return type

[**AttendanceShift**](AttendanceShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attendance_shifts_id_put

> <AttendanceShift> attendance_shifts_id_put(id, opts)

Updates a Shift

Updates a Shift

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

api_instance = F::AttendanceShiftApi.new
id = '1' # String | Id of the shift
opts = {
  attendance_shifts_id_put_request: F::AttendanceShiftsIdPutRequest.new({id: '1'}) # AttendanceShiftsIdPutRequest | 
}

begin
  # Updates a Shift
  result = api_instance.attendance_shifts_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_id_put: #{e}"
end
```

#### Using the attendance_shifts_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceShift>, Integer, Hash)> attendance_shifts_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Shift
  data, status_code, headers = api_instance.attendance_shifts_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceShift>
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id of the shift |  |
| **attendance_shifts_id_put_request** | [**AttendanceShiftsIdPutRequest**](AttendanceShiftsIdPutRequest.md) |  | [optional] |

### Return type

[**AttendanceShift**](AttendanceShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attendance_shifts_post

> <AttendanceShift> attendance_shifts_post(opts)

Creates a shift

Creates a complete shift by specifying both the clock-in and clock-out times. If you need to clock in directly, consider using or subscribing to the [clock-in endpoint](https://apidoc.factorialhr.com/v2025-01-01/reference/post_api-2025-01-01-resources-attendance-shifts-clock-in)

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

api_instance = F::AttendanceShiftApi.new
opts = {
  attendance_shifts_post_request: F::AttendanceShiftsPostRequest.new({date: '2022-01-01'}) # AttendanceShiftsPostRequest | 
}

begin
  # Creates a shift
  result = api_instance.attendance_shifts_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_post: #{e}"
end
```

#### Using the attendance_shifts_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceShift>, Integer, Hash)> attendance_shifts_post_with_http_info(opts)

```ruby
begin
  # Creates a shift
  data, status_code, headers = api_instance.attendance_shifts_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceShift>
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_shifts_post_request** | [**AttendanceShiftsPostRequest**](AttendanceShiftsPostRequest.md) |  | [optional] |

### Return type

[**AttendanceShift**](AttendanceShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attendance_shifts_toggle_clock_post

> <AttendanceShift> attendance_shifts_toggle_clock_post(opts)

Clock in/out a shift

Use this endpoint to toggle shift (it will clock in or out)

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

api_instance = F::AttendanceShiftApi.new
opts = {
  attendance_shifts_toggle_clock_post_request: F::AttendanceShiftsToggleClockPostRequest.new({employee_id: '1', clock_time: '2024-06-23T11:00:00.000+00:00'}) # AttendanceShiftsToggleClockPostRequest | 
}

begin
  # Clock in/out a shift
  result = api_instance.attendance_shifts_toggle_clock_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_toggle_clock_post: #{e}"
end
```

#### Using the attendance_shifts_toggle_clock_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceShift>, Integer, Hash)> attendance_shifts_toggle_clock_post_with_http_info(opts)

```ruby
begin
  # Clock in/out a shift
  data, status_code, headers = api_instance.attendance_shifts_toggle_clock_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceShift>
rescue F::ApiError => e
  puts "Error when calling AttendanceShiftApi->attendance_shifts_toggle_clock_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_shifts_toggle_clock_post_request** | [**AttendanceShiftsToggleClockPostRequest**](AttendanceShiftsToggleClockPostRequest.md) |  | [optional] |

### Return type

[**AttendanceShift**](AttendanceShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

