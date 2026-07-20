# F::PerformanceReviewProcessCustomTemplateApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**performance_review_process_custom_templates_get**](PerformanceReviewProcessCustomTemplateApi.md#performance_review_process_custom_templates_get) | **GET** /api/2026-07-01/resources/performance/review_process_custom_templates | Reads all Review process custom templates |
| [**performance_review_process_custom_templates_id_get**](PerformanceReviewProcessCustomTemplateApi.md#performance_review_process_custom_templates_id_get) | **GET** /api/2026-07-01/resources/performance/review_process_custom_templates/{id} | Reads a single Review process custom template |


## performance_review_process_custom_templates_get

> <PerformanceReviewProcessCustomTemplatesGet200Response> performance_review_process_custom_templates_get(opts)

Reads all Review process custom templates

Retrieves the templates for the company.

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

api_instance = F::PerformanceReviewProcessCustomTemplateApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Filter by template IDs
  author_ids: ['inner_example'], # Array<String> | Filter by author IDs
  search: 'Q1 2024' # String | Filter by template name
}

begin
  # Reads all Review process custom templates
  result = api_instance.performance_review_process_custom_templates_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessCustomTemplateApi->performance_review_process_custom_templates_get: #{e}"
end
```

#### Using the performance_review_process_custom_templates_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcessCustomTemplatesGet200Response>, Integer, Hash)> performance_review_process_custom_templates_get_with_http_info(opts)

```ruby
begin
  # Reads all Review process custom templates
  data, status_code, headers = api_instance.performance_review_process_custom_templates_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcessCustomTemplatesGet200Response>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessCustomTemplateApi->performance_review_process_custom_templates_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter by template IDs | [optional] |
| **author_ids** | [**Array&lt;String&gt;**](String.md) | Filter by author IDs | [optional] |
| **search** | **String** | Filter by template name | [optional] |

### Return type

[**PerformanceReviewProcessCustomTemplatesGet200Response**](PerformanceReviewProcessCustomTemplatesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_review_process_custom_templates_id_get

> <PerformanceReviewProcessCustomTemplate> performance_review_process_custom_templates_id_get(id)

Reads a single Review process custom template

Retrieves the templates for the company.

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

api_instance = F::PerformanceReviewProcessCustomTemplateApi.new
id = '1' # String | Filter by template IDs

begin
  # Reads a single Review process custom template
  result = api_instance.performance_review_process_custom_templates_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessCustomTemplateApi->performance_review_process_custom_templates_id_get: #{e}"
end
```

#### Using the performance_review_process_custom_templates_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcessCustomTemplate>, Integer, Hash)> performance_review_process_custom_templates_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Review process custom template
  data, status_code, headers = api_instance.performance_review_process_custom_templates_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcessCustomTemplate>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessCustomTemplateApi->performance_review_process_custom_templates_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter by template IDs |  |

### Return type

[**PerformanceReviewProcessCustomTemplate**](PerformanceReviewProcessCustomTemplate.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

