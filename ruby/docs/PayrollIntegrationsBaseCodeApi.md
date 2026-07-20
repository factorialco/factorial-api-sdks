# F::PayrollIntegrationsBaseCodeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**payroll_integrations_base_codes_get**](PayrollIntegrationsBaseCodeApi.md#payroll_integrations_base_codes_get) | **GET** /api/2026-07-01/resources/payroll_integrations_base/codes | Reads all Codes |
| [**payroll_integrations_base_codes_id_delete**](PayrollIntegrationsBaseCodeApi.md#payroll_integrations_base_codes_id_delete) | **DELETE** /api/2026-07-01/resources/payroll_integrations_base/codes/{id} | Deletes a Code |
| [**payroll_integrations_base_codes_id_put**](PayrollIntegrationsBaseCodeApi.md#payroll_integrations_base_codes_id_put) | **PUT** /api/2026-07-01/resources/payroll_integrations_base/codes/{id} | Updates a Code |
| [**payroll_integrations_base_codes_post**](PayrollIntegrationsBaseCodeApi.md#payroll_integrations_base_codes_post) | **POST** /api/2026-07-01/resources/payroll_integrations_base/codes | Creates a Code |


## payroll_integrations_base_codes_get

> <PayrollIntegrationsBaseCodesGet200Response> payroll_integrations_base_codes_get(integrations, opts)

Reads all Codes

Reads all Codes

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

api_instance = F::PayrollIntegrationsBaseCodeApi.new
integrations = ['inner_example'] # Array<String> | Payroll Integration names
opts = {
  code: 'COD-51', # String | Code Value
  codeable_id: '1', # String | Related object ID. Used together with codeable_type
  codeable_type: 'Employee | Company | LegalEntity | Location' # String | Related object type. Used together with codeable_id
}

begin
  # Reads all Codes
  result = api_instance.payroll_integrations_base_codes_get(integrations, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollIntegrationsBaseCodeApi->payroll_integrations_base_codes_get: #{e}"
end
```

#### Using the payroll_integrations_base_codes_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollIntegrationsBaseCodesGet200Response>, Integer, Hash)> payroll_integrations_base_codes_get_with_http_info(integrations, opts)

```ruby
begin
  # Reads all Codes
  data, status_code, headers = api_instance.payroll_integrations_base_codes_get_with_http_info(integrations, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollIntegrationsBaseCodesGet200Response>
rescue F::ApiError => e
  puts "Error when calling PayrollIntegrationsBaseCodeApi->payroll_integrations_base_codes_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **integrations** | [**Array&lt;String&gt;**](String.md) | Payroll Integration names |  |
| **code** | **String** | Code Value | [optional] |
| **codeable_id** | **String** | Related object ID. Used together with codeable_type | [optional] |
| **codeable_type** | **String** | Related object type. Used together with codeable_id | [optional] |

### Return type

[**PayrollIntegrationsBaseCodesGet200Response**](PayrollIntegrationsBaseCodesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## payroll_integrations_base_codes_id_delete

> <PayrollIntegrationsBaseCode> payroll_integrations_base_codes_id_delete(id)

Deletes a Code

Deletes a Code

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

api_instance = F::PayrollIntegrationsBaseCodeApi.new
id = '1' # String | 

begin
  # Deletes a Code
  result = api_instance.payroll_integrations_base_codes_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollIntegrationsBaseCodeApi->payroll_integrations_base_codes_id_delete: #{e}"
end
```

#### Using the payroll_integrations_base_codes_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollIntegrationsBaseCode>, Integer, Hash)> payroll_integrations_base_codes_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Code
  data, status_code, headers = api_instance.payroll_integrations_base_codes_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollIntegrationsBaseCode>
rescue F::ApiError => e
  puts "Error when calling PayrollIntegrationsBaseCodeApi->payroll_integrations_base_codes_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**PayrollIntegrationsBaseCode**](PayrollIntegrationsBaseCode.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## payroll_integrations_base_codes_id_put

> <PayrollIntegrationsBaseCode> payroll_integrations_base_codes_id_put(id, opts)

Updates a Code

Updates a Code

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

api_instance = F::PayrollIntegrationsBaseCodeApi.new
id = '1' # String | Code identifier
opts = {
  payroll_integrations_base_codes_id_put_request: F::PayrollIntegrationsBaseCodesIdPutRequest.new({id: '1', code: 'COD-51'}) # PayrollIntegrationsBaseCodesIdPutRequest | 
}

begin
  # Updates a Code
  result = api_instance.payroll_integrations_base_codes_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollIntegrationsBaseCodeApi->payroll_integrations_base_codes_id_put: #{e}"
end
```

#### Using the payroll_integrations_base_codes_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollIntegrationsBaseCode>, Integer, Hash)> payroll_integrations_base_codes_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Code
  data, status_code, headers = api_instance.payroll_integrations_base_codes_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollIntegrationsBaseCode>
rescue F::ApiError => e
  puts "Error when calling PayrollIntegrationsBaseCodeApi->payroll_integrations_base_codes_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Code identifier |  |
| **payroll_integrations_base_codes_id_put_request** | [**PayrollIntegrationsBaseCodesIdPutRequest**](PayrollIntegrationsBaseCodesIdPutRequest.md) |  | [optional] |

### Return type

[**PayrollIntegrationsBaseCode**](PayrollIntegrationsBaseCode.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## payroll_integrations_base_codes_post

> <PayrollIntegrationsBaseCode> payroll_integrations_base_codes_post(opts)

Creates a Code

Creates a Code

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

api_instance = F::PayrollIntegrationsBaseCodeApi.new
opts = {
  payroll_integrations_base_codes_post_request: F::PayrollIntegrationsBaseCodesPostRequest.new({code: 'COD-51', codeable_id: '1', codeable_type: 'Employee | Company | LegalEntity | Location | TimeoffLeaveType', integration: 'a3innuva'}) # PayrollIntegrationsBaseCodesPostRequest | 
}

begin
  # Creates a Code
  result = api_instance.payroll_integrations_base_codes_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollIntegrationsBaseCodeApi->payroll_integrations_base_codes_post: #{e}"
end
```

#### Using the payroll_integrations_base_codes_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollIntegrationsBaseCode>, Integer, Hash)> payroll_integrations_base_codes_post_with_http_info(opts)

```ruby
begin
  # Creates a Code
  data, status_code, headers = api_instance.payroll_integrations_base_codes_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollIntegrationsBaseCode>
rescue F::ApiError => e
  puts "Error when calling PayrollIntegrationsBaseCodeApi->payroll_integrations_base_codes_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **payroll_integrations_base_codes_post_request** | [**PayrollIntegrationsBaseCodesPostRequest**](PayrollIntegrationsBaseCodesPostRequest.md) |  | [optional] |

### Return type

[**PayrollIntegrationsBaseCode**](PayrollIntegrationsBaseCode.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

