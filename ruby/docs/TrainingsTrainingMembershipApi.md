# F::TrainingsTrainingMembershipApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**trainings_training_memberships_bulk_create_post**](TrainingsTrainingMembershipApi.md#trainings_training_memberships_bulk_create_post) | **POST** /api/2026-07-01/resources/trainings/training_memberships/bulk_create | Bulk creates a Training membership |
| [**trainings_training_memberships_bulk_destroy_post**](TrainingsTrainingMembershipApi.md#trainings_training_memberships_bulk_destroy_post) | **POST** /api/2026-07-01/resources/trainings/training_memberships/bulk_destroy | Bulk destroys a Training membership |
| [**trainings_training_memberships_get**](TrainingsTrainingMembershipApi.md#trainings_training_memberships_get) | **GET** /api/2026-07-01/resources/trainings/training_memberships | Reads all Training memberships |
| [**trainings_training_memberships_id_get**](TrainingsTrainingMembershipApi.md#trainings_training_memberships_id_get) | **GET** /api/2026-07-01/resources/trainings/training_memberships/{id} | Reads a single Training membership |
| [**trainings_training_memberships_id_put**](TrainingsTrainingMembershipApi.md#trainings_training_memberships_id_put) | **PUT** /api/2026-07-01/resources/trainings/training_memberships/{id} | Updates a Training membership |


## trainings_training_memberships_bulk_create_post

> <Array<TrainingsTrainingMembership>> trainings_training_memberships_bulk_create_post(opts)

Bulk creates a Training membership

Creates training memberships in bulk

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

api_instance = F::TrainingsTrainingMembershipApi.new
opts = {
  trainings_training_memberships_bulk_create_post_request: F::TrainingsTrainingMembershipsBulkCreatePostRequest.new({employee_ids: ["20"], training_id: '1'}) # TrainingsTrainingMembershipsBulkCreatePostRequest | 
}

begin
  # Bulk creates a Training membership
  result = api_instance.trainings_training_memberships_bulk_create_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingMembershipApi->trainings_training_memberships_bulk_create_post: #{e}"
end
```

#### Using the trainings_training_memberships_bulk_create_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<TrainingsTrainingMembership>>, Integer, Hash)> trainings_training_memberships_bulk_create_post_with_http_info(opts)

```ruby
begin
  # Bulk creates a Training membership
  data, status_code, headers = api_instance.trainings_training_memberships_bulk_create_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<TrainingsTrainingMembership>>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingMembershipApi->trainings_training_memberships_bulk_create_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **trainings_training_memberships_bulk_create_post_request** | [**TrainingsTrainingMembershipsBulkCreatePostRequest**](TrainingsTrainingMembershipsBulkCreatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;TrainingsTrainingMembership&gt;**](TrainingsTrainingMembership.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## trainings_training_memberships_bulk_destroy_post

> <Array<TrainingsTrainingMembership>> trainings_training_memberships_bulk_destroy_post(opts)

Bulk destroys a Training membership

Deletes training memberships in bulk

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

api_instance = F::TrainingsTrainingMembershipApi.new
opts = {
  trainings_training_memberships_bulk_destroy_post_request: F::TrainingsTrainingMembershipsBulkDestroyPostRequest.new({ids: ["1", "2"]}) # TrainingsTrainingMembershipsBulkDestroyPostRequest | 
}

begin
  # Bulk destroys a Training membership
  result = api_instance.trainings_training_memberships_bulk_destroy_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingMembershipApi->trainings_training_memberships_bulk_destroy_post: #{e}"
end
```

#### Using the trainings_training_memberships_bulk_destroy_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<TrainingsTrainingMembership>>, Integer, Hash)> trainings_training_memberships_bulk_destroy_post_with_http_info(opts)

```ruby
begin
  # Bulk destroys a Training membership
  data, status_code, headers = api_instance.trainings_training_memberships_bulk_destroy_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<TrainingsTrainingMembership>>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingMembershipApi->trainings_training_memberships_bulk_destroy_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **trainings_training_memberships_bulk_destroy_post_request** | [**TrainingsTrainingMembershipsBulkDestroyPostRequest**](TrainingsTrainingMembershipsBulkDestroyPostRequest.md) |  | [optional] |

### Return type

[**Array&lt;TrainingsTrainingMembership&gt;**](TrainingsTrainingMembership.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## trainings_training_memberships_get

> <TrainingsTrainingMembershipsGet200Response> trainings_training_memberships_get(due_date, opts)

Reads all Training memberships

Reads all Training memberships

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

api_instance = F::TrainingsTrainingMembershipApi.new
due_date = '7' # String | This field is used to filter training memberships by due date. Values can be 'overdue', 'no_due_date', or a number of days (e.g., '7', '30', '90').
opts = {
  training_id: '1', # String | This field is used to filter those trainings memberships that belongs to this training.
  ids: ['inner_example'], # Array<String> | This field is used to filter those trainings memberships whose id match with the given.
  search: 'Jane', # String | This field is used to filter those trainings memberships whose employee name include some of the text written.
  team_id: '1', # String | This field is used to filter those memberships whose employees belongs to this team.
  status: 'notstarted', # String | This field is used to filter those trainings memberships whose attendance status is the given.
  class_id: '1', # String | This field is used to filter those trainings memberships whose employees belongs to this group.
  employee_id: '20' # String | Get the training memberships by passing the employee id
}

begin
  # Reads all Training memberships
  result = api_instance.trainings_training_memberships_get(due_date, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingMembershipApi->trainings_training_memberships_get: #{e}"
end
```

#### Using the trainings_training_memberships_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsTrainingMembershipsGet200Response>, Integer, Hash)> trainings_training_memberships_get_with_http_info(due_date, opts)

```ruby
begin
  # Reads all Training memberships
  data, status_code, headers = api_instance.trainings_training_memberships_get_with_http_info(due_date, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsTrainingMembershipsGet200Response>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingMembershipApi->trainings_training_memberships_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **due_date** | **String** | This field is used to filter training memberships by due date. Values can be &#39;overdue&#39;, &#39;no_due_date&#39;, or a number of days (e.g., &#39;7&#39;, &#39;30&#39;, &#39;90&#39;). |  |
| **training_id** | **String** | This field is used to filter those trainings memberships that belongs to this training. | [optional] |
| **ids** | [**Array&lt;String&gt;**](String.md) | This field is used to filter those trainings memberships whose id match with the given. | [optional] |
| **search** | **String** | This field is used to filter those trainings memberships whose employee name include some of the text written. | [optional] |
| **team_id** | **String** | This field is used to filter those memberships whose employees belongs to this team. | [optional] |
| **status** | **String** | This field is used to filter those trainings memberships whose attendance status is the given. | [optional] |
| **class_id** | **String** | This field is used to filter those trainings memberships whose employees belongs to this group. | [optional] |
| **employee_id** | **String** | Get the training memberships by passing the employee id | [optional] |

### Return type

[**TrainingsTrainingMembershipsGet200Response**](TrainingsTrainingMembershipsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_training_memberships_id_get

> <TrainingsTrainingMembership> trainings_training_memberships_id_get(id)

Reads a single Training membership

Reads a single Training membership

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

api_instance = F::TrainingsTrainingMembershipApi.new
id = '1' # String | This field is used to filter those trainings memberships whose id match with the given.

begin
  # Reads a single Training membership
  result = api_instance.trainings_training_memberships_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingMembershipApi->trainings_training_memberships_id_get: #{e}"
end
```

#### Using the trainings_training_memberships_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsTrainingMembership>, Integer, Hash)> trainings_training_memberships_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Training membership
  data, status_code, headers = api_instance.trainings_training_memberships_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsTrainingMembership>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingMembershipApi->trainings_training_memberships_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | This field is used to filter those trainings memberships whose id match with the given. |  |

### Return type

[**TrainingsTrainingMembership**](TrainingsTrainingMembership.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_training_memberships_id_put

> <TrainingsTrainingMembership> trainings_training_memberships_id_put(id, opts)

Updates a Training membership

Update a training membership

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

api_instance = F::TrainingsTrainingMembershipApi.new
id = '1' # String | Unique identifier for the training membership. Only used to identify the training membership to update.
opts = {
  trainings_training_memberships_id_put_request: F::TrainingsTrainingMembershipsIdPutRequest.new({id: '1'}) # TrainingsTrainingMembershipsIdPutRequest | 
}

begin
  # Updates a Training membership
  result = api_instance.trainings_training_memberships_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingMembershipApi->trainings_training_memberships_id_put: #{e}"
end
```

#### Using the trainings_training_memberships_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsTrainingMembership>, Integer, Hash)> trainings_training_memberships_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Training membership
  data, status_code, headers = api_instance.trainings_training_memberships_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsTrainingMembership>
rescue F::ApiError => e
  puts "Error when calling TrainingsTrainingMembershipApi->trainings_training_memberships_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier for the training membership. Only used to identify the training membership to update. |  |
| **trainings_training_memberships_id_put_request** | [**TrainingsTrainingMembershipsIdPutRequest**](TrainingsTrainingMembershipsIdPutRequest.md) |  | [optional] |

### Return type

[**TrainingsTrainingMembership**](TrainingsTrainingMembership.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

