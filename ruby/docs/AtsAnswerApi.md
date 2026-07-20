# F::AtsAnswerApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**ats_answers_get**](AtsAnswerApi.md#ats_answers_get) | **GET** /api/2026-07-01/resources/ats/answers | Reads all Answers |
| [**ats_answers_id_get**](AtsAnswerApi.md#ats_answers_id_get) | **GET** /api/2026-07-01/resources/ats/answers/{id} | Reads a single Answer |
| [**ats_answers_post**](AtsAnswerApi.md#ats_answers_post) | **POST** /api/2026-07-01/resources/ats/answers | Creates an Answer |


## ats_answers_get

> <AtsAnswersGet200Response> ats_answers_get(opts)

Reads all Answers

Reads all Answers

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

api_instance = F::AtsAnswerApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Identifier of the answers
  ats_application_ids: ['inner_example'] # Array<String> | Identifier of the apllications
}

begin
  # Reads all Answers
  result = api_instance.ats_answers_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsAnswerApi->ats_answers_get: #{e}"
end
```

#### Using the ats_answers_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsAnswersGet200Response>, Integer, Hash)> ats_answers_get_with_http_info(opts)

```ruby
begin
  # Reads all Answers
  data, status_code, headers = api_instance.ats_answers_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsAnswersGet200Response>
rescue F::ApiError => e
  puts "Error when calling AtsAnswerApi->ats_answers_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Identifier of the answers | [optional] |
| **ats_application_ids** | [**Array&lt;String&gt;**](String.md) | Identifier of the apllications | [optional] |

### Return type

[**AtsAnswersGet200Response**](AtsAnswersGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_answers_id_get

> <AtsAnswer> ats_answers_id_get(id)

Reads a single Answer

Reads a single Answer

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

api_instance = F::AtsAnswerApi.new
id = '1' # String | Identifier of the answers

begin
  # Reads a single Answer
  result = api_instance.ats_answers_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsAnswerApi->ats_answers_id_get: #{e}"
end
```

#### Using the ats_answers_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsAnswer>, Integer, Hash)> ats_answers_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Answer
  data, status_code, headers = api_instance.ats_answers_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsAnswer>
rescue F::ApiError => e
  puts "Error when calling AtsAnswerApi->ats_answers_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the answers |  |

### Return type

[**AtsAnswer**](AtsAnswer.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_answers_post

> <AtsAnswer> ats_answers_post(opts)

Creates an Answer

Creates an Answer

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

api_instance = F::AtsAnswerApi.new
opts = {
  ats_answers_post_request: F::AtsAnswersPostRequest.new({ats_question_id: '1', ats_application_id: '1', value: 'One of the best I have ever seen', original_question_label: 'How was your application ranked?', original_question_type: 'text'}) # AtsAnswersPostRequest | 
}

begin
  # Creates an Answer
  result = api_instance.ats_answers_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsAnswerApi->ats_answers_post: #{e}"
end
```

#### Using the ats_answers_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsAnswer>, Integer, Hash)> ats_answers_post_with_http_info(opts)

```ruby
begin
  # Creates an Answer
  data, status_code, headers = api_instance.ats_answers_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsAnswer>
rescue F::ApiError => e
  puts "Error when calling AtsAnswerApi->ats_answers_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_answers_post_request** | [**AtsAnswersPostRequest**](AtsAnswersPostRequest.md) |  | [optional] |

### Return type

[**AtsAnswer**](AtsAnswer.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

