# F::TimeoffPolicyAssignmentApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**timeoff_policy_assignments_get**](TimeoffPolicyAssignmentApi.md#timeoff_policy_assignments_get) | **GET** /api/2026-07-01/resources/timeoff/policy_assignments | Reads all Policy assignments |
| [**timeoff_policy_assignments_id_delete**](TimeoffPolicyAssignmentApi.md#timeoff_policy_assignments_id_delete) | **DELETE** /api/2026-07-01/resources/timeoff/policy_assignments/{id} | Deletes a Policy assignment |
| [**timeoff_policy_assignments_id_get**](TimeoffPolicyAssignmentApi.md#timeoff_policy_assignments_id_get) | **GET** /api/2026-07-01/resources/timeoff/policy_assignments/{id} | Reads a single Policy assignment |
| [**timeoff_policy_assignments_id_put**](TimeoffPolicyAssignmentApi.md#timeoff_policy_assignments_id_put) | **PUT** /api/2026-07-01/resources/timeoff/policy_assignments/{id} | Updates a Policy assignment |
| [**timeoff_policy_assignments_post**](TimeoffPolicyAssignmentApi.md#timeoff_policy_assignments_post) | **POST** /api/2026-07-01/resources/timeoff/policy_assignments | Creates a Policy assignment |


## timeoff_policy_assignments_get

> <TimeoffPolicyAssignmentsGet200Response> timeoff_policy_assignments_get(opts)

Reads all Policy assignments

Read Time off Policy Assignments

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

api_instance = F::TimeoffPolicyAssignmentApi.new
opts = {
  ids: ['inner_example'], # Array<String> | An array of time off policy assignment ids
  employee_ids: ['inner_example'], # Array<String> | Filter policy assignments by employee ids
  timeoff_policy_ids: ['inner_example'] # Array<String> | Filter policy assignments by time off policy ids
}

begin
  # Reads all Policy assignments
  result = api_instance.timeoff_policy_assignments_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyAssignmentApi->timeoff_policy_assignments_get: #{e}"
end
```

#### Using the timeoff_policy_assignments_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffPolicyAssignmentsGet200Response>, Integer, Hash)> timeoff_policy_assignments_get_with_http_info(opts)

```ruby
begin
  # Reads all Policy assignments
  data, status_code, headers = api_instance.timeoff_policy_assignments_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffPolicyAssignmentsGet200Response>
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyAssignmentApi->timeoff_policy_assignments_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | An array of time off policy assignment ids | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Filter policy assignments by employee ids | [optional] |
| **timeoff_policy_ids** | [**Array&lt;String&gt;**](String.md) | Filter policy assignments by time off policy ids | [optional] |

### Return type

[**TimeoffPolicyAssignmentsGet200Response**](TimeoffPolicyAssignmentsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_policy_assignments_id_delete

> <TimeoffPolicyAssignment> timeoff_policy_assignments_id_delete(id)

Deletes a Policy assignment

Delete a Time off Policy Assignment

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

api_instance = F::TimeoffPolicyAssignmentApi.new
id = '1' # String | Unique identifier of the policy assignment

begin
  # Deletes a Policy assignment
  result = api_instance.timeoff_policy_assignments_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyAssignmentApi->timeoff_policy_assignments_id_delete: #{e}"
end
```

#### Using the timeoff_policy_assignments_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffPolicyAssignment>, Integer, Hash)> timeoff_policy_assignments_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Policy assignment
  data, status_code, headers = api_instance.timeoff_policy_assignments_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffPolicyAssignment>
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyAssignmentApi->timeoff_policy_assignments_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier of the policy assignment |  |

### Return type

[**TimeoffPolicyAssignment**](TimeoffPolicyAssignment.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_policy_assignments_id_get

> <TimeoffPolicyAssignment> timeoff_policy_assignments_id_get(id)

Reads a single Policy assignment

Read Time off Policy Assignments

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

api_instance = F::TimeoffPolicyAssignmentApi.new
id = '1' # String | An array of time off policy assignment ids

begin
  # Reads a single Policy assignment
  result = api_instance.timeoff_policy_assignments_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyAssignmentApi->timeoff_policy_assignments_id_get: #{e}"
end
```

#### Using the timeoff_policy_assignments_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffPolicyAssignment>, Integer, Hash)> timeoff_policy_assignments_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Policy assignment
  data, status_code, headers = api_instance.timeoff_policy_assignments_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffPolicyAssignment>
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyAssignmentApi->timeoff_policy_assignments_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | An array of time off policy assignment ids |  |

### Return type

[**TimeoffPolicyAssignment**](TimeoffPolicyAssignment.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_policy_assignments_id_put

> <TimeoffPolicyAssignment> timeoff_policy_assignments_id_put(id, opts)

Updates a Policy assignment

Update a Time off Policy Assignment

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

api_instance = F::TimeoffPolicyAssignmentApi.new
id = '1' # String | Unique identifier of the policy assignment
opts = {
  timeoff_policy_assignments_id_put_request: F::TimeoffPolicyAssignmentsIdPutRequest.new({id: '1', timeoff_policy_id: '1', effective_at: '2024-01-01'}) # TimeoffPolicyAssignmentsIdPutRequest | 
}

begin
  # Updates a Policy assignment
  result = api_instance.timeoff_policy_assignments_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyAssignmentApi->timeoff_policy_assignments_id_put: #{e}"
end
```

#### Using the timeoff_policy_assignments_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffPolicyAssignment>, Integer, Hash)> timeoff_policy_assignments_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Policy assignment
  data, status_code, headers = api_instance.timeoff_policy_assignments_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffPolicyAssignment>
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyAssignmentApi->timeoff_policy_assignments_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier of the policy assignment |  |
| **timeoff_policy_assignments_id_put_request** | [**TimeoffPolicyAssignmentsIdPutRequest**](TimeoffPolicyAssignmentsIdPutRequest.md) |  | [optional] |

### Return type

[**TimeoffPolicyAssignment**](TimeoffPolicyAssignment.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeoff_policy_assignments_post

> <TimeoffPolicyAssignment> timeoff_policy_assignments_post(opts)

Creates a Policy assignment

Create a Time off Policy Assignment

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

api_instance = F::TimeoffPolicyAssignmentApi.new
opts = {
  timeoff_policy_assignments_post_request: F::TimeoffPolicyAssignmentsPostRequest.new({timeoff_policy_id: '1', employee_id: '1', effective_at: '2024-01-01'}) # TimeoffPolicyAssignmentsPostRequest | 
}

begin
  # Creates a Policy assignment
  result = api_instance.timeoff_policy_assignments_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyAssignmentApi->timeoff_policy_assignments_post: #{e}"
end
```

#### Using the timeoff_policy_assignments_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffPolicyAssignment>, Integer, Hash)> timeoff_policy_assignments_post_with_http_info(opts)

```ruby
begin
  # Creates a Policy assignment
  data, status_code, headers = api_instance.timeoff_policy_assignments_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffPolicyAssignment>
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyAssignmentApi->timeoff_policy_assignments_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **timeoff_policy_assignments_post_request** | [**TimeoffPolicyAssignmentsPostRequest**](TimeoffPolicyAssignmentsPostRequest.md) |  | [optional] |

### Return type

[**TimeoffPolicyAssignment**](TimeoffPolicyAssignment.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

