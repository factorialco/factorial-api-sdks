# F::AttendanceEditTimesheetRequestApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**attendance_edit_timesheet_requests_get**](AttendanceEditTimesheetRequestApi.md#attendance_edit_timesheet_requests_get) | **GET** /api/2026-07-01/resources/attendance/edit_timesheet_requests | Reads all Edit timesheet requests |
| [**attendance_edit_timesheet_requests_id_delete**](AttendanceEditTimesheetRequestApi.md#attendance_edit_timesheet_requests_id_delete) | **DELETE** /api/2026-07-01/resources/attendance/edit_timesheet_requests/{id} | Deletes an Edit timesheet request |
| [**attendance_edit_timesheet_requests_id_get**](AttendanceEditTimesheetRequestApi.md#attendance_edit_timesheet_requests_id_get) | **GET** /api/2026-07-01/resources/attendance/edit_timesheet_requests/{id} | Reads all Edit timesheet requests |
| [**attendance_edit_timesheet_requests_id_put**](AttendanceEditTimesheetRequestApi.md#attendance_edit_timesheet_requests_id_put) | **PUT** /api/2026-07-01/resources/attendance/edit_timesheet_requests/{id} | Updates an Edit timesheet request |
| [**attendance_edit_timesheet_requests_post**](AttendanceEditTimesheetRequestApi.md#attendance_edit_timesheet_requests_post) | **POST** /api/2026-07-01/resources/attendance/edit_timesheet_requests | Creates an Edit timesheet request |


## attendance_edit_timesheet_requests_get

> <AttendanceEditTimesheetRequestsGet200Response> attendance_edit_timesheet_requests_get(opts)

Reads all Edit timesheet requests

Reads all Edit timesheet requests

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

api_instance = F::AttendanceEditTimesheetRequestApi.new
opts = {
  ids: ['inner_example'], # Array<String> | filter by ids.
  employee_ids: ['inner_example'], # Array<String> | filter by employee ids.
  shift_id: '1', # String | filter by shift id.
  pending: true, # Boolean | filter by edit timesheet request status.
  start_on: '2022-01-01', # String | filter by edit timesheet requests that were created after or including this date.
  end_on: '2022-01-01' # String | filter by edit timesheet requests that were created before or including this date.
}

begin
  # Reads all Edit timesheet requests
  result = api_instance.attendance_edit_timesheet_requests_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceEditTimesheetRequestApi->attendance_edit_timesheet_requests_get: #{e}"
end
```

#### Using the attendance_edit_timesheet_requests_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceEditTimesheetRequestsGet200Response>, Integer, Hash)> attendance_edit_timesheet_requests_get_with_http_info(opts)

```ruby
begin
  # Reads all Edit timesheet requests
  data, status_code, headers = api_instance.attendance_edit_timesheet_requests_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceEditTimesheetRequestsGet200Response>
rescue F::ApiError => e
  puts "Error when calling AttendanceEditTimesheetRequestApi->attendance_edit_timesheet_requests_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | filter by ids. | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | filter by employee ids. | [optional] |
| **shift_id** | **String** | filter by shift id. | [optional] |
| **pending** | **Boolean** | filter by edit timesheet request status. | [optional] |
| **start_on** | **String** | filter by edit timesheet requests that were created after or including this date. | [optional] |
| **end_on** | **String** | filter by edit timesheet requests that were created before or including this date. | [optional] |

### Return type

[**AttendanceEditTimesheetRequestsGet200Response**](AttendanceEditTimesheetRequestsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attendance_edit_timesheet_requests_id_delete

> <AttendanceEditTimesheetRequest> attendance_edit_timesheet_requests_id_delete(id)

Deletes an Edit timesheet request

Deletes an edit timesheet.

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

api_instance = F::AttendanceEditTimesheetRequestApi.new
id = '1' # String | 

begin
  # Deletes an Edit timesheet request
  result = api_instance.attendance_edit_timesheet_requests_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceEditTimesheetRequestApi->attendance_edit_timesheet_requests_id_delete: #{e}"
end
```

#### Using the attendance_edit_timesheet_requests_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceEditTimesheetRequest>, Integer, Hash)> attendance_edit_timesheet_requests_id_delete_with_http_info(id)

```ruby
begin
  # Deletes an Edit timesheet request
  data, status_code, headers = api_instance.attendance_edit_timesheet_requests_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceEditTimesheetRequest>
rescue F::ApiError => e
  puts "Error when calling AttendanceEditTimesheetRequestApi->attendance_edit_timesheet_requests_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**AttendanceEditTimesheetRequest**](AttendanceEditTimesheetRequest.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attendance_edit_timesheet_requests_id_get

> <AttendanceEditTimesheetRequest> attendance_edit_timesheet_requests_id_get(id)

Reads all Edit timesheet requests

Reads a single Edit timesheet request

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

api_instance = F::AttendanceEditTimesheetRequestApi.new
id = '1' # String | filter by ids.

begin
  # Reads all Edit timesheet requests
  result = api_instance.attendance_edit_timesheet_requests_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceEditTimesheetRequestApi->attendance_edit_timesheet_requests_id_get: #{e}"
end
```

#### Using the attendance_edit_timesheet_requests_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceEditTimesheetRequest>, Integer, Hash)> attendance_edit_timesheet_requests_id_get_with_http_info(id)

```ruby
begin
  # Reads all Edit timesheet requests
  data, status_code, headers = api_instance.attendance_edit_timesheet_requests_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceEditTimesheetRequest>
rescue F::ApiError => e
  puts "Error when calling AttendanceEditTimesheetRequestApi->attendance_edit_timesheet_requests_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | filter by ids. |  |

### Return type

[**AttendanceEditTimesheetRequest**](AttendanceEditTimesheetRequest.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attendance_edit_timesheet_requests_id_put

> <AttendanceEditTimesheetRequest> attendance_edit_timesheet_requests_id_put(id, opts)

Updates an Edit timesheet request

Updates an edit timesheet request by specifying the fields required to update the shift.

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

api_instance = F::AttendanceEditTimesheetRequestApi.new
id = '1' # String | 
opts = {
  attendance_edit_timesheet_requests_id_put_request: F::AttendanceEditTimesheetRequestsIdPutRequest.new({employee_id: 'employee_id_example', id: 'id_example'}) # AttendanceEditTimesheetRequestsIdPutRequest | 
}

begin
  # Updates an Edit timesheet request
  result = api_instance.attendance_edit_timesheet_requests_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceEditTimesheetRequestApi->attendance_edit_timesheet_requests_id_put: #{e}"
end
```

#### Using the attendance_edit_timesheet_requests_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceEditTimesheetRequest>, Integer, Hash)> attendance_edit_timesheet_requests_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates an Edit timesheet request
  data, status_code, headers = api_instance.attendance_edit_timesheet_requests_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceEditTimesheetRequest>
rescue F::ApiError => e
  puts "Error when calling AttendanceEditTimesheetRequestApi->attendance_edit_timesheet_requests_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **attendance_edit_timesheet_requests_id_put_request** | [**AttendanceEditTimesheetRequestsIdPutRequest**](AttendanceEditTimesheetRequestsIdPutRequest.md) |  | [optional] |

### Return type

[**AttendanceEditTimesheetRequest**](AttendanceEditTimesheetRequest.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attendance_edit_timesheet_requests_post

> <AttendanceEditTimesheetRequest> attendance_edit_timesheet_requests_post(opts)

Creates an Edit timesheet request

Creates an edit timesheet request by specifying the type of the request and the fields required to create or update the shift.

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

api_instance = F::AttendanceEditTimesheetRequestApi.new
opts = {
  attendance_edit_timesheet_requests_post_request: F::AttendanceEditTimesheetRequestsPostRequest.new({employee_id: 'employee_id_example', request_type: 'create_shift'}) # AttendanceEditTimesheetRequestsPostRequest | 
}

begin
  # Creates an Edit timesheet request
  result = api_instance.attendance_edit_timesheet_requests_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceEditTimesheetRequestApi->attendance_edit_timesheet_requests_post: #{e}"
end
```

#### Using the attendance_edit_timesheet_requests_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceEditTimesheetRequest>, Integer, Hash)> attendance_edit_timesheet_requests_post_with_http_info(opts)

```ruby
begin
  # Creates an Edit timesheet request
  data, status_code, headers = api_instance.attendance_edit_timesheet_requests_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceEditTimesheetRequest>
rescue F::ApiError => e
  puts "Error when calling AttendanceEditTimesheetRequestApi->attendance_edit_timesheet_requests_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_edit_timesheet_requests_post_request** | [**AttendanceEditTimesheetRequestsPostRequest**](AttendanceEditTimesheetRequestsPostRequest.md) |  | [optional] |

### Return type

[**AttendanceEditTimesheetRequest**](AttendanceEditTimesheetRequest.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

