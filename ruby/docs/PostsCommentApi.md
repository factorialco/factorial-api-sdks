# F::PostsCommentApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**posts_comments_get**](PostsCommentApi.md#posts_comments_get) | **GET** /api/2026-07-01/resources/posts/comments | Reads all Comments |
| [**posts_comments_id_delete**](PostsCommentApi.md#posts_comments_id_delete) | **DELETE** /api/2026-07-01/resources/posts/comments/{id} | Deletes a Comment |
| [**posts_comments_id_get**](PostsCommentApi.md#posts_comments_id_get) | **GET** /api/2026-07-01/resources/posts/comments/{id} | Reads a single Comment |
| [**posts_comments_id_put**](PostsCommentApi.md#posts_comments_id_put) | **PUT** /api/2026-07-01/resources/posts/comments/{id} | Updates a Comment |
| [**posts_comments_post**](PostsCommentApi.md#posts_comments_post) | **POST** /api/2026-07-01/resources/posts/comments | Creates a Comment |


## posts_comments_get

> <PostsCommentsGet200Response> posts_comments_get(post_ids, opts)

Reads all Comments

Reads all Comments

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

api_instance = F::PostsCommentApi.new
post_ids = ['inner_example'] # Array<String> | identifiers of the post
opts = {
  ids: ['inner_example'] # Array<String> | identifiers of the comment
}

begin
  # Reads all Comments
  result = api_instance.posts_comments_get(post_ids, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsCommentApi->posts_comments_get: #{e}"
end
```

#### Using the posts_comments_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsCommentsGet200Response>, Integer, Hash)> posts_comments_get_with_http_info(post_ids, opts)

```ruby
begin
  # Reads all Comments
  data, status_code, headers = api_instance.posts_comments_get_with_http_info(post_ids, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsCommentsGet200Response>
rescue F::ApiError => e
  puts "Error when calling PostsCommentApi->posts_comments_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **post_ids** | [**Array&lt;String&gt;**](String.md) | identifiers of the post |  |
| **ids** | [**Array&lt;String&gt;**](String.md) | identifiers of the comment | [optional] |

### Return type

[**PostsCommentsGet200Response**](PostsCommentsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## posts_comments_id_delete

> <PostsComment> posts_comments_id_delete(id)

Deletes a Comment

Deletes a Comment

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

api_instance = F::PostsCommentApi.new
id = '1' # String | identifier of the comment

begin
  # Deletes a Comment
  result = api_instance.posts_comments_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsCommentApi->posts_comments_id_delete: #{e}"
end
```

#### Using the posts_comments_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsComment>, Integer, Hash)> posts_comments_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Comment
  data, status_code, headers = api_instance.posts_comments_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsComment>
rescue F::ApiError => e
  puts "Error when calling PostsCommentApi->posts_comments_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the comment |  |

### Return type

[**PostsComment**](PostsComment.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## posts_comments_id_get

> <PostsComment> posts_comments_id_get(id)

Reads a single Comment

Reads a single Comment

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

api_instance = F::PostsCommentApi.new
id = '1' # String | identifiers of the comment

begin
  # Reads a single Comment
  result = api_instance.posts_comments_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsCommentApi->posts_comments_id_get: #{e}"
end
```

#### Using the posts_comments_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsComment>, Integer, Hash)> posts_comments_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Comment
  data, status_code, headers = api_instance.posts_comments_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsComment>
rescue F::ApiError => e
  puts "Error when calling PostsCommentApi->posts_comments_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifiers of the comment |  |

### Return type

[**PostsComment**](PostsComment.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## posts_comments_id_put

> <PostsComment> posts_comments_id_put(id, opts)

Updates a Comment

Updates a Comment

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

api_instance = F::PostsCommentApi.new
id = '1' # String | identifier of the comment
opts = {
  posts_comments_id_put_request: F::PostsCommentsIdPutRequest.new({id: '1', post_id: '1', text: 'How is the week going Ana?'}) # PostsCommentsIdPutRequest | 
}

begin
  # Updates a Comment
  result = api_instance.posts_comments_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsCommentApi->posts_comments_id_put: #{e}"
end
```

#### Using the posts_comments_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsComment>, Integer, Hash)> posts_comments_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Comment
  data, status_code, headers = api_instance.posts_comments_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsComment>
rescue F::ApiError => e
  puts "Error when calling PostsCommentApi->posts_comments_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the comment |  |
| **posts_comments_id_put_request** | [**PostsCommentsIdPutRequest**](PostsCommentsIdPutRequest.md) |  | [optional] |

### Return type

[**PostsComment**](PostsComment.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## posts_comments_post

> <PostsComment> posts_comments_post(opts)

Creates a Comment

Creates a Comment

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

api_instance = F::PostsCommentApi.new
opts = {
  posts_comments_post_request: F::PostsCommentsPostRequest.new({post_id: '1', text: 'How is the week going Ana?'}) # PostsCommentsPostRequest | 
}

begin
  # Creates a Comment
  result = api_instance.posts_comments_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsCommentApi->posts_comments_post: #{e}"
end
```

#### Using the posts_comments_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsComment>, Integer, Hash)> posts_comments_post_with_http_info(opts)

```ruby
begin
  # Creates a Comment
  data, status_code, headers = api_instance.posts_comments_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsComment>
rescue F::ApiError => e
  puts "Error when calling PostsCommentApi->posts_comments_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **posts_comments_post_request** | [**PostsCommentsPostRequest**](PostsCommentsPostRequest.md) |  | [optional] |

### Return type

[**PostsComment**](PostsComment.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

