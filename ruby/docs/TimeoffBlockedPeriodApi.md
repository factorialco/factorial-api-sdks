# F::TimeoffBlockedPeriodApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**timeoff_blocked_periods_get**](TimeoffBlockedPeriodApi.md#timeoff_blocked_periods_get) | **GET** /api/2026-07-01/resources/timeoff/blocked_periods | Reads all Blocked periods |
| [**timeoff_blocked_periods_id_delete**](TimeoffBlockedPeriodApi.md#timeoff_blocked_periods_id_delete) | **DELETE** /api/2026-07-01/resources/timeoff/blocked_periods/{id} | Deletes a Blocked period |
| [**timeoff_blocked_periods_id_get**](TimeoffBlockedPeriodApi.md#timeoff_blocked_periods_id_get) | **GET** /api/2026-07-01/resources/timeoff/blocked_periods/{id} | Reads a single Blocked period |
| [**timeoff_blocked_periods_id_put**](TimeoffBlockedPeriodApi.md#timeoff_blocked_periods_id_put) | **PUT** /api/2026-07-01/resources/timeoff/blocked_periods/{id} | Updates a Blocked period |
| [**timeoff_blocked_periods_post**](TimeoffBlockedPeriodApi.md#timeoff_blocked_periods_post) | **POST** /api/2026-07-01/resources/timeoff/blocked_periods | Creates a Blocked period |


## timeoff_blocked_periods_get

> <TimeoffBlockedPeriodsGet200Response> timeoff_blocked_periods_get(opts)

Reads all Blocked periods

Retrieves blocked periods

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

api_instance = F::TimeoffBlockedPeriodApi.new
opts = {
  ids: ['inner_example'], # Array<String> | 
  company_ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Blocked periods
  result = api_instance.timeoff_blocked_periods_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffBlockedPeriodApi->timeoff_blocked_periods_get: #{e}"
end
```

#### Using the timeoff_blocked_periods_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffBlockedPeriodsGet200Response>, Integer, Hash)> timeoff_blocked_periods_get_with_http_info(opts)

```ruby
begin
  # Reads all Blocked periods
  data, status_code, headers = api_instance.timeoff_blocked_periods_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffBlockedPeriodsGet200Response>
rescue F::ApiError => e
  puts "Error when calling TimeoffBlockedPeriodApi->timeoff_blocked_periods_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **company_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**TimeoffBlockedPeriodsGet200Response**](TimeoffBlockedPeriodsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_blocked_periods_id_delete

> <TimeoffBlockedPeriodsPolicy> timeoff_blocked_periods_id_delete(id)

Deletes a Blocked period

Deletes a blocked period

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

api_instance = F::TimeoffBlockedPeriodApi.new
id = '1' # String | 

begin
  # Deletes a Blocked period
  result = api_instance.timeoff_blocked_periods_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffBlockedPeriodApi->timeoff_blocked_periods_id_delete: #{e}"
end
```

#### Using the timeoff_blocked_periods_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffBlockedPeriodsPolicy>, Integer, Hash)> timeoff_blocked_periods_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Blocked period
  data, status_code, headers = api_instance.timeoff_blocked_periods_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffBlockedPeriodsPolicy>
rescue F::ApiError => e
  puts "Error when calling TimeoffBlockedPeriodApi->timeoff_blocked_periods_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**TimeoffBlockedPeriodsPolicy**](TimeoffBlockedPeriodsPolicy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_blocked_periods_id_get

> <TimeoffBlockedPeriodsPolicy> timeoff_blocked_periods_id_get(id)

Reads a single Blocked period

Retrieves blocked periods

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

api_instance = F::TimeoffBlockedPeriodApi.new
id = '1' # String | 

begin
  # Reads a single Blocked period
  result = api_instance.timeoff_blocked_periods_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffBlockedPeriodApi->timeoff_blocked_periods_id_get: #{e}"
end
```

#### Using the timeoff_blocked_periods_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffBlockedPeriodsPolicy>, Integer, Hash)> timeoff_blocked_periods_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Blocked period
  data, status_code, headers = api_instance.timeoff_blocked_periods_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffBlockedPeriodsPolicy>
rescue F::ApiError => e
  puts "Error when calling TimeoffBlockedPeriodApi->timeoff_blocked_periods_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**TimeoffBlockedPeriodsPolicy**](TimeoffBlockedPeriodsPolicy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_blocked_periods_id_put

> <TimeoffBlockedPeriodsPolicy> timeoff_blocked_periods_id_put(id, opts)

Updates a Blocked period

Updates a blocked period

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

api_instance = F::TimeoffBlockedPeriodApi.new
id = '1' # String | 
opts = {
  timeoff_blocked_periods_id_put_request: F::TimeoffBlockedPeriodsIdPutRequest.new({id: 'id_example', name: 'Onboarding period edited', leave_type_ids: ["1", "2"], time_periods_attributes: [{"name": "Product offsite updated", "period_type": "by_contract_start_date", "duration": 2, "duration_unit": "months", "start_on": "2024-01-02", "finish_on": "2024-02-28"}], strategy: 'fqlmultiselect'}) # TimeoffBlockedPeriodsIdPutRequest | 
}

begin
  # Updates a Blocked period
  result = api_instance.timeoff_blocked_periods_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffBlockedPeriodApi->timeoff_blocked_periods_id_put: #{e}"
end
```

#### Using the timeoff_blocked_periods_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffBlockedPeriodsPolicy>, Integer, Hash)> timeoff_blocked_periods_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Blocked period
  data, status_code, headers = api_instance.timeoff_blocked_periods_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffBlockedPeriodsPolicy>
rescue F::ApiError => e
  puts "Error when calling TimeoffBlockedPeriodApi->timeoff_blocked_periods_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **timeoff_blocked_periods_id_put_request** | [**TimeoffBlockedPeriodsIdPutRequest**](TimeoffBlockedPeriodsIdPutRequest.md) |  | [optional] |

### Return type

[**TimeoffBlockedPeriodsPolicy**](TimeoffBlockedPeriodsPolicy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeoff_blocked_periods_post

> <TimeoffBlockedPeriodsPolicy> timeoff_blocked_periods_post(opts)

Creates a Blocked period

Creates a blocked period is add a range of dates during which employees cannot submit time off requests. This allows to better plan your team's work throughout the year and ensure that time off requests are in line with the company's needs

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

api_instance = F::TimeoffBlockedPeriodApi.new
opts = {
  timeoff_blocked_periods_post_request: F::TimeoffBlockedPeriodsPostRequest.new({company_id: '1', name: 'Onboarding period', leave_type_ids: ["1", "2", "4"]}) # TimeoffBlockedPeriodsPostRequest | 
}

begin
  # Creates a Blocked period
  result = api_instance.timeoff_blocked_periods_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffBlockedPeriodApi->timeoff_blocked_periods_post: #{e}"
end
```

#### Using the timeoff_blocked_periods_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffBlockedPeriodsPolicy>, Integer, Hash)> timeoff_blocked_periods_post_with_http_info(opts)

```ruby
begin
  # Creates a Blocked period
  data, status_code, headers = api_instance.timeoff_blocked_periods_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffBlockedPeriodsPolicy>
rescue F::ApiError => e
  puts "Error when calling TimeoffBlockedPeriodApi->timeoff_blocked_periods_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **timeoff_blocked_periods_post_request** | [**TimeoffBlockedPeriodsPostRequest**](TimeoffBlockedPeriodsPostRequest.md) |  | [optional] |

### Return type

[**TimeoffBlockedPeriodsPolicy**](TimeoffBlockedPeriodsPolicy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

