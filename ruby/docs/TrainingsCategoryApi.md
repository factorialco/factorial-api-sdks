# F::TrainingsCategoryApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**trainings_categories_get**](TrainingsCategoryApi.md#trainings_categories_get) | **GET** /api/2026-07-01/resources/trainings/categories | Reads all Categories |
| [**trainings_categories_id_delete**](TrainingsCategoryApi.md#trainings_categories_id_delete) | **DELETE** /api/2026-07-01/resources/trainings/categories/{id} | Deletes a Category |
| [**trainings_categories_id_get**](TrainingsCategoryApi.md#trainings_categories_id_get) | **GET** /api/2026-07-01/resources/trainings/categories/{id} | Reads a single Category |
| [**trainings_categories_post**](TrainingsCategoryApi.md#trainings_categories_post) | **POST** /api/2026-07-01/resources/trainings/categories | Creates a Category |


## trainings_categories_get

> <TrainingsCategoriesGet200Response> trainings_categories_get(opts)

Reads all Categories

Reads all Categories

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

api_instance = F::TrainingsCategoryApi.new
opts = {
  ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Categories
  result = api_instance.trainings_categories_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsCategoryApi->trainings_categories_get: #{e}"
end
```

#### Using the trainings_categories_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsCategoriesGet200Response>, Integer, Hash)> trainings_categories_get_with_http_info(opts)

```ruby
begin
  # Reads all Categories
  data, status_code, headers = api_instance.trainings_categories_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsCategoriesGet200Response>
rescue F::ApiError => e
  puts "Error when calling TrainingsCategoryApi->trainings_categories_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**TrainingsCategoriesGet200Response**](TrainingsCategoriesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_categories_id_delete

> <TrainingsCategory> trainings_categories_id_delete(id)

Deletes a Category

Deletes a Category

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

api_instance = F::TrainingsCategoryApi.new
id = '1' # String | 

begin
  # Deletes a Category
  result = api_instance.trainings_categories_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsCategoryApi->trainings_categories_id_delete: #{e}"
end
```

#### Using the trainings_categories_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsCategory>, Integer, Hash)> trainings_categories_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Category
  data, status_code, headers = api_instance.trainings_categories_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsCategory>
rescue F::ApiError => e
  puts "Error when calling TrainingsCategoryApi->trainings_categories_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**TrainingsCategory**](TrainingsCategory.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_categories_id_get

> <TrainingsCategory> trainings_categories_id_get(id)

Reads a single Category

Reads a single Category

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

api_instance = F::TrainingsCategoryApi.new
id = '1' # String | 

begin
  # Reads a single Category
  result = api_instance.trainings_categories_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsCategoryApi->trainings_categories_id_get: #{e}"
end
```

#### Using the trainings_categories_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsCategory>, Integer, Hash)> trainings_categories_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Category
  data, status_code, headers = api_instance.trainings_categories_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsCategory>
rescue F::ApiError => e
  puts "Error when calling TrainingsCategoryApi->trainings_categories_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**TrainingsCategory**](TrainingsCategory.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_categories_post

> <TrainingsCategory> trainings_categories_post(opts)

Creates a Category

Creates a Category

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

api_instance = F::TrainingsCategoryApi.new
opts = {
  trainings_categories_post_request: F::TrainingsCategoriesPostRequest.new({name: 'name_example', company_id: 'company_id_example'}) # TrainingsCategoriesPostRequest | 
}

begin
  # Creates a Category
  result = api_instance.trainings_categories_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsCategoryApi->trainings_categories_post: #{e}"
end
```

#### Using the trainings_categories_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsCategory>, Integer, Hash)> trainings_categories_post_with_http_info(opts)

```ruby
begin
  # Creates a Category
  data, status_code, headers = api_instance.trainings_categories_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsCategory>
rescue F::ApiError => e
  puts "Error when calling TrainingsCategoryApi->trainings_categories_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **trainings_categories_post_request** | [**TrainingsCategoriesPostRequest**](TrainingsCategoriesPostRequest.md) |  | [optional] |

### Return type

[**TrainingsCategory**](TrainingsCategory.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

