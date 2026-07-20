# F::PayrollFamilySituationApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**payroll_family_situations_get**](PayrollFamilySituationApi.md#payroll_family_situations_get) | **GET** /api/2026-07-01/resources/payroll/family_situations | Reads all Family situations |
| [**payroll_family_situations_id_put**](PayrollFamilySituationApi.md#payroll_family_situations_id_put) | **PUT** /api/2026-07-01/resources/payroll/family_situations/{id} | Updates a Family situation |
| [**payroll_family_situations_post**](PayrollFamilySituationApi.md#payroll_family_situations_post) | **POST** /api/2026-07-01/resources/payroll/family_situations | Creates a Family situation |


## payroll_family_situations_get

> <PayrollFamilySituationsGet200Response> payroll_family_situations_get(opts)

Reads all Family situations

Get all family situations.

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

api_instance = F::PayrollFamilySituationApi.new
opts = {
  employee_ids: ['inner_example'] # Array<String> | employee ids.
}

begin
  # Reads all Family situations
  result = api_instance.payroll_family_situations_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollFamilySituationApi->payroll_family_situations_get: #{e}"
end
```

#### Using the payroll_family_situations_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollFamilySituationsGet200Response>, Integer, Hash)> payroll_family_situations_get_with_http_info(opts)

```ruby
begin
  # Reads all Family situations
  data, status_code, headers = api_instance.payroll_family_situations_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollFamilySituationsGet200Response>
rescue F::ApiError => e
  puts "Error when calling PayrollFamilySituationApi->payroll_family_situations_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | employee ids. | [optional] |

### Return type

[**PayrollFamilySituationsGet200Response**](PayrollFamilySituationsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## payroll_family_situations_id_put

> <PayrollFamilySituation> payroll_family_situations_id_put(id, opts)

Updates a Family situation

Update a family situation.

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

api_instance = F::PayrollFamilySituationApi.new
id = '3' # String | Family situation id.
opts = {
  payroll_family_situations_id_put_request: F::PayrollFamilySituationsIdPutRequest.new({id: '3', employee_id: '10'}) # PayrollFamilySituationsIdPutRequest | 
}

begin
  # Updates a Family situation
  result = api_instance.payroll_family_situations_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollFamilySituationApi->payroll_family_situations_id_put: #{e}"
end
```

#### Using the payroll_family_situations_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollFamilySituation>, Integer, Hash)> payroll_family_situations_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Family situation
  data, status_code, headers = api_instance.payroll_family_situations_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollFamilySituation>
rescue F::ApiError => e
  puts "Error when calling PayrollFamilySituationApi->payroll_family_situations_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Family situation id. |  |
| **payroll_family_situations_id_put_request** | [**PayrollFamilySituationsIdPutRequest**](PayrollFamilySituationsIdPutRequest.md) |  | [optional] |

### Return type

[**PayrollFamilySituation**](PayrollFamilySituation.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## payroll_family_situations_post

> <PayrollFamilySituation> payroll_family_situations_post(opts)

Creates a Family situation

Create a family situation.

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

api_instance = F::PayrollFamilySituationApi.new
opts = {
  payroll_family_situations_post_request: F::PayrollFamilySituationsPostRequest.new({employee_id: '10'}) # PayrollFamilySituationsPostRequest | 
}

begin
  # Creates a Family situation
  result = api_instance.payroll_family_situations_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollFamilySituationApi->payroll_family_situations_post: #{e}"
end
```

#### Using the payroll_family_situations_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollFamilySituation>, Integer, Hash)> payroll_family_situations_post_with_http_info(opts)

```ruby
begin
  # Creates a Family situation
  data, status_code, headers = api_instance.payroll_family_situations_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollFamilySituation>
rescue F::ApiError => e
  puts "Error when calling PayrollFamilySituationApi->payroll_family_situations_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **payroll_family_situations_post_request** | [**PayrollFamilySituationsPostRequest**](PayrollFamilySituationsPostRequest.md) |  | [optional] |

### Return type

[**PayrollFamilySituation**](PayrollFamilySituation.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

