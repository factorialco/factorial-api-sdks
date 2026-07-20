# F::PerformanceReviewProcessTargetApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**performance_review_process_targets_add_peers_post**](PerformanceReviewProcessTargetApi.md#performance_review_process_targets_add_peers_post) | **POST** /api/2026-07-01/resources/performance/review_process_targets/add_peers | Add peers a Review process target |
| [**performance_review_process_targets_bulk_create_post**](PerformanceReviewProcessTargetApi.md#performance_review_process_targets_bulk_create_post) | **POST** /api/2026-07-01/resources/performance/review_process_targets/bulk_create | Bulk creates a Review process target |
| [**performance_review_process_targets_get**](PerformanceReviewProcessTargetApi.md#performance_review_process_targets_get) | **GET** /api/2026-07-01/resources/performance/review_process_targets | Reads all Review process targets |
| [**performance_review_process_targets_id_delete**](PerformanceReviewProcessTargetApi.md#performance_review_process_targets_id_delete) | **DELETE** /api/2026-07-01/resources/performance/review_process_targets/{id} | Deletes a Review process target |
| [**performance_review_process_targets_id_get**](PerformanceReviewProcessTargetApi.md#performance_review_process_targets_id_get) | **GET** /api/2026-07-01/resources/performance/review_process_targets/{id} | Reads a single Review process target |
| [**performance_review_process_targets_remove_peer_evaluations_post**](PerformanceReviewProcessTargetApi.md#performance_review_process_targets_remove_peer_evaluations_post) | **POST** /api/2026-07-01/resources/performance/review_process_targets/remove_peer_evaluations | Remove peer evaluations a Review process target |


## performance_review_process_targets_add_peers_post

> <PerformanceReviewProcessTarget> performance_review_process_targets_add_peers_post(opts)

Add peers a Review process target

Assign peers to evaluate a specific participant.

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

api_instance = F::PerformanceReviewProcessTargetApi.new
opts = {
  performance_review_process_targets_add_peers_post_request: F::PerformanceReviewProcessTargetsAddPeersPostRequest.new({id: '1-3', peer_access_ids: ["1", "2", "3"]}) # PerformanceReviewProcessTargetsAddPeersPostRequest | 
}

begin
  # Add peers a Review process target
  result = api_instance.performance_review_process_targets_add_peers_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessTargetApi->performance_review_process_targets_add_peers_post: #{e}"
end
```

#### Using the performance_review_process_targets_add_peers_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcessTarget>, Integer, Hash)> performance_review_process_targets_add_peers_post_with_http_info(opts)

```ruby
begin
  # Add peers a Review process target
  data, status_code, headers = api_instance.performance_review_process_targets_add_peers_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcessTarget>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessTargetApi->performance_review_process_targets_add_peers_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_process_targets_add_peers_post_request** | [**PerformanceReviewProcessTargetsAddPeersPostRequest**](PerformanceReviewProcessTargetsAddPeersPostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcessTarget**](PerformanceReviewProcessTarget.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_process_targets_bulk_create_post

> <Array<PerformanceReviewProcessTarget>> performance_review_process_targets_bulk_create_post(opts)

Bulk creates a Review process target

Add multiple participants to the active review process and create the evaluations for them.

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

api_instance = F::PerformanceReviewProcessTargetApi.new
opts = {
  performance_review_process_targets_bulk_create_post_request: F::PerformanceReviewProcessTargetsBulkCreatePostRequest.new({performance_review_process_id: '1', targets_access_ids: ["1", "2", "3"]}) # PerformanceReviewProcessTargetsBulkCreatePostRequest | 
}

begin
  # Bulk creates a Review process target
  result = api_instance.performance_review_process_targets_bulk_create_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessTargetApi->performance_review_process_targets_bulk_create_post: #{e}"
end
```

#### Using the performance_review_process_targets_bulk_create_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<PerformanceReviewProcessTarget>>, Integer, Hash)> performance_review_process_targets_bulk_create_post_with_http_info(opts)

```ruby
begin
  # Bulk creates a Review process target
  data, status_code, headers = api_instance.performance_review_process_targets_bulk_create_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<PerformanceReviewProcessTarget>>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessTargetApi->performance_review_process_targets_bulk_create_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_process_targets_bulk_create_post_request** | [**PerformanceReviewProcessTargetsBulkCreatePostRequest**](PerformanceReviewProcessTargetsBulkCreatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;PerformanceReviewProcessTarget&gt;**](PerformanceReviewProcessTarget.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_review_process_targets_get

> <PerformanceReviewProcessTargetsGet200Response> performance_review_process_targets_get(opts)

Reads all Review process targets

Retrieves the participants of active review processes.

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

api_instance = F::PerformanceReviewProcessTargetApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Filter by review process target IDs
  access_ids: ['inner_example'], # Array<String> | Filter by access IDs
  only_for_peer_assignment: false, # Boolean | Only participants for peer assignment
  without_manager: false, # Boolean | Only participants with no manager assigned
  performance_review_process_ids: ['inner_example'], # Array<String> | Filter by reviewer process IDs
  agreement_completion_status: 'canbeinitiated', # String | Filter by agreement status
  pending_peer_evaluations: false, # Boolean | Only participants with no peer evaluations
  managed_by_filter: F::PerformanceReviewEvaluationsGetWithTargetsManagedByFilterParameter.new({manager_employee_id: 'manager_employee_id_example', only_direct_reports: false}) # PerformanceReviewEvaluationsGetWithTargetsManagedByFilterParameter | Only participants managed by the specified employee ID
}

begin
  # Reads all Review process targets
  result = api_instance.performance_review_process_targets_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessTargetApi->performance_review_process_targets_get: #{e}"
end
```

#### Using the performance_review_process_targets_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcessTargetsGet200Response>, Integer, Hash)> performance_review_process_targets_get_with_http_info(opts)

```ruby
begin
  # Reads all Review process targets
  data, status_code, headers = api_instance.performance_review_process_targets_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcessTargetsGet200Response>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessTargetApi->performance_review_process_targets_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter by review process target IDs | [optional] |
| **access_ids** | [**Array&lt;String&gt;**](String.md) | Filter by access IDs | [optional] |
| **only_for_peer_assignment** | **Boolean** | Only participants for peer assignment | [optional] |
| **without_manager** | **Boolean** | Only participants with no manager assigned | [optional] |
| **performance_review_process_ids** | [**Array&lt;String&gt;**](String.md) | Filter by reviewer process IDs | [optional] |
| **agreement_completion_status** | **String** | Filter by agreement status | [optional] |
| **pending_peer_evaluations** | **Boolean** | Only participants with no peer evaluations | [optional] |
| **managed_by_filter** | [**PerformanceReviewEvaluationsGetWithTargetsManagedByFilterParameter**](.md) | Only participants managed by the specified employee ID | [optional] |

### Return type

[**PerformanceReviewProcessTargetsGet200Response**](PerformanceReviewProcessTargetsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_review_process_targets_id_delete

> <PerformanceReviewProcessTarget> performance_review_process_targets_id_delete(id)

Deletes a Review process target

Delete a participant from the active review process. This will also remove all previously submitted evaluations about the participant.

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

api_instance = F::PerformanceReviewProcessTargetApi.new
id = '1-1' # String | Process Target ID

begin
  # Deletes a Review process target
  result = api_instance.performance_review_process_targets_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessTargetApi->performance_review_process_targets_id_delete: #{e}"
end
```

#### Using the performance_review_process_targets_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcessTarget>, Integer, Hash)> performance_review_process_targets_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Review process target
  data, status_code, headers = api_instance.performance_review_process_targets_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcessTarget>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessTargetApi->performance_review_process_targets_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Process Target ID |  |

### Return type

[**PerformanceReviewProcessTarget**](PerformanceReviewProcessTarget.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_review_process_targets_id_get

> <PerformanceReviewProcessTarget> performance_review_process_targets_id_get(id)

Reads a single Review process target

Retrieves the participants of active review processes.

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

api_instance = F::PerformanceReviewProcessTargetApi.new
id = '1-1' # String | Filter by review process target IDs

begin
  # Reads a single Review process target
  result = api_instance.performance_review_process_targets_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessTargetApi->performance_review_process_targets_id_get: #{e}"
end
```

#### Using the performance_review_process_targets_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcessTarget>, Integer, Hash)> performance_review_process_targets_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Review process target
  data, status_code, headers = api_instance.performance_review_process_targets_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcessTarget>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessTargetApi->performance_review_process_targets_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter by review process target IDs |  |

### Return type

[**PerformanceReviewProcessTarget**](PerformanceReviewProcessTarget.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_review_process_targets_remove_peer_evaluations_post

> <PerformanceReviewProcessTarget> performance_review_process_targets_remove_peer_evaluations_post(opts)

Remove peer evaluations a Review process target

Remove peers and their evaluations from a specific participant.

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

api_instance = F::PerformanceReviewProcessTargetApi.new
opts = {
  performance_review_process_targets_remove_peer_evaluations_post_request: F::PerformanceReviewProcessTargetsRemovePeerEvaluationsPostRequest.new({id: 'id_example', evaluation_ids: ['evaluation_ids_example']}) # PerformanceReviewProcessTargetsRemovePeerEvaluationsPostRequest | 
}

begin
  # Remove peer evaluations a Review process target
  result = api_instance.performance_review_process_targets_remove_peer_evaluations_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessTargetApi->performance_review_process_targets_remove_peer_evaluations_post: #{e}"
end
```

#### Using the performance_review_process_targets_remove_peer_evaluations_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceReviewProcessTarget>, Integer, Hash)> performance_review_process_targets_remove_peer_evaluations_post_with_http_info(opts)

```ruby
begin
  # Remove peer evaluations a Review process target
  data, status_code, headers = api_instance.performance_review_process_targets_remove_peer_evaluations_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceReviewProcessTarget>
rescue F::ApiError => e
  puts "Error when calling PerformanceReviewProcessTargetApi->performance_review_process_targets_remove_peer_evaluations_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_process_targets_remove_peer_evaluations_post_request** | [**PerformanceReviewProcessTargetsRemovePeerEvaluationsPostRequest**](PerformanceReviewProcessTargetsRemovePeerEvaluationsPostRequest.md) |  | [optional] |

### Return type

[**PerformanceReviewProcessTarget**](PerformanceReviewProcessTarget.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

