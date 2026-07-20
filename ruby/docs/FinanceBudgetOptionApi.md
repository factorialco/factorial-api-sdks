# F::FinanceBudgetOptionApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**finance_budget_options_get**](FinanceBudgetOptionApi.md#finance_budget_options_get) | **GET** /api/2026-07-01/resources/finance/budget_options | Reads all Budget options |
| [**finance_budget_options_id_get**](FinanceBudgetOptionApi.md#finance_budget_options_id_get) | **GET** /api/2026-07-01/resources/finance/budget_options/{id} | Reads a single Budget option |


## finance_budget_options_get

> <FinanceBudgetOptionsGet200Response> finance_budget_options_get(include_inactive, include_archived, opts)

Reads all Budget options

Fetch budget options for the company

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

api_instance = F::FinanceBudgetOptionApi.new
include_inactive = false # Boolean | Include inactive budget options
include_archived = false # Boolean | Include archived budget options
opts = {
  ids: ['inner_example'], # Array<String> | Search budget options by ID
  employee_ids: ['inner_example'], # Array<String> | Search budget options by employee IDs
  effective_at: '2021-01-01T00:00:00Z' # String | Filter budget options effective at this date
}

begin
  # Reads all Budget options
  result = api_instance.finance_budget_options_get(include_inactive, include_archived, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceBudgetOptionApi->finance_budget_options_get: #{e}"
end
```

#### Using the finance_budget_options_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceBudgetOptionsGet200Response>, Integer, Hash)> finance_budget_options_get_with_http_info(include_inactive, include_archived, opts)

```ruby
begin
  # Reads all Budget options
  data, status_code, headers = api_instance.finance_budget_options_get_with_http_info(include_inactive, include_archived, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceBudgetOptionsGet200Response>
rescue F::ApiError => e
  puts "Error when calling FinanceBudgetOptionApi->finance_budget_options_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include_inactive** | **Boolean** | Include inactive budget options |  |
| **include_archived** | **Boolean** | Include archived budget options |  |
| **ids** | [**Array&lt;String&gt;**](String.md) | Search budget options by ID | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Search budget options by employee IDs | [optional] |
| **effective_at** | **String** | Filter budget options effective at this date | [optional] |

### Return type

[**FinanceBudgetOptionsGet200Response**](FinanceBudgetOptionsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_budget_options_id_get

> <FinanceBudgetOption> finance_budget_options_id_get(id)

Reads a single Budget option

Fetch budget options for the company

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

api_instance = F::FinanceBudgetOptionApi.new
id = '1' # String | Search budget options by ID

begin
  # Reads a single Budget option
  result = api_instance.finance_budget_options_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceBudgetOptionApi->finance_budget_options_id_get: #{e}"
end
```

#### Using the finance_budget_options_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceBudgetOption>, Integer, Hash)> finance_budget_options_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Budget option
  data, status_code, headers = api_instance.finance_budget_options_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceBudgetOption>
rescue F::ApiError => e
  puts "Error when calling FinanceBudgetOptionApi->finance_budget_options_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Search budget options by ID |  |

### Return type

[**FinanceBudgetOption**](FinanceBudgetOption.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

