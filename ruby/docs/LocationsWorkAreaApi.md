# F::LocationsWorkAreaApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**locations_work_areas_archive_post**](LocationsWorkAreaApi.md#locations_work_areas_archive_post) | **POST** /api/2026-07-01/resources/locations/work_areas/archive | Archives a Work area |
| [**locations_work_areas_get**](LocationsWorkAreaApi.md#locations_work_areas_get) | **GET** /api/2026-07-01/resources/locations/work_areas | Reads all Work areas |
| [**locations_work_areas_id_get**](LocationsWorkAreaApi.md#locations_work_areas_id_get) | **GET** /api/2026-07-01/resources/locations/work_areas/{id} | Reads a single Work area |
| [**locations_work_areas_id_put**](LocationsWorkAreaApi.md#locations_work_areas_id_put) | **PUT** /api/2026-07-01/resources/locations/work_areas/{id} | Updates a Work area |
| [**locations_work_areas_post**](LocationsWorkAreaApi.md#locations_work_areas_post) | **POST** /api/2026-07-01/resources/locations/work_areas | Creates a Work area |
| [**locations_work_areas_unarchive_post**](LocationsWorkAreaApi.md#locations_work_areas_unarchive_post) | **POST** /api/2026-07-01/resources/locations/work_areas/unarchive | Unarchives a Work area |


## locations_work_areas_archive_post

> <LocationsWorkArea> locations_work_areas_archive_post(opts)

Archives a Work area

Archives a Work area

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

api_instance = F::LocationsWorkAreaApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Archives a Work area
  result = api_instance.locations_work_areas_archive_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling LocationsWorkAreaApi->locations_work_areas_archive_post: #{e}"
end
```

#### Using the locations_work_areas_archive_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<LocationsWorkArea>, Integer, Hash)> locations_work_areas_archive_post_with_http_info(opts)

```ruby
begin
  # Archives a Work area
  data, status_code, headers = api_instance.locations_work_areas_archive_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <LocationsWorkArea>
rescue F::ApiError => e
  puts "Error when calling LocationsWorkAreaApi->locations_work_areas_archive_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**LocationsWorkArea**](LocationsWorkArea.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## locations_work_areas_get

> <LocationsWorkAreasGet200Response> locations_work_areas_get(only_non_archived, opts)

Reads all Work areas

Reads all Work areas

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

api_instance = F::LocationsWorkAreaApi.new
only_non_archived = true # Boolean | 
opts = {
  ids: ['inner_example'], # Array<String> | 
  location_ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Work areas
  result = api_instance.locations_work_areas_get(only_non_archived, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling LocationsWorkAreaApi->locations_work_areas_get: #{e}"
end
```

#### Using the locations_work_areas_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<LocationsWorkAreasGet200Response>, Integer, Hash)> locations_work_areas_get_with_http_info(only_non_archived, opts)

```ruby
begin
  # Reads all Work areas
  data, status_code, headers = api_instance.locations_work_areas_get_with_http_info(only_non_archived, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <LocationsWorkAreasGet200Response>
rescue F::ApiError => e
  puts "Error when calling LocationsWorkAreaApi->locations_work_areas_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **only_non_archived** | **Boolean** |  |  |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **location_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**LocationsWorkAreasGet200Response**](LocationsWorkAreasGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locations_work_areas_id_get

> <LocationsWorkArea> locations_work_areas_id_get(id)

Reads a single Work area

Reads a single Work area

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

api_instance = F::LocationsWorkAreaApi.new
id = '1' # String | 

begin
  # Reads a single Work area
  result = api_instance.locations_work_areas_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling LocationsWorkAreaApi->locations_work_areas_id_get: #{e}"
end
```

#### Using the locations_work_areas_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<LocationsWorkArea>, Integer, Hash)> locations_work_areas_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Work area
  data, status_code, headers = api_instance.locations_work_areas_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <LocationsWorkArea>
rescue F::ApiError => e
  puts "Error when calling LocationsWorkAreaApi->locations_work_areas_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**LocationsWorkArea**](LocationsWorkArea.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locations_work_areas_id_put

> <LocationsWorkArea> locations_work_areas_id_put(id, opts)

Updates a Work area

Updates a Work area

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

api_instance = F::LocationsWorkAreaApi.new
id = '1' # String | 
opts = {
  locations_work_areas_id_put_request: F::LocationsWorkAreasIdPutRequest.new({id: 'id_example', name: 'name_example'}) # LocationsWorkAreasIdPutRequest | 
}

begin
  # Updates a Work area
  result = api_instance.locations_work_areas_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling LocationsWorkAreaApi->locations_work_areas_id_put: #{e}"
end
```

#### Using the locations_work_areas_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<LocationsWorkArea>, Integer, Hash)> locations_work_areas_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Work area
  data, status_code, headers = api_instance.locations_work_areas_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <LocationsWorkArea>
rescue F::ApiError => e
  puts "Error when calling LocationsWorkAreaApi->locations_work_areas_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **locations_work_areas_id_put_request** | [**LocationsWorkAreasIdPutRequest**](LocationsWorkAreasIdPutRequest.md) |  | [optional] |

### Return type

[**LocationsWorkArea**](LocationsWorkArea.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## locations_work_areas_post

> <LocationsWorkArea> locations_work_areas_post(opts)

Creates a Work area

Creates a Work area

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

api_instance = F::LocationsWorkAreaApi.new
opts = {
  locations_work_areas_post_request: F::LocationsWorkAreasPostRequest.new({name: 'name_example', location_id: 'location_id_example'}) # LocationsWorkAreasPostRequest | 
}

begin
  # Creates a Work area
  result = api_instance.locations_work_areas_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling LocationsWorkAreaApi->locations_work_areas_post: #{e}"
end
```

#### Using the locations_work_areas_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<LocationsWorkArea>, Integer, Hash)> locations_work_areas_post_with_http_info(opts)

```ruby
begin
  # Creates a Work area
  data, status_code, headers = api_instance.locations_work_areas_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <LocationsWorkArea>
rescue F::ApiError => e
  puts "Error when calling LocationsWorkAreaApi->locations_work_areas_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **locations_work_areas_post_request** | [**LocationsWorkAreasPostRequest**](LocationsWorkAreasPostRequest.md) |  | [optional] |

### Return type

[**LocationsWorkArea**](LocationsWorkArea.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## locations_work_areas_unarchive_post

> <LocationsWorkArea> locations_work_areas_unarchive_post(opts)

Unarchives a Work area

Unarchives a Work area

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

api_instance = F::LocationsWorkAreaApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Unarchives a Work area
  result = api_instance.locations_work_areas_unarchive_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling LocationsWorkAreaApi->locations_work_areas_unarchive_post: #{e}"
end
```

#### Using the locations_work_areas_unarchive_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<LocationsWorkArea>, Integer, Hash)> locations_work_areas_unarchive_post_with_http_info(opts)

```ruby
begin
  # Unarchives a Work area
  data, status_code, headers = api_instance.locations_work_areas_unarchive_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <LocationsWorkArea>
rescue F::ApiError => e
  puts "Error when calling LocationsWorkAreaApi->locations_work_areas_unarchive_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**LocationsWorkArea**](LocationsWorkArea.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

