# F::PayrollSupplementApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**payroll_supplements_get**](PayrollSupplementApi.md#payroll_supplements_get) | **GET** /api/2026-07-01/resources/payroll/supplements | Reads all Supplements |
| [**payroll_supplements_id_delete**](PayrollSupplementApi.md#payroll_supplements_id_delete) | **DELETE** /api/2026-07-01/resources/payroll/supplements/{id} | Deletes a Supplement |
| [**payroll_supplements_id_get**](PayrollSupplementApi.md#payroll_supplements_id_get) | **GET** /api/2026-07-01/resources/payroll/supplements/{id} | Reads a single Supplement |
| [**payroll_supplements_id_put**](PayrollSupplementApi.md#payroll_supplements_id_put) | **PUT** /api/2026-07-01/resources/payroll/supplements/{id} | Updates a Supplement |
| [**payroll_supplements_post**](PayrollSupplementApi.md#payroll_supplements_post) | **POST** /api/2026-07-01/resources/payroll/supplements | Creates a Supplement |


## payroll_supplements_get

> <PayrollSupplementsGet200Response> payroll_supplements_get(policy_period_ids, opts)

Reads all Supplements

Reads all Supplements

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

api_instance = F::PayrollSupplementApi.new
policy_period_ids = ['inner_example'] # Array<String> | The policy period ids to retrieve
opts = {
  from: '2024-01-01', # String | Valid date following the format YYYY-MM-DD
  to: '2024-01-01', # String | Valid date following the format YYYY-MM-DD
  employee_ids: ['inner_example'], # Array<String> | The employee ids to retrieve
  compensation_id: '1', # String | The compensation id to retrieve
  ids: ['inner_example'], # Array<String> | ids
  legal_entity_ids: ['inner_example'] # Array<String> | The legal entities id to retrieve
}

begin
  # Reads all Supplements
  result = api_instance.payroll_supplements_get(policy_period_ids, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollSupplementApi->payroll_supplements_get: #{e}"
end
```

#### Using the payroll_supplements_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollSupplementsGet200Response>, Integer, Hash)> payroll_supplements_get_with_http_info(policy_period_ids, opts)

```ruby
begin
  # Reads all Supplements
  data, status_code, headers = api_instance.payroll_supplements_get_with_http_info(policy_period_ids, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollSupplementsGet200Response>
rescue F::ApiError => e
  puts "Error when calling PayrollSupplementApi->payroll_supplements_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **policy_period_ids** | [**Array&lt;String&gt;**](String.md) | The policy period ids to retrieve |  |
| **from** | **String** | Valid date following the format YYYY-MM-DD | [optional] |
| **to** | **String** | Valid date following the format YYYY-MM-DD | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | The employee ids to retrieve | [optional] |
| **compensation_id** | **String** | The compensation id to retrieve | [optional] |
| **ids** | [**Array&lt;String&gt;**](String.md) | ids | [optional] |
| **legal_entity_ids** | [**Array&lt;String&gt;**](String.md) | The legal entities id to retrieve | [optional] |

### Return type

[**PayrollSupplementsGet200Response**](PayrollSupplementsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## payroll_supplements_id_delete

> <PayrollSupplement> payroll_supplements_id_delete(id)

Deletes a Supplement

Deletes a Supplement

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

api_instance = F::PayrollSupplementApi.new
id = '1' # String | 

begin
  # Deletes a Supplement
  result = api_instance.payroll_supplements_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollSupplementApi->payroll_supplements_id_delete: #{e}"
end
```

#### Using the payroll_supplements_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollSupplement>, Integer, Hash)> payroll_supplements_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Supplement
  data, status_code, headers = api_instance.payroll_supplements_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollSupplement>
rescue F::ApiError => e
  puts "Error when calling PayrollSupplementApi->payroll_supplements_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**PayrollSupplement**](PayrollSupplement.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## payroll_supplements_id_get

> <PayrollSupplement> payroll_supplements_id_get(id)

Reads a single Supplement

Reads a single Supplement

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

api_instance = F::PayrollSupplementApi.new
id = '1' # String | ids

begin
  # Reads a single Supplement
  result = api_instance.payroll_supplements_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollSupplementApi->payroll_supplements_id_get: #{e}"
end
```

#### Using the payroll_supplements_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollSupplement>, Integer, Hash)> payroll_supplements_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Supplement
  data, status_code, headers = api_instance.payroll_supplements_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollSupplement>
rescue F::ApiError => e
  puts "Error when calling PayrollSupplementApi->payroll_supplements_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | ids |  |

### Return type

[**PayrollSupplement**](PayrollSupplement.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## payroll_supplements_id_put

> <PayrollSupplement> payroll_supplements_id_put(id, opts)

Updates a Supplement

Updates a Supplement unless it is an additional compensation supplement (In such case, you need to create a new one, then remove the old compensation supplement from the contract and add the newly created one to it).

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

api_instance = F::PayrollSupplementApi.new
id = '1' # String | The supplement id
opts = {
  payroll_supplements_id_put_request: F::PayrollSupplementsIdPutRequest.new({id: '1'}) # PayrollSupplementsIdPutRequest | 
}

begin
  # Updates a Supplement
  result = api_instance.payroll_supplements_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollSupplementApi->payroll_supplements_id_put: #{e}"
end
```

#### Using the payroll_supplements_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollSupplement>, Integer, Hash)> payroll_supplements_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Supplement
  data, status_code, headers = api_instance.payroll_supplements_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollSupplement>
rescue F::ApiError => e
  puts "Error when calling PayrollSupplementApi->payroll_supplements_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The supplement id |  |
| **payroll_supplements_id_put_request** | [**PayrollSupplementsIdPutRequest**](PayrollSupplementsIdPutRequest.md) |  | [optional] |

### Return type

[**PayrollSupplement**](PayrollSupplement.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## payroll_supplements_post

> <PayrollSupplement> payroll_supplements_post(opts)

Creates a Supplement

Creates a Supplement

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

api_instance = F::PayrollSupplementApi.new
opts = {
  payroll_supplements_post_request: F::PayrollSupplementsPostRequest.new({amount_in_cents: 50000, employee_id: '1', effective_on: '2024-01-01', contracts_taxonomy_id: '2', payroll_policy_period_id: '1'}) # PayrollSupplementsPostRequest | 
}

begin
  # Creates a Supplement
  result = api_instance.payroll_supplements_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollSupplementApi->payroll_supplements_post: #{e}"
end
```

#### Using the payroll_supplements_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollSupplement>, Integer, Hash)> payroll_supplements_post_with_http_info(opts)

```ruby
begin
  # Creates a Supplement
  data, status_code, headers = api_instance.payroll_supplements_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollSupplement>
rescue F::ApiError => e
  puts "Error when calling PayrollSupplementApi->payroll_supplements_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **payroll_supplements_post_request** | [**PayrollSupplementsPostRequest**](PayrollSupplementsPostRequest.md) |  | [optional] |

### Return type

[**PayrollSupplement**](PayrollSupplement.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

