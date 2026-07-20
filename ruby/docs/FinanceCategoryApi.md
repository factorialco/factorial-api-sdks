# F::FinanceCategoryApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**finance_categories_get**](FinanceCategoryApi.md#finance_categories_get) | **GET** /api/2026-07-01/resources/finance/categories | Reads all Categories |
| [**finance_categories_id_get**](FinanceCategoryApi.md#finance_categories_id_get) | **GET** /api/2026-07-01/resources/finance/categories/{id} | Reads a single Category |


## finance_categories_get

> <FinanceCategoriesGet200Response> finance_categories_get(category_level, type, statuses, opts)

Reads all Categories

Fetch expense categories and subcategories for the company

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

api_instance = F::FinanceCategoryApi.new
category_level = 'category' # String | Filter by category level
type = 'mileage' # String | Filter by category type
statuses = ['inner_example'] # Array<String> | Filter by category status
opts = {
  ids: ['inner_example'], # Array<String> | Search categories by ID
  company_ids: ['inner_example'], # Array<String> | Search categories by company IDs
  parent_category_ids: ['inner_example'], # Array<String> | Search subcategories by parent category ID
  search: 'accommodation' # String | Search by category label or identifier
}

begin
  # Reads all Categories
  result = api_instance.finance_categories_get(category_level, type, statuses, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceCategoryApi->finance_categories_get: #{e}"
end
```

#### Using the finance_categories_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceCategoriesGet200Response>, Integer, Hash)> finance_categories_get_with_http_info(category_level, type, statuses, opts)

```ruby
begin
  # Reads all Categories
  data, status_code, headers = api_instance.finance_categories_get_with_http_info(category_level, type, statuses, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceCategoriesGet200Response>
rescue F::ApiError => e
  puts "Error when calling FinanceCategoryApi->finance_categories_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **category_level** | **String** | Filter by category level |  |
| **type** | **String** | Filter by category type |  |
| **statuses** | [**Array&lt;String&gt;**](String.md) | Filter by category status |  |
| **ids** | [**Array&lt;String&gt;**](String.md) | Search categories by ID | [optional] |
| **company_ids** | [**Array&lt;String&gt;**](String.md) | Search categories by company IDs | [optional] |
| **parent_category_ids** | [**Array&lt;String&gt;**](String.md) | Search subcategories by parent category ID | [optional] |
| **search** | **String** | Search by category label or identifier | [optional] |

### Return type

[**FinanceCategoriesGet200Response**](FinanceCategoriesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_categories_id_get

> <FinanceCategory> finance_categories_id_get(id)

Reads a single Category

Fetch expense categories and subcategories for the company

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

api_instance = F::FinanceCategoryApi.new
id = '1' # String | Search categories by ID

begin
  # Reads a single Category
  result = api_instance.finance_categories_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceCategoryApi->finance_categories_id_get: #{e}"
end
```

#### Using the finance_categories_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceCategory>, Integer, Hash)> finance_categories_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Category
  data, status_code, headers = api_instance.finance_categories_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceCategory>
rescue F::ApiError => e
  puts "Error when calling FinanceCategoryApi->finance_categories_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Search categories by ID |  |

### Return type

[**FinanceCategory**](FinanceCategory.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

