# F::TimePlanningPlannedBreakApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**time_planning_planned_breaks_bulk_create_post**](TimePlanningPlannedBreakApi.md#time_planning_planned_breaks_bulk_create_post) | **POST** /api/2026-07-01/resources/time_planning/planned_breaks/bulk_create | Bulk creates a Planned break |
| [**time_planning_planned_breaks_get**](TimePlanningPlannedBreakApi.md#time_planning_planned_breaks_get) | **GET** /api/2026-07-01/resources/time_planning/planned_breaks | Reads all Planned breaks |
| [**time_planning_planned_breaks_id_get**](TimePlanningPlannedBreakApi.md#time_planning_planned_breaks_id_get) | **GET** /api/2026-07-01/resources/time_planning/planned_breaks/{id} | Reads a single Planned break |


## time_planning_planned_breaks_bulk_create_post

> <Array<TimePlanningPlannedBreak>> time_planning_planned_breaks_bulk_create_post(opts)

Bulk creates a Planned break

Bulk creates a Planned break

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

api_instance = F::TimePlanningPlannedBreakApi.new
opts = {
  time_planning_planned_breaks_bulk_create_post_request: F::TimePlanningPlannedBreaksBulkCreatePostRequest.new({planned_breaks: [{"id": 1, "start_at": "2020-09-07T06: 00: 00.000+00: 00", "end_at": "2020-09-07T15: 00: 00.000+00: 00", "duration": 30, "break_type": "semi_flexible", "break_configuration_id": 1, "shift_id": 1}]}) # TimePlanningPlannedBreaksBulkCreatePostRequest | 
}

begin
  # Bulk creates a Planned break
  result = api_instance.time_planning_planned_breaks_bulk_create_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlannedBreakApi->time_planning_planned_breaks_bulk_create_post: #{e}"
end
```

#### Using the time_planning_planned_breaks_bulk_create_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<TimePlanningPlannedBreak>>, Integer, Hash)> time_planning_planned_breaks_bulk_create_post_with_http_info(opts)

```ruby
begin
  # Bulk creates a Planned break
  data, status_code, headers = api_instance.time_planning_planned_breaks_bulk_create_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<TimePlanningPlannedBreak>>
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlannedBreakApi->time_planning_planned_breaks_bulk_create_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **time_planning_planned_breaks_bulk_create_post_request** | [**TimePlanningPlannedBreaksBulkCreatePostRequest**](TimePlanningPlannedBreaksBulkCreatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;TimePlanningPlannedBreak&gt;**](TimePlanningPlannedBreak.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## time_planning_planned_breaks_get

> <TimePlanningPlannedBreaksGet200Response> time_planning_planned_breaks_get(ids, paid, default_shift_ids, shift_ids, day_configuration_ids, shift_configuration_ids, active_break_configuration)

Reads all Planned breaks

Reads all Planned breaks

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

api_instance = F::TimePlanningPlannedBreakApi.new
ids = ['inner_example'] # Array<String> | List of planned break identifiers
paid = true # Boolean | Filter by paid or unpaid breaks
default_shift_ids = ['inner_example'] # Array<String> | List of default shift identifiers
shift_ids = ['inner_example'] # Array<String> | List of shift identifiers
day_configuration_ids = ['inner_example'] # Array<String> | List of day configuration identifiers
shift_configuration_ids = ['inner_example'] # Array<String> | List of shift configuration identifiers
active_break_configuration = true # Boolean | Filter by active break configurations only

begin
  # Reads all Planned breaks
  result = api_instance.time_planning_planned_breaks_get(ids, paid, default_shift_ids, shift_ids, day_configuration_ids, shift_configuration_ids, active_break_configuration)
  p result
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlannedBreakApi->time_planning_planned_breaks_get: #{e}"
end
```

#### Using the time_planning_planned_breaks_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimePlanningPlannedBreaksGet200Response>, Integer, Hash)> time_planning_planned_breaks_get_with_http_info(ids, paid, default_shift_ids, shift_ids, day_configuration_ids, shift_configuration_ids, active_break_configuration)

```ruby
begin
  # Reads all Planned breaks
  data, status_code, headers = api_instance.time_planning_planned_breaks_get_with_http_info(ids, paid, default_shift_ids, shift_ids, day_configuration_ids, shift_configuration_ids, active_break_configuration)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimePlanningPlannedBreaksGet200Response>
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlannedBreakApi->time_planning_planned_breaks_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | List of planned break identifiers |  |
| **paid** | **Boolean** | Filter by paid or unpaid breaks |  |
| **default_shift_ids** | [**Array&lt;String&gt;**](String.md) | List of default shift identifiers |  |
| **shift_ids** | [**Array&lt;String&gt;**](String.md) | List of shift identifiers |  |
| **day_configuration_ids** | [**Array&lt;String&gt;**](String.md) | List of day configuration identifiers |  |
| **shift_configuration_ids** | [**Array&lt;String&gt;**](String.md) | List of shift configuration identifiers |  |
| **active_break_configuration** | **Boolean** | Filter by active break configurations only |  |

### Return type

[**TimePlanningPlannedBreaksGet200Response**](TimePlanningPlannedBreaksGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## time_planning_planned_breaks_id_get

> <TimePlanningPlannedBreak> time_planning_planned_breaks_id_get(id)

Reads a single Planned break

Reads a single Planned break

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

api_instance = F::TimePlanningPlannedBreakApi.new
id = '1' # String | List of planned break identifiers

begin
  # Reads a single Planned break
  result = api_instance.time_planning_planned_breaks_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlannedBreakApi->time_planning_planned_breaks_id_get: #{e}"
end
```

#### Using the time_planning_planned_breaks_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimePlanningPlannedBreak>, Integer, Hash)> time_planning_planned_breaks_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Planned break
  data, status_code, headers = api_instance.time_planning_planned_breaks_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimePlanningPlannedBreak>
rescue F::ApiError => e
  puts "Error when calling TimePlanningPlannedBreakApi->time_planning_planned_breaks_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | List of planned break identifiers |  |

### Return type

[**TimePlanningPlannedBreak**](TimePlanningPlannedBreak.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

