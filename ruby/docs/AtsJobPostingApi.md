# F::AtsJobPostingApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**ats_job_postings_duplicate_post**](AtsJobPostingApi.md#ats_job_postings_duplicate_post) | **POST** /api/2026-07-01/resources/ats/job_postings/duplicate | Duplicates a Job posting |
| [**ats_job_postings_get**](AtsJobPostingApi.md#ats_job_postings_get) | **GET** /api/2026-07-01/resources/ats/job_postings | Reads all Job postings |
| [**ats_job_postings_id_delete**](AtsJobPostingApi.md#ats_job_postings_id_delete) | **DELETE** /api/2026-07-01/resources/ats/job_postings/{id} | Deletes a Job posting |
| [**ats_job_postings_id_get**](AtsJobPostingApi.md#ats_job_postings_id_get) | **GET** /api/2026-07-01/resources/ats/job_postings/{id} | Reads a single Job posting |
| [**ats_job_postings_id_put**](AtsJobPostingApi.md#ats_job_postings_id_put) | **PUT** /api/2026-07-01/resources/ats/job_postings/{id} | Updates a Job posting |
| [**ats_job_postings_post**](AtsJobPostingApi.md#ats_job_postings_post) | **POST** /api/2026-07-01/resources/ats/job_postings | Creates a Job posting |


## ats_job_postings_duplicate_post

> <AtsJobPosting> ats_job_postings_duplicate_post(opts)

Duplicates a Job posting

Duplicate an existing job posting.

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

api_instance = F::AtsJobPostingApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Duplicates a Job posting
  result = api_instance.ats_job_postings_duplicate_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsJobPostingApi->ats_job_postings_duplicate_post: #{e}"
end
```

#### Using the ats_job_postings_duplicate_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsJobPosting>, Integer, Hash)> ats_job_postings_duplicate_post_with_http_info(opts)

```ruby
begin
  # Duplicates a Job posting
  data, status_code, headers = api_instance.ats_job_postings_duplicate_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsJobPosting>
rescue F::ApiError => e
  puts "Error when calling AtsJobPostingApi->ats_job_postings_duplicate_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**AtsJobPosting**](AtsJobPosting.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ats_job_postings_get

> <AtsJobPostingsGet200Response> ats_job_postings_get(opts)

Reads all Job postings

Reads all Job postings

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

api_instance = F::AtsJobPostingApi.new
opts = {
  ids: ['inner_example'], # Array<String> | 
  status: 'draft', # String | 
  team_id: 'team_id_example', # String | 
  location_id: 'location_id_example', # String | 
  legal_entity_id: 'legal_entity_id_example' # String | 
}

begin
  # Reads all Job postings
  result = api_instance.ats_job_postings_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsJobPostingApi->ats_job_postings_get: #{e}"
end
```

#### Using the ats_job_postings_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsJobPostingsGet200Response>, Integer, Hash)> ats_job_postings_get_with_http_info(opts)

```ruby
begin
  # Reads all Job postings
  data, status_code, headers = api_instance.ats_job_postings_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsJobPostingsGet200Response>
rescue F::ApiError => e
  puts "Error when calling AtsJobPostingApi->ats_job_postings_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **status** | **String** |  | [optional] |
| **team_id** | **String** |  | [optional] |
| **location_id** | **String** |  | [optional] |
| **legal_entity_id** | **String** |  | [optional] |

### Return type

[**AtsJobPostingsGet200Response**](AtsJobPostingsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_job_postings_id_delete

> <AtsJobPosting> ats_job_postings_id_delete(id)

Deletes a Job posting

Delete a job posting.

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

api_instance = F::AtsJobPostingApi.new
id = '1' # String | 

begin
  # Deletes a Job posting
  result = api_instance.ats_job_postings_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsJobPostingApi->ats_job_postings_id_delete: #{e}"
end
```

#### Using the ats_job_postings_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsJobPosting>, Integer, Hash)> ats_job_postings_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Job posting
  data, status_code, headers = api_instance.ats_job_postings_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsJobPosting>
rescue F::ApiError => e
  puts "Error when calling AtsJobPostingApi->ats_job_postings_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**AtsJobPosting**](AtsJobPosting.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_job_postings_id_get

> <AtsJobPosting> ats_job_postings_id_get(id)

Reads a single Job posting

Reads a single Job posting

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

api_instance = F::AtsJobPostingApi.new
id = '1' # String | 

begin
  # Reads a single Job posting
  result = api_instance.ats_job_postings_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsJobPostingApi->ats_job_postings_id_get: #{e}"
end
```

#### Using the ats_job_postings_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsJobPosting>, Integer, Hash)> ats_job_postings_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Job posting
  data, status_code, headers = api_instance.ats_job_postings_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsJobPosting>
rescue F::ApiError => e
  puts "Error when calling AtsJobPostingApi->ats_job_postings_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**AtsJobPosting**](AtsJobPosting.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_job_postings_id_put

> <AtsJobPosting> ats_job_postings_id_put(id, opts)

Updates a Job posting

Update a job posting.

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

api_instance = F::AtsJobPostingApi.new
id = '1' # String | 
opts = {
  ats_job_postings_id_put_request: F::AtsJobPostingsIdPutRequest.new({id: '1'}) # AtsJobPostingsIdPutRequest | 
}

begin
  # Updates a Job posting
  result = api_instance.ats_job_postings_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsJobPostingApi->ats_job_postings_id_put: #{e}"
end
```

#### Using the ats_job_postings_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsJobPosting>, Integer, Hash)> ats_job_postings_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Job posting
  data, status_code, headers = api_instance.ats_job_postings_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsJobPosting>
rescue F::ApiError => e
  puts "Error when calling AtsJobPostingApi->ats_job_postings_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **ats_job_postings_id_put_request** | [**AtsJobPostingsIdPutRequest**](AtsJobPostingsIdPutRequest.md) |  | [optional] |

### Return type

[**AtsJobPosting**](AtsJobPosting.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ats_job_postings_post

> <AtsJobPosting> ats_job_postings_post(opts)

Creates a Job posting

Create a new job posting.

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

api_instance = F::AtsJobPostingApi.new
opts = {
  ats_job_postings_post_request: F::AtsJobPostingsPostRequest.new({title: 'My job title', status: 'draft', cv_requirement: 'mandatory', cover_letter_requirement: 'mandatory', phone_requirement: 'mandatory', photo_requirement: 'mandatory', personal_url_requirement: 'mandatory'}) # AtsJobPostingsPostRequest | 
}

begin
  # Creates a Job posting
  result = api_instance.ats_job_postings_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsJobPostingApi->ats_job_postings_post: #{e}"
end
```

#### Using the ats_job_postings_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsJobPosting>, Integer, Hash)> ats_job_postings_post_with_http_info(opts)

```ruby
begin
  # Creates a Job posting
  data, status_code, headers = api_instance.ats_job_postings_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsJobPosting>
rescue F::ApiError => e
  puts "Error when calling AtsJobPostingApi->ats_job_postings_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_job_postings_post_request** | [**AtsJobPostingsPostRequest**](AtsJobPostingsPostRequest.md) |  | [optional] |

### Return type

[**AtsJobPosting**](AtsJobPosting.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

