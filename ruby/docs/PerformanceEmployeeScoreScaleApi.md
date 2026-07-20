# F::PerformanceEmployeeScoreScaleApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**performance_employee_score_scales_get**](PerformanceEmployeeScoreScaleApi.md#performance_employee_score_scales_get) | **GET** /api/2026-07-01/resources/performance/employee_score_scales | Reads all Employee score scales |
| [**performance_employee_score_scales_id_get**](PerformanceEmployeeScoreScaleApi.md#performance_employee_score_scales_id_get) | **GET** /api/2026-07-01/resources/performance/employee_score_scales/{id} | Reads a single Employee score scale |


## performance_employee_score_scales_get

> <PerformanceEmployeeScoreScalesGet200Response> performance_employee_score_scales_get(opts)

Reads all Employee score scales

Retrieves the predefined employee score scales that can be set for the company to be used when scoring the employee inside a review.

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

api_instance = F::PerformanceEmployeeScoreScaleApi.new
opts = {
  ids: ['inner_example'] # Array<String> | Filter by employee score scale IDs
}

begin
  # Reads all Employee score scales
  result = api_instance.performance_employee_score_scales_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceEmployeeScoreScaleApi->performance_employee_score_scales_get: #{e}"
end
```

#### Using the performance_employee_score_scales_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceEmployeeScoreScalesGet200Response>, Integer, Hash)> performance_employee_score_scales_get_with_http_info(opts)

```ruby
begin
  # Reads all Employee score scales
  data, status_code, headers = api_instance.performance_employee_score_scales_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceEmployeeScoreScalesGet200Response>
rescue F::ApiError => e
  puts "Error when calling PerformanceEmployeeScoreScaleApi->performance_employee_score_scales_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter by employee score scale IDs | [optional] |

### Return type

[**PerformanceEmployeeScoreScalesGet200Response**](PerformanceEmployeeScoreScalesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_employee_score_scales_id_get

> <PerformanceEmployeeScoreScale> performance_employee_score_scales_id_get(id)

Reads a single Employee score scale

Retrieves the predefined employee score scales that can be set for the company to be used when scoring the employee inside a review.

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

api_instance = F::PerformanceEmployeeScoreScaleApi.new
id = '1' # String | Filter by employee score scale IDs

begin
  # Reads a single Employee score scale
  result = api_instance.performance_employee_score_scales_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceEmployeeScoreScaleApi->performance_employee_score_scales_id_get: #{e}"
end
```

#### Using the performance_employee_score_scales_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceEmployeeScoreScale>, Integer, Hash)> performance_employee_score_scales_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Employee score scale
  data, status_code, headers = api_instance.performance_employee_score_scales_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceEmployeeScoreScale>
rescue F::ApiError => e
  puts "Error when calling PerformanceEmployeeScoreScaleApi->performance_employee_score_scales_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter by employee score scale IDs |  |

### Return type

[**PerformanceEmployeeScoreScale**](PerformanceEmployeeScoreScale.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

