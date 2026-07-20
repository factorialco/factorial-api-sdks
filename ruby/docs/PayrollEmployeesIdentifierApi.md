# F::PayrollEmployeesIdentifierApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**payroll_employees_identifiers_get**](PayrollEmployeesIdentifierApi.md#payroll_employees_identifiers_get) | **GET** /api/2026-07-01/resources/payroll_employees/identifiers | Reads all Identifiers |
| [**payroll_employees_identifiers_id_delete**](PayrollEmployeesIdentifierApi.md#payroll_employees_identifiers_id_delete) | **DELETE** /api/2026-07-01/resources/payroll_employees/identifiers/{id} | Deletes an Identifier |
| [**payroll_employees_identifiers_id_get**](PayrollEmployeesIdentifierApi.md#payroll_employees_identifiers_id_get) | **GET** /api/2026-07-01/resources/payroll_employees/identifiers/{id} | Reads a single Identifier |
| [**payroll_employees_identifiers_id_put**](PayrollEmployeesIdentifierApi.md#payroll_employees_identifiers_id_put) | **PUT** /api/2026-07-01/resources/payroll_employees/identifiers/{id} | Updates an Identifier |
| [**payroll_employees_identifiers_post**](PayrollEmployeesIdentifierApi.md#payroll_employees_identifiers_post) | **POST** /api/2026-07-01/resources/payroll_employees/identifiers | Creates an Identifier |


## payroll_employees_identifiers_get

> <PayrollEmployeesIdentifiersGet200Response> payroll_employees_identifiers_get(country, opts)

Reads all Identifiers

Reads Payroll employee identifier codes, current countries supported are Portugal, Italy and Germany

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

api_instance = F::PayrollEmployeesIdentifierApi.new
country = 'pt' # String | filters by country code pt | it | de
opts = {
  ids: ['inner_example'], # Array<String> | 
  employees_ids: ['inner_example'], # Array<String> | filters by employee identifiers
  legal_entities_ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Identifiers
  result = api_instance.payroll_employees_identifiers_get(country, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollEmployeesIdentifierApi->payroll_employees_identifiers_get: #{e}"
end
```

#### Using the payroll_employees_identifiers_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollEmployeesIdentifiersGet200Response>, Integer, Hash)> payroll_employees_identifiers_get_with_http_info(country, opts)

```ruby
begin
  # Reads all Identifiers
  data, status_code, headers = api_instance.payroll_employees_identifiers_get_with_http_info(country, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollEmployeesIdentifiersGet200Response>
rescue F::ApiError => e
  puts "Error when calling PayrollEmployeesIdentifierApi->payroll_employees_identifiers_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **country** | **String** | filters by country code pt | it | de |  |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **employees_ids** | [**Array&lt;String&gt;**](String.md) | filters by employee identifiers | [optional] |
| **legal_entities_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**PayrollEmployeesIdentifiersGet200Response**](PayrollEmployeesIdentifiersGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## payroll_employees_identifiers_id_delete

> <PayrollEmployeesIdentifier> payroll_employees_identifiers_id_delete(id)

Deletes an Identifier

Reads Payroll employee identifier codes, current countries supported are Portugal, Italy and Germany

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

api_instance = F::PayrollEmployeesIdentifierApi.new
id = '1' # String | payroll employee identifier

begin
  # Deletes an Identifier
  result = api_instance.payroll_employees_identifiers_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollEmployeesIdentifierApi->payroll_employees_identifiers_id_delete: #{e}"
end
```

#### Using the payroll_employees_identifiers_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollEmployeesIdentifier>, Integer, Hash)> payroll_employees_identifiers_id_delete_with_http_info(id)

```ruby
begin
  # Deletes an Identifier
  data, status_code, headers = api_instance.payroll_employees_identifiers_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollEmployeesIdentifier>
rescue F::ApiError => e
  puts "Error when calling PayrollEmployeesIdentifierApi->payroll_employees_identifiers_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | payroll employee identifier |  |

### Return type

[**PayrollEmployeesIdentifier**](PayrollEmployeesIdentifier.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## payroll_employees_identifiers_id_get

> <PayrollEmployeesIdentifier> payroll_employees_identifiers_id_get(id)

Reads a single Identifier

Reads Payroll employee identifier codes, current countries supported are Portugal, Italy and Germany

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

api_instance = F::PayrollEmployeesIdentifierApi.new
id = '1' # String | 

begin
  # Reads a single Identifier
  result = api_instance.payroll_employees_identifiers_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollEmployeesIdentifierApi->payroll_employees_identifiers_id_get: #{e}"
end
```

#### Using the payroll_employees_identifiers_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollEmployeesIdentifier>, Integer, Hash)> payroll_employees_identifiers_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Identifier
  data, status_code, headers = api_instance.payroll_employees_identifiers_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollEmployeesIdentifier>
rescue F::ApiError => e
  puts "Error when calling PayrollEmployeesIdentifierApi->payroll_employees_identifiers_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**PayrollEmployeesIdentifier**](PayrollEmployeesIdentifier.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## payroll_employees_identifiers_id_put

> <PayrollEmployeesIdentifier> payroll_employees_identifiers_id_put(id, opts)

Updates an Identifier

Reads Payroll employee identifier codes, current countries supported are Portugal, Italy and Germany

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

api_instance = F::PayrollEmployeesIdentifierApi.new
id = '1' # String | payroll employee identifier
opts = {
  payroll_employees_identifiers_id_put_request: F::PayrollEmployeesIdentifiersIdPutRequest.new({id: '1', country: 'pt'}) # PayrollEmployeesIdentifiersIdPutRequest | 
}

begin
  # Updates an Identifier
  result = api_instance.payroll_employees_identifiers_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollEmployeesIdentifierApi->payroll_employees_identifiers_id_put: #{e}"
end
```

#### Using the payroll_employees_identifiers_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollEmployeesIdentifier>, Integer, Hash)> payroll_employees_identifiers_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates an Identifier
  data, status_code, headers = api_instance.payroll_employees_identifiers_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollEmployeesIdentifier>
rescue F::ApiError => e
  puts "Error when calling PayrollEmployeesIdentifierApi->payroll_employees_identifiers_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | payroll employee identifier |  |
| **payroll_employees_identifiers_id_put_request** | [**PayrollEmployeesIdentifiersIdPutRequest**](PayrollEmployeesIdentifiersIdPutRequest.md) |  | [optional] |

### Return type

[**PayrollEmployeesIdentifier**](PayrollEmployeesIdentifier.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## payroll_employees_identifiers_post

> <PayrollEmployeesIdentifier> payroll_employees_identifiers_post(opts)

Creates an Identifier

Reads Payroll employee identifier codes, current countries supported are Portugal, Italy and Germany

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

api_instance = F::PayrollEmployeesIdentifierApi.new
opts = {
  payroll_employees_identifiers_post_request: F::PayrollEmployeesIdentifiersPostRequest.new({employee_id: '1', country: 'pt'}) # PayrollEmployeesIdentifiersPostRequest | 
}

begin
  # Creates an Identifier
  result = api_instance.payroll_employees_identifiers_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollEmployeesIdentifierApi->payroll_employees_identifiers_post: #{e}"
end
```

#### Using the payroll_employees_identifiers_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollEmployeesIdentifier>, Integer, Hash)> payroll_employees_identifiers_post_with_http_info(opts)

```ruby
begin
  # Creates an Identifier
  data, status_code, headers = api_instance.payroll_employees_identifiers_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollEmployeesIdentifier>
rescue F::ApiError => e
  puts "Error when calling PayrollEmployeesIdentifierApi->payroll_employees_identifiers_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **payroll_employees_identifiers_post_request** | [**PayrollEmployeesIdentifiersPostRequest**](PayrollEmployeesIdentifiersPostRequest.md) |  | [optional] |

### Return type

[**PayrollEmployeesIdentifier**](PayrollEmployeesIdentifier.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

