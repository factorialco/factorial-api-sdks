# F::PerformanceReviewVisibilitySettingApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**performance_review_visibility_settings_get**](PerformanceReviewVisibilitySettingApi.md#performance_review_visibility_settings_get) | **GET** /api/2026-07-01/resources/performance/review_visibility_settings | Reads all Review visibility settings |
| [**performance_review_visibility_settings_id_put**](PerformanceReviewVisibilitySettingApi.md#performance_review_visibility_settings_id_put) | **PUT** /api/2026-07-01/resources/performance/review_visibility_settings/{id} | Updates a Review visibility setting |


## performance_review_visibility_settings_get

> <PerformanceReviewVisibilitySettingsGet200Response> performance_review_visibility_settings_get(opts)

Reads all Review visibility settings

Retrieves the visibility settings of review processes.

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

api_instance = F::PerformanceReviewVisibilitySettingApi.new
opts = {
  performance_review_process_ids: ['inner_example'] # Array<String> | Filter by review process IDs
}

begin
  # Reads all Review visibility settings
  result = api_instance.performance_review_visibility_settings_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewVisibilitySettingApi->performance_review_visibility_settings_get: #{e}"
end
```

#### Using the performance_review_visibility_settings_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewVisibilitySettingsGet200Response>, Integer, Hash)> performance_review_visibility_settings_get_with_http_info(opts)

```ruby
begin
  # Reads all Review visibility settings
  data, status_code, headers = api_instance.performance_review_visibility_settings_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewVisibilitySettingsGet200Response>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewVisibilitySettingApi->performance_review_visibility_settings_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_process_ids** | [**Array&lt;String&gt;**](String.md) | Filter by review process IDs | [optional] |

### Return type

[**PerformanceReviewVisibilitySettingsGet200Response**](PerformanceReviewVisibilitySettingsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_review_visibility_settings_id_put

> <PerformanceReviewVisibilitySetting> performance_review_visibility_settings_id_put(id, opts)

Updates a Review visibility setting

Modifiy the visibility settings of the review process.

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

api_instance = F::PerformanceReviewVisibilitySettingApi.new
id = '1' # String | Review process ID
opts = {
  performance_review_visibility_settings_id_put_request: F::PerformanceReviewVisibilitySettingsIdPutRequest.new({restrict_answers_visibility_to_reportees: false, early_access_to_answers_for_managers: true, anonymous_peer_evaluation_for_target: false}) # PerformanceReviewVisibilitySettingsIdPutRequest | 
}

begin
  # Updates a Review visibility setting
  result = api_instance.performance_review_visibility_settings_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewVisibilitySettingApi->performance_review_visibility_settings_id_put: #{e}"
end
```

#### Using the performance_review_visibility_settings_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewVisibilitySetting>, Integer, Hash)> performance_review_visibility_settings_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Review visibility setting
  data, status_code, headers = api_instance.performance_review_visibility_settings_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewVisibilitySetting>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewVisibilitySettingApi->performance_review_visibility_settings_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process ID |  |
| **performance_review_visibility_settings_id_put_request** | [**PerformanceReviewVisibilitySettingsIdPutRequest**](PerformanceReviewVisibilitySettingsIdPutRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewVisibilitySetting**](PerformanceReviewVisibilitySetting.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

