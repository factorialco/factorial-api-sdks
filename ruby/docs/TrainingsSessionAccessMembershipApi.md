# F::TrainingsSessionAccessMembershipApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**trainings_session_access_memberships_bulk_create_post**](TrainingsSessionAccessMembershipApi.md#trainings_session_access_memberships_bulk_create_post) | **POST** /api/2026-07-01/resources/trainings/session_access_memberships/bulk_create | Bulk creates a Session access membership |
| [**trainings_session_access_memberships_bulk_destroy_post**](TrainingsSessionAccessMembershipApi.md#trainings_session_access_memberships_bulk_destroy_post) | **POST** /api/2026-07-01/resources/trainings/session_access_memberships/bulk_destroy | Bulk destroys a Session access membership |
| [**trainings_session_access_memberships_get**](TrainingsSessionAccessMembershipApi.md#trainings_session_access_memberships_get) | **GET** /api/2026-07-01/resources/trainings/session_access_memberships | Reads all Session access memberships |
| [**trainings_session_access_memberships_id_get**](TrainingsSessionAccessMembershipApi.md#trainings_session_access_memberships_id_get) | **GET** /api/2026-07-01/resources/trainings/session_access_memberships/{id} | Reads a single Session access membership |


## trainings_session_access_memberships_bulk_create_post

> <Array<TrainingsSessionAccessMembership>> trainings_session_access_memberships_bulk_create_post(opts)

Bulk creates a Session access membership

Bulk creates a Session access membership

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

api_instance = F::TrainingsSessionAccessMembershipApi.new
opts = {
  trainings_session_access_memberships_bulk_create_post_request: F::TrainingsSessionAccessMembershipsBulkCreatePostRequest.new({session_id: 'session_id_example', notify: false}) # TrainingsSessionAccessMembershipsBulkCreatePostRequest | 
}

begin
  # Bulk creates a Session access membership
  result = api_instance.trainings_session_access_memberships_bulk_create_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionAccessMembershipApi->trainings_session_access_memberships_bulk_create_post: #{e}"
end
```

#### Using the trainings_session_access_memberships_bulk_create_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<TrainingsSessionAccessMembership>>, Integer, Hash)> trainings_session_access_memberships_bulk_create_post_with_http_info(opts)

```ruby
begin
  # Bulk creates a Session access membership
  data, status_code, headers = api_instance.trainings_session_access_memberships_bulk_create_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<TrainingsSessionAccessMembership>>
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionAccessMembershipApi->trainings_session_access_memberships_bulk_create_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **trainings_session_access_memberships_bulk_create_post_request** | [**TrainingsSessionAccessMembershipsBulkCreatePostRequest**](TrainingsSessionAccessMembershipsBulkCreatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;TrainingsSessionAccessMembership&gt;**](TrainingsSessionAccessMembership.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## trainings_session_access_memberships_bulk_destroy_post

> <Array<TrainingsSessionAccessMembership>> trainings_session_access_memberships_bulk_destroy_post(opts)

Bulk destroys a Session access membership

Bulk destroys a Session access membership

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

api_instance = F::TrainingsSessionAccessMembershipApi.new
opts = {
  trainings_session_access_memberships_bulk_destroy_post_request: F::TrainingsSessionAccessMembershipsBulkDestroyPostRequest.new({ids: ['ids_example'], notify: false}) # TrainingsSessionAccessMembershipsBulkDestroyPostRequest | 
}

begin
  # Bulk destroys a Session access membership
  result = api_instance.trainings_session_access_memberships_bulk_destroy_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionAccessMembershipApi->trainings_session_access_memberships_bulk_destroy_post: #{e}"
end
```

#### Using the trainings_session_access_memberships_bulk_destroy_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<TrainingsSessionAccessMembership>>, Integer, Hash)> trainings_session_access_memberships_bulk_destroy_post_with_http_info(opts)

```ruby
begin
  # Bulk destroys a Session access membership
  data, status_code, headers = api_instance.trainings_session_access_memberships_bulk_destroy_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<TrainingsSessionAccessMembership>>
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionAccessMembershipApi->trainings_session_access_memberships_bulk_destroy_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **trainings_session_access_memberships_bulk_destroy_post_request** | [**TrainingsSessionAccessMembershipsBulkDestroyPostRequest**](TrainingsSessionAccessMembershipsBulkDestroyPostRequest.md) |  | [optional] |

### Return type

[**Array&lt;TrainingsSessionAccessMembership&gt;**](TrainingsSessionAccessMembership.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## trainings_session_access_memberships_get

> <TrainingsSessionAccessMembershipsGet200Response> trainings_session_access_memberships_get(session_id, opts)

Reads all Session access memberships

Reads all Session access memberships

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

api_instance = F::TrainingsSessionAccessMembershipApi.new
session_id = '1' # String | Filter memberships by session ID
opts = {
  ids: ['inner_example'], # Array<String> | Filter memberships by specific IDs
  search: 'John', # String | Filter memberships by user name
  team_ids: ['inner_example'], # Array<String> | ID of the team associated with this membership
  status: ['inner_example'] # Array<String> | Current status of the session attendance
}

begin
  # Reads all Session access memberships
  result = api_instance.trainings_session_access_memberships_get(session_id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionAccessMembershipApi->trainings_session_access_memberships_get: #{e}"
end
```

#### Using the trainings_session_access_memberships_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsSessionAccessMembershipsGet200Response>, Integer, Hash)> trainings_session_access_memberships_get_with_http_info(session_id, opts)

```ruby
begin
  # Reads all Session access memberships
  data, status_code, headers = api_instance.trainings_session_access_memberships_get_with_http_info(session_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsSessionAccessMembershipsGet200Response>
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionAccessMembershipApi->trainings_session_access_memberships_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **session_id** | **String** | Filter memberships by session ID |  |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter memberships by specific IDs | [optional] |
| **search** | **String** | Filter memberships by user name | [optional] |
| **team_ids** | [**Array&lt;String&gt;**](String.md) | ID of the team associated with this membership | [optional] |
| **status** | [**Array&lt;String&gt;**](String.md) | Current status of the session attendance | [optional] |

### Return type

[**TrainingsSessionAccessMembershipsGet200Response**](TrainingsSessionAccessMembershipsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_session_access_memberships_id_get

> <TrainingsSessionAccessMembership> trainings_session_access_memberships_id_get(id)

Reads a single Session access membership

Reads a single Session access membership

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

api_instance = F::TrainingsSessionAccessMembershipApi.new
id = '1' # String | Filter memberships by specific IDs

begin
  # Reads a single Session access membership
  result = api_instance.trainings_session_access_memberships_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionAccessMembershipApi->trainings_session_access_memberships_id_get: #{e}"
end
```

#### Using the trainings_session_access_memberships_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsSessionAccessMembership>, Integer, Hash)> trainings_session_access_memberships_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Session access membership
  data, status_code, headers = api_instance.trainings_session_access_memberships_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsSessionAccessMembership>
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionAccessMembershipApi->trainings_session_access_memberships_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter memberships by specific IDs |  |

### Return type

[**TrainingsSessionAccessMembership**](TrainingsSessionAccessMembership.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

