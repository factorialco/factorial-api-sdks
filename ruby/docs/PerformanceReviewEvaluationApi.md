# F::PerformanceReviewEvaluationApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**performance_review_evaluations_get**](PerformanceReviewEvaluationApi.md#performance_review_evaluations_get) | **GET** /api/2026-07-01/resources/performance/review_evaluations | Reads all Review evaluations |
| [**performance_review_evaluations_id_get**](PerformanceReviewEvaluationApi.md#performance_review_evaluations_id_get) | **GET** /api/2026-07-01/resources/performance/review_evaluations/{id} | Reads a single Review evaluation |
| [**performance_review_evaluations_replace_reviewer_post**](PerformanceReviewEvaluationApi.md#performance_review_evaluations_replace_reviewer_post) | **POST** /api/2026-07-01/resources/performance/review_evaluations/replace_reviewer | Replace reviewers a Review evaluation |


## performance_review_evaluations_get

> <PerformanceReviewEvaluationsGet200Response> performance_review_evaluations_get(opts)

Reads all Review evaluations

Retrieves the pending and published review evaluations. The evaluations are created based on the participants and the review types when the review process is started.  For example, if the defined review types are \"self-review\" and \"manager review,\" two evaluations will be created for each participant when the review process starts. One will be for the self-review, where the participant is both the target and the reviewer. The other will be for the manager review, where the participant is the target, and the manager is the reviewer.

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

api_instance = F::PerformanceReviewEvaluationApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Filter by evaluation IDs
  performance_review_process_ids: ['inner_example'], # Array<String> | Filter by review process IDs
  published: true, # Boolean | Only published or unpublished evaluations
  reviewer_ids: ['inner_example'], # Array<String> | Filter by reviewer access IDs
  reviewer_strategies: ['inner_example'], # Array<String> | Filter by reviewer strategies
  target_access_ids: ['inner_example'], # Array<String> | Filter by participant access IDs
  review_process_target_ids: ['inner_example'], # Array<String> | Filter by review process target IDs. Composite key format: review_process_id-target_access_id
  with_targets_managed_by_filter: F::PerformanceReviewEvaluationsGetWithTargetsManagedByFilterParameter.new({manager_employee_id: 'manager_employee_id_example', only_direct_reports: false}), # PerformanceReviewEvaluationsGetWithTargetsManagedByFilterParameter | Only evaluations where the participant is managed by the specified employee ID
  exclude_ids: ['inner_example'] # Array<String> | Exclude evaluations by IDs
}

begin
  # Reads all Review evaluations
  result = api_instance.performance_review_evaluations_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewEvaluationApi->performance_review_evaluations_get: #{e}"
end
```

#### Using the performance_review_evaluations_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewEvaluationsGet200Response>, Integer, Hash)> performance_review_evaluations_get_with_http_info(opts)

```ruby
begin
  # Reads all Review evaluations
  data, status_code, headers = api_instance.performance_review_evaluations_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewEvaluationsGet200Response>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewEvaluationApi->performance_review_evaluations_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter by evaluation IDs | [optional] |
| **performance_review_process_ids** | [**Array&lt;String&gt;**](String.md) | Filter by review process IDs | [optional] |
| **published** | **Boolean** | Only published or unpublished evaluations | [optional] |
| **reviewer_ids** | [**Array&lt;String&gt;**](String.md) | Filter by reviewer access IDs | [optional] |
| **reviewer_strategies** | [**Array&lt;String&gt;**](String.md) | Filter by reviewer strategies | [optional] |
| **target_access_ids** | [**Array&lt;String&gt;**](String.md) | Filter by participant access IDs | [optional] |
| **review_process_target_ids** | [**Array&lt;String&gt;**](String.md) | Filter by review process target IDs. Composite key format: review_process_id-target_access_id | [optional] |
| **with_targets_managed_by_filter** | [**PerformanceReviewEvaluationsGetWithTargetsManagedByFilterParameter**](.md) | Only evaluations where the participant is managed by the specified employee ID | [optional] |
| **exclude_ids** | [**Array&lt;String&gt;**](String.md) | Exclude evaluations by IDs | [optional] |

### Return type

[**PerformanceReviewEvaluationsGet200Response**](PerformanceReviewEvaluationsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_review_evaluations_id_get

> <PerformanceReviewEvaluation> performance_review_evaluations_id_get(id)

Reads a single Review evaluation

Retrieves the pending and published review evaluations. The evaluations are created based on the participants and the review types when the review process is started.  For example, if the defined review types are \"self-review\" and \"manager review,\" two evaluations will be created for each participant when the review process starts. One will be for the self-review, where the participant is both the target and the reviewer. The other will be for the manager review, where the participant is the target, and the manager is the reviewer.

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

api_instance = F::PerformanceReviewEvaluationApi.new
id = '1' # String | Filter by evaluation IDs

begin
  # Reads a single Review evaluation
  result = api_instance.performance_review_evaluations_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewEvaluationApi->performance_review_evaluations_id_get: #{e}"
end
```

#### Using the performance_review_evaluations_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewEvaluation>, Integer, Hash)> performance_review_evaluations_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Review evaluation
  data, status_code, headers = api_instance.performance_review_evaluations_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewEvaluation>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewEvaluationApi->performance_review_evaluations_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter by evaluation IDs |  |

### Return type

[**PerformanceReviewEvaluation**](PerformanceReviewEvaluation.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_review_evaluations_replace_reviewer_post

> <PerformanceReviewEvaluation> performance_review_evaluations_replace_reviewer_post(opts)

Replace reviewers a Review evaluation

Define a new reviewer for the evaluation that will only be able to leave feedback about the employee. This can only be done if the process is active, the evaluation is not published and the evaluation type is not \"self\".

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

api_instance = F::PerformanceReviewEvaluationApi.new
opts = {
  performance_review_evaluations_replace_reviewer_post_request: F::PerformanceReviewEvaluationsReplaceReviewerPostRequest.new({id: '1', new_reviewer_access_id: '5'}) # PerformanceReviewEvaluationsReplaceReviewerPostRequest | 
}

begin
  # Replace reviewers a Review evaluation
  result = api_instance.performance_review_evaluations_replace_reviewer_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewEvaluationApi->performance_review_evaluations_replace_reviewer_post: #{e}"
end
```

#### Using the performance_review_evaluations_replace_reviewer_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewEvaluation>, Integer, Hash)> performance_review_evaluations_replace_reviewer_post_with_http_info(opts)

```ruby
begin
  # Replace reviewers a Review evaluation
  data, status_code, headers = api_instance.performance_review_evaluations_replace_reviewer_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewEvaluation>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewEvaluationApi->performance_review_evaluations_replace_reviewer_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_evaluations_replace_reviewer_post_request** | [**PerformanceReviewEvaluationsReplaceReviewerPostRequest**](PerformanceReviewEvaluationsReplaceReviewerPostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewEvaluation**](PerformanceReviewEvaluation.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

