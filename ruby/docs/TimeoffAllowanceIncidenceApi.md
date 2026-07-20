# F::TimeoffAllowanceIncidenceApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**timeoff_allowance_incidences_get**](TimeoffAllowanceIncidenceApi.md#timeoff_allowance_incidences_get) | **GET** /api/2026-07-01/resources/timeoff/allowance_incidences | Reads all Allowance incidences |
| [**timeoff_allowance_incidences_id_delete**](TimeoffAllowanceIncidenceApi.md#timeoff_allowance_incidences_id_delete) | **DELETE** /api/2026-07-01/resources/timeoff/allowance_incidences/{id} | Deletes an Allowance incidence |
| [**timeoff_allowance_incidences_id_get**](TimeoffAllowanceIncidenceApi.md#timeoff_allowance_incidences_id_get) | **GET** /api/2026-07-01/resources/timeoff/allowance_incidences/{id} | Reads a single Allowance incidence |
| [**timeoff_allowance_incidences_id_put**](TimeoffAllowanceIncidenceApi.md#timeoff_allowance_incidences_id_put) | **PUT** /api/2026-07-01/resources/timeoff/allowance_incidences/{id} | Updates an Allowance incidence |
| [**timeoff_allowance_incidences_post**](TimeoffAllowanceIncidenceApi.md#timeoff_allowance_incidences_post) | **POST** /api/2026-07-01/resources/timeoff/allowance_incidences | Creates an Allowance incidence |


## timeoff_allowance_incidences_get

> <TimeoffAllowanceIncidencesGet200Response> timeoff_allowance_incidences_get(opts)

Reads all Allowance incidences

Reads all Allowance incidences

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

api_instance = F::TimeoffAllowanceIncidenceApi.new
opts = {
  ids: ['inner_example'], # Array<String> | 
  employee_ids: ['inner_example'], # Array<String> | 
  timeoff_allowance_ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Allowance incidences
  result = api_instance.timeoff_allowance_incidences_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceIncidenceApi->timeoff_allowance_incidences_get: #{e}"
end
```

#### Using the timeoff_allowance_incidences_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffAllowanceIncidencesGet200Response>, Integer, Hash)> timeoff_allowance_incidences_get_with_http_info(opts)

```ruby
begin
  # Reads all Allowance incidences
  data, status_code, headers = api_instance.timeoff_allowance_incidences_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffAllowanceIncidencesGet200Response>
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceIncidenceApi->timeoff_allowance_incidences_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **timeoff_allowance_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**TimeoffAllowanceIncidencesGet200Response**](TimeoffAllowanceIncidencesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_allowance_incidences_id_delete

> <TimeoffAllowanceIncidence> timeoff_allowance_incidences_id_delete(id)

Deletes an Allowance incidence

Deletes an allowance incidence

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

api_instance = F::TimeoffAllowanceIncidenceApi.new
id = '1' # String | 

begin
  # Deletes an Allowance incidence
  result = api_instance.timeoff_allowance_incidences_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceIncidenceApi->timeoff_allowance_incidences_id_delete: #{e}"
end
```

#### Using the timeoff_allowance_incidences_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffAllowanceIncidence>, Integer, Hash)> timeoff_allowance_incidences_id_delete_with_http_info(id)

```ruby
begin
  # Deletes an Allowance incidence
  data, status_code, headers = api_instance.timeoff_allowance_incidences_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffAllowanceIncidence>
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceIncidenceApi->timeoff_allowance_incidences_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**TimeoffAllowanceIncidence**](TimeoffAllowanceIncidence.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_allowance_incidences_id_get

> <TimeoffAllowanceIncidence> timeoff_allowance_incidences_id_get(id)

Reads a single Allowance incidence

Reads a single Allowance incidence

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

api_instance = F::TimeoffAllowanceIncidenceApi.new
id = '1' # String | 

begin
  # Reads a single Allowance incidence
  result = api_instance.timeoff_allowance_incidences_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceIncidenceApi->timeoff_allowance_incidences_id_get: #{e}"
end
```

#### Using the timeoff_allowance_incidences_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffAllowanceIncidence>, Integer, Hash)> timeoff_allowance_incidences_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Allowance incidence
  data, status_code, headers = api_instance.timeoff_allowance_incidences_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffAllowanceIncidence>
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceIncidenceApi->timeoff_allowance_incidences_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**TimeoffAllowanceIncidence**](TimeoffAllowanceIncidence.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_allowance_incidences_id_put

> <TimeoffAllowanceIncidence> timeoff_allowance_incidences_id_put(id, opts)

Updates an Allowance incidence

Updates an allowance incidence

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

api_instance = F::TimeoffAllowanceIncidenceApi.new
id = '1' # String | 
opts = {
  timeoff_allowance_incidences_id_put_request: F::TimeoffAllowanceIncidencesIdPutRequest.new({id: 'id_example'}) # TimeoffAllowanceIncidencesIdPutRequest | 
}

begin
  # Updates an Allowance incidence
  result = api_instance.timeoff_allowance_incidences_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceIncidenceApi->timeoff_allowance_incidences_id_put: #{e}"
end
```

#### Using the timeoff_allowance_incidences_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffAllowanceIncidence>, Integer, Hash)> timeoff_allowance_incidences_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates an Allowance incidence
  data, status_code, headers = api_instance.timeoff_allowance_incidences_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffAllowanceIncidence>
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceIncidenceApi->timeoff_allowance_incidences_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **timeoff_allowance_incidences_id_put_request** | [**TimeoffAllowanceIncidencesIdPutRequest**](TimeoffAllowanceIncidencesIdPutRequest.md) |  | [optional] |

### Return type

[**TimeoffAllowanceIncidence**](TimeoffAllowanceIncidence.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeoff_allowance_incidences_post

> <TimeoffAllowanceIncidence> timeoff_allowance_incidences_post(opts)

Creates an Allowance incidence

Creates an allowance incidence, also known as an Allowance Adjustment in the Employee Time off Page. They are hours or days added or subtracted from the time off allowance

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

api_instance = F::TimeoffAllowanceIncidenceApi.new
opts = {
  timeoff_allowance_incidences_post_request: F::TimeoffAllowanceIncidencesPostRequest.new({employee_id: '6', timeoff_allowance_id: '1', days_in_cents: 100, effective_on: '2024-01-05', target_balance: 'available'}) # TimeoffAllowanceIncidencesPostRequest | 
}

begin
  # Creates an Allowance incidence
  result = api_instance.timeoff_allowance_incidences_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceIncidenceApi->timeoff_allowance_incidences_post: #{e}"
end
```

#### Using the timeoff_allowance_incidences_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffAllowanceIncidence>, Integer, Hash)> timeoff_allowance_incidences_post_with_http_info(opts)

```ruby
begin
  # Creates an Allowance incidence
  data, status_code, headers = api_instance.timeoff_allowance_incidences_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffAllowanceIncidence>
rescue F::ApiError => e
  puts "Error when calling TimeoffAllowanceIncidenceApi->timeoff_allowance_incidences_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **timeoff_allowance_incidences_post_request** | [**TimeoffAllowanceIncidencesPostRequest**](TimeoffAllowanceIncidencesPostRequest.md) |  | [optional] |

### Return type

[**TimeoffAllowanceIncidence**](TimeoffAllowanceIncidence.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

