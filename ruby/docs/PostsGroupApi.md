# F::PostsGroupApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**posts_groups_archive_post**](PostsGroupApi.md#posts_groups_archive_post) | **POST** /api/2026-07-01/resources/posts/groups/archive | Archives a Group |
| [**posts_groups_get**](PostsGroupApi.md#posts_groups_get) | **GET** /api/2026-07-01/resources/posts/groups | Reads all Groups |
| [**posts_groups_id_delete**](PostsGroupApi.md#posts_groups_id_delete) | **DELETE** /api/2026-07-01/resources/posts/groups/{id} | Deletes a Group |
| [**posts_groups_id_get**](PostsGroupApi.md#posts_groups_id_get) | **GET** /api/2026-07-01/resources/posts/groups/{id} | Reads a single Group |
| [**posts_groups_id_put**](PostsGroupApi.md#posts_groups_id_put) | **PUT** /api/2026-07-01/resources/posts/groups/{id} | Updates a Group |
| [**posts_groups_post**](PostsGroupApi.md#posts_groups_post) | **POST** /api/2026-07-01/resources/posts/groups | Creates a Group |


## posts_groups_archive_post

> <PostsGroup> posts_groups_archive_post(opts)

Archives a Group

Archives a group but keeps the data.

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

api_instance = F::PostsGroupApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Archives a Group
  result = api_instance.posts_groups_archive_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsGroupApi->posts_groups_archive_post: #{e}"
end
```

#### Using the posts_groups_archive_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsGroup>, Integer, Hash)> posts_groups_archive_post_with_http_info(opts)

```ruby
begin
  # Archives a Group
  data, status_code, headers = api_instance.posts_groups_archive_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsGroup>
rescue F::ApiError => e
  puts "Error when calling PostsGroupApi->posts_groups_archive_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**PostsGroup**](PostsGroup.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## posts_groups_get

> <PostsGroupsGet200Response> posts_groups_get(opts)

Reads all Groups

> ###### **What does it do?** > These endpoints will allow you to retrieve groups > ###### **What can you do with groups?** > Increase visibility and communication within the company by creating events and announcements. You can create groups for different departments, teams, or projects. > ###### **Who can use it?** > For having this funcionality available, you need to have Communities V2 feature enabled.

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

api_instance = F::PostsGroupApi.new
opts = {
  ids: ['inner_example'], # Array<String> | identifier of the group.
  search: 'announcements' # String | search term to filter groups by title or description.
}

begin
  # Reads all Groups
  result = api_instance.posts_groups_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsGroupApi->posts_groups_get: #{e}"
end
```

#### Using the posts_groups_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsGroupsGet200Response>, Integer, Hash)> posts_groups_get_with_http_info(opts)

```ruby
begin
  # Reads all Groups
  data, status_code, headers = api_instance.posts_groups_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsGroupsGet200Response>
rescue F::ApiError => e
  puts "Error when calling PostsGroupApi->posts_groups_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | identifier of the group. | [optional] |
| **search** | **String** | search term to filter groups by title or description. | [optional] |

### Return type

[**PostsGroupsGet200Response**](PostsGroupsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## posts_groups_id_delete

> <PostsGroup> posts_groups_id_delete(id)

Deletes a Group

Deletes a Group

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

api_instance = F::PostsGroupApi.new
id = '1' # String | identifier of the group.

begin
  # Deletes a Group
  result = api_instance.posts_groups_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsGroupApi->posts_groups_id_delete: #{e}"
end
```

#### Using the posts_groups_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsGroup>, Integer, Hash)> posts_groups_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Group
  data, status_code, headers = api_instance.posts_groups_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsGroup>
rescue F::ApiError => e
  puts "Error when calling PostsGroupApi->posts_groups_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the group. |  |

### Return type

[**PostsGroup**](PostsGroup.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## posts_groups_id_get

> <PostsGroup> posts_groups_id_get(id)

Reads a single Group

> ###### **What does it do?** > These endpoints will allow you to retrieve groups > ###### **What can you do with groups?** > Increase visibility and communication within the company by creating events and announcements. You can create groups for different departments, teams, or projects. > ###### **Who can use it?** > For having this funcionality available, you need to have Communities V2 feature enabled.

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

api_instance = F::PostsGroupApi.new
id = '1' # String | identifier of the group.

begin
  # Reads a single Group
  result = api_instance.posts_groups_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsGroupApi->posts_groups_id_get: #{e}"
end
```

#### Using the posts_groups_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsGroup>, Integer, Hash)> posts_groups_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Group
  data, status_code, headers = api_instance.posts_groups_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsGroup>
rescue F::ApiError => e
  puts "Error when calling PostsGroupApi->posts_groups_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the group. |  |

### Return type

[**PostsGroup**](PostsGroup.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## posts_groups_id_put

> <PostsGroup> posts_groups_id_put(id, opts)

Updates a Group

Updates a Group

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

api_instance = F::PostsGroupApi.new
id = '1' # String | Identifier of the group.
opts = {
  posts_groups_id_put_request: F::PostsGroupsIdPutRequest.new({id: '1'}) # PostsGroupsIdPutRequest | 
}

begin
  # Updates a Group
  result = api_instance.posts_groups_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsGroupApi->posts_groups_id_put: #{e}"
end
```

#### Using the posts_groups_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsGroup>, Integer, Hash)> posts_groups_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Group
  data, status_code, headers = api_instance.posts_groups_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsGroup>
rescue F::ApiError => e
  puts "Error when calling PostsGroupApi->posts_groups_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the group. |  |
| **posts_groups_id_put_request** | [**PostsGroupsIdPutRequest**](PostsGroupsIdPutRequest.md) |  | [optional] |

### Return type

[**PostsGroup**](PostsGroup.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## posts_groups_post

> <PostsGroup> posts_groups_post(opts)

Creates a Group

Creates a Group

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

api_instance = F::PostsGroupApi.new
opts = {
  posts_groups_post_request: F::PostsGroupsPostRequest.new({title: 'Company announcements', description: 'The place to find all company announcements.', company_id: '1'}) # PostsGroupsPostRequest | 
}

begin
  # Creates a Group
  result = api_instance.posts_groups_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsGroupApi->posts_groups_post: #{e}"
end
```

#### Using the posts_groups_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsGroup>, Integer, Hash)> posts_groups_post_with_http_info(opts)

```ruby
begin
  # Creates a Group
  data, status_code, headers = api_instance.posts_groups_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsGroup>
rescue F::ApiError => e
  puts "Error when calling PostsGroupApi->posts_groups_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **posts_groups_post_request** | [**PostsGroupsPostRequest**](PostsGroupsPostRequest.md) |  | [optional] |

### Return type

[**PostsGroup**](PostsGroup.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

