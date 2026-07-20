# F::ContractsCompensationApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**contracts_compensations_get**](ContractsCompensationApi.md#contracts_compensations_get) | **GET** /api/2026-07-01/resources/contracts/compensations | Reads all Compensations |
| [**contracts_compensations_id_delete**](ContractsCompensationApi.md#contracts_compensations_id_delete) | **DELETE** /api/2026-07-01/resources/contracts/compensations/{id} | Deletes a Compensation |
| [**contracts_compensations_id_get**](ContractsCompensationApi.md#contracts_compensations_id_get) | **GET** /api/2026-07-01/resources/contracts/compensations/{id} | Reads a single Compensation |
| [**contracts_compensations_id_put**](ContractsCompensationApi.md#contracts_compensations_id_put) | **PUT** /api/2026-07-01/resources/contracts/compensations/{id} | Updates a Compensation |
| [**contracts_compensations_post**](ContractsCompensationApi.md#contracts_compensations_post) | **POST** /api/2026-07-01/resources/contracts/compensations | Creates a Compensation |


## contracts_compensations_get

> <ContractsCompensationsGet200Response> contracts_compensations_get(opts)

Reads all Compensations

Reads all Compensations

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

api_instance = F::ContractsCompensationApi.new
opts = {
  ids: ['inner_example'], # Array<String> | 
  contract_version_ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Compensations
  result = api_instance.contracts_compensations_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsCompensationApi->contracts_compensations_get: #{e}"
end
```

#### Using the contracts_compensations_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsCompensationsGet200Response>, Integer, Hash)> contracts_compensations_get_with_http_info(opts)

```ruby
begin
  # Reads all Compensations
  data, status_code, headers = api_instance.contracts_compensations_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsCompensationsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ContractsCompensationApi->contracts_compensations_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **contract_version_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**ContractsCompensationsGet200Response**](ContractsCompensationsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_compensations_id_delete

> <ContractsCompensation> contracts_compensations_id_delete(id)

Deletes a Compensation

Deletes a Compensation

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

api_instance = F::ContractsCompensationApi.new
id = '1' # String | 

begin
  # Deletes a Compensation
  result = api_instance.contracts_compensations_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsCompensationApi->contracts_compensations_id_delete: #{e}"
end
```

#### Using the contracts_compensations_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsCompensation>, Integer, Hash)> contracts_compensations_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Compensation
  data, status_code, headers = api_instance.contracts_compensations_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsCompensation>
rescue F::ApiError => e
  puts "Error when calling ContractsCompensationApi->contracts_compensations_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**ContractsCompensation**](ContractsCompensation.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_compensations_id_get

> <ContractsCompensation> contracts_compensations_id_get(id)

Reads a single Compensation

Reads a single Compensation

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

api_instance = F::ContractsCompensationApi.new
id = '1' # String | 

begin
  # Reads a single Compensation
  result = api_instance.contracts_compensations_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsCompensationApi->contracts_compensations_id_get: #{e}"
end
```

#### Using the contracts_compensations_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsCompensation>, Integer, Hash)> contracts_compensations_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Compensation
  data, status_code, headers = api_instance.contracts_compensations_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsCompensation>
rescue F::ApiError => e
  puts "Error when calling ContractsCompensationApi->contracts_compensations_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**ContractsCompensation**](ContractsCompensation.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_compensations_id_put

> <ContractsCompensation> contracts_compensations_id_put(id, opts)

Updates a Compensation

Updates a Compensation

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

api_instance = F::ContractsCompensationApi.new
id = '1' # String | 
opts = {
  contracts_compensations_id_put_request: F::ContractsCompensationsIdPutRequest.new({contracts_taxonomy_id: 'contracts_taxonomy_id_example'}) # ContractsCompensationsIdPutRequest | 
}

begin
  # Updates a Compensation
  result = api_instance.contracts_compensations_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsCompensationApi->contracts_compensations_id_put: #{e}"
end
```

#### Using the contracts_compensations_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsCompensation>, Integer, Hash)> contracts_compensations_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Compensation
  data, status_code, headers = api_instance.contracts_compensations_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsCompensation>
rescue F::ApiError => e
  puts "Error when calling ContractsCompensationApi->contracts_compensations_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **contracts_compensations_id_put_request** | [**ContractsCompensationsIdPutRequest**](ContractsCompensationsIdPutRequest.md) |  | [optional] |

### Return type

[**ContractsCompensation**](ContractsCompensation.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contracts_compensations_post

> <ContractsCompensation> contracts_compensations_post(opts)

Creates a Compensation

Creates a Compensation

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

api_instance = F::ContractsCompensationApi.new
opts = {
  contracts_compensations_post_request: F::ContractsCompensationsPostRequest.new({contract_version_id: 'contract_version_id_example', contracts_taxonomy_id: 'contracts_taxonomy_id_example'}) # ContractsCompensationsPostRequest | 
}

begin
  # Creates a Compensation
  result = api_instance.contracts_compensations_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsCompensationApi->contracts_compensations_post: #{e}"
end
```

#### Using the contracts_compensations_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsCompensation>, Integer, Hash)> contracts_compensations_post_with_http_info(opts)

```ruby
begin
  # Creates a Compensation
  data, status_code, headers = api_instance.contracts_compensations_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsCompensation>
rescue F::ApiError => e
  puts "Error when calling ContractsCompensationApi->contracts_compensations_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **contracts_compensations_post_request** | [**ContractsCompensationsPostRequest**](ContractsCompensationsPostRequest.md) |  | [optional] |

### Return type

[**ContractsCompensation**](ContractsCompensation.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

