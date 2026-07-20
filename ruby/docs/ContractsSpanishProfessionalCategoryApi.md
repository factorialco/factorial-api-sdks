# F::ContractsSpanishProfessionalCategoryApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**contracts_spanish_professional_categories_get**](ContractsSpanishProfessionalCategoryApi.md#contracts_spanish_professional_categories_get) | **GET** /api/2026-07-01/resources/contracts/spanish_professional_categories | Reads all Spanish professional categories |
| [**contracts_spanish_professional_categories_id_get**](ContractsSpanishProfessionalCategoryApi.md#contracts_spanish_professional_categories_id_get) | **GET** /api/2026-07-01/resources/contracts/spanish_professional_categories/{id} | Reads a single Spanish professional category |
| [**contracts_spanish_professional_categories_post**](ContractsSpanishProfessionalCategoryApi.md#contracts_spanish_professional_categories_post) | **POST** /api/2026-07-01/resources/contracts/spanish_professional_categories | Creates a Spanish professional category |


## contracts_spanish_professional_categories_get

> <ContractsSpanishProfessionalCategoriesGet200Response> contracts_spanish_professional_categories_get(opts)

Reads all Spanish professional categories

Reads all Spanish professional categories

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

api_instance = F::ContractsSpanishProfessionalCategoryApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Professional category ids
  contract_template_id: '1' # String | Contract template identifier, refers to contracts/contract_templates
}

begin
  # Reads all Spanish professional categories
  result = api_instance.contracts_spanish_professional_categories_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishProfessionalCategoryApi->contracts_spanish_professional_categories_get: #{e}"
end
```

#### Using the contracts_spanish_professional_categories_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsSpanishProfessionalCategoriesGet200Response>, Integer, Hash)> contracts_spanish_professional_categories_get_with_http_info(opts)

```ruby
begin
  # Reads all Spanish professional categories
  data, status_code, headers = api_instance.contracts_spanish_professional_categories_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsSpanishProfessionalCategoriesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishProfessionalCategoryApi->contracts_spanish_professional_categories_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Professional category ids | [optional] |
| **contract_template_id** | **String** | Contract template identifier, refers to contracts/contract_templates | [optional] |

### Return type

[**ContractsSpanishProfessionalCategoriesGet200Response**](ContractsSpanishProfessionalCategoriesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_spanish_professional_categories_id_get

> <ContractsSpanishProfessionalCategory> contracts_spanish_professional_categories_id_get(id)

Reads a single Spanish professional category

Reads a single Spanish professional category

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

api_instance = F::ContractsSpanishProfessionalCategoryApi.new
id = '1' # String | Professional category ids

begin
  # Reads a single Spanish professional category
  result = api_instance.contracts_spanish_professional_categories_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishProfessionalCategoryApi->contracts_spanish_professional_categories_id_get: #{e}"
end
```

#### Using the contracts_spanish_professional_categories_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsSpanishProfessionalCategory>, Integer, Hash)> contracts_spanish_professional_categories_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Spanish professional category
  data, status_code, headers = api_instance.contracts_spanish_professional_categories_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsSpanishProfessionalCategory>
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishProfessionalCategoryApi->contracts_spanish_professional_categories_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Professional category ids |  |

### Return type

[**ContractsSpanishProfessionalCategory**](ContractsSpanishProfessionalCategory.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_spanish_professional_categories_post

> <ContractsSpanishProfessionalCategory> contracts_spanish_professional_categories_post(opts)

Creates a Spanish professional category

Creates a Spanish professional category

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

api_instance = F::ContractsSpanishProfessionalCategoryApi.new
opts = {
  contracts_spanish_contract_types_post_request: F::ContractsSpanishContractTypesPostRequest.new({name: 'Indefinido', contracts_contract_template_id: '1'}) # ContractsSpanishContractTypesPostRequest | 
}

begin
  # Creates a Spanish professional category
  result = api_instance.contracts_spanish_professional_categories_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishProfessionalCategoryApi->contracts_spanish_professional_categories_post: #{e}"
end
```

#### Using the contracts_spanish_professional_categories_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsSpanishProfessionalCategory>, Integer, Hash)> contracts_spanish_professional_categories_post_with_http_info(opts)

```ruby
begin
  # Creates a Spanish professional category
  data, status_code, headers = api_instance.contracts_spanish_professional_categories_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsSpanishProfessionalCategory>
rescue F::ApiError => e
  puts "Error when calling ContractsSpanishProfessionalCategoryApi->contracts_spanish_professional_categories_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **contracts_spanish_contract_types_post_request** | [**ContractsSpanishContractTypesPostRequest**](ContractsSpanishContractTypesPostRequest.md) |  | [optional] |

### Return type

[**ContractsSpanishProfessionalCategory**](ContractsSpanishProfessionalCategory.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

