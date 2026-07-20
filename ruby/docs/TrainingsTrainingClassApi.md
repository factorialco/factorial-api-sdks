# F::TrainingsTrainingClassApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**trainings_training_classes_get**](TrainingsTrainingClassApi.md#trainings_training_classes_get) | **GET** /api/2026-07-01/resources/trainings/training_classes | Reads all Training classes |
| [**trainings_training_classes_id_delete**](TrainingsTrainingClassApi.md#trainings_training_classes_id_delete) | **DELETE** /api/2026-07-01/resources/trainings/training_classes/{id} | Deletes a Training class |
| [**trainings_training_classes_id_get**](TrainingsTrainingClassApi.md#trainings_training_classes_id_get) | **GET** /api/2026-07-01/resources/trainings/training_classes/{id} | Reads a single Training class |
| [**trainings_training_classes_id_put**](TrainingsTrainingClassApi.md#trainings_training_classes_id_put) | **PUT** /api/2026-07-01/resources/trainings/training_classes/{id} | Updates a Training class |
| [**trainings_training_classes_post**](TrainingsTrainingClassApi.md#trainings_training_classes_post) | **POST** /api/2026-07-01/resources/trainings/training_classes | Creates a Training class |


## trainings_training_classes_get

> <TrainingsTrainingClassesGet200Response> trainings_training_classes_get(opts)

Reads all Training classes

Reads all Training classes

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

api_instance = F::TrainingsTrainingClassApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Filter those training classes whose id match with the given.
  id: 'id_example', # String | Get a specific training class.
  training_id: 'training_id_example', # String | Get training classes for the specified training.
  search: 'search_example', # String | This field is used to search in the training class name.
  start_date: ['inner_example'], # Array<String> | Field those classes that start on the given date.
  end_date: ['inner_example'] # Array<String> | Filter those classes that end on the given date.
}

begin
  # Reads all Training classes
  result = api_instance.trainings_training_classes_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingClassApi->trainings_training_classes_get: #{e}"
end
```

#### Using the trainings_training_classes_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsTrainingClassesGet200Response>, Integer, Hash)> trainings_training_classes_get_with_http_info(opts)

```ruby
begin
  # Reads all Training classes
  data, status_code, headers = api_instance.trainings_training_classes_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsTrainingClassesGet200Response>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingClassApi->trainings_training_classes_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter those training classes whose id match with the given. | [optional] |
| **id** | **String** | Get a specific training class. | [optional] |
| **training_id** | **String** | Get training classes for the specified training. | [optional] |
| **search** | **String** | This field is used to search in the training class name. | [optional] |
| **start_date** | [**Array&lt;String&gt;**](String.md) | Field those classes that start on the given date. | [optional] |
| **end_date** | [**Array&lt;String&gt;**](String.md) | Filter those classes that end on the given date. | [optional] |

### Return type

[**TrainingsTrainingClassesGet200Response**](TrainingsTrainingClassesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_training_classes_id_delete

> <TrainingsTrainingClass> trainings_training_classes_id_delete(id)

Deletes a Training class

Deletes a Training class

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

api_instance = F::TrainingsTrainingClassApi.new
id = '1' # String | Identifier of the training class to delete

begin
  # Deletes a Training class
  result = api_instance.trainings_training_classes_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingClassApi->trainings_training_classes_id_delete: #{e}"
end
```

#### Using the trainings_training_classes_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsTrainingClass>, Integer, Hash)> trainings_training_classes_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Training class
  data, status_code, headers = api_instance.trainings_training_classes_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsTrainingClass>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingClassApi->trainings_training_classes_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the training class to delete |  |

### Return type

[**TrainingsTrainingClass**](TrainingsTrainingClass.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_training_classes_id_get

> <TrainingsTrainingClass> trainings_training_classes_id_get(id)

Reads a single Training class

Reads a single Training class

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

api_instance = F::TrainingsTrainingClassApi.new
id = '1' # String | Filter those training classes whose id match with the given.

begin
  # Reads a single Training class
  result = api_instance.trainings_training_classes_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingClassApi->trainings_training_classes_id_get: #{e}"
end
```

#### Using the trainings_training_classes_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsTrainingClass>, Integer, Hash)> trainings_training_classes_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Training class
  data, status_code, headers = api_instance.trainings_training_classes_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsTrainingClass>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingClassApi->trainings_training_classes_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter those training classes whose id match with the given. |  |

### Return type

[**TrainingsTrainingClass**](TrainingsTrainingClass.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_training_classes_id_put

> <TrainingsTrainingClass> trainings_training_classes_id_put(id, opts)

Updates a Training class

Updates a Training class

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

api_instance = F::TrainingsTrainingClassApi.new
id = '1' # String | Identifier of the training class to update
opts = {
  trainings_training_classes_id_put_request: F::TrainingsTrainingClassesIdPutRequest.new({id: '1', cost: '100.0', subsidized_cost: '50.0', salary_cost: '60.0', indirect_cost: '30.0', payment_status: 'paid'}) # TrainingsTrainingClassesIdPutRequest | 
}

begin
  # Updates a Training class
  result = api_instance.trainings_training_classes_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingClassApi->trainings_training_classes_id_put: #{e}"
end
```

#### Using the trainings_training_classes_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsTrainingClass>, Integer, Hash)> trainings_training_classes_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Training class
  data, status_code, headers = api_instance.trainings_training_classes_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsTrainingClass>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingClassApi->trainings_training_classes_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the training class to update |  |
| **trainings_training_classes_id_put_request** | [**TrainingsTrainingClassesIdPutRequest**](TrainingsTrainingClassesIdPutRequest.md) |  | [optional] |

### Return type

[**TrainingsTrainingClass**](TrainingsTrainingClass.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## trainings_training_classes_post

> <TrainingsTrainingClass> trainings_training_classes_post(opts)

Creates a Training class

Creates a Training class

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

api_instance = F::TrainingsTrainingClassApi.new
opts = {
  trainings_training_classes_post_request: F::TrainingsTrainingClassesPostRequest.new({start_date: '2025-03-24', end_date: '2025-03-28', training_id: '1', company_id: '1', author_id: '20', cost: '100.0', subsidized_cost: '50.0', indirect_cost: '30.0', salary_cost: '60.0', payment_status: 'paid'}) # TrainingsTrainingClassesPostRequest | 
}

begin
  # Creates a Training class
  result = api_instance.trainings_training_classes_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingClassApi->trainings_training_classes_post: #{e}"
end
```

#### Using the trainings_training_classes_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsTrainingClass>, Integer, Hash)> trainings_training_classes_post_with_http_info(opts)

```ruby
begin
  # Creates a Training class
  data, status_code, headers = api_instance.trainings_training_classes_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsTrainingClass>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingClassApi->trainings_training_classes_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **trainings_training_classes_post_request** | [**TrainingsTrainingClassesPostRequest**](TrainingsTrainingClassesPostRequest.md) |  | [optional] |

### Return type

[**TrainingsTrainingClass**](TrainingsTrainingClass.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

