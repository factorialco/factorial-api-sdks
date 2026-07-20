# F::ContractsTaxonomyApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**contracts_taxonomies_get**](ContractsTaxonomyApi.md#contracts_taxonomies_get) | **GET** /api/2026-07-01/resources/contracts/taxonomies | Reads all Taxonomies |
| [**contracts_taxonomies_id_get**](ContractsTaxonomyApi.md#contracts_taxonomies_id_get) | **GET** /api/2026-07-01/resources/contracts/taxonomies/{id} | Reads a single Taxonomy |


## contracts_taxonomies_get

> <ContractsTaxonomiesGet200Response> contracts_taxonomies_get(opts)

Reads all Taxonomies

Reads all Taxonomies

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

api_instance = F::ContractsTaxonomyApi.new
opts = {
  ids: ['inner_example'], # Array<String> | 
  legal_entity_ids: ['inner_example'], # Array<String> | 
  legal_entity_id: 'legal_entity_id_example' # String | 
}

begin
  # Reads all Taxonomies
  result = api_instance.contracts_taxonomies_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsTaxonomyApi->contracts_taxonomies_get: #{e}"
end
```

#### Using the contracts_taxonomies_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsTaxonomiesGet200Response>, Integer, Hash)> contracts_taxonomies_get_with_http_info(opts)

```ruby
begin
  # Reads all Taxonomies
  data, status_code, headers = api_instance.contracts_taxonomies_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsTaxonomiesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ContractsTaxonomyApi->contracts_taxonomies_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **legal_entity_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **legal_entity_id** | **String** |  | [optional] |

### Return type

[**ContractsTaxonomiesGet200Response**](ContractsTaxonomiesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_taxonomies_id_get

> <ContractsTaxonomy> contracts_taxonomies_id_get(id)

Reads a single Taxonomy

Reads a single Taxonomy

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

api_instance = F::ContractsTaxonomyApi.new
id = '1' # String | 

begin
  # Reads a single Taxonomy
  result = api_instance.contracts_taxonomies_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsTaxonomyApi->contracts_taxonomies_id_get: #{e}"
end
```

#### Using the contracts_taxonomies_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsTaxonomy>, Integer, Hash)> contracts_taxonomies_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Taxonomy
  data, status_code, headers = api_instance.contracts_taxonomies_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsTaxonomy>
rescue F::ApiError => e
  puts "Error when calling ContractsTaxonomyApi->contracts_taxonomies_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**ContractsTaxonomy**](ContractsTaxonomy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

