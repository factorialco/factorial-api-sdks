# F::AtsFeedbackApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**ats_feedbacks_get**](AtsFeedbackApi.md#ats_feedbacks_get) | **GET** /api/2026-07-01/resources/ats/feedbacks | Reads all Feedbacks |
| [**ats_feedbacks_id_delete**](AtsFeedbackApi.md#ats_feedbacks_id_delete) | **DELETE** /api/2026-07-01/resources/ats/feedbacks/{id} | Deletes a Feedback |
| [**ats_feedbacks_id_get**](AtsFeedbackApi.md#ats_feedbacks_id_get) | **GET** /api/2026-07-01/resources/ats/feedbacks/{id} | Reads a single Feedback |
| [**ats_feedbacks_id_put**](AtsFeedbackApi.md#ats_feedbacks_id_put) | **PUT** /api/2026-07-01/resources/ats/feedbacks/{id} | Updates a Feedback |
| [**ats_feedbacks_post**](AtsFeedbackApi.md#ats_feedbacks_post) | **POST** /api/2026-07-01/resources/ats/feedbacks | Creates a Feedback |


## ats_feedbacks_get

> <AtsFeedbacksGet200Response> ats_feedbacks_get(opts)

Reads all Feedbacks

This endpoint retrieves all feedbacks associated with a candidate's applications.

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

api_instance = F::AtsFeedbackApi.new
opts = {
  ids: ['inner_example'], # Array<String> | retrieve only the feedbacks that match the IDs passed in the request.
  ats_application_ids: ['inner_example'], # Array<String> | filter feedbacks based on multiple application IDs.
  ats_candidate_id: '[1, 2, 3]' # String | fetch feedbacks related to a specific candidate.
}

begin
  # Reads all Feedbacks
  result = api_instance.ats_feedbacks_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsFeedbackApi->ats_feedbacks_get: #{e}"
end
```

#### Using the ats_feedbacks_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsFeedbacksGet200Response>, Integer, Hash)> ats_feedbacks_get_with_http_info(opts)

```ruby
begin
  # Reads all Feedbacks
  data, status_code, headers = api_instance.ats_feedbacks_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsFeedbacksGet200Response>
rescue F::ApiError => e
  puts "Error when calling AtsFeedbackApi->ats_feedbacks_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | retrieve only the feedbacks that match the IDs passed in the request. | [optional] |
| **ats_application_ids** | [**Array&lt;String&gt;**](String.md) | filter feedbacks based on multiple application IDs. | [optional] |
| **ats_candidate_id** | **String** | fetch feedbacks related to a specific candidate. | [optional] |

### Return type

[**AtsFeedbacksGet200Response**](AtsFeedbacksGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_feedbacks_id_delete

> <AtsFeedback> ats_feedbacks_id_delete(id)

Deletes a Feedback

This endpoint allows to delete a specific feedback entry associated with a candidate's application.

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

api_instance = F::AtsFeedbackApi.new
id = '1' # String | 

begin
  # Deletes a Feedback
  result = api_instance.ats_feedbacks_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsFeedbackApi->ats_feedbacks_id_delete: #{e}"
end
```

#### Using the ats_feedbacks_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsFeedback>, Integer, Hash)> ats_feedbacks_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Feedback
  data, status_code, headers = api_instance.ats_feedbacks_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsFeedback>
rescue F::ApiError => e
  puts "Error when calling AtsFeedbackApi->ats_feedbacks_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**AtsFeedback**](AtsFeedback.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_feedbacks_id_get

> <AtsFeedback> ats_feedbacks_id_get(id)

Reads a single Feedback

This endpoint retrieves all feedbacks associated with a candidate's applications.

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

api_instance = F::AtsFeedbackApi.new
id = '1' # String | retrieve only the feedbacks that match the IDs passed in the request.

begin
  # Reads a single Feedback
  result = api_instance.ats_feedbacks_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsFeedbackApi->ats_feedbacks_id_get: #{e}"
end
```

#### Using the ats_feedbacks_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsFeedback>, Integer, Hash)> ats_feedbacks_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Feedback
  data, status_code, headers = api_instance.ats_feedbacks_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsFeedback>
rescue F::ApiError => e
  puts "Error when calling AtsFeedbackApi->ats_feedbacks_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | retrieve only the feedbacks that match the IDs passed in the request. |  |

### Return type

[**AtsFeedback**](AtsFeedback.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_feedbacks_id_put

> <AtsFeedback> ats_feedbacks_id_put(id, opts)

Updates a Feedback

This endpoint allows to update existing feedback entries associated with candidates' applications.

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

api_instance = F::AtsFeedbackApi.new
id = '1' # String | the ID of the feedback entry to be updated.
opts = {
  ats_feedbacks_id_put_request: F::AtsFeedbacksIdPutRequest.new # AtsFeedbacksIdPutRequest | 
}

begin
  # Updates a Feedback
  result = api_instance.ats_feedbacks_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsFeedbackApi->ats_feedbacks_id_put: #{e}"
end
```

#### Using the ats_feedbacks_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsFeedback>, Integer, Hash)> ats_feedbacks_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Feedback
  data, status_code, headers = api_instance.ats_feedbacks_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsFeedback>
rescue F::ApiError => e
  puts "Error when calling AtsFeedbackApi->ats_feedbacks_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | the ID of the feedback entry to be updated. |  |
| **ats_feedbacks_id_put_request** | [**AtsFeedbacksIdPutRequest**](AtsFeedbacksIdPutRequest.md) |  | [optional] |

### Return type

[**AtsFeedback**](AtsFeedback.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ats_feedbacks_post

> <AtsFeedback> ats_feedbacks_post(opts)

Creates a Feedback

This endpoint allows to create new feedback entries for candidates.

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

api_instance = F::AtsFeedbackApi.new
opts = {
  ats_feedbacks_post_request: F::AtsFeedbacksPostRequest.new({ats_candidate_id: '1'}) # AtsFeedbacksPostRequest | 
}

begin
  # Creates a Feedback
  result = api_instance.ats_feedbacks_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsFeedbackApi->ats_feedbacks_post: #{e}"
end
```

#### Using the ats_feedbacks_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsFeedback>, Integer, Hash)> ats_feedbacks_post_with_http_info(opts)

```ruby
begin
  # Creates a Feedback
  data, status_code, headers = api_instance.ats_feedbacks_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsFeedback>
rescue F::ApiError => e
  puts "Error when calling AtsFeedbackApi->ats_feedbacks_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_feedbacks_post_request** | [**AtsFeedbacksPostRequest**](AtsFeedbacksPostRequest.md) |  | [optional] |

### Return type

[**AtsFeedback**](AtsFeedback.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

