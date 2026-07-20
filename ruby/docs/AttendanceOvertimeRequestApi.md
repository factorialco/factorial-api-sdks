# F::AttendanceOvertimeRequestApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**attendance_overtime_requests_approve_post**](AttendanceOvertimeRequestApi.md#attendance_overtime_requests_approve_post) | **POST** /api/2026-07-01/resources/attendance/overtime_requests/approve | Approves an Overtime request |
| [**attendance_overtime_requests_get**](AttendanceOvertimeRequestApi.md#attendance_overtime_requests_get) | **GET** /api/2026-07-01/resources/attendance/overtime_requests | Reads all Overtime requests |
| [**attendance_overtime_requests_id_delete**](AttendanceOvertimeRequestApi.md#attendance_overtime_requests_id_delete) | **DELETE** /api/2026-07-01/resources/attendance/overtime_requests/{id} | Deletes an Overtime request |
| [**attendance_overtime_requests_id_get**](AttendanceOvertimeRequestApi.md#attendance_overtime_requests_id_get) | **GET** /api/2026-07-01/resources/attendance/overtime_requests/{id} | Reads a single Overtime request |
| [**attendance_overtime_requests_id_put**](AttendanceOvertimeRequestApi.md#attendance_overtime_requests_id_put) | **PUT** /api/2026-07-01/resources/attendance/overtime_requests/{id} | Updates an Overtime request |
| [**attendance_overtime_requests_post**](AttendanceOvertimeRequestApi.md#attendance_overtime_requests_post) | **POST** /api/2026-07-01/resources/attendance/overtime_requests | Creates an Overtime request |
| [**attendance_overtime_requests_reject_post**](AttendanceOvertimeRequestApi.md#attendance_overtime_requests_reject_post) | **POST** /api/2026-07-01/resources/attendance/overtime_requests/reject | Rejects an Overtime request |


## attendance_overtime_requests_approve_post

> <AttendanceOvertimeRequest> attendance_overtime_requests_approve_post(opts)

Approves an Overtime request

Approves an Overtime request

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

api_instance = F::AttendanceOvertimeRequestApi.new
opts = {
  attendance_overtime_requests_approve_post_request: F::AttendanceOvertimeRequestsApprovePostRequest.new({id: 'id_example'}) # AttendanceOvertimeRequestsApprovePostRequest | 
}

begin
  # Approves an Overtime request
  result = api_instance.attendance_overtime_requests_approve_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceOvertimeRequestApi->attendance_overtime_requests_approve_post: #{e}"
end
```

#### Using the attendance_overtime_requests_approve_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceOvertimeRequest>, Integer, Hash)> attendance_overtime_requests_approve_post_with_http_info(opts)

```ruby
begin
  # Approves an Overtime request
  data, status_code, headers = api_instance.attendance_overtime_requests_approve_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceOvertimeRequest>
rescue F::ApiError => e
  puts "Error when calling AttendanceOvertimeRequestApi->attendance_overtime_requests_approve_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_overtime_requests_approve_post_request** | [**AttendanceOvertimeRequestsApprovePostRequest**](AttendanceOvertimeRequestsApprovePostRequest.md) |  | [optional] |

### Return type

[**AttendanceOvertimeRequest**](AttendanceOvertimeRequest.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attendance_overtime_requests_get

> <AttendanceOvertimeRequestsGet200Response> attendance_overtime_requests_get(include_approval_flow, opts)

Reads all Overtime requests

Reads all Overtime requests

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

api_instance = F::AttendanceOvertimeRequestApi.new
include_approval_flow = true # Boolean | 
opts = {
  ids: ['inner_example'], # Array<String> | 
  employee_ids: ['inner_example'], # Array<String> | 
  start_on: 'start_on_example', # String | 
  end_on: 'end_on_example', # String | 
  status: 'pending' # String | 
}

begin
  # Reads all Overtime requests
  result = api_instance.attendance_overtime_requests_get(include_approval_flow, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceOvertimeRequestApi->attendance_overtime_requests_get: #{e}"
end
```

#### Using the attendance_overtime_requests_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceOvertimeRequestsGet200Response>, Integer, Hash)> attendance_overtime_requests_get_with_http_info(include_approval_flow, opts)

```ruby
begin
  # Reads all Overtime requests
  data, status_code, headers = api_instance.attendance_overtime_requests_get_with_http_info(include_approval_flow, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceOvertimeRequestsGet200Response>
rescue F::ApiError => e
  puts "Error when calling AttendanceOvertimeRequestApi->attendance_overtime_requests_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include_approval_flow** | **Boolean** |  |  |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **start_on** | **String** |  | [optional] |
| **end_on** | **String** |  | [optional] |
| **status** | **String** |  | [optional] |

### Return type

[**AttendanceOvertimeRequestsGet200Response**](AttendanceOvertimeRequestsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attendance_overtime_requests_id_delete

> <AttendanceOvertimeRequest> attendance_overtime_requests_id_delete(id)

Deletes an Overtime request

Deletes an Overtime request

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

api_instance = F::AttendanceOvertimeRequestApi.new
id = '1' # String | 

begin
  # Deletes an Overtime request
  result = api_instance.attendance_overtime_requests_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceOvertimeRequestApi->attendance_overtime_requests_id_delete: #{e}"
end
```

#### Using the attendance_overtime_requests_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceOvertimeRequest>, Integer, Hash)> attendance_overtime_requests_id_delete_with_http_info(id)

```ruby
begin
  # Deletes an Overtime request
  data, status_code, headers = api_instance.attendance_overtime_requests_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceOvertimeRequest>
rescue F::ApiError => e
  puts "Error when calling AttendanceOvertimeRequestApi->attendance_overtime_requests_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**AttendanceOvertimeRequest**](AttendanceOvertimeRequest.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attendance_overtime_requests_id_get

> <AttendanceOvertimeRequest> attendance_overtime_requests_id_get(id)

Reads a single Overtime request

Reads a single Overtime request

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

api_instance = F::AttendanceOvertimeRequestApi.new
id = '1' # String | 

begin
  # Reads a single Overtime request
  result = api_instance.attendance_overtime_requests_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceOvertimeRequestApi->attendance_overtime_requests_id_get: #{e}"
end
```

#### Using the attendance_overtime_requests_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceOvertimeRequest>, Integer, Hash)> attendance_overtime_requests_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Overtime request
  data, status_code, headers = api_instance.attendance_overtime_requests_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceOvertimeRequest>
rescue F::ApiError => e
  puts "Error when calling AttendanceOvertimeRequestApi->attendance_overtime_requests_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**AttendanceOvertimeRequest**](AttendanceOvertimeRequest.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attendance_overtime_requests_id_put

> <AttendanceOvertimeRequest> attendance_overtime_requests_id_put(id, opts)

Updates an Overtime request

Updates an Overtime request

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

api_instance = F::AttendanceOvertimeRequestApi.new
id = '1' # String | 
opts = {
  attendance_overtime_requests_id_put_request: F::AttendanceOvertimeRequestsIdPutRequest.new({id: 'id_example'}) # AttendanceOvertimeRequestsIdPutRequest | 
}

begin
  # Updates an Overtime request
  result = api_instance.attendance_overtime_requests_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceOvertimeRequestApi->attendance_overtime_requests_id_put: #{e}"
end
```

#### Using the attendance_overtime_requests_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceOvertimeRequest>, Integer, Hash)> attendance_overtime_requests_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates an Overtime request
  data, status_code, headers = api_instance.attendance_overtime_requests_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceOvertimeRequest>
rescue F::ApiError => e
  puts "Error when calling AttendanceOvertimeRequestApi->attendance_overtime_requests_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **attendance_overtime_requests_id_put_request** | [**AttendanceOvertimeRequestsIdPutRequest**](AttendanceOvertimeRequestsIdPutRequest.md) |  | [optional] |

### Return type

[**AttendanceOvertimeRequest**](AttendanceOvertimeRequest.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attendance_overtime_requests_post

> <AttendanceOvertimeRequest> attendance_overtime_requests_post(opts)

Creates an Overtime request

Creates an Overtime request

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

api_instance = F::AttendanceOvertimeRequestApi.new
opts = {
  attendance_overtime_requests_post_request: F::AttendanceOvertimeRequestsPostRequest.new({date: 'date_example', employee_id: 'employee_id_example', author_id: 'author_id_example'}) # AttendanceOvertimeRequestsPostRequest | 
}

begin
  # Creates an Overtime request
  result = api_instance.attendance_overtime_requests_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceOvertimeRequestApi->attendance_overtime_requests_post: #{e}"
end
```

#### Using the attendance_overtime_requests_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceOvertimeRequest>, Integer, Hash)> attendance_overtime_requests_post_with_http_info(opts)

```ruby
begin
  # Creates an Overtime request
  data, status_code, headers = api_instance.attendance_overtime_requests_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceOvertimeRequest>
rescue F::ApiError => e
  puts "Error when calling AttendanceOvertimeRequestApi->attendance_overtime_requests_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_overtime_requests_post_request** | [**AttendanceOvertimeRequestsPostRequest**](AttendanceOvertimeRequestsPostRequest.md) |  | [optional] |

### Return type

[**AttendanceOvertimeRequest**](AttendanceOvertimeRequest.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attendance_overtime_requests_reject_post

> <AttendanceOvertimeRequest> attendance_overtime_requests_reject_post(opts)

Rejects an Overtime request

Rejects an Overtime request

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

api_instance = F::AttendanceOvertimeRequestApi.new
opts = {
  attendance_overtime_requests_reject_post_request: F::AttendanceOvertimeRequestsRejectPostRequest.new({id: 'id_example', reason: 'reason_example'}) # AttendanceOvertimeRequestsRejectPostRequest | 
}

begin
  # Rejects an Overtime request
  result = api_instance.attendance_overtime_requests_reject_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceOvertimeRequestApi->attendance_overtime_requests_reject_post: #{e}"
end
```

#### Using the attendance_overtime_requests_reject_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceOvertimeRequest>, Integer, Hash)> attendance_overtime_requests_reject_post_with_http_info(opts)

```ruby
begin
  # Rejects an Overtime request
  data, status_code, headers = api_instance.attendance_overtime_requests_reject_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceOvertimeRequest>
rescue F::ApiError => e
  puts "Error when calling AttendanceOvertimeRequestApi->attendance_overtime_requests_reject_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_overtime_requests_reject_post_request** | [**AttendanceOvertimeRequestsRejectPostRequest**](AttendanceOvertimeRequestsRejectPostRequest.md) |  | [optional] |

### Return type

[**AttendanceOvertimeRequest**](AttendanceOvertimeRequest.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

