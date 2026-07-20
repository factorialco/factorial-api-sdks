# F::TrainingsTrainingApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**trainings_trainings_bulk_delete_post**](TrainingsTrainingApi.md#trainings_trainings_bulk_delete_post) | **POST** /api/2026-07-01/resources/trainings/trainings/bulk_delete | Bulk deletes a Training |
| [**trainings_trainings_bulk_update_catalog_post**](TrainingsTrainingApi.md#trainings_trainings_bulk_update_catalog_post) | **POST** /api/2026-07-01/resources/trainings/trainings/bulk_update_catalog | Bulk update catalogs a Training |
| [**trainings_trainings_get**](TrainingsTrainingApi.md#trainings_trainings_get) | **GET** /api/2026-07-01/resources/trainings/trainings | Reads all Trainings |
| [**trainings_trainings_id_delete**](TrainingsTrainingApi.md#trainings_trainings_id_delete) | **DELETE** /api/2026-07-01/resources/trainings/trainings/{id} | Deletes a Training |
| [**trainings_trainings_id_get**](TrainingsTrainingApi.md#trainings_trainings_id_get) | **GET** /api/2026-07-01/resources/trainings/trainings/{id} | Reads a single Training |
| [**trainings_trainings_id_put**](TrainingsTrainingApi.md#trainings_trainings_id_put) | **PUT** /api/2026-07-01/resources/trainings/trainings/{id} | Updates a Training |
| [**trainings_trainings_post**](TrainingsTrainingApi.md#trainings_trainings_post) | **POST** /api/2026-07-01/resources/trainings/trainings | Creates a Training |
| [**trainings_trainings_update_status_post**](TrainingsTrainingApi.md#trainings_trainings_update_status_post) | **POST** /api/2026-07-01/resources/trainings/trainings/update_status | Update statuses a Training |


## trainings_trainings_bulk_delete_post

> <Array<TrainingsTraining>> trainings_trainings_bulk_delete_post(opts)

Bulk deletes a Training

Bulk deletes a Training

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

api_instance = F::TrainingsTrainingApi.new
opts = {
  expenses_expensables_bulk_set_to_paid_post_request: F::ExpensesExpensablesBulkSetToPaidPostRequest.new({ids: ["1"]}) # ExpensesExpensablesBulkSetToPaidPostRequest | 
}

begin
  # Bulk deletes a Training
  result = api_instance.trainings_trainings_bulk_delete_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_bulk_delete_post: #{e}"
end
```

#### Using the trainings_trainings_bulk_delete_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<TrainingsTraining>>, Integer, Hash)> trainings_trainings_bulk_delete_post_with_http_info(opts)

```ruby
begin
  # Bulk deletes a Training
  data, status_code, headers = api_instance.trainings_trainings_bulk_delete_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<TrainingsTraining>>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_bulk_delete_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **expenses_expensables_bulk_set_to_paid_post_request** | [**ExpensesExpensablesBulkSetToPaidPostRequest**](ExpensesExpensablesBulkSetToPaidPostRequest.md) |  | [optional] |

### Return type

[**Array&lt;TrainingsTraining&gt;**](TrainingsTraining.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## trainings_trainings_bulk_update_catalog_post

> <Array<TrainingsTraining>> trainings_trainings_bulk_update_catalog_post(opts)

Bulk update catalogs a Training

Bulk update catalogs a Training

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

api_instance = F::TrainingsTrainingApi.new
opts = {
  trainings_trainings_bulk_update_catalog_post_request: F::TrainingsTrainingsBulkUpdateCatalogPostRequest.new({ids: ['ids_example'], catalog: false}) # TrainingsTrainingsBulkUpdateCatalogPostRequest | 
}

begin
  # Bulk update catalogs a Training
  result = api_instance.trainings_trainings_bulk_update_catalog_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_bulk_update_catalog_post: #{e}"
end
```

#### Using the trainings_trainings_bulk_update_catalog_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<TrainingsTraining>>, Integer, Hash)> trainings_trainings_bulk_update_catalog_post_with_http_info(opts)

```ruby
begin
  # Bulk update catalogs a Training
  data, status_code, headers = api_instance.trainings_trainings_bulk_update_catalog_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<TrainingsTraining>>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_bulk_update_catalog_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **trainings_trainings_bulk_update_catalog_post_request** | [**TrainingsTrainingsBulkUpdateCatalogPostRequest**](TrainingsTrainingsBulkUpdateCatalogPostRequest.md) |  | [optional] |

### Return type

[**Array&lt;TrainingsTraining&gt;**](TrainingsTraining.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## trainings_trainings_get

> <TrainingsTrainingsGet200Response> trainings_trainings_get(opts)

Reads all Trainings

Reads all Trainings

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

api_instance = F::TrainingsTrainingApi.new
opts = {
  id: 'id_example', # String | This field is used to get a specific training.
  ids: ['inner_example'], # Array<String> | This field is used to filter those trainings whose id match with the given.
  access_id: 'access_id_example', # String | @deprecated
  search: 'search_example', # String | This field is used to search in the training name, training description or training category.
  status: 'status_example', # String | This field is used to filter those trainings whose status is the same as the one we pass.
  catalog: true, # Boolean | This field is used to filter those trainings whose are visible in the catalog.
  only_assigned: true, # Boolean | This field is used to filter those trainings whose attendance status is different from not assigned.
  with_expired_memberships: true, # Boolean | This field is used to filter those trainings whose members have the course expired (if 'true') or not (if 'false').
  return_expired_memberships: true, # Boolean | Fills the information of the field 'number_of_expired_participants' if 'true'
  is_mandatory: false, # Boolean | This field is used to filter by mandatory or non-mandatory trainings if provided
  with_current_training_classes: false # Boolean | This field is used to filter those trainings whose have current training classes if 'true'
}

begin
  # Reads all Trainings
  result = api_instance.trainings_trainings_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_get: #{e}"
end
```

#### Using the trainings_trainings_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsTrainingsGet200Response>, Integer, Hash)> trainings_trainings_get_with_http_info(opts)

```ruby
begin
  # Reads all Trainings
  data, status_code, headers = api_instance.trainings_trainings_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsTrainingsGet200Response>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | This field is used to get a specific training. | [optional] |
| **ids** | [**Array&lt;String&gt;**](String.md) | This field is used to filter those trainings whose id match with the given. | [optional] |
| **access_id** | **String** | @deprecated | [optional] |
| **search** | **String** | This field is used to search in the training name, training description or training category. | [optional] |
| **status** | **String** | This field is used to filter those trainings whose status is the same as the one we pass. | [optional] |
| **catalog** | **Boolean** | This field is used to filter those trainings whose are visible in the catalog. | [optional] |
| **only_assigned** | **Boolean** | This field is used to filter those trainings whose attendance status is different from not assigned. | [optional] |
| **with_expired_memberships** | **Boolean** | This field is used to filter those trainings whose members have the course expired (if &#39;true&#39;) or not (if &#39;false&#39;). | [optional] |
| **return_expired_memberships** | **Boolean** | Fills the information of the field &#39;number_of_expired_participants&#39; if &#39;true&#39; | [optional] |
| **is_mandatory** | **Boolean** | This field is used to filter by mandatory or non-mandatory trainings if provided | [optional] |
| **with_current_training_classes** | **Boolean** | This field is used to filter those trainings whose have current training classes if &#39;true&#39; | [optional] |

### Return type

[**TrainingsTrainingsGet200Response**](TrainingsTrainingsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_trainings_id_delete

> <TrainingsTraining> trainings_trainings_id_delete(id)

Deletes a Training

Deletes a Training

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

api_instance = F::TrainingsTrainingApi.new
id = '1' # String | 

begin
  # Deletes a Training
  result = api_instance.trainings_trainings_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_id_delete: #{e}"
end
```

#### Using the trainings_trainings_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsTraining>, Integer, Hash)> trainings_trainings_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Training
  data, status_code, headers = api_instance.trainings_trainings_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsTraining>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**TrainingsTraining**](TrainingsTraining.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_trainings_id_get

> <TrainingsTraining> trainings_trainings_id_get(id)

Reads a single Training

Reads a single Training

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

api_instance = F::TrainingsTrainingApi.new
id = '1' # String | This field is used to get a specific training.

begin
  # Reads a single Training
  result = api_instance.trainings_trainings_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_id_get: #{e}"
end
```

#### Using the trainings_trainings_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsTraining>, Integer, Hash)> trainings_trainings_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Training
  data, status_code, headers = api_instance.trainings_trainings_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsTraining>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | This field is used to get a specific training. |  |

### Return type

[**TrainingsTraining**](TrainingsTraining.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_trainings_id_put

> <TrainingsTraining> trainings_trainings_id_put(id, opts)

Updates a Training

Updates a Training

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

api_instance = F::TrainingsTrainingApi.new
id = '1' # String | 
opts = {
  trainings_trainings_id_put_request: F::TrainingsTrainingsIdPutRequest.new({id: 'id_example', name: 'name_example', description: 'description_example', external: false, year: 37}) # TrainingsTrainingsIdPutRequest | 
}

begin
  # Updates a Training
  result = api_instance.trainings_trainings_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_id_put: #{e}"
end
```

#### Using the trainings_trainings_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsTraining>, Integer, Hash)> trainings_trainings_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Training
  data, status_code, headers = api_instance.trainings_trainings_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsTraining>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **trainings_trainings_id_put_request** | [**TrainingsTrainingsIdPutRequest**](TrainingsTrainingsIdPutRequest.md) |  | [optional] |

### Return type

[**TrainingsTraining**](TrainingsTraining.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## trainings_trainings_post

> <TrainingsTraining> trainings_trainings_post(opts)

Creates a Training

Creates a Training

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

api_instance = F::TrainingsTrainingApi.new
opts = {
  trainings_trainings_post_request: F::TrainingsTrainingsPostRequest.new({name: 'Communication Course', description: 'Intermediate-level communication course that focuses on building and enhancing language skills.', external: false, year: 2022, attachments: [3.56]}) # TrainingsTrainingsPostRequest | 
}

begin
  # Creates a Training
  result = api_instance.trainings_trainings_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_post: #{e}"
end
```

#### Using the trainings_trainings_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsTraining>, Integer, Hash)> trainings_trainings_post_with_http_info(opts)

```ruby
begin
  # Creates a Training
  data, status_code, headers = api_instance.trainings_trainings_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsTraining>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **trainings_trainings_post_request** | [**TrainingsTrainingsPostRequest**](TrainingsTrainingsPostRequest.md) |  | [optional] |

### Return type

[**TrainingsTraining**](TrainingsTraining.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## trainings_trainings_update_status_post

> <TrainingsTraining> trainings_trainings_update_status_post(opts)

Update statuses a Training

Update statuses a Training

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

api_instance = F::TrainingsTrainingApi.new
opts = {
  trainings_trainings_update_status_post_request: F::TrainingsTrainingsUpdateStatusPostRequest.new({id: 'id_example', status: 'status_example', notify: false}) # TrainingsTrainingsUpdateStatusPostRequest | 
}

begin
  # Update statuses a Training
  result = api_instance.trainings_trainings_update_status_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_update_status_post: #{e}"
end
```

#### Using the trainings_trainings_update_status_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsTraining>, Integer, Hash)> trainings_trainings_update_status_post_with_http_info(opts)

```ruby
begin
  # Update statuses a Training
  data, status_code, headers = api_instance.trainings_trainings_update_status_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsTraining>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingApi->trainings_trainings_update_status_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **trainings_trainings_update_status_post_request** | [**TrainingsTrainingsUpdateStatusPostRequest**](TrainingsTrainingsUpdateStatusPostRequest.md) |  | [optional] |

### Return type

[**TrainingsTraining**](TrainingsTraining.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

