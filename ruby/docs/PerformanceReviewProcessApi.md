# F::PerformanceReviewProcessApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**performance_review_processes_create_from_template_post**](PerformanceReviewProcessApi.md#performance_review_processes_create_from_template_post) | **POST** /api/2026-07-01/resources/performance/review_processes/create_from_template | Create from templates a Review process |
| [**performance_review_processes_duplicate_post**](PerformanceReviewProcessApi.md#performance_review_processes_duplicate_post) | **POST** /api/2026-07-01/resources/performance/review_processes/duplicate | Duplicates a Review process |
| [**performance_review_processes_get**](PerformanceReviewProcessApi.md#performance_review_processes_get) | **GET** /api/2026-07-01/resources/performance/review_processes | Reads all Review processes |
| [**performance_review_processes_id_delete**](PerformanceReviewProcessApi.md#performance_review_processes_id_delete) | **DELETE** /api/2026-07-01/resources/performance/review_processes/{id} | Deletes a Review process |
| [**performance_review_processes_id_get**](PerformanceReviewProcessApi.md#performance_review_processes_id_get) | **GET** /api/2026-07-01/resources/performance/review_processes/{id} | Reads a single Review process |
| [**performance_review_processes_post**](PerformanceReviewProcessApi.md#performance_review_processes_post) | **POST** /api/2026-07-01/resources/performance/review_processes | Creates a Review process |
| [**performance_review_processes_remind_in_bulk_post**](PerformanceReviewProcessApi.md#performance_review_processes_remind_in_bulk_post) | **POST** /api/2026-07-01/resources/performance/review_processes/remind_in_bulk | Remind in bulks a Review process |
| [**performance_review_processes_remove_schedule_post**](PerformanceReviewProcessApi.md#performance_review_processes_remove_schedule_post) | **POST** /api/2026-07-01/resources/performance/review_processes/remove_schedule | Remove schedules a Review process |
| [**performance_review_processes_reopen_post**](PerformanceReviewProcessApi.md#performance_review_processes_reopen_post) | **POST** /api/2026-07-01/resources/performance/review_processes/reopen | Reopens a Review process |
| [**performance_review_processes_schedule_post**](PerformanceReviewProcessApi.md#performance_review_processes_schedule_post) | **POST** /api/2026-07-01/resources/performance/review_processes/schedule | Schedules a Review process |
| [**performance_review_processes_start_post**](PerformanceReviewProcessApi.md#performance_review_processes_start_post) | **POST** /api/2026-07-01/resources/performance/review_processes/start | Starts a Review process |
| [**performance_review_processes_stop_post**](PerformanceReviewProcessApi.md#performance_review_processes_stop_post) | **POST** /api/2026-07-01/resources/performance/review_processes/stop | Stops a Review process |
| [**performance_review_processes_toggle_archive_post**](PerformanceReviewProcessApi.md#performance_review_processes_toggle_archive_post) | **POST** /api/2026-07-01/resources/performance/review_processes/toggle_archive | Toggle archives a Review process |
| [**performance_review_processes_update_agreements_configuration_post**](PerformanceReviewProcessApi.md#performance_review_processes_update_agreements_configuration_post) | **POST** /api/2026-07-01/resources/performance/review_processes/update_agreements_configuration | Update agreements configurations a Review process |
| [**performance_review_processes_update_basic_info_post**](PerformanceReviewProcessApi.md#performance_review_processes_update_basic_info_post) | **POST** /api/2026-07-01/resources/performance/review_processes/update_basic_info | Update basic infos a Review process |
| [**performance_review_processes_update_competencies_assessments_configuration_post**](PerformanceReviewProcessApi.md#performance_review_processes_update_competencies_assessments_configuration_post) | **POST** /api/2026-07-01/resources/performance/review_processes/update_competencies_assessments_configuration | Update competencies assessments configurations a Review process |
| [**performance_review_processes_update_deadline_post**](PerformanceReviewProcessApi.md#performance_review_processes_update_deadline_post) | **POST** /api/2026-07-01/resources/performance/review_processes/update_deadline | Update deadlines a Review process |
| [**performance_review_processes_update_employee_score_configuration_post**](PerformanceReviewProcessApi.md#performance_review_processes_update_employee_score_configuration_post) | **POST** /api/2026-07-01/resources/performance/review_processes/update_employee_score_configuration | Update employee score configurations a Review process |
| [**performance_review_processes_update_reviewer_strategies_post**](PerformanceReviewProcessApi.md#performance_review_processes_update_reviewer_strategies_post) | **POST** /api/2026-07-01/resources/performance/review_processes/update_reviewer_strategies | Update reviewer strategies a Review process |
| [**performance_review_processes_update_schedule_post**](PerformanceReviewProcessApi.md#performance_review_processes_update_schedule_post) | **POST** /api/2026-07-01/resources/performance/review_processes/update_schedule | Update schedules a Review process |
| [**performance_review_processes_update_target_strategy_post**](PerformanceReviewProcessApi.md#performance_review_processes_update_target_strategy_post) | **POST** /api/2026-07-01/resources/performance/review_processes/update_target_strategy | Update target strategies a Review process |


## performance_review_processes_create_from_template_post

> <PerformanceReviewProcess> performance_review_processes_create_from_template_post(opts)

Create from templates a Review process

Create a new review process from a template.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  performance_review_processes_create_from_template_post_request: F::PerformanceReviewProcessesCreateFromTemplatePostRequest.new({author_access_id: '1', template_id: '1', template_type: 'predefined'}) # PerformanceReviewProcessesCreateFromTemplatePostRequest | 
}

begin
  # Create from templates a Review process
  result = api_instance.performance_review_processes_create_from_template_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_create_from_template_post: #{e}"
end
```

#### Using the performance_review_processes_create_from_template_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_create_from_template_post_with_http_info(opts)

```ruby
begin
  # Create from templates a Review process
  data, status_code, headers = api_instance.performance_review_processes_create_from_template_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_create_from_template_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_processes_create_from_template_post_request** | [**PerformanceReviewProcessesCreateFromTemplatePostRequest**](PerformanceReviewProcessesCreateFromTemplatePostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_duplicate_post

> <PerformanceReviewProcess> performance_review_processes_duplicate_post(opts)

Duplicates a Review process

Duplicate an existing review process

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  performance_review_processes_duplicate_post_request: F::PerformanceReviewProcessesDuplicatePostRequest.new({id: '1', author_access_id: '1'}) # PerformanceReviewProcessesDuplicatePostRequest | 
}

begin
  # Duplicates a Review process
  result = api_instance.performance_review_processes_duplicate_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_duplicate_post: #{e}"
end
```

#### Using the performance_review_processes_duplicate_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_duplicate_post_with_http_info(opts)

```ruby
begin
  # Duplicates a Review process
  data, status_code, headers = api_instance.performance_review_processes_duplicate_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_duplicate_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_processes_duplicate_post_request** | [**PerformanceReviewProcessesDuplicatePostRequest**](PerformanceReviewProcessesDuplicatePostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_get

> <PerformanceReviewProcessesGet200Response> performance_review_processes_get(opts)

Reads all Review processes

Reads all Review processes

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Filter by review process IDs
  search: '2024' # String | Filter by review process name
}

begin
  # Reads all Review processes
  result = api_instance.performance_review_processes_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_get: #{e}"
end
```

#### Using the performance_review_processes_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcessesGet200Response>, Integer, Hash)> performance_review_processes_get_with_http_info(opts)

```ruby
begin
  # Reads all Review processes
  data, status_code, headers = api_instance.performance_review_processes_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcessesGet200Response>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter by review process IDs | [optional] |
| **search** | **String** | Filter by review process name | [optional] |

### Return type

[**PerformanceReviewProcessesGet200Response**](PerformanceReviewProcessesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_review_processes_id_delete

> <PerformanceReviewProcess> performance_review_processes_id_delete(id)

Deletes a Review process

Delete an existing review process.

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

api_instance = F::PerformanceReviewProcessApi.new
id = '1' # String | Review process ID

begin
  # Deletes a Review process
  result = api_instance.performance_review_processes_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_id_delete: #{e}"
end
```

#### Using the performance_review_processes_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Review process
  data, status_code, headers = api_instance.performance_review_processes_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process ID |  |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_review_processes_id_get

> <PerformanceReviewProcess> performance_review_processes_id_get(id)

Reads a single Review process

Reads a single Review process

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

api_instance = F::PerformanceReviewProcessApi.new
id = '1' # String | Filter by review process IDs

begin
  # Reads a single Review process
  result = api_instance.performance_review_processes_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_id_get: #{e}"
end
```

#### Using the performance_review_processes_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Review process
  data, status_code, headers = api_instance.performance_review_processes_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter by review process IDs |  |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_review_processes_post

> <PerformanceReviewProcess> performance_review_processes_post(opts)

Creates a Review process

Create a new review process.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  performance_review_processes_post_request: F::PerformanceReviewProcessesPostRequest.new({author_access_id: '1'}) # PerformanceReviewProcessesPostRequest | 
}

begin
  # Creates a Review process
  result = api_instance.performance_review_processes_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_post: #{e}"
end
```

#### Using the performance_review_processes_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_post_with_http_info(opts)

```ruby
begin
  # Creates a Review process
  data, status_code, headers = api_instance.performance_review_processes_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_processes_post_request** | [**PerformanceReviewProcessesPostRequest**](PerformanceReviewProcessesPostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_remind_in_bulk_post

> <PerformanceReviewProcess> performance_review_processes_remind_in_bulk_post(opts)

Remind in bulks a Review process

Send bulk reminders to the reviewers that haven't answered their evaluations in a review process.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  performance_review_processes_remind_in_bulk_post_request: F::PerformanceReviewProcessesRemindInBulkPostRequest.new({id: '1'}) # PerformanceReviewProcessesRemindInBulkPostRequest | 
}

begin
  # Remind in bulks a Review process
  result = api_instance.performance_review_processes_remind_in_bulk_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_remind_in_bulk_post: #{e}"
end
```

#### Using the performance_review_processes_remind_in_bulk_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_remind_in_bulk_post_with_http_info(opts)

```ruby
begin
  # Remind in bulks a Review process
  data, status_code, headers = api_instance.performance_review_processes_remind_in_bulk_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_remind_in_bulk_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_processes_remind_in_bulk_post_request** | [**PerformanceReviewProcessesRemindInBulkPostRequest**](PerformanceReviewProcessesRemindInBulkPostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_remove_schedule_post

> <PerformanceReviewProcess> performance_review_processes_remove_schedule_post(opts)

Remove schedules a Review process

Removes the schedule job for a review process. This is only allowed if the process is scheduled.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Remove schedules a Review process
  result = api_instance.performance_review_processes_remove_schedule_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_remove_schedule_post: #{e}"
end
```

#### Using the performance_review_processes_remove_schedule_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_remove_schedule_post_with_http_info(opts)

```ruby
begin
  # Remove schedules a Review process
  data, status_code, headers = api_instance.performance_review_processes_remove_schedule_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_remove_schedule_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_reopen_post

> <PerformanceReviewProcess> performance_review_processes_reopen_post(opts)

Reopens a Review process

Reopen a finished review process.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  performance_review_processes_reopen_post_request: F::PerformanceReviewProcessesReopenPostRequest.new({id: '1', ends_at: '2024-04-01T00:00:00Z'}) # PerformanceReviewProcessesReopenPostRequest | 
}

begin
  # Reopens a Review process
  result = api_instance.performance_review_processes_reopen_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_reopen_post: #{e}"
end
```

#### Using the performance_review_processes_reopen_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_reopen_post_with_http_info(opts)

```ruby
begin
  # Reopens a Review process
  data, status_code, headers = api_instance.performance_review_processes_reopen_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_reopen_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_processes_reopen_post_request** | [**PerformanceReviewProcessesReopenPostRequest**](PerformanceReviewProcessesReopenPostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_schedule_post

> <PerformanceReviewProcess> performance_review_processes_schedule_post(opts)

Schedules a Review process

Schedule a review process to start at a given date. This is only allowed if the process is in draft.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  performance_review_processes_schedule_post_request: F::PerformanceReviewProcessesSchedulePostRequest.new({id: '1', starts_at: '2024-01-01T00:00:00Z'}) # PerformanceReviewProcessesSchedulePostRequest | 
}

begin
  # Schedules a Review process
  result = api_instance.performance_review_processes_schedule_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_schedule_post: #{e}"
end
```

#### Using the performance_review_processes_schedule_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_schedule_post_with_http_info(opts)

```ruby
begin
  # Schedules a Review process
  data, status_code, headers = api_instance.performance_review_processes_schedule_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_schedule_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_processes_schedule_post_request** | [**PerformanceReviewProcessesSchedulePostRequest**](PerformanceReviewProcessesSchedulePostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_start_post

> <PerformanceReviewProcess> performance_review_processes_start_post(opts)

Starts a Review process

Start a review process. This is only allowed if the process is in draft or scheduled.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Starts a Review process
  result = api_instance.performance_review_processes_start_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_start_post: #{e}"
end
```

#### Using the performance_review_processes_start_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_start_post_with_http_info(opts)

```ruby
begin
  # Starts a Review process
  data, status_code, headers = api_instance.performance_review_processes_start_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_start_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_stop_post

> <PerformanceReviewProcess> performance_review_processes_stop_post(opts)

Stops a Review process

Stop a review process.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Stops a Review process
  result = api_instance.performance_review_processes_stop_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_stop_post: #{e}"
end
```

#### Using the performance_review_processes_stop_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_stop_post_with_http_info(opts)

```ruby
begin
  # Stops a Review process
  data, status_code, headers = api_instance.performance_review_processes_stop_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_stop_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_toggle_archive_post

> <PerformanceReviewProcess> performance_review_processes_toggle_archive_post(opts)

Toggle archives a Review process

Archive or unarchive a review process

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Toggle archives a Review process
  result = api_instance.performance_review_processes_toggle_archive_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_toggle_archive_post: #{e}"
end
```

#### Using the performance_review_processes_toggle_archive_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_toggle_archive_post_with_http_info(opts)

```ruby
begin
  # Toggle archives a Review process
  data, status_code, headers = api_instance.performance_review_processes_toggle_archive_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_toggle_archive_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_update_agreements_configuration_post

> <PerformanceReviewProcess> performance_review_processes_update_agreements_configuration_post(opts)

Update agreements configurations a Review process

Enable or disable action plans in a review process.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  performance_review_processes_update_agreements_configuration_post_request: F::PerformanceReviewProcessesUpdateAgreementsConfigurationPostRequest.new({id: '1', enabled: true}) # PerformanceReviewProcessesUpdateAgreementsConfigurationPostRequest | 
}

begin
  # Update agreements configurations a Review process
  result = api_instance.performance_review_processes_update_agreements_configuration_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_agreements_configuration_post: #{e}"
end
```

#### Using the performance_review_processes_update_agreements_configuration_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_update_agreements_configuration_post_with_http_info(opts)

```ruby
begin
  # Update agreements configurations a Review process
  data, status_code, headers = api_instance.performance_review_processes_update_agreements_configuration_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_agreements_configuration_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_processes_update_agreements_configuration_post_request** | [**PerformanceReviewProcessesUpdateAgreementsConfigurationPostRequest**](PerformanceReviewProcessesUpdateAgreementsConfigurationPostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_update_basic_info_post

> <PerformanceReviewProcess> performance_review_processes_update_basic_info_post(opts)

Update basic infos a Review process

Update the basic information of an existing review process.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  performance_review_processes_update_basic_info_post_request: F::PerformanceReviewProcessesUpdateBasicInfoPostRequest.new({id: '1'}) # PerformanceReviewProcessesUpdateBasicInfoPostRequest | 
}

begin
  # Update basic infos a Review process
  result = api_instance.performance_review_processes_update_basic_info_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_basic_info_post: #{e}"
end
```

#### Using the performance_review_processes_update_basic_info_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_update_basic_info_post_with_http_info(opts)

```ruby
begin
  # Update basic infos a Review process
  data, status_code, headers = api_instance.performance_review_processes_update_basic_info_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_basic_info_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_processes_update_basic_info_post_request** | [**PerformanceReviewProcessesUpdateBasicInfoPostRequest**](PerformanceReviewProcessesUpdateBasicInfoPostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_update_competencies_assessments_configuration_post

> <PerformanceReviewProcess> performance_review_processes_update_competencies_assessments_configuration_post(opts)

Update competencies assessments configurations a Review process

Allows to assess employees based on their assigned competencies through both manager and self-reviews.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  performance_review_processes_update_agreements_configuration_post_request: F::PerformanceReviewProcessesUpdateAgreementsConfigurationPostRequest.new({id: '1', enabled: true}) # PerformanceReviewProcessesUpdateAgreementsConfigurationPostRequest | 
}

begin
  # Update competencies assessments configurations a Review process
  result = api_instance.performance_review_processes_update_competencies_assessments_configuration_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_competencies_assessments_configuration_post: #{e}"
end
```

#### Using the performance_review_processes_update_competencies_assessments_configuration_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_update_competencies_assessments_configuration_post_with_http_info(opts)

```ruby
begin
  # Update competencies assessments configurations a Review process
  data, status_code, headers = api_instance.performance_review_processes_update_competencies_assessments_configuration_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_competencies_assessments_configuration_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_processes_update_agreements_configuration_post_request** | [**PerformanceReviewProcessesUpdateAgreementsConfigurationPostRequest**](PerformanceReviewProcessesUpdateAgreementsConfigurationPostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_update_deadline_post

> <PerformanceReviewProcess> performance_review_processes_update_deadline_post(opts)

Update deadlines a Review process

Update the deadline of a review process.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  performance_review_processes_reopen_post_request: F::PerformanceReviewProcessesReopenPostRequest.new({id: '1', ends_at: '2024-04-01T00:00:00Z'}) # PerformanceReviewProcessesReopenPostRequest | 
}

begin
  # Update deadlines a Review process
  result = api_instance.performance_review_processes_update_deadline_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_deadline_post: #{e}"
end
```

#### Using the performance_review_processes_update_deadline_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_update_deadline_post_with_http_info(opts)

```ruby
begin
  # Update deadlines a Review process
  data, status_code, headers = api_instance.performance_review_processes_update_deadline_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_deadline_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_processes_reopen_post_request** | [**PerformanceReviewProcessesReopenPostRequest**](PerformanceReviewProcessesReopenPostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_update_employee_score_configuration_post

> <PerformanceReviewProcess> performance_review_processes_update_employee_score_configuration_post(opts)

Update employee score configurations a Review process

Includes or not one question at the end of the review to rate participants' performance.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  performance_review_processes_update_agreements_configuration_post_request: F::PerformanceReviewProcessesUpdateAgreementsConfigurationPostRequest.new({id: '1', enabled: true}) # PerformanceReviewProcessesUpdateAgreementsConfigurationPostRequest | 
}

begin
  # Update employee score configurations a Review process
  result = api_instance.performance_review_processes_update_employee_score_configuration_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_employee_score_configuration_post: #{e}"
end
```

#### Using the performance_review_processes_update_employee_score_configuration_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_update_employee_score_configuration_post_with_http_info(opts)

```ruby
begin
  # Update employee score configurations a Review process
  data, status_code, headers = api_instance.performance_review_processes_update_employee_score_configuration_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_employee_score_configuration_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_processes_update_agreements_configuration_post_request** | [**PerformanceReviewProcessesUpdateAgreementsConfigurationPostRequest**](PerformanceReviewProcessesUpdateAgreementsConfigurationPostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_update_reviewer_strategies_post

> <PerformanceReviewProcess> performance_review_processes_update_reviewer_strategies_post(opts)

Update reviewer strategies a Review process

Update the review types of a review process. This is only allowed while the process is in draft.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  performance_review_processes_update_reviewer_strategies_post_request: F::PerformanceReviewProcessesUpdateReviewerStrategiesPostRequest.new({id: '1', reviewer_strategies: ["self", "manager"]}) # PerformanceReviewProcessesUpdateReviewerStrategiesPostRequest | 
}

begin
  # Update reviewer strategies a Review process
  result = api_instance.performance_review_processes_update_reviewer_strategies_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_reviewer_strategies_post: #{e}"
end
```

#### Using the performance_review_processes_update_reviewer_strategies_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_update_reviewer_strategies_post_with_http_info(opts)

```ruby
begin
  # Update reviewer strategies a Review process
  data, status_code, headers = api_instance.performance_review_processes_update_reviewer_strategies_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_reviewer_strategies_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_processes_update_reviewer_strategies_post_request** | [**PerformanceReviewProcessesUpdateReviewerStrategiesPostRequest**](PerformanceReviewProcessesUpdateReviewerStrategiesPostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_update_schedule_post

> <PerformanceReviewProcess> performance_review_processes_update_schedule_post(opts)

Update schedules a Review process

Update the starting date of a scheduled review process. This is only allowed if the process is scheduled.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  performance_review_processes_schedule_post_request: F::PerformanceReviewProcessesSchedulePostRequest.new({id: '1', starts_at: '2024-01-01T00:00:00Z'}) # PerformanceReviewProcessesSchedulePostRequest | 
}

begin
  # Update schedules a Review process
  result = api_instance.performance_review_processes_update_schedule_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_schedule_post: #{e}"
end
```

#### Using the performance_review_processes_update_schedule_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_update_schedule_post_with_http_info(opts)

```ruby
begin
  # Update schedules a Review process
  data, status_code, headers = api_instance.performance_review_processes_update_schedule_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_schedule_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_processes_schedule_post_request** | [**PerformanceReviewProcessesSchedulePostRequest**](PerformanceReviewProcessesSchedulePostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_processes_update_target_strategy_post

> <PerformanceReviewProcess> performance_review_processes_update_target_strategy_post(opts)

Update target strategies a Review process

Update the criteria for calculating the participants of a review process. This is only allowed while the process is in draft.

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

api_instance = F::PerformanceReviewProcessApi.new
opts = {
  performance_review_processes_update_target_strategy_post_request: F::PerformanceReviewProcessesUpdateTargetStrategyPostRequest.new({id: '1'}) # PerformanceReviewProcessesUpdateTargetStrategyPostRequest | 
}

begin
  # Update target strategies a Review process
  result = api_instance.performance_review_processes_update_target_strategy_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_target_strategy_post: #{e}"
end
```

#### Using the performance_review_processes_update_target_strategy_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcess>, Integer, Hash)> performance_review_processes_update_target_strategy_post_with_http_info(opts)

```ruby
begin
  # Update target strategies a Review process
  data, status_code, headers = api_instance.performance_review_processes_update_target_strategy_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcess>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessApi->performance_review_processes_update_target_strategy_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_processes_update_target_strategy_post_request** | [**PerformanceReviewProcessesUpdateTargetStrategyPostRequest**](PerformanceReviewProcessesUpdateTargetStrategyPostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcess**](PerformanceReviewProcess.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

