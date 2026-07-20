# F::WorkScheduleDayConfigurationApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**work_schedule_day_configurations_bulk_cud_post**](WorkScheduleDayConfigurationApi.md#work_schedule_day_configurations_bulk_cud_post) | **POST** /api/2026-07-01/resources/work_schedule/day_configurations/bulk_cud | Bulk cuds a Day configuration |
| [**work_schedule_day_configurations_get**](WorkScheduleDayConfigurationApi.md#work_schedule_day_configurations_get) | **GET** /api/2026-07-01/resources/work_schedule/day_configurations | Reads all Day configurations |
| [**work_schedule_day_configurations_id_get**](WorkScheduleDayConfigurationApi.md#work_schedule_day_configurations_id_get) | **GET** /api/2026-07-01/resources/work_schedule/day_configurations/{id} | Reads a single Day configuration |


## work_schedule_day_configurations_bulk_cud_post

> <WorkScheduleDayConfiguration> work_schedule_day_configurations_bulk_cud_post(opts)

Bulk cuds a Day configuration

Bulk cuds a Day configuration

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

api_instance = F::WorkScheduleDayConfigurationApi.new
opts = {
  work_schedule_day_configurations_bulk_cud_post_request: F::WorkScheduleDayConfigurationsBulkCudPostRequest.new({overlap_period_id: 'overlap_period_id_example', day_configurations: [3.56]}) # WorkScheduleDayConfigurationsBulkCudPostRequest | 
}

begin
  # Bulk cuds a Day configuration
  result = api_instance.work_schedule_day_configurations_bulk_cud_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling WorkScheduleDayConfigurationApi->work_schedule_day_configurations_bulk_cud_post: #{e}"
end
```

#### Using the work_schedule_day_configurations_bulk_cud_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkScheduleDayConfiguration>, Integer, Hash)> work_schedule_day_configurations_bulk_cud_post_with_http_info(opts)

```ruby
begin
  # Bulk cuds a Day configuration
  data, status_code, headers = api_instance.work_schedule_day_configurations_bulk_cud_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkScheduleDayConfiguration>
rescue F::ApiError => e
  puts "Error when calling WorkScheduleDayConfigurationApi->work_schedule_day_configurations_bulk_cud_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **work_schedule_day_configurations_bulk_cud_post_request** | [**WorkScheduleDayConfigurationsBulkCudPostRequest**](WorkScheduleDayConfigurationsBulkCudPostRequest.md) |  | [optional] |

### Return type

[**WorkScheduleDayConfiguration**](WorkScheduleDayConfiguration.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## work_schedule_day_configurations_get

> <WorkScheduleDayConfigurationsGet200Response> work_schedule_day_configurations_get(opts)

Reads all Day configurations

Reads all Day configurations

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

api_instance = F::WorkScheduleDayConfigurationApi.new
opts = {
  ids: ['inner_example'], # Array<String> | 
  overlap_period_id: 'overlap_period_id_example', # String | 
  schedule_id: 'schedule_id_example' # String | 
}

begin
  # Reads all Day configurations
  result = api_instance.work_schedule_day_configurations_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling WorkScheduleDayConfigurationApi->work_schedule_day_configurations_get: #{e}"
end
```

#### Using the work_schedule_day_configurations_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkScheduleDayConfigurationsGet200Response>, Integer, Hash)> work_schedule_day_configurations_get_with_http_info(opts)

```ruby
begin
  # Reads all Day configurations
  data, status_code, headers = api_instance.work_schedule_day_configurations_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkScheduleDayConfigurationsGet200Response>
rescue F::ApiError => e
  puts "Error when calling WorkScheduleDayConfigurationApi->work_schedule_day_configurations_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **overlap_period_id** | **String** |  | [optional] |
| **schedule_id** | **String** |  | [optional] |

### Return type

[**WorkScheduleDayConfigurationsGet200Response**](WorkScheduleDayConfigurationsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## work_schedule_day_configurations_id_get

> <WorkScheduleDayConfiguration> work_schedule_day_configurations_id_get(id)

Reads a single Day configuration

Reads a single Day configuration

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

api_instance = F::WorkScheduleDayConfigurationApi.new
id = '1' # String | 

begin
  # Reads a single Day configuration
  result = api_instance.work_schedule_day_configurations_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling WorkScheduleDayConfigurationApi->work_schedule_day_configurations_id_get: #{e}"
end
```

#### Using the work_schedule_day_configurations_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WorkScheduleDayConfiguration>, Integer, Hash)> work_schedule_day_configurations_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Day configuration
  data, status_code, headers = api_instance.work_schedule_day_configurations_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WorkScheduleDayConfiguration>
rescue F::ApiError => e
  puts "Error when calling WorkScheduleDayConfigurationApi->work_schedule_day_configurations_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**WorkScheduleDayConfiguration**](WorkScheduleDayConfiguration.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

