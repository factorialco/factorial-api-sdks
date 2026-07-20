# F::AtsEvaluationFormApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**ats_evaluation_forms_get**](AtsEvaluationFormApi.md#ats_evaluation_forms_get) | **GET** /api/2026-07-01/resources/ats/evaluation_forms | Reads all Evaluation forms |
| [**ats_evaluation_forms_id_get**](AtsEvaluationFormApi.md#ats_evaluation_forms_id_get) | **GET** /api/2026-07-01/resources/ats/evaluation_forms/{id} | Reads a single Evaluation form |
| [**ats_evaluation_forms_save_as_template_post**](AtsEvaluationFormApi.md#ats_evaluation_forms_save_as_template_post) | **POST** /api/2026-07-01/resources/ats/evaluation_forms/save_as_template | Save as templates an Evaluation form |


## ats_evaluation_forms_get

> <AtsEvaluationFormsGet200Response> ats_evaluation_forms_get(opts)

Reads all Evaluation forms

Reads all Evaluation forms

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

api_instance = F::AtsEvaluationFormApi.new
opts = {
  ids: ['inner_example'], # Array<String> | List of IDs of the evaluation forms to be fetched.
  ats_job_posting_ids: ['inner_example'], # Array<String> | List of IDs of the job postings to filter the evaluation forms by.
  template: true # Boolean | If true, only the evaluation forms that are templates will be fetched.
}

begin
  # Reads all Evaluation forms
  result = api_instance.ats_evaluation_forms_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsEvaluationFormApi->ats_evaluation_forms_get: #{e}"
end
```

#### Using the ats_evaluation_forms_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsEvaluationFormsGet200Response>, Integer, Hash)> ats_evaluation_forms_get_with_http_info(opts)

```ruby
begin
  # Reads all Evaluation forms
  data, status_code, headers = api_instance.ats_evaluation_forms_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsEvaluationFormsGet200Response>
rescue F::ApiError => e
  puts "Error when calling AtsEvaluationFormApi->ats_evaluation_forms_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | List of IDs of the evaluation forms to be fetched. | [optional] |
| **ats_job_posting_ids** | [**Array&lt;String&gt;**](String.md) | List of IDs of the job postings to filter the evaluation forms by. | [optional] |
| **template** | **Boolean** | If true, only the evaluation forms that are templates will be fetched. | [optional] |

### Return type

[**AtsEvaluationFormsGet200Response**](AtsEvaluationFormsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_evaluation_forms_id_get

> <AtsEvaluationForm> ats_evaluation_forms_id_get(id)

Reads a single Evaluation form

Reads a single Evaluation form

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

api_instance = F::AtsEvaluationFormApi.new
id = '1' # String | List of IDs of the evaluation forms to be fetched.

begin
  # Reads a single Evaluation form
  result = api_instance.ats_evaluation_forms_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsEvaluationFormApi->ats_evaluation_forms_id_get: #{e}"
end
```

#### Using the ats_evaluation_forms_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsEvaluationForm>, Integer, Hash)> ats_evaluation_forms_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Evaluation form
  data, status_code, headers = api_instance.ats_evaluation_forms_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsEvaluationForm>
rescue F::ApiError => e
  puts "Error when calling AtsEvaluationFormApi->ats_evaluation_forms_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | List of IDs of the evaluation forms to be fetched. |  |

### Return type

[**AtsEvaluationForm**](AtsEvaluationForm.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_evaluation_forms_save_as_template_post

> <AtsEvaluationForm> ats_evaluation_forms_save_as_template_post(opts)

Save as templates an Evaluation form

Save an evaluation form as a template.

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

api_instance = F::AtsEvaluationFormApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Save as templates an Evaluation form
  result = api_instance.ats_evaluation_forms_save_as_template_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsEvaluationFormApi->ats_evaluation_forms_save_as_template_post: #{e}"
end
```

#### Using the ats_evaluation_forms_save_as_template_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsEvaluationForm>, Integer, Hash)> ats_evaluation_forms_save_as_template_post_with_http_info(opts)

```ruby
begin
  # Save as templates an Evaluation form
  data, status_code, headers = api_instance.ats_evaluation_forms_save_as_template_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsEvaluationForm>
rescue F::ApiError => e
  puts "Error when calling AtsEvaluationFormApi->ats_evaluation_forms_save_as_template_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**AtsEvaluationForm**](AtsEvaluationForm.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

