# F::AtsQuestionApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**ats_questions_get**](AtsQuestionApi.md#ats_questions_get) | **GET** /api/2026-07-01/resources/ats/questions | Reads all Questions |
| [**ats_questions_id_delete**](AtsQuestionApi.md#ats_questions_id_delete) | **DELETE** /api/2026-07-01/resources/ats/questions/{id} | Deletes a Question |
| [**ats_questions_id_get**](AtsQuestionApi.md#ats_questions_id_get) | **GET** /api/2026-07-01/resources/ats/questions/{id} | Reads a single Question |
| [**ats_questions_id_put**](AtsQuestionApi.md#ats_questions_id_put) | **PUT** /api/2026-07-01/resources/ats/questions/{id} | Updates a Question |
| [**ats_questions_post**](AtsQuestionApi.md#ats_questions_post) | **POST** /api/2026-07-01/resources/ats/questions | Creates a Question |


## ats_questions_get

> <AtsQuestionsGet200Response> ats_questions_get(opts)

Reads all Questions

Reads all Questions

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

api_instance = F::AtsQuestionApi.new
opts = {
  ids: ['inner_example'], # Array<String> | identifiers of the questions
  ats_job_posting_ids: ['inner_example'] # Array<String> | identifiers of the related job postings
}

begin
  # Reads all Questions
  result = api_instance.ats_questions_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsQuestionApi->ats_questions_get: #{e}"
end
```

#### Using the ats_questions_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsQuestionsGet200Response>, Integer, Hash)> ats_questions_get_with_http_info(opts)

```ruby
begin
  # Reads all Questions
  data, status_code, headers = api_instance.ats_questions_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsQuestionsGet200Response>
rescue F::ApiError => e
  puts "Error when calling AtsQuestionApi->ats_questions_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | identifiers of the questions | [optional] |
| **ats_job_posting_ids** | [**Array&lt;String&gt;**](String.md) | identifiers of the related job postings | [optional] |

### Return type

[**AtsQuestionsGet200Response**](AtsQuestionsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_questions_id_delete

> <AtsQuestion> ats_questions_id_delete(id)

Deletes a Question

Deletes a Question

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

api_instance = F::AtsQuestionApi.new
id = '1' # String | identifier of the question

begin
  # Deletes a Question
  result = api_instance.ats_questions_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsQuestionApi->ats_questions_id_delete: #{e}"
end
```

#### Using the ats_questions_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsQuestion>, Integer, Hash)> ats_questions_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Question
  data, status_code, headers = api_instance.ats_questions_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsQuestion>
rescue F::ApiError => e
  puts "Error when calling AtsQuestionApi->ats_questions_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the question |  |

### Return type

[**AtsQuestion**](AtsQuestion.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_questions_id_get

> <AtsQuestion> ats_questions_id_get(id)

Reads a single Question

Reads a single Question

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

api_instance = F::AtsQuestionApi.new
id = '1' # String | identifiers of the questions

begin
  # Reads a single Question
  result = api_instance.ats_questions_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsQuestionApi->ats_questions_id_get: #{e}"
end
```

#### Using the ats_questions_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsQuestion>, Integer, Hash)> ats_questions_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Question
  data, status_code, headers = api_instance.ats_questions_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsQuestion>
rescue F::ApiError => e
  puts "Error when calling AtsQuestionApi->ats_questions_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifiers of the questions |  |

### Return type

[**AtsQuestion**](AtsQuestion.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_questions_id_put

> <AtsQuestion> ats_questions_id_put(id, opts)

Updates a Question

Updates a Question

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

api_instance = F::AtsQuestionApi.new
id = '1' # String | identifier of the question
opts = {
  ats_questions_id_put_request: F::AtsQuestionsIdPutRequest.new({id: '1'}) # AtsQuestionsIdPutRequest | 
}

begin
  # Updates a Question
  result = api_instance.ats_questions_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsQuestionApi->ats_questions_id_put: #{e}"
end
```

#### Using the ats_questions_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsQuestion>, Integer, Hash)> ats_questions_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Question
  data, status_code, headers = api_instance.ats_questions_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsQuestion>
rescue F::ApiError => e
  puts "Error when calling AtsQuestionApi->ats_questions_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the question |  |
| **ats_questions_id_put_request** | [**AtsQuestionsIdPutRequest**](AtsQuestionsIdPutRequest.md) |  | [optional] |

### Return type

[**AtsQuestion**](AtsQuestion.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ats_questions_post

> <AtsQuestion> ats_questions_post(opts)

Creates a Question

Creates a Question

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

api_instance = F::AtsQuestionApi.new
opts = {
  ats_questions_post_request: F::AtsQuestionsPostRequest.new({ats_job_posting_id: '1', company_id: '1', label: 'Are you open to relocate?', position: 1, question_type: 'text'}) # AtsQuestionsPostRequest | 
}

begin
  # Creates a Question
  result = api_instance.ats_questions_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsQuestionApi->ats_questions_post: #{e}"
end
```

#### Using the ats_questions_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsQuestion>, Integer, Hash)> ats_questions_post_with_http_info(opts)

```ruby
begin
  # Creates a Question
  data, status_code, headers = api_instance.ats_questions_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsQuestion>
rescue F::ApiError => e
  puts "Error when calling AtsQuestionApi->ats_questions_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_questions_post_request** | [**AtsQuestionsPostRequest**](AtsQuestionsPostRequest.md) |  | [optional] |

### Return type

[**AtsQuestion**](AtsQuestion.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

