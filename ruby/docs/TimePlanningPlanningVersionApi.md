# F::TimePlanningPlanningVersionApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**time_planning_planning_versions_bulk_create_post**](TimePlanningPlanningVersionApi.md#time_planning_planning_versions_bulk_create_post) | **POST** /api/2026-07-01/resources/time_planning/planning_versions/bulk_create | Bulk creates a Planning version |
| [**time_planning_planning_versions_get**](TimePlanningPlanningVersionApi.md#time_planning_planning_versions_get) | **GET** /api/2026-07-01/resources/time_planning/planning_versions | Reads all Planning versions |
| [**time_planning_planning_versions_id_delete**](TimePlanningPlanningVersionApi.md#time_planning_planning_versions_id_delete) | **DELETE** /api/2026-07-01/resources/time_planning/planning_versions/{id} | Deletes a Planning version |
| [**time_planning_planning_versions_id_put**](TimePlanningPlanningVersionApi.md#time_planning_planning_versions_id_put) | **PUT** /api/2026-07-01/resources/time_planning/planning_versions/{id} | Updates a Planning version |
| [**time_planning_planning_versions_post**](TimePlanningPlanningVersionApi.md#time_planning_planning_versions_post) | **POST** /api/2026-07-01/resources/time_planning/planning_versions | Creates a Planning version |


## time_planning_planning_versions_bulk_create_post

> <Array<TimePlanningPlanningVersion>> time_planning_planning_versions_bulk_create_post(opts)

Bulk creates a Planning version

Bulk creates a Planning version

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

api_instance = F::TimePlanningPlanningVersionApi.new
opts = {
  time_planning_planning_versions_bulk_create_post_request: F::TimePlanningPlanningVersionsBulkCreatePostRequest.new({effective_at: '2020-09-07', planning_tool: 'shift_management', employee_ids: [1,  2,  3]}) # TimePlanningPlanningVersionsBulkCreatePostRequest | 
}

begin
  # Bulk creates a Planning version
  result = api_instance.time_planning_planning_versions_bulk_create_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlanningVersionApi->time_planning_planning_versions_bulk_create_post: #{e}"
end
```

#### Using the time_planning_planning_versions_bulk_create_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<TimePlanningPlanningVersion>>, Integer, Hash)> time_planning_planning_versions_bulk_create_post_with_http_info(opts)

```ruby
begin
  # Bulk creates a Planning version
  data, status_code, headers = api_instance.time_planning_planning_versions_bulk_create_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<TimePlanningPlanningVersion>>
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlanningVersionApi->time_planning_planning_versions_bulk_create_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **time_planning_planning_versions_bulk_create_post_request** | [**TimePlanningPlanningVersionsBulkCreatePostRequest**](TimePlanningPlanningVersionsBulkCreatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;TimePlanningPlanningVersion&gt;**](TimePlanningPlanningVersion.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## time_planning_planning_versions_get

> <TimePlanningPlanningVersionsGet200Response> time_planning_planning_versions_get(only_active, opts)

Reads all Planning versions

Reads all Planning versions

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

api_instance = F::TimePlanningPlanningVersionApi.new
only_active = false # Boolean | Filter by active planning versions only
opts = {
  employee_ids: ['inner_example'], # Array<String> | List of employee identifiers
  for_shifts: true, # Boolean | Filter by shift management planning tool
  planning_tool: 'shift_management', # String | Type of planning tool (shift_management, work_schedules, contract_hours)
  schedule_ids: ['inner_example'] # Array<String> | List of work schedule identifiers to include
}

begin
  # Reads all Planning versions
  result = api_instance.time_planning_planning_versions_get(only_active, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlanningVersionApi->time_planning_planning_versions_get: #{e}"
end
```

#### Using the time_planning_planning_versions_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimePlanningPlanningVersionsGet200Response>, Integer, Hash)> time_planning_planning_versions_get_with_http_info(only_active, opts)

```ruby
begin
  # Reads all Planning versions
  data, status_code, headers = api_instance.time_planning_planning_versions_get_with_http_info(only_active, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimePlanningPlanningVersionsGet200Response>
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlanningVersionApi->time_planning_planning_versions_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **only_active** | **Boolean** | Filter by active planning versions only |  |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | List of employee identifiers | [optional] |
| **for_shifts** | **Boolean** | Filter by shift management planning tool | [optional] |
| **planning_tool** | **String** | Type of planning tool (shift_management, work_schedules, contract_hours) | [optional] |
| **schedule_ids** | [**Array&lt;String&gt;**](String.md) | List of work schedule identifiers to include | [optional] |

### Return type

[**TimePlanningPlanningVersionsGet200Response**](TimePlanningPlanningVersionsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## time_planning_planning_versions_id_delete

> <TimePlanningPlanningVersion> time_planning_planning_versions_id_delete(id)

Deletes a Planning version

Deletes a Planning version

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

api_instance = F::TimePlanningPlanningVersionApi.new
id = '1' # String | 

begin
  # Deletes a Planning version
  result = api_instance.time_planning_planning_versions_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlanningVersionApi->time_planning_planning_versions_id_delete: #{e}"
end
```

#### Using the time_planning_planning_versions_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimePlanningPlanningVersion>, Integer, Hash)> time_planning_planning_versions_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Planning version
  data, status_code, headers = api_instance.time_planning_planning_versions_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimePlanningPlanningVersion>
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlanningVersionApi->time_planning_planning_versions_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**TimePlanningPlanningVersion**](TimePlanningPlanningVersion.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## time_planning_planning_versions_id_put

> <TimePlanningPlanningVersion> time_planning_planning_versions_id_put(id, opts)

Updates a Planning version

Updates a Planning version

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

api_instance = F::TimePlanningPlanningVersionApi.new
id = '1' # String | Planning version identifier
opts = {
  time_planning_planning_versions_id_put_request: F::TimePlanningPlanningVersionsIdPutRequest.new({id: '1', effective_at: '2020-09-07', planning_tool: 'shift_management'}) # TimePlanningPlanningVersionsIdPutRequest | 
}

begin
  # Updates a Planning version
  result = api_instance.time_planning_planning_versions_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlanningVersionApi->time_planning_planning_versions_id_put: #{e}"
end
```

#### Using the time_planning_planning_versions_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimePlanningPlanningVersion>, Integer, Hash)> time_planning_planning_versions_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Planning version
  data, status_code, headers = api_instance.time_planning_planning_versions_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimePlanningPlanningVersion>
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlanningVersionApi->time_planning_planning_versions_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Planning version identifier |  |
| **time_planning_planning_versions_id_put_request** | [**TimePlanningPlanningVersionsIdPutRequest**](TimePlanningPlanningVersionsIdPutRequest.md) |  | [optional] |

### Return type

[**TimePlanningPlanningVersion**](TimePlanningPlanningVersion.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## time_planning_planning_versions_post

> <TimePlanningPlanningVersion> time_planning_planning_versions_post(opts)

Creates a Planning version

Creates a Planning version

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

api_instance = F::TimePlanningPlanningVersionApi.new
opts = {
  time_planning_planning_versions_post_request: F::TimePlanningPlanningVersionsPostRequest.new({effective_at: '2020-09-07', planning_tool: 'shift_management', employee_id: '1'}) # TimePlanningPlanningVersionsPostRequest | 
}

begin
  # Creates a Planning version
  result = api_instance.time_planning_planning_versions_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlanningVersionApi->time_planning_planning_versions_post: #{e}"
end
```

#### Using the time_planning_planning_versions_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimePlanningPlanningVersion>, Integer, Hash)> time_planning_planning_versions_post_with_http_info(opts)

```ruby
begin
  # Creates a Planning version
  data, status_code, headers = api_instance.time_planning_planning_versions_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimePlanningPlanningVersion>
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlanningVersionApi->time_planning_planning_versions_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **time_planning_planning_versions_post_request** | [**TimePlanningPlanningVersionsPostRequest**](TimePlanningPlanningVersionsPostRequest.md) |  | [optional] |

### Return type

[**TimePlanningPlanningVersion**](TimePlanningPlanningVersion.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

