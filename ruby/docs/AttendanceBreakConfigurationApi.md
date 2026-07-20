# F::AttendanceBreakConfigurationApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**attendance_break_configurations_get**](AttendanceBreakConfigurationApi.md#attendance_break_configurations_get) | **GET** /api/2026-07-01/resources/attendance/break_configurations | Reads all Break configurations |
| [**attendance_break_configurations_id_get**](AttendanceBreakConfigurationApi.md#attendance_break_configurations_id_get) | **GET** /api/2026-07-01/resources/attendance/break_configurations/{id} | Reads a single Break configuration |
| [**attendance_break_configurations_id_put**](AttendanceBreakConfigurationApi.md#attendance_break_configurations_id_put) | **PUT** /api/2026-07-01/resources/attendance/break_configurations/{id} | Updates a Break configuration |
| [**attendance_break_configurations_post**](AttendanceBreakConfigurationApi.md#attendance_break_configurations_post) | **POST** /api/2026-07-01/resources/attendance/break_configurations | Creates a Break configuration |


## attendance_break_configurations_get

> <AttendanceBreakConfigurationsGet200Response> attendance_break_configurations_get(opts)

Reads all Break configurations

Reads all Break configurations

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

api_instance = F::AttendanceBreakConfigurationApi.new
opts = {
  ids: ['inner_example'], # Array<String> | The break configuration ids to retrieve
  time_settings_break_configuration_ids: ['inner_example'], # Array<String> | Ids of the time settings break configuration
  attendance_employees_setting_id: '1', # String | Id of the attendance employee setting
  enabled: true # Boolean | Status of the break configuration if enabled or not
}

begin
  # Reads all Break configurations
  result = api_instance.attendance_break_configurations_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceBreakConfigurationApi->attendance_break_configurations_get: #{e}"
end
```

#### Using the attendance_break_configurations_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceBreakConfigurationsGet200Response>, Integer, Hash)> attendance_break_configurations_get_with_http_info(opts)

```ruby
begin
  # Reads all Break configurations
  data, status_code, headers = api_instance.attendance_break_configurations_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceBreakConfigurationsGet200Response>
rescue F::ApiError => e
  puts "Error when calling AttendanceBreakConfigurationApi->attendance_break_configurations_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | The break configuration ids to retrieve | [optional] |
| **time_settings_break_configuration_ids** | [**Array&lt;String&gt;**](String.md) | Ids of the time settings break configuration | [optional] |
| **attendance_employees_setting_id** | **String** | Id of the attendance employee setting | [optional] |
| **enabled** | **Boolean** | Status of the break configuration if enabled or not | [optional] |

### Return type

[**AttendanceBreakConfigurationsGet200Response**](AttendanceBreakConfigurationsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attendance_break_configurations_id_get

> <AttendanceBreakConfiguration> attendance_break_configurations_id_get(id)

Reads a single Break configuration

Reads a single Break configuration

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

api_instance = F::AttendanceBreakConfigurationApi.new
id = '1' # String | The break configuration ids to retrieve

begin
  # Reads a single Break configuration
  result = api_instance.attendance_break_configurations_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceBreakConfigurationApi->attendance_break_configurations_id_get: #{e}"
end
```

#### Using the attendance_break_configurations_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceBreakConfiguration>, Integer, Hash)> attendance_break_configurations_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Break configuration
  data, status_code, headers = api_instance.attendance_break_configurations_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceBreakConfiguration>
rescue F::ApiError => e
  puts "Error when calling AttendanceBreakConfigurationApi->attendance_break_configurations_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The break configuration ids to retrieve |  |

### Return type

[**AttendanceBreakConfiguration**](AttendanceBreakConfiguration.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attendance_break_configurations_id_put

> <AttendanceBreakConfiguration> attendance_break_configurations_id_put(id, opts)

Updates a Break configuration

Updates a Break configuration

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

api_instance = F::AttendanceBreakConfigurationApi.new
id = '1' # String | Id of the break configuration
opts = {
  attendance_break_configurations_id_put_request: F::AttendanceBreakConfigurationsIdPutRequest.new({id: '1'}) # AttendanceBreakConfigurationsIdPutRequest | 
}

begin
  # Updates a Break configuration
  result = api_instance.attendance_break_configurations_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceBreakConfigurationApi->attendance_break_configurations_id_put: #{e}"
end
```

#### Using the attendance_break_configurations_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceBreakConfiguration>, Integer, Hash)> attendance_break_configurations_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Break configuration
  data, status_code, headers = api_instance.attendance_break_configurations_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceBreakConfiguration>
rescue F::ApiError => e
  puts "Error when calling AttendanceBreakConfigurationApi->attendance_break_configurations_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id of the break configuration |  |
| **attendance_break_configurations_id_put_request** | [**AttendanceBreakConfigurationsIdPutRequest**](AttendanceBreakConfigurationsIdPutRequest.md) |  | [optional] |

### Return type

[**AttendanceBreakConfiguration**](AttendanceBreakConfiguration.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attendance_break_configurations_post

> <AttendanceBreakConfiguration> attendance_break_configurations_post(opts)

Creates a Break configuration

Creates a Break configuration

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

api_instance = F::AttendanceBreakConfigurationApi.new
opts = {
  attendance_break_configurations_post_request: F::AttendanceBreakConfigurationsPostRequest.new({time_settings_break_configuration_id: '1', attendance_employees_setting_id: '1', enabled: false}) # AttendanceBreakConfigurationsPostRequest | 
}

begin
  # Creates a Break configuration
  result = api_instance.attendance_break_configurations_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceBreakConfigurationApi->attendance_break_configurations_post: #{e}"
end
```

#### Using the attendance_break_configurations_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceBreakConfiguration>, Integer, Hash)> attendance_break_configurations_post_with_http_info(opts)

```ruby
begin
  # Creates a Break configuration
  data, status_code, headers = api_instance.attendance_break_configurations_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceBreakConfiguration>
rescue F::ApiError => e
  puts "Error when calling AttendanceBreakConfigurationApi->attendance_break_configurations_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_break_configurations_post_request** | [**AttendanceBreakConfigurationsPostRequest**](AttendanceBreakConfigurationsPostRequest.md) |  | [optional] |

### Return type

[**AttendanceBreakConfiguration**](AttendanceBreakConfiguration.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

