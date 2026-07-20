# F::PerformanceReviewEvaluationScoreApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**performance_review_evaluation_scores_get**](PerformanceReviewEvaluationScoreApi.md#performance_review_evaluation_scores_get) | **GET** /api/2026-07-01/resources/performance/review_evaluation_scores | Reads all Review evaluation scores |
| [**performance_review_evaluation_scores_id_get**](PerformanceReviewEvaluationScoreApi.md#performance_review_evaluation_scores_id_get) | **GET** /api/2026-07-01/resources/performance/review_evaluation_scores/{id} | Reads a single Review evaluation score |


## performance_review_evaluation_scores_get

> <PerformanceReviewEvaluationScoresGet200Response> performance_review_evaluation_scores_get(opts)

Reads all Review evaluation scores

Retrieves the published evaluation scores of performance reviews.

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

api_instance = F::PerformanceReviewEvaluationScoreApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Filter by evaluation score IDs
  review_process_ids: ['inner_example'], # Array<String> | Filter by review process IDs
  review_evaluation_ids: ['inner_example'], # Array<String> | Filter by evaluation IDs
  target_access_ids: ['inner_example'], # Array<String> | Filter by employee access IDs
  reviewer_strategies: ['inner_example'], # Array<String> | Filter by who scored the employee
  review_process_target_ids: ['inner_example'] # Array<String> | Filter by review process target IDs
}

begin
  # Reads all Review evaluation scores
  result = api_instance.performance_review_evaluation_scores_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewEvaluationScoreApi->performance_review_evaluation_scores_get: #{e}"
end
```

#### Using the performance_review_evaluation_scores_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewEvaluationScoresGet200Response>, Integer, Hash)> performance_review_evaluation_scores_get_with_http_info(opts)

```ruby
begin
  # Reads all Review evaluation scores
  data, status_code, headers = api_instance.performance_review_evaluation_scores_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewEvaluationScoresGet200Response>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewEvaluationScoreApi->performance_review_evaluation_scores_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter by evaluation score IDs | [optional] |
| **review_process_ids** | [**Array&lt;String&gt;**](String.md) | Filter by review process IDs | [optional] |
| **review_evaluation_ids** | [**Array&lt;String&gt;**](String.md) | Filter by evaluation IDs | [optional] |
| **target_access_ids** | [**Array&lt;String&gt;**](String.md) | Filter by employee access IDs | [optional] |
| **reviewer_strategies** | [**Array&lt;String&gt;**](String.md) | Filter by who scored the employee | [optional] |
| **review_process_target_ids** | [**Array&lt;String&gt;**](String.md) | Filter by review process target IDs | [optional] |

### Return type

[**PerformanceReviewEvaluationScoresGet200Response**](PerformanceReviewEvaluationScoresGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_review_evaluation_scores_id_get

> <PerformanceReviewEvaluationScore> performance_review_evaluation_scores_id_get(id)

Reads a single Review evaluation score

Retrieves the published evaluation scores of performance reviews.

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

api_instance = F::PerformanceReviewEvaluationScoreApi.new
id = '1' # String | Filter by evaluation score IDs

begin
  # Reads a single Review evaluation score
  result = api_instance.performance_review_evaluation_scores_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewEvaluationScoreApi->performance_review_evaluation_scores_id_get: #{e}"
end
```

#### Using the performance_review_evaluation_scores_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewEvaluationScore>, Integer, Hash)> performance_review_evaluation_scores_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Review evaluation score
  data, status_code, headers = api_instance.performance_review_evaluation_scores_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewEvaluationScore>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewEvaluationScoreApi->performance_review_evaluation_scores_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter by evaluation score IDs |  |

### Return type

[**PerformanceReviewEvaluationScore**](PerformanceReviewEvaluationScore.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

