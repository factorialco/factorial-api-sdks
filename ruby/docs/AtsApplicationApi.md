# F::AtsApplicationApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**ats_applications_apply_post**](AtsApplicationApi.md#ats_applications_apply_post) | **POST** /api/2026-07-01/resources/ats/applications/apply | Applies an Application |
| [**ats_applications_get**](AtsApplicationApi.md#ats_applications_get) | **GET** /api/2026-07-01/resources/ats/applications | Reads all Applications |
| [**ats_applications_id_delete**](AtsApplicationApi.md#ats_applications_id_delete) | **DELETE** /api/2026-07-01/resources/ats/applications/{id} | Deletes an Application |
| [**ats_applications_id_get**](AtsApplicationApi.md#ats_applications_id_get) | **GET** /api/2026-07-01/resources/ats/applications/{id} | Reads a single Application |
| [**ats_applications_id_put**](AtsApplicationApi.md#ats_applications_id_put) | **PUT** /api/2026-07-01/resources/ats/applications/{id} | Updates an Application |
| [**ats_applications_move_to_phase_post**](AtsApplicationApi.md#ats_applications_move_to_phase_post) | **POST** /api/2026-07-01/resources/ats/applications/move_to_phase | Move to phases an Application |
| [**ats_applications_post**](AtsApplicationApi.md#ats_applications_post) | **POST** /api/2026-07-01/resources/ats/applications | Creates an Application |


## ats_applications_apply_post

> <AtsApplication> ats_applications_apply_post(opts)

Applies an Application

Apply to a job posting

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

api_instance = F::AtsApplicationApi.new
opts = {
  ats_applications_apply_post_request: F::AtsApplicationsApplyPostRequest.new({first_name: 'Jane', last_name: 'Doe', ats_job_posting_id: '1', email: 'jane.doe@service.com'}) # AtsApplicationsApplyPostRequest | 
}

begin
  # Applies an Application
  result = api_instance.ats_applications_apply_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsApplicationApi->ats_applications_apply_post: #{e}"
end
```

#### Using the ats_applications_apply_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsApplication>, Integer, Hash)> ats_applications_apply_post_with_http_info(opts)

```ruby
begin
  # Applies an Application
  data, status_code, headers = api_instance.ats_applications_apply_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsApplication>
rescue F::ApiError => e
  puts "Error when calling AtsApplicationApi->ats_applications_apply_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_applications_apply_post_request** | [**AtsApplicationsApplyPostRequest**](AtsApplicationsApplyPostRequest.md) |  | [optional] |

### Return type

[**AtsApplication**](AtsApplication.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ats_applications_get

> <AtsApplicationsGet200Response> ats_applications_get(opts)

Reads all Applications

Reads all Applications

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

api_instance = F::AtsApplicationApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Application ids to retrieve
  ats_job_posting_id: '1', # String | Application job posting id to retrieve
  qualified: true, # Boolean | Retrieve applications by their qualified status
  ats_application_phase_id: '1', # String | Application phase id
  ats_candidate_ids: ['inner_example'], # Array<String> | Application candidates ids
  ats_rejection_reason_ids: ['inner_example'], # Array<String> | Application rejection reason ids
  search: 'application', # String | Application search
  ats_tags_ids: ['inner_example'] # Array<String> | Application tag ids
}

begin
  # Reads all Applications
  result = api_instance.ats_applications_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsApplicationApi->ats_applications_get: #{e}"
end
```

#### Using the ats_applications_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsApplicationsGet200Response>, Integer, Hash)> ats_applications_get_with_http_info(opts)

```ruby
begin
  # Reads all Applications
  data, status_code, headers = api_instance.ats_applications_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsApplicationsGet200Response>
rescue F::ApiError => e
  puts "Error when calling AtsApplicationApi->ats_applications_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Application ids to retrieve | [optional] |
| **ats_job_posting_id** | **String** | Application job posting id to retrieve | [optional] |
| **qualified** | **Boolean** | Retrieve applications by their qualified status | [optional] |
| **ats_application_phase_id** | **String** | Application phase id | [optional] |
| **ats_candidate_ids** | [**Array&lt;String&gt;**](String.md) | Application candidates ids | [optional] |
| **ats_rejection_reason_ids** | [**Array&lt;String&gt;**](String.md) | Application rejection reason ids | [optional] |
| **search** | **String** | Application search | [optional] |
| **ats_tags_ids** | [**Array&lt;String&gt;**](String.md) | Application tag ids | [optional] |

### Return type

[**AtsApplicationsGet200Response**](AtsApplicationsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_applications_id_delete

> <AtsApplication> ats_applications_id_delete(id)

Deletes an Application

Deletes an Application

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

api_instance = F::AtsApplicationApi.new
id = '1' # String | 

begin
  # Deletes an Application
  result = api_instance.ats_applications_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsApplicationApi->ats_applications_id_delete: #{e}"
end
```

#### Using the ats_applications_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsApplication>, Integer, Hash)> ats_applications_id_delete_with_http_info(id)

```ruby
begin
  # Deletes an Application
  data, status_code, headers = api_instance.ats_applications_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsApplication>
rescue F::ApiError => e
  puts "Error when calling AtsApplicationApi->ats_applications_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**AtsApplication**](AtsApplication.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_applications_id_get

> <AtsApplication> ats_applications_id_get(id)

Reads a single Application

Reads a single Application

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

api_instance = F::AtsApplicationApi.new
id = '1' # String | Application ids to retrieve

begin
  # Reads a single Application
  result = api_instance.ats_applications_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsApplicationApi->ats_applications_id_get: #{e}"
end
```

#### Using the ats_applications_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsApplication>, Integer, Hash)> ats_applications_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Application
  data, status_code, headers = api_instance.ats_applications_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsApplication>
rescue F::ApiError => e
  puts "Error when calling AtsApplicationApi->ats_applications_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Application ids to retrieve |  |

### Return type

[**AtsApplication**](AtsApplication.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_applications_id_put

> <AtsApplication> ats_applications_id_put(id, opts)

Updates an Application

Updates an Application

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

api_instance = F::AtsApplicationApi.new
id = '1' # String | Application id
opts = {
  ats_applications_id_put_request: F::AtsApplicationsIdPutRequest.new({id: '1'}) # AtsApplicationsIdPutRequest | 
}

begin
  # Updates an Application
  result = api_instance.ats_applications_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsApplicationApi->ats_applications_id_put: #{e}"
end
```

#### Using the ats_applications_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsApplication>, Integer, Hash)> ats_applications_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates an Application
  data, status_code, headers = api_instance.ats_applications_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsApplication>
rescue F::ApiError => e
  puts "Error when calling AtsApplicationApi->ats_applications_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Application id |  |
| **ats_applications_id_put_request** | [**AtsApplicationsIdPutRequest**](AtsApplicationsIdPutRequest.md) |  | [optional] |

### Return type

[**AtsApplication**](AtsApplication.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ats_applications_move_to_phase_post

> <AtsApplication> ats_applications_move_to_phase_post(opts)

Move to phases an Application

Move an application to a different phase within the same job posting. Triggers the same side effects as moving a candidate in the product: configured phase-change automations and emails (smart actions) are executed.

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

api_instance = F::AtsApplicationApi.new
opts = {
  ats_applications_move_to_phase_post_request: F::AtsApplicationsMoveToPhasePostRequest.new({id: '1', ats_application_phase_id: '1'}) # AtsApplicationsMoveToPhasePostRequest | 
}

begin
  # Move to phases an Application
  result = api_instance.ats_applications_move_to_phase_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsApplicationApi->ats_applications_move_to_phase_post: #{e}"
end
```

#### Using the ats_applications_move_to_phase_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsApplication>, Integer, Hash)> ats_applications_move_to_phase_post_with_http_info(opts)

```ruby
begin
  # Move to phases an Application
  data, status_code, headers = api_instance.ats_applications_move_to_phase_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsApplication>
rescue F::ApiError => e
  puts "Error when calling AtsApplicationApi->ats_applications_move_to_phase_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_applications_move_to_phase_post_request** | [**AtsApplicationsMoveToPhasePostRequest**](AtsApplicationsMoveToPhasePostRequest.md) |  | [optional] |

### Return type

[**AtsApplication**](AtsApplication.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ats_applications_post

> <AtsApplication> ats_applications_post(opts)

Creates an Application

Creates an Application

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

api_instance = F::AtsApplicationApi.new
opts = {
  ats_applications_post_request: F::AtsApplicationsPostRequest.new({ats_job_posting_id: '1'}) # AtsApplicationsPostRequest | 
}

begin
  # Creates an Application
  result = api_instance.ats_applications_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsApplicationApi->ats_applications_post: #{e}"
end
```

#### Using the ats_applications_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsApplication>, Integer, Hash)> ats_applications_post_with_http_info(opts)

```ruby
begin
  # Creates an Application
  data, status_code, headers = api_instance.ats_applications_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsApplication>
rescue F::ApiError => e
  puts "Error when calling AtsApplicationApi->ats_applications_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_applications_post_request** | [**AtsApplicationsPostRequest**](AtsApplicationsPostRequest.md) |  | [optional] |

### Return type

[**AtsApplication**](AtsApplication.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

