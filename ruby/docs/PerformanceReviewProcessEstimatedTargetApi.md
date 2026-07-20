# F::PerformanceReviewProcessEstimatedTargetApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**performance_review_process_estimated_targets_get**](PerformanceReviewProcessEstimatedTargetApi.md#performance_review_process_estimated_targets_get) | **GET** /api/2026-07-01/resources/performance/review_process_estimated_targets | Reads all Review process estimated targets |


## performance_review_process_estimated_targets_get

> <PerformanceReviewProcessEstimatedTargetsGet200Response> performance_review_process_estimated_targets_get(opts)

Reads all Review process estimated targets

Retrieve review process estimated target before the review process is launched

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

api_instance = F::PerformanceReviewProcessEstimatedTargetApi.new
opts = {
  performance_review_process_ids: ['inner_example'], # Array<String> | Filter by review process IDs
  access_ids: ['inner_example'] # Array<String> | Filter by access IDs
}

begin
  # Reads all Review process estimated targets
  result = api_instance.performance_review_process_estimated_targets_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessEstimatedTargetApi->performance_review_process_estimated_targets_get: #{e}"
end
```

#### Using the performance_review_process_estimated_targets_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcessEstimatedTargetsGet200Response>, Integer, Hash)> performance_review_process_estimated_targets_get_with_http_info(opts)

```ruby
begin
  # Reads all Review process estimated targets
  data, status_code, headers = api_instance.performance_review_process_estimated_targets_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcessEstimatedTargetsGet200Response>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessEstimatedTargetApi->performance_review_process_estimated_targets_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_process_ids** | [**Array&lt;String&gt;**](String.md) | Filter by review process IDs | [optional] |
| **access_ids** | [**Array&lt;String&gt;**](String.md) | Filter by access IDs | [optional] |

### Return type

[**PerformanceReviewProcessEstimatedTargetsGet200Response**](PerformanceReviewProcessEstimatedTargetsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

