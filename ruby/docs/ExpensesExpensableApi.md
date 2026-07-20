# F::ExpensesExpensableApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**expenses_expensables_bulk_set_to_paid_post**](ExpensesExpensableApi.md#expenses_expensables_bulk_set_to_paid_post) | **POST** /api/2026-07-01/resources/expenses/expensables/bulk_set_to_paid | Bulk set to paids an Expensable |
| [**expenses_expensables_get**](ExpensesExpensableApi.md#expenses_expensables_get) | **GET** /api/2026-07-01/resources/expenses/expensables | Reads all Expensables |
| [**expenses_expensables_id_get**](ExpensesExpensableApi.md#expenses_expensables_id_get) | **GET** /api/2026-07-01/resources/expenses/expensables/{id} | Reads a single Expensable |
| [**expenses_expensables_update_reimbursable_amount_post**](ExpensesExpensableApi.md#expenses_expensables_update_reimbursable_amount_post) | **POST** /api/2026-07-01/resources/expenses/expensables/update_reimbursable_amount | Update reimbursable amount on an expensable |


## expenses_expensables_bulk_set_to_paid_post

> <Array<ExpensesExpensable>> expenses_expensables_bulk_set_to_paid_post(opts)

Bulk set to paids an Expensable

Bulk set to paids an Expensable

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

api_instance = F::ExpensesExpensableApi.new
opts = {
  expenses_expensables_bulk_set_to_paid_post_request: F::ExpensesExpensablesBulkSetToPaidPostRequest.new({ids: ["1"]}) # ExpensesExpensablesBulkSetToPaidPostRequest | 
}

begin
  # Bulk set to paids an Expensable
  result = api_instance.expenses_expensables_bulk_set_to_paid_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ExpensesExpensableApi->expenses_expensables_bulk_set_to_paid_post: #{e}"
end
```

#### Using the expenses_expensables_bulk_set_to_paid_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<ExpensesExpensable>>, Integer, Hash)> expenses_expensables_bulk_set_to_paid_post_with_http_info(opts)

```ruby
begin
  # Bulk set to paids an Expensable
  data, status_code, headers = api_instance.expenses_expensables_bulk_set_to_paid_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<ExpensesExpensable>>
rescue F::ApiError => e
  puts "Error when calling ExpensesExpensableApi->expenses_expensables_bulk_set_to_paid_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **expenses_expensables_bulk_set_to_paid_post_request** | [**ExpensesExpensablesBulkSetToPaidPostRequest**](ExpensesExpensablesBulkSetToPaidPostRequest.md) |  | [optional] |

### Return type

[**Array&lt;ExpensesExpensable&gt;**](ExpensesExpensable.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## expenses_expensables_get

> <ExpensesExpensablesGet200Response> expenses_expensables_get(include_grouped, include_attachments, include_manual_drafts, opts)

Reads all Expensables

Reads all Expensables

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

api_instance = F::ExpensesExpensableApi.new
include_grouped = true # Boolean | 
include_attachments = true # Boolean | 
include_manual_drafts = true # Boolean | 
opts = {
  ids: ['inner_example'], # Array<String> | 
  company_id: 'company_id_example', # String | 
  group_ids: ['inner_example'], # Array<String> | 
  by_resources: [3.56], # Array<Object> | 
  employee_ids: ['inner_example'], # Array<String> | 
  reporter_ids: ['inner_example'], # Array<String> | 
  status: ['inner_example'], # Array<String> | 
  creation_type: ['inner_example'], # Array<String> | 
  from: 'from_example', # String | 
  to: 'to_example', # String | 
  search: 'search_example' # String | 
}

begin
  # Reads all Expensables
  result = api_instance.expenses_expensables_get(include_grouped, include_attachments, include_manual_drafts, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ExpensesExpensableApi->expenses_expensables_get: #{e}"
end
```

#### Using the expenses_expensables_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ExpensesExpensablesGet200Response>, Integer, Hash)> expenses_expensables_get_with_http_info(include_grouped, include_attachments, include_manual_drafts, opts)

```ruby
begin
  # Reads all Expensables
  data, status_code, headers = api_instance.expenses_expensables_get_with_http_info(include_grouped, include_attachments, include_manual_drafts, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ExpensesExpensablesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ExpensesExpensableApi->expenses_expensables_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include_grouped** | **Boolean** |  |  |
| **include_attachments** | **Boolean** |  |  |
| **include_manual_drafts** | **Boolean** |  |  |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **company_id** | **String** |  | [optional] |
| **group_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **by_resources** | [**Array&lt;Object&gt;**](Object.md) |  | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **reporter_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **status** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **creation_type** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **from** | **String** |  | [optional] |
| **to** | **String** |  | [optional] |
| **search** | **String** |  | [optional] |

### Return type

[**ExpensesExpensablesGet200Response**](ExpensesExpensablesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expenses_expensables_id_get

> <ExpensesExpensable> expenses_expensables_id_get(id)

Reads a single Expensable

Reads a single Expensable

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

api_instance = F::ExpensesExpensableApi.new
id = '1' # String | 

begin
  # Reads a single Expensable
  result = api_instance.expenses_expensables_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ExpensesExpensableApi->expenses_expensables_id_get: #{e}"
end
```

#### Using the expenses_expensables_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ExpensesExpensable>, Integer, Hash)> expenses_expensables_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Expensable
  data, status_code, headers = api_instance.expenses_expensables_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ExpensesExpensable>
rescue F::ApiError => e
  puts "Error when calling ExpensesExpensableApi->expenses_expensables_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**ExpensesExpensable**](ExpensesExpensable.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expenses_expensables_update_reimbursable_amount_post

> <ExpensesExpensable> expenses_expensables_update_reimbursable_amount_post(opts)

Update reimbursable amount on an expensable

Update the reimbursable amount on an expensable. Only expense-type expensables with reimbursable payment are supported.

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

api_instance = F::ExpensesExpensableApi.new
opts = {
  expenses_expensables_update_reimbursable_amount_post_request: F::ExpensesExpensablesUpdateReimbursableAmountPostRequest.new({id: '1', reimbursable_amount: 2000}) # ExpensesExpensablesUpdateReimbursableAmountPostRequest | 
}

begin
  # Update reimbursable amount on an expensable
  result = api_instance.expenses_expensables_update_reimbursable_amount_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ExpensesExpensableApi->expenses_expensables_update_reimbursable_amount_post: #{e}"
end
```

#### Using the expenses_expensables_update_reimbursable_amount_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ExpensesExpensable>, Integer, Hash)> expenses_expensables_update_reimbursable_amount_post_with_http_info(opts)

```ruby
begin
  # Update reimbursable amount on an expensable
  data, status_code, headers = api_instance.expenses_expensables_update_reimbursable_amount_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ExpensesExpensable>
rescue F::ApiError => e
  puts "Error when calling ExpensesExpensableApi->expenses_expensables_update_reimbursable_amount_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **expenses_expensables_update_reimbursable_amount_post_request** | [**ExpensesExpensablesUpdateReimbursableAmountPostRequest**](ExpensesExpensablesUpdateReimbursableAmountPostRequest.md) |  | [optional] |

### Return type

[**ExpensesExpensable**](ExpensesExpensable.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

