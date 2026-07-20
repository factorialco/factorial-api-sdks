# F::PostsPostApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**posts_posts_get**](PostsPostApi.md#posts_posts_get) | **GET** /api/2026-07-01/resources/posts/posts | Reads all Posts |
| [**posts_posts_id_delete**](PostsPostApi.md#posts_posts_id_delete) | **DELETE** /api/2026-07-01/resources/posts/posts/{id} | Deletes a Post |
| [**posts_posts_id_get**](PostsPostApi.md#posts_posts_id_get) | **GET** /api/2026-07-01/resources/posts/posts/{id} | Reads a single Post |
| [**posts_posts_id_put**](PostsPostApi.md#posts_posts_id_put) | **PUT** /api/2026-07-01/resources/posts/posts/{id} | Updates a Post |
| [**posts_posts_post**](PostsPostApi.md#posts_posts_post) | **POST** /api/2026-07-01/resources/posts/posts | Creates a Post |


## posts_posts_get

> <PostsPostsGet200Response> posts_posts_get(opts)

Reads all Posts

###### **What does it do?** These endpoints allow you to retrieve posts of a community ###### **What can you do with groups?** Increase visibility and communication within the company by creating interaction and community within your company. ###### **Who can use it?** For having this funcionality available, you need to have Communities V2 feature available

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

api_instance = F::PostsPostApi.new
opts = {
  groups: ['inner_example'], # Array<String> | group identifiers of the posts
  from: '2024-05-02', # String | date from which posts will be retrieved
  _until: '2024-08-01', # String | date until which the posts will be retrieved
  ids: ['inner_example'] # Array<String> | identifiers of the post
}

begin
  # Reads all Posts
  result = api_instance.posts_posts_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsPostApi->posts_posts_get: #{e}"
end
```

#### Using the posts_posts_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsPostsGet200Response>, Integer, Hash)> posts_posts_get_with_http_info(opts)

```ruby
begin
  # Reads all Posts
  data, status_code, headers = api_instance.posts_posts_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsPostsGet200Response>
rescue F::ApiError => e
  puts "Error when calling PostsPostApi->posts_posts_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **groups** | [**Array&lt;String&gt;**](String.md) | group identifiers of the posts | [optional] |
| **from** | **String** | date from which posts will be retrieved | [optional] |
| **_until** | **String** | date until which the posts will be retrieved | [optional] |
| **ids** | [**Array&lt;String&gt;**](String.md) | identifiers of the post | [optional] |

### Return type

[**PostsPostsGet200Response**](PostsPostsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## posts_posts_id_delete

> <PostsPost> posts_posts_id_delete(id)

Deletes a Post

Deletes a Post

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

api_instance = F::PostsPostApi.new
id = '1' # String | identifier of the post

begin
  # Deletes a Post
  result = api_instance.posts_posts_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsPostApi->posts_posts_id_delete: #{e}"
end
```

#### Using the posts_posts_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsPost>, Integer, Hash)> posts_posts_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Post
  data, status_code, headers = api_instance.posts_posts_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsPost>
rescue F::ApiError => e
  puts "Error when calling PostsPostApi->posts_posts_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the post |  |

### Return type

[**PostsPost**](PostsPost.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## posts_posts_id_get

> <PostsPost> posts_posts_id_get(id)

Reads a single Post

###### **What does it do?** These endpoints allow you to retrieve posts of a community ###### **What can you do with groups?** Increase visibility and communication within the company by creating interaction and community within your company. ###### **Who can use it?** For having this funcionality available, you need to have Communities V2 feature available

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

api_instance = F::PostsPostApi.new
id = '1' # String | identifiers of the post

begin
  # Reads a single Post
  result = api_instance.posts_posts_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsPostApi->posts_posts_id_get: #{e}"
end
```

#### Using the posts_posts_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsPost>, Integer, Hash)> posts_posts_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Post
  data, status_code, headers = api_instance.posts_posts_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsPost>
rescue F::ApiError => e
  puts "Error when calling PostsPostApi->posts_posts_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifiers of the post |  |

### Return type

[**PostsPost**](PostsPost.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## posts_posts_id_put

> <PostsPost> posts_posts_id_put(id, opts)

Updates a Post

Updates a Post

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

api_instance = F::PostsPostApi.new
id = '1' # String | identifier of the post
opts = {
  posts_posts_id_put_request: F::PostsPostsIdPutRequest.new({id: '1'}) # PostsPostsIdPutRequest | 
}

begin
  # Updates a Post
  result = api_instance.posts_posts_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsPostApi->posts_posts_id_put: #{e}"
end
```

#### Using the posts_posts_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsPost>, Integer, Hash)> posts_posts_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Post
  data, status_code, headers = api_instance.posts_posts_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsPost>
rescue F::ApiError => e
  puts "Error when calling PostsPostApi->posts_posts_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the post |  |
| **posts_posts_id_put_request** | [**PostsPostsIdPutRequest**](PostsPostsIdPutRequest.md) |  | [optional] |

### Return type

[**PostsPost**](PostsPost.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## posts_posts_post

> <PostsPost> posts_posts_post(opts)

Creates a Post

Creates a Post

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

api_instance = F::PostsPostApi.new
opts = {
  posts_posts_post_request: F::PostsPostsPostRequest.new({title: 'Are you ready for the perfomance review?', description: 'As you know today we start the performance review process.', post_group_id: '1'}) # PostsPostsPostRequest | 
}

begin
  # Creates a Post
  result = api_instance.posts_posts_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PostsPostApi->posts_posts_post: #{e}"
end
```

#### Using the posts_posts_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PostsPost>, Integer, Hash)> posts_posts_post_with_http_info(opts)

```ruby
begin
  # Creates a Post
  data, status_code, headers = api_instance.posts_posts_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PostsPost>
rescue F::ApiError => e
  puts "Error when calling PostsPostApi->posts_posts_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **posts_posts_post_request** | [**PostsPostsPostRequest**](PostsPostsPostRequest.md) |  | [optional] |

### Return type

[**PostsPost**](PostsPost.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

