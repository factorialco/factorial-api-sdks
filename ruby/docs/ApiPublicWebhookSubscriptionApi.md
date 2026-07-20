# F::ApiPublicWebhookSubscriptionApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**api_public_webhook_subscriptions_get**](ApiPublicWebhookSubscriptionApi.md#api_public_webhook_subscriptions_get) | **GET** /api/2026-07-01/resources/api_public/webhook_subscriptions | Reads all Webhook subscriptions |
| [**api_public_webhook_subscriptions_id_delete**](ApiPublicWebhookSubscriptionApi.md#api_public_webhook_subscriptions_id_delete) | **DELETE** /api/2026-07-01/resources/api_public/webhook_subscriptions/{id} | Deletes a Webhook subscription |
| [**api_public_webhook_subscriptions_id_get**](ApiPublicWebhookSubscriptionApi.md#api_public_webhook_subscriptions_id_get) | **GET** /api/2026-07-01/resources/api_public/webhook_subscriptions/{id} | Reads a single Webhook subscription |
| [**api_public_webhook_subscriptions_id_put**](ApiPublicWebhookSubscriptionApi.md#api_public_webhook_subscriptions_id_put) | **PUT** /api/2026-07-01/resources/api_public/webhook_subscriptions/{id} | Updates a Webhook subscription |
| [**api_public_webhook_subscriptions_post**](ApiPublicWebhookSubscriptionApi.md#api_public_webhook_subscriptions_post) | **POST** /api/2026-07-01/resources/api_public/webhook_subscriptions | Creates a Webhook subscription |


## api_public_webhook_subscriptions_get

> <ApiPublicWebhookSubscriptionsGet200Response> api_public_webhook_subscriptions_get(opts)

Reads all Webhook subscriptions

Reads all Webhook subscriptions

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

api_instance = F::ApiPublicWebhookSubscriptionApi.new
opts = {
  id: '1', # String | Identifier of the webhook subscription
  company_id: '1', # String | Company identifier of the webhook subscription
  type: 'ats/job_posting/create', # String | Type of the webhook subscription
  enabled: true # Boolean | List only enabled webhook subscriptions
}

begin
  # Reads all Webhook subscriptions
  result = api_instance.api_public_webhook_subscriptions_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ApiPublicWebhookSubscriptionApi->api_public_webhook_subscriptions_get: #{e}"
end
```

#### Using the api_public_webhook_subscriptions_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ApiPublicWebhookSubscriptionsGet200Response>, Integer, Hash)> api_public_webhook_subscriptions_get_with_http_info(opts)

```ruby
begin
  # Reads all Webhook subscriptions
  data, status_code, headers = api_instance.api_public_webhook_subscriptions_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ApiPublicWebhookSubscriptionsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ApiPublicWebhookSubscriptionApi->api_public_webhook_subscriptions_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the webhook subscription | [optional] |
| **company_id** | **String** | Company identifier of the webhook subscription | [optional] |
| **type** | **String** | Type of the webhook subscription | [optional] |
| **enabled** | **Boolean** | List only enabled webhook subscriptions | [optional] |

### Return type

[**ApiPublicWebhookSubscriptionsGet200Response**](ApiPublicWebhookSubscriptionsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## api_public_webhook_subscriptions_id_delete

> <ApiPublicWebhookSubscription> api_public_webhook_subscriptions_id_delete(id)

Deletes a Webhook subscription

Deletes a Webhook subscription

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

api_instance = F::ApiPublicWebhookSubscriptionApi.new
id = '1' # String | 

begin
  # Deletes a Webhook subscription
  result = api_instance.api_public_webhook_subscriptions_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ApiPublicWebhookSubscriptionApi->api_public_webhook_subscriptions_id_delete: #{e}"
end
```

#### Using the api_public_webhook_subscriptions_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ApiPublicWebhookSubscription>, Integer, Hash)> api_public_webhook_subscriptions_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Webhook subscription
  data, status_code, headers = api_instance.api_public_webhook_subscriptions_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ApiPublicWebhookSubscription>
rescue F::ApiError => e
  puts "Error when calling ApiPublicWebhookSubscriptionApi->api_public_webhook_subscriptions_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**ApiPublicWebhookSubscription**](ApiPublicWebhookSubscription.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## api_public_webhook_subscriptions_id_get

> <ApiPublicWebhookSubscription> api_public_webhook_subscriptions_id_get(id)

Reads a single Webhook subscription

Reads a single Webhook subscription

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

api_instance = F::ApiPublicWebhookSubscriptionApi.new
id = '1' # String | Identifier of the webhook subscription

begin
  # Reads a single Webhook subscription
  result = api_instance.api_public_webhook_subscriptions_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ApiPublicWebhookSubscriptionApi->api_public_webhook_subscriptions_id_get: #{e}"
end
```

#### Using the api_public_webhook_subscriptions_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ApiPublicWebhookSubscription>, Integer, Hash)> api_public_webhook_subscriptions_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Webhook subscription
  data, status_code, headers = api_instance.api_public_webhook_subscriptions_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ApiPublicWebhookSubscription>
rescue F::ApiError => e
  puts "Error when calling ApiPublicWebhookSubscriptionApi->api_public_webhook_subscriptions_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the webhook subscription |  |

### Return type

[**ApiPublicWebhookSubscription**](ApiPublicWebhookSubscription.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## api_public_webhook_subscriptions_id_put

> <ApiPublicWebhookSubscription> api_public_webhook_subscriptions_id_put(id, opts)

Updates a Webhook subscription

Updates a Webhook subscription

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

api_instance = F::ApiPublicWebhookSubscriptionApi.new
id = '1' # String | Identifier of the webhook subscription
opts = {
  api_public_webhook_subscriptions_id_put_request: F::ApiPublicWebhookSubscriptionsIdPutRequest.new({id: '1'}) # ApiPublicWebhookSubscriptionsIdPutRequest | 
}

begin
  # Updates a Webhook subscription
  result = api_instance.api_public_webhook_subscriptions_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ApiPublicWebhookSubscriptionApi->api_public_webhook_subscriptions_id_put: #{e}"
end
```

#### Using the api_public_webhook_subscriptions_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ApiPublicWebhookSubscription>, Integer, Hash)> api_public_webhook_subscriptions_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Webhook subscription
  data, status_code, headers = api_instance.api_public_webhook_subscriptions_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ApiPublicWebhookSubscription>
rescue F::ApiError => e
  puts "Error when calling ApiPublicWebhookSubscriptionApi->api_public_webhook_subscriptions_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the webhook subscription |  |
| **api_public_webhook_subscriptions_id_put_request** | [**ApiPublicWebhookSubscriptionsIdPutRequest**](ApiPublicWebhookSubscriptionsIdPutRequest.md) |  | [optional] |

### Return type

[**ApiPublicWebhookSubscription**](ApiPublicWebhookSubscription.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## api_public_webhook_subscriptions_post

> <ApiPublicWebhookSubscription> api_public_webhook_subscriptions_post(opts)

Creates a Webhook subscription

Creates a Webhook subscription

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

api_instance = F::ApiPublicWebhookSubscriptionApi.new
opts = {
  api_public_webhook_subscriptions_post_request: F::ApiPublicWebhookSubscriptionsPostRequest.new({subscription_type: 'ats/job_posting/create', target_url: 'https://webhook.site/', company_id: '1'}) # ApiPublicWebhookSubscriptionsPostRequest | 
}

begin
  # Creates a Webhook subscription
  result = api_instance.api_public_webhook_subscriptions_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ApiPublicWebhookSubscriptionApi->api_public_webhook_subscriptions_post: #{e}"
end
```

#### Using the api_public_webhook_subscriptions_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ApiPublicWebhookSubscription>, Integer, Hash)> api_public_webhook_subscriptions_post_with_http_info(opts)

```ruby
begin
  # Creates a Webhook subscription
  data, status_code, headers = api_instance.api_public_webhook_subscriptions_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ApiPublicWebhookSubscription>
rescue F::ApiError => e
  puts "Error when calling ApiPublicWebhookSubscriptionApi->api_public_webhook_subscriptions_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **api_public_webhook_subscriptions_post_request** | [**ApiPublicWebhookSubscriptionsPostRequest**](ApiPublicWebhookSubscriptionsPostRequest.md) |  | [optional] |

### Return type

[**ApiPublicWebhookSubscription**](ApiPublicWebhookSubscription.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

