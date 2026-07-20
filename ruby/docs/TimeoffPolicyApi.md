# F::TimeoffPolicyApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**timeoff_policies_get**](TimeoffPolicyApi.md#timeoff_policies_get) | **GET** /api/2026-07-01/resources/timeoff/policies | Reads all Policies |
| [**timeoff_policies_id_delete**](TimeoffPolicyApi.md#timeoff_policies_id_delete) | **DELETE** /api/2026-07-01/resources/timeoff/policies/{id} | Deletes a Policy |
| [**timeoff_policies_id_get**](TimeoffPolicyApi.md#timeoff_policies_id_get) | **GET** /api/2026-07-01/resources/timeoff/policies/{id} | Reads a single Policy |
| [**timeoff_policies_id_put**](TimeoffPolicyApi.md#timeoff_policies_id_put) | **PUT** /api/2026-07-01/resources/timeoff/policies/{id} | Updates a Policy |
| [**timeoff_policies_post**](TimeoffPolicyApi.md#timeoff_policies_post) | **POST** /api/2026-07-01/resources/timeoff/policies | Creates a Policy |


## timeoff_policies_get

> <TimeoffPoliciesGet200Response> timeoff_policies_get(opts)

Reads all Policies

Reads all Policies

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

api_instance = F::TimeoffPolicyApi.new
opts = {
  ids: ['inner_example'], # Array<String> | The policies ids to retrieve.
  company_ids: ['inner_example'] # Array<String> | The company ids to retrieve policies.
}

begin
  # Reads all Policies
  result = api_instance.timeoff_policies_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyApi->timeoff_policies_get: #{e}"
end
```

#### Using the timeoff_policies_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffPoliciesGet200Response>, Integer, Hash)> timeoff_policies_get_with_http_info(opts)

```ruby
begin
  # Reads all Policies
  data, status_code, headers = api_instance.timeoff_policies_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffPoliciesGet200Response>
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyApi->timeoff_policies_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | The policies ids to retrieve. | [optional] |
| **company_ids** | [**Array&lt;String&gt;**](String.md) | The company ids to retrieve policies. | [optional] |

### Return type

[**TimeoffPoliciesGet200Response**](TimeoffPoliciesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_policies_id_delete

> <TimeoffPolicy> timeoff_policies_id_delete(id)

Deletes a Policy

Deletes a Policy

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

api_instance = F::TimeoffPolicyApi.new
id = '1' # String | Id of the policy to delete.

begin
  # Deletes a Policy
  result = api_instance.timeoff_policies_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyApi->timeoff_policies_id_delete: #{e}"
end
```

#### Using the timeoff_policies_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffPolicy>, Integer, Hash)> timeoff_policies_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Policy
  data, status_code, headers = api_instance.timeoff_policies_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffPolicy>
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyApi->timeoff_policies_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id of the policy to delete. |  |

### Return type

[**TimeoffPolicy**](TimeoffPolicy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_policies_id_get

> <TimeoffPolicy> timeoff_policies_id_get(id)

Reads a single Policy

Reads a single Policy

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

api_instance = F::TimeoffPolicyApi.new
id = '1' # String | The policies ids to retrieve.

begin
  # Reads a single Policy
  result = api_instance.timeoff_policies_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyApi->timeoff_policies_id_get: #{e}"
end
```

#### Using the timeoff_policies_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffPolicy>, Integer, Hash)> timeoff_policies_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Policy
  data, status_code, headers = api_instance.timeoff_policies_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffPolicy>
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyApi->timeoff_policies_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The policies ids to retrieve. |  |

### Return type

[**TimeoffPolicy**](TimeoffPolicy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeoff_policies_id_put

> <TimeoffPolicy> timeoff_policies_id_put(id, opts)

Updates a Policy

Updates a Policy

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

api_instance = F::TimeoffPolicyApi.new
id = '1' # String | Id of the policy to update.
opts = {
  timeoff_policies_id_put_request: F::TimeoffPoliciesIdPutRequest.new({id: '1'}) # TimeoffPoliciesIdPutRequest | 
}

begin
  # Updates a Policy
  result = api_instance.timeoff_policies_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyApi->timeoff_policies_id_put: #{e}"
end
```

#### Using the timeoff_policies_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffPolicy>, Integer, Hash)> timeoff_policies_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Policy
  data, status_code, headers = api_instance.timeoff_policies_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffPolicy>
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyApi->timeoff_policies_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id of the policy to update. |  |
| **timeoff_policies_id_put_request** | [**TimeoffPoliciesIdPutRequest**](TimeoffPoliciesIdPutRequest.md) |  | [optional] |

### Return type

[**TimeoffPolicy**](TimeoffPolicy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeoff_policies_post

> <TimeoffPolicy> timeoff_policies_post(opts)

Creates a Policy

Creates a Policy

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

api_instance = F::TimeoffPolicyApi.new
opts = {
  timeoff_policies_post_request: F::TimeoffPoliciesPostRequest.new({name: 'Policy for remotes'}) # TimeoffPoliciesPostRequest | 
}

begin
  # Creates a Policy
  result = api_instance.timeoff_policies_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyApi->timeoff_policies_post: #{e}"
end
```

#### Using the timeoff_policies_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffPolicy>, Integer, Hash)> timeoff_policies_post_with_http_info(opts)

```ruby
begin
  # Creates a Policy
  data, status_code, headers = api_instance.timeoff_policies_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffPolicy>
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyApi->timeoff_policies_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **timeoff_policies_post_request** | [**TimeoffPoliciesPostRequest**](TimeoffPoliciesPostRequest.md) |  | [optional] |

### Return type

[**TimeoffPolicy**](TimeoffPolicy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

