# F::FinanceTaxTypeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**finance_tax_types_get**](FinanceTaxTypeApi.md#finance_tax_types_get) | **GET** /api/2026-07-01/resources/finance/tax_types | Reads all Tax types |
| [**finance_tax_types_id_get**](FinanceTaxTypeApi.md#finance_tax_types_id_get) | **GET** /api/2026-07-01/resources/finance/tax_types/{id} | Reads a single Tax type |
| [**finance_tax_types_id_put**](FinanceTaxTypeApi.md#finance_tax_types_id_put) | **PUT** /api/2026-07-01/resources/finance/tax_types/{id} | Updates a Tax type |
| [**finance_tax_types_post**](FinanceTaxTypeApi.md#finance_tax_types_post) | **POST** /api/2026-07-01/resources/finance/tax_types | Creates a Tax type |


## finance_tax_types_get

> <FinanceTaxTypesGet200Response> finance_tax_types_get(opts)

Reads all Tax types

Reads all Tax types

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

api_instance = F::FinanceTaxTypeApi.new
opts = {
  ids: ['inner_example'], # Array<String> | List of TaxType IDs to filter.
  country_code: 'ES', # String | Filters TaxTypes by a specified country code or includes those without any country code if set to nil.
  type: 'vat', # String | Filters TaxTypes by a type (vat, personal_income).
  updated_from: '2025-01-01' # String | Start date for filtering TaxType records based on their last update.
}

begin
  # Reads all Tax types
  result = api_instance.finance_tax_types_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceTaxTypeApi->finance_tax_types_get: #{e}"
end
```

#### Using the finance_tax_types_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceTaxTypesGet200Response>, Integer, Hash)> finance_tax_types_get_with_http_info(opts)

```ruby
begin
  # Reads all Tax types
  data, status_code, headers = api_instance.finance_tax_types_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceTaxTypesGet200Response>
rescue F::ApiError => e
  puts "Error when calling FinanceTaxTypeApi->finance_tax_types_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | List of TaxType IDs to filter. | [optional] |
| **country_code** | **String** | Filters TaxTypes by a specified country code or includes those without any country code if set to nil. | [optional] |
| **type** | **String** | Filters TaxTypes by a type (vat, personal_income). | [optional] |
| **updated_from** | **String** | Start date for filtering TaxType records based on their last update. | [optional] |

### Return type

[**FinanceTaxTypesGet200Response**](FinanceTaxTypesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_tax_types_id_get

> <FinanceTaxType> finance_tax_types_id_get(id)

Reads a single Tax type

Reads a single Tax type

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

api_instance = F::FinanceTaxTypeApi.new
id = '1234' # String | List of TaxType IDs to filter.

begin
  # Reads a single Tax type
  result = api_instance.finance_tax_types_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceTaxTypeApi->finance_tax_types_id_get: #{e}"
end
```

#### Using the finance_tax_types_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceTaxType>, Integer, Hash)> finance_tax_types_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Tax type
  data, status_code, headers = api_instance.finance_tax_types_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceTaxType>
rescue F::ApiError => e
  puts "Error when calling FinanceTaxTypeApi->finance_tax_types_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | List of TaxType IDs to filter. |  |

### Return type

[**FinanceTaxType**](FinanceTaxType.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_tax_types_id_put

> <FinanceTaxType> finance_tax_types_id_put(id, opts)

Updates a Tax type

Updates a Tax type

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

api_instance = F::FinanceTaxTypeApi.new
id = '1234' # String | The id of the tax type.
opts = {
  finance_tax_types_id_put_request: F::FinanceTaxTypesIdPutRequest.new({id: '1234', type: 'vat'}) # FinanceTaxTypesIdPutRequest | 
}

begin
  # Updates a Tax type
  result = api_instance.finance_tax_types_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceTaxTypeApi->finance_tax_types_id_put: #{e}"
end
```

#### Using the finance_tax_types_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceTaxType>, Integer, Hash)> finance_tax_types_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Tax type
  data, status_code, headers = api_instance.finance_tax_types_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceTaxType>
rescue F::ApiError => e
  puts "Error when calling FinanceTaxTypeApi->finance_tax_types_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the tax type. |  |
| **finance_tax_types_id_put_request** | [**FinanceTaxTypesIdPutRequest**](FinanceTaxTypesIdPutRequest.md) |  | [optional] |

### Return type

[**FinanceTaxType**](FinanceTaxType.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## finance_tax_types_post

> <FinanceTaxType> finance_tax_types_post(opts)

Creates a Tax type

Creates a Tax type

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

api_instance = F::FinanceTaxTypeApi.new
opts = {
  finance_tax_types_post_request: F::FinanceTaxTypesPostRequest.new({name: 'general IVA', type: 'vat'}) # FinanceTaxTypesPostRequest | 
}

begin
  # Creates a Tax type
  result = api_instance.finance_tax_types_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceTaxTypeApi->finance_tax_types_post: #{e}"
end
```

#### Using the finance_tax_types_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceTaxType>, Integer, Hash)> finance_tax_types_post_with_http_info(opts)

```ruby
begin
  # Creates a Tax type
  data, status_code, headers = api_instance.finance_tax_types_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceTaxType>
rescue F::ApiError => e
  puts "Error when calling FinanceTaxTypeApi->finance_tax_types_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **finance_tax_types_post_request** | [**FinanceTaxTypesPostRequest**](FinanceTaxTypesPostRequest.md) |  | [optional] |

### Return type

[**FinanceTaxType**](FinanceTaxType.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

