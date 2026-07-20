# F::FinanceTaxRateApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**finance_tax_rates_get**](FinanceTaxRateApi.md#finance_tax_rates_get) | **GET** /api/2026-07-01/resources/finance/tax_rates | Reads all Tax rates |
| [**finance_tax_rates_id_get**](FinanceTaxRateApi.md#finance_tax_rates_id_get) | **GET** /api/2026-07-01/resources/finance/tax_rates/{id} | Reads a single Tax rate |
| [**finance_tax_rates_id_put**](FinanceTaxRateApi.md#finance_tax_rates_id_put) | **PUT** /api/2026-07-01/resources/finance/tax_rates/{id} | Updates a Tax rate |
| [**finance_tax_rates_post**](FinanceTaxRateApi.md#finance_tax_rates_post) | **POST** /api/2026-07-01/resources/finance/tax_rates | Creates a Tax rate |


## finance_tax_rates_get

> <FinanceTaxRatesGet200Response> finance_tax_rates_get(opts)

Reads all Tax rates

Reads all Tax rates

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

api_instance = F::FinanceTaxRateApi.new
opts = {
  ids: ['inner_example'], # Array<String> | List of TaxRate IDs to filter.
  tax_type_ids: ['inner_example'], # Array<String> | List of TaxType IDs to filter TaxRate records.
  updated_from: '2025-01-01' # String | Start date for filtering TaxRate records based on their last update.
}

begin
  # Reads all Tax rates
  result = api_instance.finance_tax_rates_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceTaxRateApi->finance_tax_rates_get: #{e}"
end
```

#### Using the finance_tax_rates_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceTaxRatesGet200Response>, Integer, Hash)> finance_tax_rates_get_with_http_info(opts)

```ruby
begin
  # Reads all Tax rates
  data, status_code, headers = api_instance.finance_tax_rates_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceTaxRatesGet200Response>
rescue F::ApiError => e
  puts "Error when calling FinanceTaxRateApi->finance_tax_rates_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | List of TaxRate IDs to filter. | [optional] |
| **tax_type_ids** | [**Array&lt;String&gt;**](String.md) | List of TaxType IDs to filter TaxRate records. | [optional] |
| **updated_from** | **String** | Start date for filtering TaxRate records based on their last update. | [optional] |

### Return type

[**FinanceTaxRatesGet200Response**](FinanceTaxRatesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_tax_rates_id_get

> <FinanceTaxRate> finance_tax_rates_id_get(id)

Reads a single Tax rate

Reads a single Tax rate

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

api_instance = F::FinanceTaxRateApi.new
id = '123' # String | List of TaxRate IDs to filter.

begin
  # Reads a single Tax rate
  result = api_instance.finance_tax_rates_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceTaxRateApi->finance_tax_rates_id_get: #{e}"
end
```

#### Using the finance_tax_rates_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceTaxRate>, Integer, Hash)> finance_tax_rates_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Tax rate
  data, status_code, headers = api_instance.finance_tax_rates_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceTaxRate>
rescue F::ApiError => e
  puts "Error when calling FinanceTaxRateApi->finance_tax_rates_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | List of TaxRate IDs to filter. |  |

### Return type

[**FinanceTaxRate**](FinanceTaxRate.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_tax_rates_id_put

> <FinanceTaxRate> finance_tax_rates_id_put(id, opts)

Updates a Tax rate

Updates a Tax rate

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

api_instance = F::FinanceTaxRateApi.new
id = '123' # String | The id of the tax rate.
opts = {
  finance_tax_rates_id_put_request: F::FinanceTaxRatesIdPutRequest.new({id: '123'}) # FinanceTaxRatesIdPutRequest | 
}

begin
  # Updates a Tax rate
  result = api_instance.finance_tax_rates_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceTaxRateApi->finance_tax_rates_id_put: #{e}"
end
```

#### Using the finance_tax_rates_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceTaxRate>, Integer, Hash)> finance_tax_rates_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Tax rate
  data, status_code, headers = api_instance.finance_tax_rates_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceTaxRate>
rescue F::ApiError => e
  puts "Error when calling FinanceTaxRateApi->finance_tax_rates_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the tax rate. |  |
| **finance_tax_rates_id_put_request** | [**FinanceTaxRatesIdPutRequest**](FinanceTaxRatesIdPutRequest.md) |  | [optional] |

### Return type

[**FinanceTaxRate**](FinanceTaxRate.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## finance_tax_rates_post

> <FinanceTaxRate> finance_tax_rates_post(opts)

Creates a Tax rate

Creates a Tax rate

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

api_instance = F::FinanceTaxRateApi.new
opts = {
  finance_tax_rates_post_request: F::FinanceTaxRatesPostRequest.new # FinanceTaxRatesPostRequest | 
}

begin
  # Creates a Tax rate
  result = api_instance.finance_tax_rates_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceTaxRateApi->finance_tax_rates_post: #{e}"
end
```

#### Using the finance_tax_rates_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceTaxRate>, Integer, Hash)> finance_tax_rates_post_with_http_info(opts)

```ruby
begin
  # Creates a Tax rate
  data, status_code, headers = api_instance.finance_tax_rates_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceTaxRate>
rescue F::ApiError => e
  puts "Error when calling FinanceTaxRateApi->finance_tax_rates_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **finance_tax_rates_post_request** | [**FinanceTaxRatesPostRequest**](FinanceTaxRatesPostRequest.md) |  | [optional] |

### Return type

[**FinanceTaxRate**](FinanceTaxRate.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

