# F::TimeoffLeaveTypeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**timeoff_leave_types_get**](TimeoffLeaveTypeApi.md#timeoff_leave_types_get) | **GET** /api/2026-07-01/resources/timeoff/leave_types | Reads all Leave types |
| [**timeoff_leave_types_id_get**](TimeoffLeaveTypeApi.md#timeoff_leave_types_id_get) | **GET** /api/2026-07-01/resources/timeoff/leave_types/{id} | Reads a single Leave type |
| [**timeoff_leave_types_id_put**](TimeoffLeaveTypeApi.md#timeoff_leave_types_id_put) | **PUT** /api/2026-07-01/resources/timeoff/leave_types/{id} | Updates a Leave type |
| [**timeoff_leave_types_post**](TimeoffLeaveTypeApi.md#timeoff_leave_types_post) | **POST** /api/2026-07-01/resources/timeoff/leave_types | Creates a Leave type |


## timeoff_leave_types_get

> <TimeoffLeaveTypesGet200Response> timeoff_leave_types_get(opts)

Reads all Leave types

Reads all Leave types

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

api_instance = F::TimeoffLeaveTypeApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Identifiers of the leave types
  company_ids: ['inner_example'], # Array<String> | Identifiers of the companies
  active: true, # Boolean | Whether the leave type is active
  payable: false, # Boolean | Whether the leave type is payable
  identifier: TODO, # Unknown | A unique identifier for the leave type, or an array of identifiers
  employee_id: '1', # String | Identifier of the employee
  reference_date: '2024-08-22', # String | A reference date for the leave type
  leave_type_id: '1', # String | Identifier of a specific leave type
  allow_endless: true # Boolean | Whether the leave type allows for no end date
}

begin
  # Reads all Leave types
  result = api_instance.timeoff_leave_types_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveTypeApi->timeoff_leave_types_get: #{e}"
end
```

#### Using the timeoff_leave_types_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffLeaveTypesGet200Response>, Integer, Hash)> timeoff_leave_types_get_with_http_info(opts)

```ruby
begin
  # Reads all Leave types
  data, status_code, headers = api_instance.timeoff_leave_types_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffLeaveTypesGet200Response>
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveTypeApi->timeoff_leave_types_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Identifiers of the leave types | [optional] |
| **company_ids** | [**Array&lt;String&gt;**](String.md) | Identifiers of the companies | [optional] |
| **active** | **Boolean** | Whether the leave type is active | [optional] |
| **payable** | **Boolean** | Whether the leave type is payable | [optional] |
| **identifier** | [**Unknown**](.md) | A unique identifier for the leave type, or an array of identifiers | [optional] |
| **employee_id** | **String** | Identifier of the employee | [optional] |
| **reference_date** | **String** | A reference date for the leave type | [optional] |
| **leave_type_id** | **String** | Identifier of a specific leave type | [optional] |
| **allow_endless** | **Boolean** | Whether the leave type allows for no end date | [optional] |

### Return type

[**TimeoffLeaveTypesGet200Response**](TimeoffLeaveTypesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_leave_types_id_get

> <TimeoffLeaveType> timeoff_leave_types_id_get(id)

Reads a single Leave type

Reads a single Leave type

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

api_instance = F::TimeoffLeaveTypeApi.new
id = '1' # String | Identifiers of the leave types

begin
  # Reads a single Leave type
  result = api_instance.timeoff_leave_types_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveTypeApi->timeoff_leave_types_id_get: #{e}"
end
```

#### Using the timeoff_leave_types_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffLeaveType>, Integer, Hash)> timeoff_leave_types_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Leave type
  data, status_code, headers = api_instance.timeoff_leave_types_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffLeaveType>
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveTypeApi->timeoff_leave_types_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifiers of the leave types |  |

### Return type

[**TimeoffLeaveType**](TimeoffLeaveType.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_leave_types_id_put

> <TimeoffLeaveType> timeoff_leave_types_id_put(id, opts)

Updates a Leave type

Updates a Leave type

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

api_instance = F::TimeoffLeaveTypeApi.new
id = '5' # String | Identifier of the leave type to update
opts = {
  timeoff_leave_types_id_put_request: F::TimeoffLeaveTypesIdPutRequest.new # TimeoffLeaveTypesIdPutRequest | 
}

begin
  # Updates a Leave type
  result = api_instance.timeoff_leave_types_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveTypeApi->timeoff_leave_types_id_put: #{e}"
end
```

#### Using the timeoff_leave_types_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffLeaveType>, Integer, Hash)> timeoff_leave_types_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Leave type
  data, status_code, headers = api_instance.timeoff_leave_types_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffLeaveType>
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveTypeApi->timeoff_leave_types_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the leave type to update |  |
| **timeoff_leave_types_id_put_request** | [**TimeoffLeaveTypesIdPutRequest**](TimeoffLeaveTypesIdPutRequest.md) |  | [optional] |

### Return type

[**TimeoffLeaveType**](TimeoffLeaveType.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeoff_leave_types_post

> <TimeoffLeaveType> timeoff_leave_types_post(opts)

Creates a Leave type

Creates a Leave type

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

api_instance = F::TimeoffLeaveTypeApi.new
opts = {
  timeoff_leave_types_post_request: F::TimeoffLeaveTypesPostRequest.new({accrues: true, approval_required: true, identifier: 'custom', color: 'red', name: 'Sick Leave', workable: false, company_id: '1', details_required: false}) # TimeoffLeaveTypesPostRequest | 
}

begin
  # Creates a Leave type
  result = api_instance.timeoff_leave_types_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveTypeApi->timeoff_leave_types_post: #{e}"
end
```

#### Using the timeoff_leave_types_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffLeaveType>, Integer, Hash)> timeoff_leave_types_post_with_http_info(opts)

```ruby
begin
  # Creates a Leave type
  data, status_code, headers = api_instance.timeoff_leave_types_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffLeaveType>
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveTypeApi->timeoff_leave_types_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **timeoff_leave_types_post_request** | [**TimeoffLeaveTypesPostRequest**](TimeoffLeaveTypesPostRequest.md) |  | [optional] |

### Return type

[**TimeoffLeaveType**](TimeoffLeaveType.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

