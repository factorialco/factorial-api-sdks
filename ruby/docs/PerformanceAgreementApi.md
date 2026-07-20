# F::PerformanceAgreementApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**performance_agreements_bulk_initiate_post**](PerformanceAgreementApi.md#performance_agreements_bulk_initiate_post) | **POST** /api/2026-07-01/resources/performance/agreements/bulk_initiate | Bulk initiates an Agreement |
| [**performance_agreements_get**](PerformanceAgreementApi.md#performance_agreements_get) | **GET** /api/2026-07-01/resources/performance/agreements | Reads all Agreements |
| [**performance_agreements_id_get**](PerformanceAgreementApi.md#performance_agreements_id_get) | **GET** /api/2026-07-01/resources/performance/agreements/{id} | Reads a single Agreement |
| [**performance_agreements_initiate_post**](PerformanceAgreementApi.md#performance_agreements_initiate_post) | **POST** /api/2026-07-01/resources/performance/agreements/initiate | Initiates an Agreement |


## performance_agreements_bulk_initiate_post

> <Array<PerformanceAgreement>> performance_agreements_bulk_initiate_post(opts)

Bulk initiates an Agreement

Initiate the action plan for all your direct reports in a review process. If you are acting as a company, the action plan from all employees in the review process will be initiated.

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

api_instance = F::PerformanceAgreementApi.new
opts = {
  performance_agreements_bulk_initiate_post_request: F::PerformanceAgreementsBulkInitiatePostRequest.new({process_id: '1'}) # PerformanceAgreementsBulkInitiatePostRequest | 
}

begin
  # Bulk initiates an Agreement
  result = api_instance.performance_agreements_bulk_initiate_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceAgreementApi->performance_agreements_bulk_initiate_post: #{e}"
end
```

#### Using the performance_agreements_bulk_initiate_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<PerformanceAgreement>>, Integer, Hash)> performance_agreements_bulk_initiate_post_with_http_info(opts)

```ruby
begin
  # Bulk initiates an Agreement
  data, status_code, headers = api_instance.performance_agreements_bulk_initiate_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<PerformanceAgreement>>
rescue F::ApiError => e
  puts "Error when calling PerformanceAgreementApi->performance_agreements_bulk_initiate_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_agreements_bulk_initiate_post_request** | [**PerformanceAgreementsBulkInitiatePostRequest**](PerformanceAgreementsBulkInitiatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;PerformanceAgreement&gt;**](PerformanceAgreement.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performance_agreements_get

> <PerformanceAgreementsGet200Response> performance_agreements_get(opts)

Reads all Agreements

Retrieves the action plans of review processes.

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

api_instance = F::PerformanceAgreementApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Filter by action plan IDs
  process_ids: ['inner_example'], # Array<String> | Filter by review process IDs
  target_ids: ['inner_example'] # Array<String> | Filter by review process target IDs
}

begin
  # Reads all Agreements
  result = api_instance.performance_agreements_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceAgreementApi->performance_agreements_get: #{e}"
end
```

#### Using the performance_agreements_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceAgreementsGet200Response>, Integer, Hash)> performance_agreements_get_with_http_info(opts)

```ruby
begin
  # Reads all Agreements
  data, status_code, headers = api_instance.performance_agreements_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceAgreementsGet200Response>
rescue F::ApiError => e
  puts "Error when calling PerformanceAgreementApi->performance_agreements_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter by action plan IDs | [optional] |
| **process_ids** | [**Array&lt;String&gt;**](String.md) | Filter by review process IDs | [optional] |
| **target_ids** | [**Array&lt;String&gt;**](String.md) | Filter by review process target IDs | [optional] |

### Return type

[**PerformanceAgreementsGet200Response**](PerformanceAgreementsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_agreements_id_get

> <PerformanceAgreement> performance_agreements_id_get(id)

Reads a single Agreement

Retrieves the action plans of review processes.

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

api_instance = F::PerformanceAgreementApi.new
id = '1' # String | Filter by action plan IDs

begin
  # Reads a single Agreement
  result = api_instance.performance_agreements_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceAgreementApi->performance_agreements_id_get: #{e}"
end
```

#### Using the performance_agreements_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceAgreement>, Integer, Hash)> performance_agreements_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Agreement
  data, status_code, headers = api_instance.performance_agreements_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceAgreement>
rescue F::ApiError => e
  puts "Error when calling PerformanceAgreementApi->performance_agreements_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter by action plan IDs |  |

### Return type

[**PerformanceAgreement**](PerformanceAgreement.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## performance_agreements_initiate_post

> <PerformanceAgreement> performance_agreements_initiate_post(opts)

Initiates an Agreement

Initiate the action plan for a review process target ID in a review process.

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

api_instance = F::PerformanceAgreementApi.new
opts = {
  performance_agreements_initiate_post_request: F::PerformanceAgreementsInitiatePostRequest.new({process_id: '1', target_id: '1-3'}) # PerformanceAgreementsInitiatePostRequest | 
}

begin
  # Initiates an Agreement
  result = api_instance.performance_agreements_initiate_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PerformanceAgreementApi->performance_agreements_initiate_post: #{e}"
end
```

#### Using the performance_agreements_initiate_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PerformanceAgreement>, Integer, Hash)> performance_agreements_initiate_post_with_http_info(opts)

```ruby
begin
  # Initiates an Agreement
  data, status_code, headers = api_instance.performance_agreements_initiate_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PerformanceAgreement>
rescue F::ApiError => e
  puts "Error when calling PerformanceAgreementApi->performance_agreements_initiate_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_agreements_initiate_post_request** | [**PerformanceAgreementsInitiatePostRequest**](PerformanceAgreementsInitiatePostRequest.md) |  | [optional] |

### Return type

[**PerformanceAgreement**](PerformanceAgreement.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

