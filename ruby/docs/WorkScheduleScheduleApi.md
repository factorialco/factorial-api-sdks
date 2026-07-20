# F::WorkScheduleScheduleApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**work_schedule_schedules_get**](WorkScheduleScheduleApi.md#work_schedule_schedules_get) | **GET** /api/2026-07-01/resources/work_schedule/schedules | Reads all Schedules |
| [**work_schedule_schedules_id_get**](WorkScheduleScheduleApi.md#work_schedule_schedules_id_get) | **GET** /api/2026-07-01/resources/work_schedule/schedules/{id} | Reads a single Schedule |
| [**work_schedule_schedules_id_put**](WorkScheduleScheduleApi.md#work_schedule_schedules_id_put) | **PUT** /api/2026-07-01/resources/work_schedule/schedules/{id} | Updates a Schedule |
| [**work_schedule_schedules_post**](WorkScheduleScheduleApi.md#work_schedule_schedules_post) | **POST** /api/2026-07-01/resources/work_schedule/schedules | Creates a Schedule |
| [**work_schedule_schedules_toggle_archive_post**](WorkScheduleScheduleApi.md#work_schedule_schedules_toggle_archive_post) | **POST** /api/2026-07-01/resources/work_schedule/schedules/toggle_archive | Toggle archives a Schedule |


## work_schedule_schedules_get

> <WorkScheduleSchedulesGet200Response> work_schedule_schedules_get(with_employee_ids, with_periods, opts)

Reads all Schedules

Reads all Schedules

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

api_instance = F::WorkScheduleScheduleApi.new
with_employee_ids = true # Boolean | 
with_periods = true # Boolean | 
opts = {
  ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Schedules
  result = api_instance.work_schedule_schedules_get(with_employee_ids, with_periods, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling WorkScheduleScheduleApi->work_schedule_schedules_get: #{e}"
end
```

#### Using the work_schedule_schedules_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkScheduleSchedulesGet200Response>, Integer, Hash)> work_schedule_schedules_get_with_http_info(with_employee_ids, with_periods, opts)

```ruby
begin
  # Reads all Schedules
  data, status_code, headers = api_instance.work_schedule_schedules_get_with_http_info(with_employee_ids, with_periods, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkScheduleSchedulesGet200Response>
rescue F::ApiError => e
  puts "Error when calling WorkScheduleScheduleApi->work_schedule_schedules_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **with_employee_ids** | **Boolean** |  |  |
| **with_periods** | **Boolean** |  |  |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**WorkScheduleSchedulesGet200Response**](WorkScheduleSchedulesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## work_schedule_schedules_id_get

> <WorkScheduleSchedule> work_schedule_schedules_id_get(id)

Reads a single Schedule

Reads a single Schedule

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

api_instance = F::WorkScheduleScheduleApi.new
id = '1' # String | 

begin
  # Reads a single Schedule
  result = api_instance.work_schedule_schedules_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling WorkScheduleScheduleApi->work_schedule_schedules_id_get: #{e}"
end
```

#### Using the work_schedule_schedules_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkScheduleSchedule>, Integer, Hash)> work_schedule_schedules_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Schedule
  data, status_code, headers = api_instance.work_schedule_schedules_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkScheduleSchedule>
rescue F::ApiError => e
  puts "Error when calling WorkScheduleScheduleApi->work_schedule_schedules_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**WorkScheduleSchedule**](WorkScheduleSchedule.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## work_schedule_schedules_id_put

> <WorkScheduleSchedule> work_schedule_schedules_id_put(id, opts)

Updates a Schedule

Updates a Schedule

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

api_instance = F::WorkScheduleScheduleApi.new
id = '1' # String | 
opts = {
  work_schedule_schedules_id_put_request: F::WorkScheduleSchedulesIdPutRequest.new({id: 'id_example'}) # WorkScheduleSchedulesIdPutRequest | 
}

begin
  # Updates a Schedule
  result = api_instance.work_schedule_schedules_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling WorkScheduleScheduleApi->work_schedule_schedules_id_put: #{e}"
end
```

#### Using the work_schedule_schedules_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkScheduleSchedule>, Integer, Hash)> work_schedule_schedules_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Schedule
  data, status_code, headers = api_instance.work_schedule_schedules_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkScheduleSchedule>
rescue F::ApiError => e
  puts "Error when calling WorkScheduleScheduleApi->work_schedule_schedules_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **work_schedule_schedules_id_put_request** | [**WorkScheduleSchedulesIdPutRequest**](WorkScheduleSchedulesIdPutRequest.md) |  | [optional] |

### Return type

[**WorkScheduleSchedule**](WorkScheduleSchedule.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## work_schedule_schedules_post

> <WorkScheduleSchedule> work_schedule_schedules_post(opts)

Creates a Schedule

Creates a Schedule

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

api_instance = F::WorkScheduleScheduleApi.new
opts = {
  work_schedule_schedules_post_request: F::WorkScheduleSchedulesPostRequest.new({name: 'name_example', schedule_type: 'schedule_type_example'}) # WorkScheduleSchedulesPostRequest | 
}

begin
  # Creates a Schedule
  result = api_instance.work_schedule_schedules_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling WorkScheduleScheduleApi->work_schedule_schedules_post: #{e}"
end
```

#### Using the work_schedule_schedules_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkScheduleSchedule>, Integer, Hash)> work_schedule_schedules_post_with_http_info(opts)

```ruby
begin
  # Creates a Schedule
  data, status_code, headers = api_instance.work_schedule_schedules_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkScheduleSchedule>
rescue F::ApiError => e
  puts "Error when calling WorkScheduleScheduleApi->work_schedule_schedules_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **work_schedule_schedules_post_request** | [**WorkScheduleSchedulesPostRequest**](WorkScheduleSchedulesPostRequest.md) |  | [optional] |

### Return type

[**WorkScheduleSchedule**](WorkScheduleSchedule.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## work_schedule_schedules_toggle_archive_post

> <WorkScheduleSchedule> work_schedule_schedules_toggle_archive_post(opts)

Toggle archives a Schedule

Toggle archives a Schedule

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

api_instance = F::WorkScheduleScheduleApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Toggle archives a Schedule
  result = api_instance.work_schedule_schedules_toggle_archive_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling WorkScheduleScheduleApi->work_schedule_schedules_toggle_archive_post: #{e}"
end
```

#### Using the work_schedule_schedules_toggle_archive_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkScheduleSchedule>, Integer, Hash)> work_schedule_schedules_toggle_archive_post_with_http_info(opts)

```ruby
begin
  # Toggle archives a Schedule
  data, status_code, headers = api_instance.work_schedule_schedules_toggle_archive_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkScheduleSchedule>
rescue F::ApiError => e
  puts "Error when calling WorkScheduleScheduleApi->work_schedule_schedules_toggle_archive_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**WorkScheduleSchedule**](WorkScheduleSchedule.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

