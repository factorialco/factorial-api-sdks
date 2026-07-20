# F::LocationsLocationApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**locations_locations_get**](LocationsLocationApi.md#locations_locations_get) | **GET** /api/2026-07-01/resources/locations/locations | Reads all Locations |
| [**locations_locations_id_delete**](LocationsLocationApi.md#locations_locations_id_delete) | **DELETE** /api/2026-07-01/resources/locations/locations/{id} | Deletes a Location |
| [**locations_locations_id_get**](LocationsLocationApi.md#locations_locations_id_get) | **GET** /api/2026-07-01/resources/locations/locations/{id} | Reads a single Location |
| [**locations_locations_id_put**](LocationsLocationApi.md#locations_locations_id_put) | **PUT** /api/2026-07-01/resources/locations/locations/{id} | Updates a Location |
| [**locations_locations_post**](LocationsLocationApi.md#locations_locations_post) | **POST** /api/2026-07-01/resources/locations/locations | Creates a Location |


## locations_locations_get

> <LocationsLocationsGet200Response> locations_locations_get(opts)

Reads all Locations

Reads all Locations

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

api_instance = F::LocationsLocationApi.new
opts = {
  ids: ['inner_example'], # Array<String> | The location IDs to filter the results.
  employee_ids: ['inner_example'], # Array<String> | Return only the locations assigned to these employees.
  main: false # Boolean | Wether to filter only the main location.
}

begin
  # Reads all Locations
  result = api_instance.locations_locations_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling LocationsLocationApi->locations_locations_get: #{e}"
end
```

#### Using the locations_locations_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<LocationsLocationsGet200Response>, Integer, Hash)> locations_locations_get_with_http_info(opts)

```ruby
begin
  # Reads all Locations
  data, status_code, headers = api_instance.locations_locations_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <LocationsLocationsGet200Response>
rescue F::ApiError => e
  puts "Error when calling LocationsLocationApi->locations_locations_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | The location IDs to filter the results. | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Return only the locations assigned to these employees. | [optional] |
| **main** | **Boolean** | Wether to filter only the main location. | [optional] |

### Return type

[**LocationsLocationsGet200Response**](LocationsLocationsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locations_locations_id_delete

> <LocationsLocation> locations_locations_id_delete(id)

Deletes a Location

Deletes a Location

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

api_instance = F::LocationsLocationApi.new
id = '1' # String | 

begin
  # Deletes a Location
  result = api_instance.locations_locations_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling LocationsLocationApi->locations_locations_id_delete: #{e}"
end
```

#### Using the locations_locations_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<LocationsLocation>, Integer, Hash)> locations_locations_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Location
  data, status_code, headers = api_instance.locations_locations_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <LocationsLocation>
rescue F::ApiError => e
  puts "Error when calling LocationsLocationApi->locations_locations_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**LocationsLocation**](LocationsLocation.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locations_locations_id_get

> <LocationsLocation> locations_locations_id_get(id)

Reads a single Location

Reads a single Location

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

api_instance = F::LocationsLocationApi.new
id = '1' # String | The location IDs to filter the results.

begin
  # Reads a single Location
  result = api_instance.locations_locations_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling LocationsLocationApi->locations_locations_id_get: #{e}"
end
```

#### Using the locations_locations_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<LocationsLocation>, Integer, Hash)> locations_locations_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Location
  data, status_code, headers = api_instance.locations_locations_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <LocationsLocation>
rescue F::ApiError => e
  puts "Error when calling LocationsLocationApi->locations_locations_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The location IDs to filter the results. |  |

### Return type

[**LocationsLocation**](LocationsLocation.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locations_locations_id_put

> <LocationsLocation> locations_locations_id_put(id, opts)

Updates a Location

Updates a Location

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

api_instance = F::LocationsLocationApi.new
id = '1' # String | identifier of the location
opts = {
  locations_locations_id_put_request: F::LocationsLocationsIdPutRequest.new({id: '1'}) # LocationsLocationsIdPutRequest | 
}

begin
  # Updates a Location
  result = api_instance.locations_locations_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling LocationsLocationApi->locations_locations_id_put: #{e}"
end
```

#### Using the locations_locations_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<LocationsLocation>, Integer, Hash)> locations_locations_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Location
  data, status_code, headers = api_instance.locations_locations_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <LocationsLocation>
rescue F::ApiError => e
  puts "Error when calling LocationsLocationApi->locations_locations_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the location |  |
| **locations_locations_id_put_request** | [**LocationsLocationsIdPutRequest**](LocationsLocationsIdPutRequest.md) |  | [optional] |

### Return type

[**LocationsLocation**](LocationsLocation.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## locations_locations_post

> <LocationsLocation> locations_locations_post(opts)

Creates a Location

Creates a Location

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

api_instance = F::LocationsLocationApi.new
opts = {
  locations_locations_post_request: F::LocationsLocationsPostRequest.new({name: 'Barcelona Office', country: 'es', timezone: 'Europe/Madrid', company_id: '1'}) # LocationsLocationsPostRequest | 
}

begin
  # Creates a Location
  result = api_instance.locations_locations_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling LocationsLocationApi->locations_locations_post: #{e}"
end
```

#### Using the locations_locations_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<LocationsLocation>, Integer, Hash)> locations_locations_post_with_http_info(opts)

```ruby
begin
  # Creates a Location
  data, status_code, headers = api_instance.locations_locations_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <LocationsLocation>
rescue F::ApiError => e
  puts "Error when calling LocationsLocationApi->locations_locations_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **locations_locations_post_request** | [**LocationsLocationsPostRequest**](LocationsLocationsPostRequest.md) |  | [optional] |

### Return type

[**LocationsLocation**](LocationsLocation.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

