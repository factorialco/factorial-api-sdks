# F::TimeoffAllowanceApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**timeoff_allowances_delete_with_alt_allowance_post**](TimeoffAllowanceApi.md#timeoff_allowances_delete_with_alt_allowance_post) | **POST** /api/2026-07-01/resources/timeoff/allowances/delete_with_alt_allowance | Delete with alt allowances an Allowance |
| [**timeoff_allowances_get**](TimeoffAllowanceApi.md#timeoff_allowances_get) | **GET** /api/2026-07-01/resources/timeoff/allowances | Reads all Allowances |
| [**timeoff_allowances_id_delete**](TimeoffAllowanceApi.md#timeoff_allowances_id_delete) | **DELETE** /api/2026-07-01/resources/timeoff/allowances/{id} | Deletes an Allowance |
| [**timeoff_allowances_id_get**](TimeoffAllowanceApi.md#timeoff_allowances_id_get) | **GET** /api/2026-07-01/resources/timeoff/allowances/{id} | Reads a single Allowance |
| [**timeoff_allowances_id_put**](TimeoffAllowanceApi.md#timeoff_allowances_id_put) | **PUT** /api/2026-07-01/resources/timeoff/allowances/{id} | Updates an Allowance |
| [**timeoff_allowances_post**](TimeoffAllowanceApi.md#timeoff_allowances_post) | **POST** /api/2026-07-01/resources/timeoff/allowances | Creates an Allowance |


## timeoff_allowances_delete_with_alt_allowance_post

> <TimeoffAllowance> timeoff_allowances_delete_with_alt_allowance_post(opts)

Delete with alt allowances an Allowance

Deletes an allowance and migrate the existing incidences in the alternative allowance

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

api_instance = F::TimeoffAllowanceApi.new
opts = {
  timeoff_allowances_delete_with_alt_allowance_post_request: F::TimeoffAllowancesDeleteWithAltAllowancePostRequest.new({id: 'id_example', alt_allowance_id: '1'}) # TimeoffAllowancesDeleteWithAltAllowancePostRequest | 
}

begin
  # Delete with alt allowances an Allowance
  result = api_instance.timeoff_allowances_delete_with_alt_allowance_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceApi->timeoff_allowances_delete_with_alt_allowance_post: #{e}"
end
```

#### Using the timeoff_allowances_delete_with_alt_allowance_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffAllowance>, Integer, Hash)> timeoff_allowances_delete_with_alt_allowance_post_with_http_info(opts)

```ruby
begin
  # Delete with alt allowances an Allowance
  data, status_code, headers = api_instance.timeoff_allowances_delete_with_alt_allowance_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffAllowance>
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceApi->timeoff_allowances_delete_with_alt_allowance_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **timeoff_allowances_delete_with_alt_allowance_post_request** | [**TimeoffAllowancesDeleteWithAltAllowancePostRequest**](TimeoffAllowancesDeleteWithAltAllowancePostRequest.md) |  | [optional] |

### Return type

[**TimeoffAllowance**](TimeoffAllowance.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeoff_allowances_get

> <TimeoffAllowancesGet200Response> timeoff_allowances_get(opts)

Reads all Allowances

Retrieves allowances

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

api_instance = F::TimeoffAllowanceApi.new
opts = {
  ids: ['inner_example'], # Array<String> | An array of allowance ids to look for
  timeoff_policy_id: '1', # String | Filter allowances by Time off policy id
  by_overtime: true # Boolean | Filter by only overtime allowances
}

begin
  # Reads all Allowances
  result = api_instance.timeoff_allowances_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceApi->timeoff_allowances_get: #{e}"
end
```

#### Using the timeoff_allowances_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffAllowancesGet200Response>, Integer, Hash)> timeoff_allowances_get_with_http_info(opts)

```ruby
begin
  # Reads all Allowances
  data, status_code, headers = api_instance.timeoff_allowances_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffAllowancesGet200Response>
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceApi->timeoff_allowances_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | An array of allowance ids to look for | [optional] |
| **timeoff_policy_id** | **String** | Filter allowances by Time off policy id | [optional] |
| **by_overtime** | **Boolean** | Filter by only overtime allowances | [optional] |

### Return type

[**TimeoffAllowancesGet200Response**](TimeoffAllowancesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_allowances_id_delete

> <TimeoffAllowance> timeoff_allowances_id_delete(id)

Deletes an Allowance

Deletes an allowance

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

api_instance = F::TimeoffAllowanceApi.new
id = '1' # String | 

begin
  # Deletes an Allowance
  result = api_instance.timeoff_allowances_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceApi->timeoff_allowances_id_delete: #{e}"
end
```

#### Using the timeoff_allowances_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffAllowance>, Integer, Hash)> timeoff_allowances_id_delete_with_http_info(id)

```ruby
begin
  # Deletes an Allowance
  data, status_code, headers = api_instance.timeoff_allowances_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffAllowance>
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceApi->timeoff_allowances_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**TimeoffAllowance**](TimeoffAllowance.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_allowances_id_get

> <TimeoffAllowance> timeoff_allowances_id_get(id)

Reads a single Allowance

Retrieves allowances

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

api_instance = F::TimeoffAllowanceApi.new
id = '1' # String | An array of allowance ids to look for

begin
  # Reads a single Allowance
  result = api_instance.timeoff_allowances_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceApi->timeoff_allowances_id_get: #{e}"
end
```

#### Using the timeoff_allowances_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffAllowance>, Integer, Hash)> timeoff_allowances_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Allowance
  data, status_code, headers = api_instance.timeoff_allowances_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffAllowance>
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceApi->timeoff_allowances_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | An array of allowance ids to look for |  |

### Return type

[**TimeoffAllowance**](TimeoffAllowance.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_allowances_id_put

> <TimeoffAllowance> timeoff_allowances_id_put(id, opts)

Updates an Allowance

Updates an existing Time Off Allowance

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

api_instance = F::TimeoffAllowanceApi.new
id = '1' # String | 
opts = {
  timeoff_allowances_id_put_request: F::TimeoffAllowancesIdPutRequest.new({id: 'id_example'}) # TimeoffAllowancesIdPutRequest | 
}

begin
  # Updates an Allowance
  result = api_instance.timeoff_allowances_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceApi->timeoff_allowances_id_put: #{e}"
end
```

#### Using the timeoff_allowances_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffAllowance>, Integer, Hash)> timeoff_allowances_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates an Allowance
  data, status_code, headers = api_instance.timeoff_allowances_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffAllowance>
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceApi->timeoff_allowances_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **timeoff_allowances_id_put_request** | [**TimeoffAllowancesIdPutRequest**](TimeoffAllowancesIdPutRequest.md) |  | [optional] |

### Return type

[**TimeoffAllowance**](TimeoffAllowance.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeoff_allowances_post

> <TimeoffAllowance> timeoff_allowances_post(opts)

Creates an Allowance

Creates a new Time off allowance

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

api_instance = F::TimeoffAllowanceApi.new
opts = {
  timeoff_allowances_post_request: F::TimeoffAllowancesPostRequest.new({accrued_units_availability: 'current_cycle', allowance_type: 'days', available_days: 'all_days', count_holiday_as_workable: false, cycle_start: 'jan', days_type: 'working_days', holiday_allowance_in_cents: 2300, leave_type_ids: [1,  2,  3,  4], name: 'Holiday Allowance', negative_counter_type: 'negative_counter_disabled', proration_type: 'proration_enabled', pto_proratio_enabled: false, rounding: 'half_day', source_units: 'base_units', tenure_periods: [{"period_type": "years", "period_length": 1, "adjustment_in_cents": 100, "timeoff_allowance_id": 23, "max_cap_in_cents": 100, "time_worked_based_hours_accrued_in_cents": 100, "time_worked_based_per_hours_worked_in_cents": 100, "balance_type": "fixed_balance"}], timeoff_policy_id: '1', unlimited_accrued_hours: false, unlimited_carry_over: false, unlimited_carry_over_expiration: false, unlimited_holidays: false}) # TimeoffAllowancesPostRequest | 
}

begin
  # Creates an Allowance
  result = api_instance.timeoff_allowances_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceApi->timeoff_allowances_post: #{e}"
end
```

#### Using the timeoff_allowances_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffAllowance>, Integer, Hash)> timeoff_allowances_post_with_http_info(opts)

```ruby
begin
  # Creates an Allowance
  data, status_code, headers = api_instance.timeoff_allowances_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffAllowance>
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceApi->timeoff_allowances_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **timeoff_allowances_post_request** | [**TimeoffAllowancesPostRequest**](TimeoffAllowancesPostRequest.md) |  | [optional] |

### Return type

[**TimeoffAllowance**](TimeoffAllowance.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

