# F::PerformanceTargetManagerApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**performance_target_managers_get**](PerformanceTargetManagerApi.md#performance_target_managers_get) | **GET** /api/2026-07-01/resources/performance/target_managers | Reads all Target managers |
| [**performance_target_managers_id_get**](PerformanceTargetManagerApi.md#performance_target_managers_id_get) | **GET** /api/2026-07-01/resources/performance/target_managers/{id} | Reads a single Target manager |


## performance_target_managers_get

> <PerformanceTargetManagersGet200Response> performance_target_managers_get(performance_review_process_ids, opts)

Reads all Target managers

Retrieves the participants' managers of a review process.

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

api_instance = F::PerformanceTargetManagerApi.new
performance_review_process_ids = ['inner_example'] # Array<String> | Review process ID (only one ID is allowed)
opts = {
  ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Target managers
  result = api_instance.performance_target_managers_get(performance_review_process_ids, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceTargetManagerApi->performance_target_managers_get: #{e}"
end
```

#### Using the performance_target_managers_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceTargetManagersGet200Response>, Integer, Hash)> performance_target_managers_get_with_http_info(performance_review_process_ids, opts)

```ruby
begin
  # Reads all Target managers
  data, status_code, headers = api_instance.performance_target_managers_get_with_http_info(performance_review_process_ids, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceTargetManagersGet200Response>
rescue F::ApiError => e
  puts "Error when calling PerformanceTargetManagerApi->performance_target_managers_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_process_ids** | [**Array&lt;String&gt;**](String.md) | Review process ID (only one ID is allowed) |  |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**PerformanceTargetManagersGet200Response**](PerformanceTargetManagersGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_target_managers_id_get

> <PerformanceTargetManager> performance_target_managers_id_get(id)

Reads a single Target manager

Retrieves the participants' managers of a review process.

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

api_instance = F::PerformanceTargetManagerApi.new
id = '1' # String | 

begin
  # Reads a single Target manager
  result = api_instance.performance_target_managers_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceTargetManagerApi->performance_target_managers_id_get: #{e}"
end
```

#### Using the performance_target_managers_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceTargetManager>, Integer, Hash)> performance_target_managers_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Target manager
  data, status_code, headers = api_instance.performance_target_managers_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceTargetManager>
rescue F::ApiError => e
  puts "Error when calling PerformanceTargetManagerApi->performance_target_managers_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**PerformanceTargetManager**](PerformanceTargetManager.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

