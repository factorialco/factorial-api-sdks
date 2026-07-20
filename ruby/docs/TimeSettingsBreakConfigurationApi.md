# F::TimeSettingsBreakConfigurationApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**time_settings_break_configurations_get**](TimeSettingsBreakConfigurationApi.md#time_settings_break_configurations_get) | **GET** /api/2026-07-01/resources/time_settings/break_configurations | Reads all Break configurations |
| [**time_settings_break_configurations_id_get**](TimeSettingsBreakConfigurationApi.md#time_settings_break_configurations_id_get) | **GET** /api/2026-07-01/resources/time_settings/break_configurations/{id} | Reads a single Break configuration |
| [**time_settings_break_configurations_id_put**](TimeSettingsBreakConfigurationApi.md#time_settings_break_configurations_id_put) | **PUT** /api/2026-07-01/resources/time_settings/break_configurations/{id} | Updates a Break configuration |
| [**time_settings_break_configurations_post**](TimeSettingsBreakConfigurationApi.md#time_settings_break_configurations_post) | **POST** /api/2026-07-01/resources/time_settings/break_configurations | Creates a Break configuration |


## time_settings_break_configurations_get

> <TimeSettingsBreakConfigurationsGet200Response> time_settings_break_configurations_get(active, opts)

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

api_instance = F::TimeSettingsBreakConfigurationApi.new
active = true # Boolean | 
opts = {
  ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Break configurations
  result = api_instance.time_settings_break_configurations_get(active, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeSettingsBreakConfigurationApi->time_settings_break_configurations_get: #{e}"
end
```

#### Using the time_settings_break_configurations_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeSettingsBreakConfigurationsGet200Response>, Integer, Hash)> time_settings_break_configurations_get_with_http_info(active, opts)

```ruby
begin
  # Reads all Break configurations
  data, status_code, headers = api_instance.time_settings_break_configurations_get_with_http_info(active, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeSettingsBreakConfigurationsGet200Response>
rescue F::ApiError => e
  puts "Error when calling TimeSettingsBreakConfigurationApi->time_settings_break_configurations_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **active** | **Boolean** |  |  |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**TimeSettingsBreakConfigurationsGet200Response**](TimeSettingsBreakConfigurationsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## time_settings_break_configurations_id_get

> <TimeSettingsBreakConfiguration> time_settings_break_configurations_id_get(id)

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

api_instance = F::TimeSettingsBreakConfigurationApi.new
id = '1' # String | 

begin
  # Reads a single Break configuration
  result = api_instance.time_settings_break_configurations_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeSettingsBreakConfigurationApi->time_settings_break_configurations_id_get: #{e}"
end
```

#### Using the time_settings_break_configurations_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeSettingsBreakConfiguration>, Integer, Hash)> time_settings_break_configurations_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Break configuration
  data, status_code, headers = api_instance.time_settings_break_configurations_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeSettingsBreakConfiguration>
rescue F::ApiError => e
  puts "Error when calling TimeSettingsBreakConfigurationApi->time_settings_break_configurations_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**TimeSettingsBreakConfiguration**](TimeSettingsBreakConfiguration.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## time_settings_break_configurations_id_put

> <TimeSettingsBreakConfiguration> time_settings_break_configurations_id_put(id, opts)

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

api_instance = F::TimeSettingsBreakConfigurationApi.new
id = '1' # String | 
opts = {
  time_settings_break_configurations_id_put_request: F::TimeSettingsBreakConfigurationsIdPutRequest.new({id: 'id_example'}) # TimeSettingsBreakConfigurationsIdPutRequest | 
}

begin
  # Updates a Break configuration
  result = api_instance.time_settings_break_configurations_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeSettingsBreakConfigurationApi->time_settings_break_configurations_id_put: #{e}"
end
```

#### Using the time_settings_break_configurations_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeSettingsBreakConfiguration>, Integer, Hash)> time_settings_break_configurations_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Break configuration
  data, status_code, headers = api_instance.time_settings_break_configurations_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeSettingsBreakConfiguration>
rescue F::ApiError => e
  puts "Error when calling TimeSettingsBreakConfigurationApi->time_settings_break_configurations_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **time_settings_break_configurations_id_put_request** | [**TimeSettingsBreakConfigurationsIdPutRequest**](TimeSettingsBreakConfigurationsIdPutRequest.md) |  | [optional] |

### Return type

[**TimeSettingsBreakConfiguration**](TimeSettingsBreakConfiguration.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## time_settings_break_configurations_post

> <TimeSettingsBreakConfiguration> time_settings_break_configurations_post(opts)

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

api_instance = F::TimeSettingsBreakConfigurationApi.new
opts = {
  time_settings_break_configurations_post_request: F::TimeSettingsBreakConfigurationsPostRequest.new({name: 'name_example', paid: false}) # TimeSettingsBreakConfigurationsPostRequest | 
}

begin
  # Creates a Break configuration
  result = api_instance.time_settings_break_configurations_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeSettingsBreakConfigurationApi->time_settings_break_configurations_post: #{e}"
end
```

#### Using the time_settings_break_configurations_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeSettingsBreakConfiguration>, Integer, Hash)> time_settings_break_configurations_post_with_http_info(opts)

```ruby
begin
  # Creates a Break configuration
  data, status_code, headers = api_instance.time_settings_break_configurations_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeSettingsBreakConfiguration>
rescue F::ApiError => e
  puts "Error when calling TimeSettingsBreakConfigurationApi->time_settings_break_configurations_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **time_settings_break_configurations_post_request** | [**TimeSettingsBreakConfigurationsPostRequest**](TimeSettingsBreakConfigurationsPostRequest.md) |  | [optional] |

### Return type

[**TimeSettingsBreakConfiguration**](TimeSettingsBreakConfiguration.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

