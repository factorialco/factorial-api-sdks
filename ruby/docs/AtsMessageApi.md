# F::AtsMessageApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**ats_messages_get**](AtsMessageApi.md#ats_messages_get) | **GET** /api/2026-07-01/resources/ats/messages | Reads all Messages |
| [**ats_messages_id_get**](AtsMessageApi.md#ats_messages_id_get) | **GET** /api/2026-07-01/resources/ats/messages/{id} | Reads a single Message |
| [**ats_messages_post**](AtsMessageApi.md#ats_messages_post) | **POST** /api/2026-07-01/resources/ats/messages | Creates a Message |


## ats_messages_get

> <AtsMessagesGet200Response> ats_messages_get(last_per_conversation, opts)

Reads all Messages

Reads all Messages

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

api_instance = F::AtsMessageApi.new
last_per_conversation = true # Boolean | 
opts = {
  id: 'id_example', # String | 
  ids: ['inner_example'], # Array<String> | 
  ats_conversation_id: 'ats_conversation_id_example', # String | 
  ats_conversation_ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Messages
  result = api_instance.ats_messages_get(last_per_conversation, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsMessageApi->ats_messages_get: #{e}"
end
```

#### Using the ats_messages_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsMessagesGet200Response>, Integer, Hash)> ats_messages_get_with_http_info(last_per_conversation, opts)

```ruby
begin
  # Reads all Messages
  data, status_code, headers = api_instance.ats_messages_get_with_http_info(last_per_conversation, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsMessagesGet200Response>
rescue F::ApiError => e
  puts "Error when calling AtsMessageApi->ats_messages_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **last_per_conversation** | **Boolean** |  |  |
| **id** | **String** |  | [optional] |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **ats_conversation_id** | **String** |  | [optional] |
| **ats_conversation_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**AtsMessagesGet200Response**](AtsMessagesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_messages_id_get

> <AtsMessage> ats_messages_id_get(id)

Reads a single Message

Reads a single Message

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

api_instance = F::AtsMessageApi.new
id = '1' # String | 

begin
  # Reads a single Message
  result = api_instance.ats_messages_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsMessageApi->ats_messages_id_get: #{e}"
end
```

#### Using the ats_messages_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsMessage>, Integer, Hash)> ats_messages_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Message
  data, status_code, headers = api_instance.ats_messages_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsMessage>
rescue F::ApiError => e
  puts "Error when calling AtsMessageApi->ats_messages_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**AtsMessage**](AtsMessage.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_messages_post

> <AtsMessage> ats_messages_post(content, sent_by_id, sent_by_type, ats_application_id, attachments, topic, send_as_corporate_email, opts)

Creates a Message

Creates a Message

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

api_instance = F::AtsMessageApi.new
content = 'content_example' # String | 
sent_by_id = 'sent_by_id_example' # String | 
sent_by_type = 'candidate' # String | 
ats_application_id = 'ats_application_id_example' # String | 
attachments = [File.new('/path/to/some/file')] # Array<File> | 
topic = 'topic_example' # String | 
send_as_corporate_email = true # Boolean | 
opts = {
  delayed_until: 'delayed_until_example' # String | 
}

begin
  # Creates a Message
  result = api_instance.ats_messages_post(content, sent_by_id, sent_by_type, ats_application_id, attachments, topic, send_as_corporate_email, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsMessageApi->ats_messages_post: #{e}"
end
```

#### Using the ats_messages_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsMessage>, Integer, Hash)> ats_messages_post_with_http_info(content, sent_by_id, sent_by_type, ats_application_id, attachments, topic, send_as_corporate_email, opts)

```ruby
begin
  # Creates a Message
  data, status_code, headers = api_instance.ats_messages_post_with_http_info(content, sent_by_id, sent_by_type, ats_application_id, attachments, topic, send_as_corporate_email, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsMessage>
rescue F::ApiError => e
  puts "Error when calling AtsMessageApi->ats_messages_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **content** | **String** |  |  |
| **sent_by_id** | **String** |  |  |
| **sent_by_type** | **String** |  |  |
| **ats_application_id** | **String** |  |  |
| **attachments** | **Array&lt;File&gt;** |  |  |
| **topic** | **String** |  |  |
| **send_as_corporate_email** | **Boolean** |  |  |
| **delayed_until** | **String** |  | [optional] |

### Return type

[**AtsMessage**](AtsMessage.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

