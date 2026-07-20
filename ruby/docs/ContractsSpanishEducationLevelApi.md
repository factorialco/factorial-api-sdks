# F::ContractsSpanishEducationLevelApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**contracts_spanish_education_levels_get**](ContractsSpanishEducationLevelApi.md#contracts_spanish_education_levels_get) | **GET** /api/2026-07-01/resources/contracts/spanish_education_levels | Reads all Spanish education levels |
| [**contracts_spanish_education_levels_id_get**](ContractsSpanishEducationLevelApi.md#contracts_spanish_education_levels_id_get) | **GET** /api/2026-07-01/resources/contracts/spanish_education_levels/{id} | Reads a single Spanish education level |
| [**contracts_spanish_education_levels_post**](ContractsSpanishEducationLevelApi.md#contracts_spanish_education_levels_post) | **POST** /api/2026-07-01/resources/contracts/spanish_education_levels | Creates a Spanish education level |


## contracts_spanish_education_levels_get

> <ContractsSpanishEducationLevelsGet200Response> contracts_spanish_education_levels_get(opts)

Reads all Spanish education levels

Reads all Spanish education levels

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

api_instance = F::ContractsSpanishEducationLevelApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Education level ids
  contract_template_id: '1' # String | Contract template identifier, refers to contracts/contract_templates
}

begin
  # Reads all Spanish education levels
  result = api_instance.contracts_spanish_education_levels_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishEducationLevelApi->contracts_spanish_education_levels_get: #{e}"
end
```

#### Using the contracts_spanish_education_levels_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsSpanishEducationLevelsGet200Response>, Integer, Hash)> contracts_spanish_education_levels_get_with_http_info(opts)

```ruby
begin
  # Reads all Spanish education levels
  data, status_code, headers = api_instance.contracts_spanish_education_levels_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsSpanishEducationLevelsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishEducationLevelApi->contracts_spanish_education_levels_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Education level ids | [optional] |
| **contract_template_id** | **String** | Contract template identifier, refers to contracts/contract_templates | [optional] |

### Return type

[**ContractsSpanishEducationLevelsGet200Response**](ContractsSpanishEducationLevelsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_spanish_education_levels_id_get

> <ContractsSpanishEducationLevel> contracts_spanish_education_levels_id_get(id)

Reads a single Spanish education level

Reads a single Spanish education level

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

api_instance = F::ContractsSpanishEducationLevelApi.new
id = '1' # String | Education level ids

begin
  # Reads a single Spanish education level
  result = api_instance.contracts_spanish_education_levels_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishEducationLevelApi->contracts_spanish_education_levels_id_get: #{e}"
end
```

#### Using the contracts_spanish_education_levels_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsSpanishEducationLevel>, Integer, Hash)> contracts_spanish_education_levels_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Spanish education level
  data, status_code, headers = api_instance.contracts_spanish_education_levels_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsSpanishEducationLevel>
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishEducationLevelApi->contracts_spanish_education_levels_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Education level ids |  |

### Return type

[**ContractsSpanishEducationLevel**](ContractsSpanishEducationLevel.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_spanish_education_levels_post

> <ContractsSpanishEducationLevel> contracts_spanish_education_levels_post(opts)

Creates a Spanish education level

Creates a Spanish education level

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

api_instance = F::ContractsSpanishEducationLevelApi.new
opts = {
  contracts_spanish_contract_types_post_request: F::ContractsSpanishContractTypesPostRequest.new({name: 'Indefinido', contracts_contract_template_id: '1'}) # ContractsSpanishContractTypesPostRequest | 
}

begin
  # Creates a Spanish education level
  result = api_instance.contracts_spanish_education_levels_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishEducationLevelApi->contracts_spanish_education_levels_post: #{e}"
end
```

#### Using the contracts_spanish_education_levels_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsSpanishEducationLevel>, Integer, Hash)> contracts_spanish_education_levels_post_with_http_info(opts)

```ruby
begin
  # Creates a Spanish education level
  data, status_code, headers = api_instance.contracts_spanish_education_levels_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsSpanishEducationLevel>
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishEducationLevelApi->contracts_spanish_education_levels_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **contracts_spanish_contract_types_post_request** | [**ContractsSpanishContractTypesPostRequest**](ContractsSpanishContractTypesPostRequest.md) |  | [optional] |

### Return type

[**ContractsSpanishEducationLevel**](ContractsSpanishEducationLevel.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

