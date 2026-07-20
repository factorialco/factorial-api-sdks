# F::PerformanceReviewEvaluationAnswerApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**performance_review_evaluation_answers_get**](PerformanceReviewEvaluationAnswerApi.md#performance_review_evaluation_answers_get) | **GET** /api/2026-07-01/resources/performance/review_evaluation_answers | Reads all Review evaluation answers |


## performance_review_evaluation_answers_get

> <PerformanceReviewEvaluationAnswersGet200Response> performance_review_evaluation_answers_get(opts)

Reads all Review evaluation answers

Retrieves the questions and answers of review evaluations.

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

api_instance = F::PerformanceReviewEvaluationAnswerApi.new
opts = {
  performance_review_evaluation_ids: ['inner_example'] # Array<String> | Filter by review evaluation IDs
}

begin
  # Reads all Review evaluation answers
  result = api_instance.performance_review_evaluation_answers_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewEvaluationAnswerApi->performance_review_evaluation_answers_get: #{e}"
end
```

#### Using the performance_review_evaluation_answers_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewEvaluationAnswersGet200Response>, Integer, Hash)> performance_review_evaluation_answers_get_with_http_info(opts)

```ruby
begin
  # Reads all Review evaluation answers
  data, status_code, headers = api_instance.performance_review_evaluation_answers_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewEvaluationAnswersGet200Response>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewEvaluationAnswerApi->performance_review_evaluation_answers_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_evaluation_ids** | [**Array&lt;String&gt;**](String.md) | Filter by review evaluation IDs | [optional] |

### Return type

[**PerformanceReviewEvaluationAnswersGet200Response**](PerformanceReviewEvaluationAnswersGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

