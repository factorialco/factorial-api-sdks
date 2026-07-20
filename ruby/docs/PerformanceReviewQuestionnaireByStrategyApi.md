# F::PerformanceReviewQuestionnaireByStrategyApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**performance_review_questionnaire_by_strategies_get**](PerformanceReviewQuestionnaireByStrategyApi.md#performance_review_questionnaire_by_strategies_get) | **GET** /api/2026-07-01/resources/performance/review_questionnaire_by_strategies | Reads all Review questionnaire by strategies |
| [**performance_review_questionnaire_by_strategies_id_get**](PerformanceReviewQuestionnaireByStrategyApi.md#performance_review_questionnaire_by_strategies_id_get) | **GET** /api/2026-07-01/resources/performance/review_questionnaire_by_strategies/{id} | Reads a single Review questionnaire by strategy |
| [**performance_review_questionnaire_by_strategies_update_default_rating_scale_post**](PerformanceReviewQuestionnaireByStrategyApi.md#performance_review_questionnaire_by_strategies_update_default_rating_scale_post) | **POST** /api/2026-07-01/resources/performance/review_questionnaire_by_strategies/update_default_rating_scale | Update default rating scales a Review questionnaire by strategy |
| [**performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_post**](PerformanceReviewQuestionnaireByStrategyApi.md#performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_post) | **POST** /api/2026-07-01/resources/performance/review_questionnaire_by_strategies/update_questionnaire_for_strategy | Update questionnaire for strategies a Review questionnaire by strategy |


## performance_review_questionnaire_by_strategies_get

> <PerformanceReviewQuestionnaireByStrategiesGet200Response> performance_review_questionnaire_by_strategies_get(opts)

Reads all Review questionnaire by strategies

Retrieves the questionnaires by reviewer strategy for review processes.

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

api_instance = F::PerformanceReviewQuestionnaireByStrategyApi.new
opts = {
  ids: ['inner_example'] # Array<String> | Filter by review process IDs
}

begin
  # Reads all Review questionnaire by strategies
  result = api_instance.performance_review_questionnaire_by_strategies_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewQuestionnaireByStrategyApi->performance_review_questionnaire_by_strategies_get: #{e}"
end
```

#### Using the performance_review_questionnaire_by_strategies_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewQuestionnaireByStrategiesGet200Response>, Integer, Hash)> performance_review_questionnaire_by_strategies_get_with_http_info(opts)

```ruby
begin
  # Reads all Review questionnaire by strategies
  data, status_code, headers = api_instance.performance_review_questionnaire_by_strategies_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewQuestionnaireByStrategiesGet200Response>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewQuestionnaireByStrategyApi->performance_review_questionnaire_by_strategies_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter by review process IDs | [optional] |

### Return type

[**PerformanceReviewQuestionnaireByStrategiesGet200Response**](PerformanceReviewQuestionnaireByStrategiesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_review_questionnaire_by_strategies_id_get

> <PerformanceReviewQuestionnairesByStrategy> performance_review_questionnaire_by_strategies_id_get(id)

Reads a single Review questionnaire by strategy

Retrieves the questionnaires by reviewer strategy for review processes.

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

api_instance = F::PerformanceReviewQuestionnaireByStrategyApi.new
id = '1' # String | Filter by review process IDs

begin
  # Reads a single Review questionnaire by strategy
  result = api_instance.performance_review_questionnaire_by_strategies_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewQuestionnaireByStrategyApi->performance_review_questionnaire_by_strategies_id_get: #{e}"
end
```

#### Using the performance_review_questionnaire_by_strategies_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewQuestionnairesByStrategy>, Integer, Hash)> performance_review_questionnaire_by_strategies_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Review questionnaire by strategy
  data, status_code, headers = api_instance.performance_review_questionnaire_by_strategies_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewQuestionnairesByStrategy>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewQuestionnaireByStrategyApi->performance_review_questionnaire_by_strategies_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter by review process IDs |  |

### Return type

[**PerformanceReviewQuestionnairesByStrategy**](PerformanceReviewQuestionnairesByStrategy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_review_questionnaire_by_strategies_update_default_rating_scale_post

> <PerformanceReviewQuestionnairesByStrategy> performance_review_questionnaire_by_strategies_update_default_rating_scale_post(opts)

Update default rating scales a Review questionnaire by strategy

Update the scoring range used in rating questions for all reviewer strategies.

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

api_instance = F::PerformanceReviewQuestionnaireByStrategyApi.new
opts = {
  performance_review_questionnaire_by_strategies_update_default_rating_scale_post_request: F::PerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatingScalePostRequest.new({performance_review_process_id: '1', default_rating_scale: [{"value": 1, "text": "Poor"}, {"value": 2, "text": "Inconsistent"}, {"value": 3, "text": "Meets expectations"}, {"value": 4, "text": "Exceeds expectations"}, {"value": 5, "text": "Exceptional"}]}) # PerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatingScalePostRequest | 
}

begin
  # Update default rating scales a Review questionnaire by strategy
  result = api_instance.performance_review_questionnaire_by_strategies_update_default_rating_scale_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewQuestionnaireByStrategyApi->performance_review_questionnaire_by_strategies_update_default_rating_scale_post: #{e}"
end
```

#### Using the performance_review_questionnaire_by_strategies_update_default_rating_scale_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewQuestionnairesByStrategy>, Integer, Hash)> performance_review_questionnaire_by_strategies_update_default_rating_scale_post_with_http_info(opts)

```ruby
begin
  # Update default rating scales a Review questionnaire by strategy
  data, status_code, headers = api_instance.performance_review_questionnaire_by_strategies_update_default_rating_scale_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewQuestionnairesByStrategy>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewQuestionnaireByStrategyApi->performance_review_questionnaire_by_strategies_update_default_rating_scale_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_questionnaire_by_strategies_update_default_rating_scale_post_request** | [**PerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatingScalePostRequest**](PerformanceReviewQuestionnaireByStrategiesUpdateDefaultRatingScalePostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewQuestionnairesByStrategy**](PerformanceReviewQuestionnairesByStrategy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_post

> <PerformanceReviewQuestionnairesByStrategy> performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_post(opts)

Update questionnaire for strategies a Review questionnaire by strategy

Update the review process questionnaire for a specific reviewer strategy (review type). It can be used to add, edit or delete questions from a draft review process.

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

api_instance = F::PerformanceReviewQuestionnaireByStrategyApi.new
opts = {
  performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_post_request: F::PerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyPostRequest.new({performance_review_process_id: '1', strategy: 'self', questionnaire_content: [{"uuid": "b69c9b4d-0aa6-4ada-89d5-5fdcb04c1327", "type": "section", "section_title": "Performance", "questions": [{"uuid": "a347a2fd-1a0a-4eee-b6c8-f74be63624fb", "mandatory": true, "with_comment": true, "title": "How would you rate the commitment of the employee?", "answer_type": "rating"}, {"uuid": "a922bd33-e9c8-4856-87c6-92eb895f4271", "mandatory": true, "with_comment": false, "title": "What are the strengths of the employee?", "answer_type": "text"}]}, {"uuid": "26f26623-043f-4110-a5cb-1fd54a69626f", "type": "question", "questions": [{"uuid": "84ba99f3-4e4f-4917-a2af-6d0aa8c2e0f2", "mandatory": true, "with_comment": false, "title": "Do you think the employee is a team player?", "answer_type": "multiple_choice", "max_choices": 1, "choice_options": ["Yes", "No"]}]}]}) # PerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyPostRequest | 
}

begin
  # Update questionnaire for strategies a Review questionnaire by strategy
  result = api_instance.performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewQuestionnaireByStrategyApi->performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_post: #{e}"
end
```

#### Using the performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewQuestionnairesByStrategy>, Integer, Hash)> performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_post_with_http_info(opts)

```ruby
begin
  # Update questionnaire for strategies a Review questionnaire by strategy
  data, status_code, headers = api_instance.performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewQuestionnairesByStrategy>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewQuestionnaireByStrategyApi->performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_questionnaire_by_strategies_update_questionnaire_for_strategy_post_request** | [**PerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyPostRequest**](PerformanceReviewQuestionnaireByStrategiesUpdateQuestionnaireForStrategyPostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewQuestionnairesByStrategy**](PerformanceReviewQuestionnairesByStrategy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

