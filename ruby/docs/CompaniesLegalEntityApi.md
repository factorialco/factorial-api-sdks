# F::CompaniesLegalEntityApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**companies_legal_entities_get**](CompaniesLegalEntityApi.md#companies_legal_entities_get) | **GET** /api/2026-07-01/resources/companies/legal_entities | Reads all Legal entities |
| [**companies_legal_entities_id_get**](CompaniesLegalEntityApi.md#companies_legal_entities_id_get) | **GET** /api/2026-07-01/resources/companies/legal_entities/{id} | Reads a single Legal entity |
| [**companies_legal_entities_post**](CompaniesLegalEntityApi.md#companies_legal_entities_post) | **POST** /api/2026-07-01/resources/companies/legal_entities | Creates a Legal entity |


## companies_legal_entities_get

> <CompaniesLegalEntitiesGet200Response> companies_legal_entities_get(opts)

Reads all Legal entities

Reads all Legal entities

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

api_instance = F::CompaniesLegalEntityApi.new
opts = {
  ids: ['inner_example'], # Array<String> | identifier of the legal entity
  employees_ids: ['inner_example'], # Array<String> | identifier of the employees asigned to the legal entity
  companies_ids: ['inner_example'], # Array<String> | identifier of the companies to which the legal entity belongs
  country_ids: ['inner_example'] # Array<String> | country code of the legal entity
}

begin
  # Reads all Legal entities
  result = api_instance.companies_legal_entities_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CompaniesLegalEntityApi->companies_legal_entities_get: #{e}"
end
```

#### Using the companies_legal_entities_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CompaniesLegalEntitiesGet200Response>, Integer, Hash)> companies_legal_entities_get_with_http_info(opts)

```ruby
begin
  # Reads all Legal entities
  data, status_code, headers = api_instance.companies_legal_entities_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CompaniesLegalEntitiesGet200Response>
rescue F::ApiError => e
  puts "Error when calling CompaniesLegalEntityApi->companies_legal_entities_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | identifier of the legal entity | [optional] |
| **employees_ids** | [**Array&lt;String&gt;**](String.md) | identifier of the employees asigned to the legal entity | [optional] |
| **companies_ids** | [**Array&lt;String&gt;**](String.md) | identifier of the companies to which the legal entity belongs | [optional] |
| **country_ids** | [**Array&lt;String&gt;**](String.md) | country code of the legal entity | [optional] |

### Return type

[**CompaniesLegalEntitiesGet200Response**](CompaniesLegalEntitiesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companies_legal_entities_id_get

> <CompaniesLegalEntity> companies_legal_entities_id_get(id)

Reads a single Legal entity

Reads a single Legal entity

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

api_instance = F::CompaniesLegalEntityApi.new
id = '754' # String | identifier of the legal entity

begin
  # Reads a single Legal entity
  result = api_instance.companies_legal_entities_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling CompaniesLegalEntityApi->companies_legal_entities_id_get: #{e}"
end
```

#### Using the companies_legal_entities_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CompaniesLegalEntity>, Integer, Hash)> companies_legal_entities_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Legal entity
  data, status_code, headers = api_instance.companies_legal_entities_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CompaniesLegalEntity>
rescue F::ApiError => e
  puts "Error when calling CompaniesLegalEntityApi->companies_legal_entities_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the legal entity |  |

### Return type

[**CompaniesLegalEntity**](CompaniesLegalEntity.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## companies_legal_entities_post

> <CompaniesLegalEntity> companies_legal_entities_post(opts)

Creates a Legal entity

Creates a Legal entity

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

api_instance = F::CompaniesLegalEntityApi.new
opts = {
  companies_legal_entities_post_request: F::CompaniesLegalEntitiesPostRequest.new({company_id: '1', country: 'es', legal_name: 'Acme Inc.', currency: 'EUR'}) # CompaniesLegalEntitiesPostRequest | 
}

begin
  # Creates a Legal entity
  result = api_instance.companies_legal_entities_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CompaniesLegalEntityApi->companies_legal_entities_post: #{e}"
end
```

#### Using the companies_legal_entities_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CompaniesLegalEntity>, Integer, Hash)> companies_legal_entities_post_with_http_info(opts)

```ruby
begin
  # Creates a Legal entity
  data, status_code, headers = api_instance.companies_legal_entities_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CompaniesLegalEntity>
rescue F::ApiError => e
  puts "Error when calling CompaniesLegalEntityApi->companies_legal_entities_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **companies_legal_entities_post_request** | [**CompaniesLegalEntitiesPostRequest**](CompaniesLegalEntitiesPostRequest.md) |  | [optional] |

### Return type

[**CompaniesLegalEntity**](CompaniesLegalEntity.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

