# F::WorkScheduleOverlapPeriodApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**work_schedule_overlap_periods_get**](WorkScheduleOverlapPeriodApi.md#work_schedule_overlap_periods_get) | **GET** /api/2026-07-01/resources/work_schedule/overlap_periods | Reads all Overlap periods |
| [**work_schedule_overlap_periods_id_delete**](WorkScheduleOverlapPeriodApi.md#work_schedule_overlap_periods_id_delete) | **DELETE** /api/2026-07-01/resources/work_schedule/overlap_periods/{id} | Deletes an Overlap period |
| [**work_schedule_overlap_periods_id_get**](WorkScheduleOverlapPeriodApi.md#work_schedule_overlap_periods_id_get) | **GET** /api/2026-07-01/resources/work_schedule/overlap_periods/{id} | Reads a single Overlap period |
| [**work_schedule_overlap_periods_id_put**](WorkScheduleOverlapPeriodApi.md#work_schedule_overlap_periods_id_put) | **PUT** /api/2026-07-01/resources/work_schedule/overlap_periods/{id} | Updates an Overlap period |
| [**work_schedule_overlap_periods_post**](WorkScheduleOverlapPeriodApi.md#work_schedule_overlap_periods_post) | **POST** /api/2026-07-01/resources/work_schedule/overlap_periods | Creates an Overlap period |


## work_schedule_overlap_periods_get

> <WorkScheduleOverlapPeriodsGet200Response> work_schedule_overlap_periods_get(opts)

Reads all Overlap periods

Reads all Overlap periods

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

api_instance = F::WorkScheduleOverlapPeriodApi.new
opts = {
  ids: ['inner_example'] # Array<String> | List of overlap period identifiers to retrieve. If provided, returns only overlap periods matching these IDs
}

begin
  # Reads all Overlap periods
  result = api_instance.work_schedule_overlap_periods_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling WorkScheduleOverlapPeriodApi->work_schedule_overlap_periods_get: #{e}"
end
```

#### Using the work_schedule_overlap_periods_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkScheduleOverlapPeriodsGet200Response>, Integer, Hash)> work_schedule_overlap_periods_get_with_http_info(opts)

```ruby
begin
  # Reads all Overlap periods
  data, status_code, headers = api_instance.work_schedule_overlap_periods_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkScheduleOverlapPeriodsGet200Response>
rescue F::ApiError => e
  puts "Error when calling WorkScheduleOverlapPeriodApi->work_schedule_overlap_periods_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | List of overlap period identifiers to retrieve. If provided, returns only overlap periods matching these IDs | [optional] |

### Return type

[**WorkScheduleOverlapPeriodsGet200Response**](WorkScheduleOverlapPeriodsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## work_schedule_overlap_periods_id_delete

> <WorkScheduleOverlapPeriod> work_schedule_overlap_periods_id_delete(id)

Deletes an Overlap period

Deletes an Overlap period

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

api_instance = F::WorkScheduleOverlapPeriodApi.new
id = '1' # String | 

begin
  # Deletes an Overlap period
  result = api_instance.work_schedule_overlap_periods_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling WorkScheduleOverlapPeriodApi->work_schedule_overlap_periods_id_delete: #{e}"
end
```

#### Using the work_schedule_overlap_periods_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkScheduleOverlapPeriod>, Integer, Hash)> work_schedule_overlap_periods_id_delete_with_http_info(id)

```ruby
begin
  # Deletes an Overlap period
  data, status_code, headers = api_instance.work_schedule_overlap_periods_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkScheduleOverlapPeriod>
rescue F::ApiError => e
  puts "Error when calling WorkScheduleOverlapPeriodApi->work_schedule_overlap_periods_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**WorkScheduleOverlapPeriod**](WorkScheduleOverlapPeriod.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## work_schedule_overlap_periods_id_get

> <WorkScheduleOverlapPeriod> work_schedule_overlap_periods_id_get(id)

Reads a single Overlap period

Reads a single Overlap period

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

api_instance = F::WorkScheduleOverlapPeriodApi.new
id = '1' # String | List of overlap period identifiers to retrieve. If provided, returns only overlap periods matching these IDs

begin
  # Reads a single Overlap period
  result = api_instance.work_schedule_overlap_periods_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling WorkScheduleOverlapPeriodApi->work_schedule_overlap_periods_id_get: #{e}"
end
```

#### Using the work_schedule_overlap_periods_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkScheduleOverlapPeriod>, Integer, Hash)> work_schedule_overlap_periods_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Overlap period
  data, status_code, headers = api_instance.work_schedule_overlap_periods_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkScheduleOverlapPeriod>
rescue F::ApiError => e
  puts "Error when calling WorkScheduleOverlapPeriodApi->work_schedule_overlap_periods_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | List of overlap period identifiers to retrieve. If provided, returns only overlap periods matching these IDs |  |

### Return type

[**WorkScheduleOverlapPeriod**](WorkScheduleOverlapPeriod.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## work_schedule_overlap_periods_id_put

> <WorkScheduleOverlapPeriod> work_schedule_overlap_periods_id_put(id, opts)

Updates an Overlap period

Updates an Overlap period

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

api_instance = F::WorkScheduleOverlapPeriodApi.new
id = '1' # String | 
opts = {
  work_schedule_overlap_periods_id_put_request: F::WorkScheduleOverlapPeriodsIdPutRequest.new({id: 'id_example', update_params: TODO}) # WorkScheduleOverlapPeriodsIdPutRequest | 
}

begin
  # Updates an Overlap period
  result = api_instance.work_schedule_overlap_periods_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling WorkScheduleOverlapPeriodApi->work_schedule_overlap_periods_id_put: #{e}"
end
```

#### Using the work_schedule_overlap_periods_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkScheduleOverlapPeriod>, Integer, Hash)> work_schedule_overlap_periods_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates an Overlap period
  data, status_code, headers = api_instance.work_schedule_overlap_periods_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkScheduleOverlapPeriod>
rescue F::ApiError => e
  puts "Error when calling WorkScheduleOverlapPeriodApi->work_schedule_overlap_periods_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **work_schedule_overlap_periods_id_put_request** | [**WorkScheduleOverlapPeriodsIdPutRequest**](WorkScheduleOverlapPeriodsIdPutRequest.md) |  | [optional] |

### Return type

[**WorkScheduleOverlapPeriod**](WorkScheduleOverlapPeriod.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## work_schedule_overlap_periods_post

> <WorkScheduleOverlapPeriod> work_schedule_overlap_periods_post(opts)

Creates an Overlap period

Creates an Overlap period

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

api_instance = F::WorkScheduleOverlapPeriodApi.new
opts = {
  work_schedule_overlap_periods_post_request: F::WorkScheduleOverlapPeriodsPostRequest.new({schedule_id: 'schedule_id_example', create_params: TODO}) # WorkScheduleOverlapPeriodsPostRequest | 
}

begin
  # Creates an Overlap period
  result = api_instance.work_schedule_overlap_periods_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling WorkScheduleOverlapPeriodApi->work_schedule_overlap_periods_post: #{e}"
end
```

#### Using the work_schedule_overlap_periods_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkScheduleOverlapPeriod>, Integer, Hash)> work_schedule_overlap_periods_post_with_http_info(opts)

```ruby
begin
  # Creates an Overlap period
  data, status_code, headers = api_instance.work_schedule_overlap_periods_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkScheduleOverlapPeriod>
rescue F::ApiError => e
  puts "Error when calling WorkScheduleOverlapPeriodApi->work_schedule_overlap_periods_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **work_schedule_overlap_periods_post_request** | [**WorkScheduleOverlapPeriodsPostRequest**](WorkScheduleOverlapPeriodsPostRequest.md) |  | [optional] |

### Return type

[**WorkScheduleOverlapPeriod**](WorkScheduleOverlapPeriod.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

