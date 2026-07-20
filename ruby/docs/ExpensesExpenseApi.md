# F::ExpensesExpenseApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**expenses_expenses_get**](ExpensesExpenseApi.md#expenses_expenses_get) | **GET** /api/2026-07-01/resources/expenses/expenses | Reads all Expenses |
| [**expenses_expenses_id_get**](ExpensesExpenseApi.md#expenses_expenses_id_get) | **GET** /api/2026-07-01/resources/expenses/expenses/{id} | Reads a single Expense |


## expenses_expenses_get

> <ExpensesExpensesGet200Response> expenses_expenses_get(include_manual_drafts, include_attachments, opts)

Reads all Expenses

Reads all Expenses

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

api_instance = F::ExpensesExpenseApi.new
include_manual_drafts = true # Boolean | Whether to include manual drafts
include_attachments = true # Boolean | Wether to include the attachments
opts = {
  ids: ['inner_example'], # Array<String> | The ids of the expenses to filter by
  expenses_expensable_ids: ['inner_example'], # Array<String> | The ids of the expensables to filter by
  employee_ids: ['inner_example'], # Array<String> | The ids of the employees to filter by
  external_authorization_ids: ['inner_example'], # Array<String> | The ids of the external authorizations to filter by
  card_ids: ['inner_example'], # Array<String> | The ids of the cards to filter by
  card_payment_ids: ['inner_example'], # Array<String> | The ids of the card payments to filter by
  from: 'from_example', # String | The time from which to filter expenses
  to: 'to_example', # String | The time to which to filter expenses
  dispute_ids: ['inner_example'] # Array<String> | The ids of the disputes to filter by
}

begin
  # Reads all Expenses
  result = api_instance.expenses_expenses_get(include_manual_drafts, include_attachments, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ExpensesExpenseApi->expenses_expenses_get: #{e}"
end
```

#### Using the expenses_expenses_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ExpensesExpensesGet200Response>, Integer, Hash)> expenses_expenses_get_with_http_info(include_manual_drafts, include_attachments, opts)

```ruby
begin
  # Reads all Expenses
  data, status_code, headers = api_instance.expenses_expenses_get_with_http_info(include_manual_drafts, include_attachments, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ExpensesExpensesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ExpensesExpenseApi->expenses_expenses_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include_manual_drafts** | **Boolean** | Whether to include manual drafts |  |
| **include_attachments** | **Boolean** | Wether to include the attachments |  |
| **ids** | [**Array&lt;String&gt;**](String.md) | The ids of the expenses to filter by | [optional] |
| **expenses_expensable_ids** | [**Array&lt;String&gt;**](String.md) | The ids of the expensables to filter by | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | The ids of the employees to filter by | [optional] |
| **external_authorization_ids** | [**Array&lt;String&gt;**](String.md) | The ids of the external authorizations to filter by | [optional] |
| **card_ids** | [**Array&lt;String&gt;**](String.md) | The ids of the cards to filter by | [optional] |
| **card_payment_ids** | [**Array&lt;String&gt;**](String.md) | The ids of the card payments to filter by | [optional] |
| **from** | **String** | The time from which to filter expenses | [optional] |
| **to** | **String** | The time to which to filter expenses | [optional] |
| **dispute_ids** | [**Array&lt;String&gt;**](String.md) | The ids of the disputes to filter by | [optional] |

### Return type

[**ExpensesExpensesGet200Response**](ExpensesExpensesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expenses_expenses_id_get

> <ExpensesExpense> expenses_expenses_id_get(id)

Reads a single Expense

Reads a single Expense

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

api_instance = F::ExpensesExpenseApi.new
id = '1' # String | The ids of the expenses to filter by

begin
  # Reads a single Expense
  result = api_instance.expenses_expenses_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ExpensesExpenseApi->expenses_expenses_id_get: #{e}"
end
```

#### Using the expenses_expenses_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ExpensesExpense>, Integer, Hash)> expenses_expenses_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Expense
  data, status_code, headers = api_instance.expenses_expenses_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ExpensesExpense>
rescue F::ApiError => e
  puts "Error when calling ExpensesExpenseApi->expenses_expenses_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The ids of the expenses to filter by |  |

### Return type

[**ExpensesExpense**](ExpensesExpense.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

