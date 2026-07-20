# F::TimeoffLeaveApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**timeoff_leaves_approve_all_post**](TimeoffLeaveApi.md#timeoff_leaves_approve_all_post) | **POST** /api/2026-07-01/resources/timeoff/leaves/approve_all | Approve alls a Leave |
| [**timeoff_leaves_approve_post**](TimeoffLeaveApi.md#timeoff_leaves_approve_post) | **POST** /api/2026-07-01/resources/timeoff/leaves/approve | Approves a Leave |
| [**timeoff_leaves_get**](TimeoffLeaveApi.md#timeoff_leaves_get) | **GET** /api/2026-07-01/resources/timeoff/leaves | Reads all Leaves |
| [**timeoff_leaves_id_delete**](TimeoffLeaveApi.md#timeoff_leaves_id_delete) | **DELETE** /api/2026-07-01/resources/timeoff/leaves/{id} | Deletes a Leave |
| [**timeoff_leaves_id_get**](TimeoffLeaveApi.md#timeoff_leaves_id_get) | **GET** /api/2026-07-01/resources/timeoff/leaves/{id} | Reads a single Leave |
| [**timeoff_leaves_id_put**](TimeoffLeaveApi.md#timeoff_leaves_id_put) | **PUT** /api/2026-07-01/resources/timeoff/leaves/{id} | Updates a Leave |
| [**timeoff_leaves_post**](TimeoffLeaveApi.md#timeoff_leaves_post) | **POST** /api/2026-07-01/resources/timeoff/leaves | Creates a Leave |
| [**timeoff_leaves_reject_post**](TimeoffLeaveApi.md#timeoff_leaves_reject_post) | **POST** /api/2026-07-01/resources/timeoff/leaves/reject | Rejects a Leave |


## timeoff_leaves_approve_all_post

> <TimeoffLeave> timeoff_leaves_approve_all_post(opts)

Approve alls a Leave

Allows authorized users to approve employee time-off requests by directly approving the leave

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

api_instance = F::TimeoffLeaveApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Approve alls a Leave
  result = api_instance.timeoff_leaves_approve_all_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_approve_all_post: #{e}"
end
```

#### Using the timeoff_leaves_approve_all_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffLeave>, Integer, Hash)> timeoff_leaves_approve_all_post_with_http_info(opts)

```ruby
begin
  # Approve alls a Leave
  data, status_code, headers = api_instance.timeoff_leaves_approve_all_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffLeave>
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_approve_all_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**TimeoffLeave**](TimeoffLeave.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeoff_leaves_approve_post

> <TimeoffLeave> timeoff_leaves_approve_post(opts)

Approves a Leave

Allows authorized users to approve employee time-off requests by approving the corresponding approval flow if it exists

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

api_instance = F::TimeoffLeaveApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Approves a Leave
  result = api_instance.timeoff_leaves_approve_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_approve_post: #{e}"
end
```

#### Using the timeoff_leaves_approve_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffLeave>, Integer, Hash)> timeoff_leaves_approve_post_with_http_info(opts)

```ruby
begin
  # Approves a Leave
  data, status_code, headers = api_instance.timeoff_leaves_approve_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffLeave>
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_approve_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**TimeoffLeave**](TimeoffLeave.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeoff_leaves_get

> <TimeoffLeavesGet200Response> timeoff_leaves_get(include_deleted_leaves, opts)

Reads all Leaves

Reads all Leaves

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

api_instance = F::TimeoffLeaveApi.new
include_deleted_leaves = true # Boolean | Whether to include deleted leaves (not included by default if not specified)
opts = {
  ids: ['inner_example'], # Array<String> | The leave ids to retrieve
  employee_ids: ['inner_example'], # Array<String> | The employee ids to retrieve
  leave_type_id: ['inner_example'], # Array<String> | The leave type id to retrieve
  to: '2028-09-30', # String | Valid date following the format YYYY-MM-DD
  from: '2028-09-01', # String | Valid date following the format YYYY-MM-DD
  only_active: false, # Boolean | Retrieve only active leaves
  approved: true, # Boolean | Retrieve approved leaves
  include_pending: true, # Boolean | Retrieve pending leaves
  include_leave_type: false, # Boolean | Retrieve leave types
  include_duration: true, # Boolean | Retrieve leave duration
  type_is_workable: false, # Boolean | Retrieve workable leaves
  type_is_payable: false # Boolean | Retrieve payable leaves
}

begin
  # Reads all Leaves
  result = api_instance.timeoff_leaves_get(include_deleted_leaves, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_get: #{e}"
end
```

#### Using the timeoff_leaves_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffLeavesGet200Response>, Integer, Hash)> timeoff_leaves_get_with_http_info(include_deleted_leaves, opts)

```ruby
begin
  # Reads all Leaves
  data, status_code, headers = api_instance.timeoff_leaves_get_with_http_info(include_deleted_leaves, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffLeavesGet200Response>
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include_deleted_leaves** | **Boolean** | Whether to include deleted leaves (not included by default if not specified) |  |
| **ids** | [**Array&lt;String&gt;**](String.md) | The leave ids to retrieve | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | The employee ids to retrieve | [optional] |
| **leave_type_id** | [**Array&lt;String&gt;**](String.md) | The leave type id to retrieve | [optional] |
| **to** | **String** | Valid date following the format YYYY-MM-DD | [optional] |
| **from** | **String** | Valid date following the format YYYY-MM-DD | [optional] |
| **only_active** | **Boolean** | Retrieve only active leaves | [optional] |
| **approved** | **Boolean** | Retrieve approved leaves | [optional] |
| **include_pending** | **Boolean** | Retrieve pending leaves | [optional] |
| **include_leave_type** | **Boolean** | Retrieve leave types | [optional] |
| **include_duration** | **Boolean** | Retrieve leave duration | [optional] |
| **type_is_workable** | **Boolean** | Retrieve workable leaves | [optional] |
| **type_is_payable** | **Boolean** | Retrieve payable leaves | [optional] |

### Return type

[**TimeoffLeavesGet200Response**](TimeoffLeavesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_leaves_id_delete

> <TimeoffLeave> timeoff_leaves_id_delete(id)

Deletes a Leave

Deletes a Leave

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

api_instance = F::TimeoffLeaveApi.new
id = '1' # String | 

begin
  # Deletes a Leave
  result = api_instance.timeoff_leaves_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_id_delete: #{e}"
end
```

#### Using the timeoff_leaves_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffLeave>, Integer, Hash)> timeoff_leaves_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Leave
  data, status_code, headers = api_instance.timeoff_leaves_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffLeave>
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**TimeoffLeave**](TimeoffLeave.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_leaves_id_get

> <TimeoffLeave> timeoff_leaves_id_get(id)

Reads a single Leave

Reads a single Leave

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

api_instance = F::TimeoffLeaveApi.new
id = '1' # String | The leave ids to retrieve

begin
  # Reads a single Leave
  result = api_instance.timeoff_leaves_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_id_get: #{e}"
end
```

#### Using the timeoff_leaves_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffLeave>, Integer, Hash)> timeoff_leaves_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Leave
  data, status_code, headers = api_instance.timeoff_leaves_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffLeave>
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The leave ids to retrieve |  |

### Return type

[**TimeoffLeave**](TimeoffLeave.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_leaves_id_put

> <TimeoffLeave> timeoff_leaves_id_put(id, opts)

Updates a Leave

Updates a Leave

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

api_instance = F::TimeoffLeaveApi.new
id = '1' # String | The leave id
opts = {
  timeoff_leaves_id_put_request: F::TimeoffLeavesIdPutRequest.new({id: 'id_example'}) # TimeoffLeavesIdPutRequest | 
}

begin
  # Updates a Leave
  result = api_instance.timeoff_leaves_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_id_put: #{e}"
end
```

#### Using the timeoff_leaves_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffLeave>, Integer, Hash)> timeoff_leaves_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Leave
  data, status_code, headers = api_instance.timeoff_leaves_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffLeave>
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The leave id |  |
| **timeoff_leaves_id_put_request** | [**TimeoffLeavesIdPutRequest**](TimeoffLeavesIdPutRequest.md) |  | [optional] |

### Return type

[**TimeoffLeave**](TimeoffLeave.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeoff_leaves_post

> <TimeoffLeave> timeoff_leaves_post(opts)

Creates a Leave

Creates a Leave

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

api_instance = F::TimeoffLeaveApi.new
opts = {
  timeoff_leaves_post_request: F::TimeoffLeavesPostRequest.new({employee_id: '1', start_on: '2028-09-05'}) # TimeoffLeavesPostRequest | 
}

begin
  # Creates a Leave
  result = api_instance.timeoff_leaves_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_post: #{e}"
end
```

#### Using the timeoff_leaves_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffLeave>, Integer, Hash)> timeoff_leaves_post_with_http_info(opts)

```ruby
begin
  # Creates a Leave
  data, status_code, headers = api_instance.timeoff_leaves_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffLeave>
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **timeoff_leaves_post_request** | [**TimeoffLeavesPostRequest**](TimeoffLeavesPostRequest.md) |  | [optional] |

### Return type

[**TimeoffLeave**](TimeoffLeave.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeoff_leaves_reject_post

> <TimeoffLeave> timeoff_leaves_reject_post(opts)

Rejects a Leave

Allows authorized users to reject employee time-off requests

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

api_instance = F::TimeoffLeaveApi.new
opts = {
  timeoff_leaves_reject_post_request: F::TimeoffLeavesRejectPostRequest.new({id: '1'}) # TimeoffLeavesRejectPostRequest | 
}

begin
  # Rejects a Leave
  result = api_instance.timeoff_leaves_reject_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_reject_post: #{e}"
end
```

#### Using the timeoff_leaves_reject_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffLeave>, Integer, Hash)> timeoff_leaves_reject_post_with_http_info(opts)

```ruby
begin
  # Rejects a Leave
  data, status_code, headers = api_instance.timeoff_leaves_reject_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffLeave>
rescue F::ApiError => e
  puts "Error when calling TimeoffLeaveApi->timeoff_leaves_reject_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **timeoff_leaves_reject_post_request** | [**TimeoffLeavesRejectPostRequest**](TimeoffLeavesRejectPostRequest.md) |  | [optional] |

### Return type

[**TimeoffLeave**](TimeoffLeave.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

