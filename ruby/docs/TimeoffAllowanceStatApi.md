# F::TimeoffAllowanceStatApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**timeoff_allowance_stats_get**](TimeoffAllowanceStatApi.md#timeoff_allowance_stats_get) | **GET** /api/2026-07-01/resources/timeoff/allowance_stats | Reads all Allowance stats |
| [**timeoff_allowance_stats_id_get**](TimeoffAllowanceStatApi.md#timeoff_allowance_stats_id_get) | **GET** /api/2026-07-01/resources/timeoff/allowance_stats/{id} | Reads a single Allowance stat |


## timeoff_allowance_stats_get

> <TimeoffAllowanceStatsGet200Response> timeoff_allowance_stats_get(opts)

Reads all Allowance stats

Retrieves the employee time off counters for a specific allowance with a reference date

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

api_instance = F::TimeoffAllowanceStatApi.new
opts = {
  ids: ['inner_example'], # Array<String> | A virtual ID for the allowance stat, composed of employee_id/allowance_id/reference_date. Cannot be used to fetch this resource.
  employee_ids: ['inner_example'], # Array<String> | Get the allowance stats for specific employees
  allowance_ids: ['inner_example'], # Array<String> | Filter the stats by these allowance IDs
  reference_date: '2023-10-01' # String | The reference date to calculate the allowance stats. If not provided, it will use today's date.
}

begin
  # Reads all Allowance stats
  result = api_instance.timeoff_allowance_stats_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceStatApi->timeoff_allowance_stats_get: #{e}"
end
```

#### Using the timeoff_allowance_stats_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffAllowanceStatsGet200Response>, Integer, Hash)> timeoff_allowance_stats_get_with_http_info(opts)

```ruby
begin
  # Reads all Allowance stats
  data, status_code, headers = api_instance.timeoff_allowance_stats_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffAllowanceStatsGet200Response>
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceStatApi->timeoff_allowance_stats_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | A virtual ID for the allowance stat, composed of employee_id/allowance_id/reference_date. Cannot be used to fetch this resource. | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Get the allowance stats for specific employees | [optional] |
| **allowance_ids** | [**Array&lt;String&gt;**](String.md) | Filter the stats by these allowance IDs | [optional] |
| **reference_date** | **String** | The reference date to calculate the allowance stats. If not provided, it will use today&#39;s date. | [optional] |

### Return type

[**TimeoffAllowanceStatsGet200Response**](TimeoffAllowanceStatsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_allowance_stats_id_get

> <TimeoffAllowanceStatsNew> timeoff_allowance_stats_id_get(id)

Reads a single Allowance stat

Retrieves the employee time off counters for a specific allowance with a reference date

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

api_instance = F::TimeoffAllowanceStatApi.new
id = '1/2/2023-10-01' # String | A virtual ID for the allowance stat, composed of employee_id/allowance_id/reference_date. Cannot be used to fetch this resource.

begin
  # Reads a single Allowance stat
  result = api_instance.timeoff_allowance_stats_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceStatApi->timeoff_allowance_stats_id_get: #{e}"
end
```

#### Using the timeoff_allowance_stats_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffAllowanceStatsNew>, Integer, Hash)> timeoff_allowance_stats_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Allowance stat
  data, status_code, headers = api_instance.timeoff_allowance_stats_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffAllowanceStatsNew>
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceStatApi->timeoff_allowance_stats_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | A virtual ID for the allowance stat, composed of employee_id/allowance_id/reference_date. Cannot be used to fetch this resource. |  |

### Return type

[**TimeoffAllowanceStatsNew**](TimeoffAllowanceStatsNew.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

