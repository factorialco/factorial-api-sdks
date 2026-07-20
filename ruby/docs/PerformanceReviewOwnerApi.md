# F::PerformanceReviewOwnerApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**performance_review_owners_bulk_create_post**](PerformanceReviewOwnerApi.md#performance_review_owners_bulk_create_post) | **POST** /api/2026-07-01/resources/performance/review_owners/bulk_create | Bulk creates a Review owner |
| [**performance_review_owners_get**](PerformanceReviewOwnerApi.md#performance_review_owners_get) | **GET** /api/2026-07-01/resources/performance/review_owners | Reads all Review owners |
| [**performance_review_owners_id_delete**](PerformanceReviewOwnerApi.md#performance_review_owners_id_delete) | **DELETE** /api/2026-07-01/resources/performance/review_owners/{id} | Deletes a Review owner |


## performance_review_owners_bulk_create_post

> <Array<PerformanceReviewOwner>> performance_review_owners_bulk_create_post(opts)

Bulk creates a Review owner

Add multiple owners to a review process.

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

api_instance = F::PerformanceReviewOwnerApi.new
opts = {
  performance_review_owners_bulk_create_post_request: F::PerformanceReviewOwnersBulkCreatePostRequest.new({review_process_id: '1', owner_access_ids: ["1", "2", "3"]}) # PerformanceReviewOwnersBulkCreatePostRequest | 
}

begin
  # Bulk creates a Review owner
  result = api_instance.performance_review_owners_bulk_create_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewOwnerApi->performance_review_owners_bulk_create_post: #{e}"
end
```

#### Using the performance_review_owners_bulk_create_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<PerformanceReviewOwner>>, Integer, Hash)> performance_review_owners_bulk_create_post_with_http_info(opts)

```ruby
begin
  # Bulk creates a Review owner
  data, status_code, headers = api_instance.performance_review_owners_bulk_create_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<PerformanceReviewOwner>>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewOwnerApi->performance_review_owners_bulk_create_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_owners_bulk_create_post_request** | [**PerformanceReviewOwnersBulkCreatePostRequest**](PerformanceReviewOwnersBulkCreatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;PerformanceReviewOwner&gt;**](PerformanceReviewOwner.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_owners_get

> <PerformanceReviewOwnersGet200Response> performance_review_owners_get(opts)

Reads all Review owners

Retrieves the review owners of review processes (each process has at least one owner). The owners can edit the review process and access its results.

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

api_instance = F::PerformanceReviewOwnerApi.new
opts = {
  performance_review_process_ids: ['inner_example'] # Array<String> | Filter by review process IDs
}

begin
  # Reads all Review owners
  result = api_instance.performance_review_owners_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewOwnerApi->performance_review_owners_get: #{e}"
end
```

#### Using the performance_review_owners_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewOwnersGet200Response>, Integer, Hash)> performance_review_owners_get_with_http_info(opts)

```ruby
begin
  # Reads all Review owners
  data, status_code, headers = api_instance.performance_review_owners_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewOwnersGet200Response>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewOwnerApi->performance_review_owners_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_process_ids** | [**Array&lt;String&gt;**](String.md) | Filter by review process IDs | [optional] |

### Return type

[**PerformanceReviewOwnersGet200Response**](PerformanceReviewOwnersGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_review_owners_id_delete

> <PerformanceReviewOwner> performance_review_owners_id_delete(id)

Deletes a Review owner

Remove an owner from a review process. The review process must have at least one owner.

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

api_instance = F::PerformanceReviewOwnerApi.new
id = '1' # String | Review owner ID

begin
  # Deletes a Review owner
  result = api_instance.performance_review_owners_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewOwnerApi->performance_review_owners_id_delete: #{e}"
end
```

#### Using the performance_review_owners_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewOwner>, Integer, Hash)> performance_review_owners_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Review owner
  data, status_code, headers = api_instance.performance_review_owners_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewOwner>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewOwnerApi->performance_review_owners_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review owner ID |  |

### Return type

[**PerformanceReviewOwner**](PerformanceReviewOwner.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

