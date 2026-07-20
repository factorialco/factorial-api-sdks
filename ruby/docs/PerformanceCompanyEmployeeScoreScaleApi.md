# F::PerformanceCompanyEmployeeScoreScaleApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**performance_company_employee_score_scales_get**](PerformanceCompanyEmployeeScoreScaleApi.md#performance_company_employee_score_scales_get) | **GET** /api/2026-07-01/resources/performance/company_employee_score_scales | Reads all Company employee score scales |
| [**performance_company_employee_score_scales_id_get**](PerformanceCompanyEmployeeScoreScaleApi.md#performance_company_employee_score_scales_id_get) | **GET** /api/2026-07-01/resources/performance/company_employee_score_scales/{id} | Reads a single Company employee score scale |
| [**performance_company_employee_score_scales_set_post**](PerformanceCompanyEmployeeScoreScaleApi.md#performance_company_employee_score_scales_set_post) | **POST** /api/2026-07-01/resources/performance/company_employee_score_scales/set | Sets a Company employee score scale |


## performance_company_employee_score_scales_get

> <PerformanceCompanyEmployeeScoreScalesGet200Response> performance_company_employee_score_scales_get(opts)

Reads all Company employee score scales

Retrieves the predefined scale set for the company and used when scoring the employee inside a review.

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

api_instance = F::PerformanceCompanyEmployeeScoreScaleApi.new
opts = {
  ids: ['inner_example'] # Array<String> | Filter by company IDs
}

begin
  # Reads all Company employee score scales
  result = api_instance.performance_company_employee_score_scales_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceCompanyEmployeeScoreScaleApi->performance_company_employee_score_scales_get: #{e}"
end
```

#### Using the performance_company_employee_score_scales_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceCompanyEmployeeScoreScalesGet200Response>, Integer, Hash)> performance_company_employee_score_scales_get_with_http_info(opts)

```ruby
begin
  # Reads all Company employee score scales
  data, status_code, headers = api_instance.performance_company_employee_score_scales_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceCompanyEmployeeScoreScalesGet200Response>
rescue F::ApiError => e
  puts "Error when calling PerformanceCompanyEmployeeScoreScaleApi->performance_company_employee_score_scales_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter by company IDs | [optional] |

### Return type

[**PerformanceCompanyEmployeeScoreScalesGet200Response**](PerformanceCompanyEmployeeScoreScalesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_company_employee_score_scales_id_get

> <PerformanceCompanyEmployeeScoreScale> performance_company_employee_score_scales_id_get(id)

Reads a single Company employee score scale

Retrieves the predefined scale set for the company and used when scoring the employee inside a review.

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

api_instance = F::PerformanceCompanyEmployeeScoreScaleApi.new
id = '1' # String | Filter by company IDs

begin
  # Reads a single Company employee score scale
  result = api_instance.performance_company_employee_score_scales_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceCompanyEmployeeScoreScaleApi->performance_company_employee_score_scales_id_get: #{e}"
end
```

#### Using the performance_company_employee_score_scales_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceCompanyEmployeeScoreScale>, Integer, Hash)> performance_company_employee_score_scales_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Company employee score scale
  data, status_code, headers = api_instance.performance_company_employee_score_scales_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceCompanyEmployeeScoreScale>
rescue F::ApiError => e
  puts "Error when calling PerformanceCompanyEmployeeScoreScaleApi->performance_company_employee_score_scales_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter by company IDs |  |

### Return type

[**PerformanceCompanyEmployeeScoreScale**](PerformanceCompanyEmployeeScoreScale.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_company_employee_score_scales_set_post

> <PerformanceCompanyEmployeeScoreScale> performance_company_employee_score_scales_set_post(opts)

Sets a Company employee score scale

Set the predefined employee score scale for the company.

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

api_instance = F::PerformanceCompanyEmployeeScoreScaleApi.new
opts = {
  performance_company_employee_score_scales_set_post_request: F::PerformanceCompanyEmployeeScoreScalesSetPostRequest.new({id: 'id_example', scale_id: 'scale_id_example'}) # PerformanceCompanyEmployeeScoreScalesSetPostRequest | 
}

begin
  # Sets a Company employee score scale
  result = api_instance.performance_company_employee_score_scales_set_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceCompanyEmployeeScoreScaleApi->performance_company_employee_score_scales_set_post: #{e}"
end
```

#### Using the performance_company_employee_score_scales_set_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceCompanyEmployeeScoreScale>, Integer, Hash)> performance_company_employee_score_scales_set_post_with_http_info(opts)

```ruby
begin
  # Sets a Company employee score scale
  data, status_code, headers = api_instance.performance_company_employee_score_scales_set_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceCompanyEmployeeScoreScale>
rescue F::ApiError => e
  puts "Error when calling PerformanceCompanyEmployeeScoreScaleApi->performance_company_employee_score_scales_set_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_company_employee_score_scales_set_post_request** | [**PerformanceCompanyEmployeeScoreScalesSetPostRequest**](PerformanceCompanyEmployeeScoreScalesSetPostRequest.md) |  | [optional] |

### Return type

[**PerformanceCompanyEmployeeScoreScale**](PerformanceCompanyEmployeeScoreScale.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

