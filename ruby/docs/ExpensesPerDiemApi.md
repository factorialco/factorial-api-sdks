# F::ExpensesPerDiemApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**expenses_per_diems_get**](ExpensesPerDiemApi.md#expenses_per_diems_get) | **GET** /api/2026-07-01/resources/expenses/per_diems | Reads all Per diems |
| [**expenses_per_diems_id_get**](ExpensesPerDiemApi.md#expenses_per_diems_id_get) | **GET** /api/2026-07-01/resources/expenses/per_diems/{id} | Reads a single Per diem |


## expenses_per_diems_get

> <ExpensesPerDiemsGet200Response> expenses_per_diems_get(opts)

Reads all Per diems

Reads all Per diems

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

api_instance = F::ExpensesPerDiemApi.new
opts = {
  ids: ['inner_example'], # Array<String> | The IDs of the per diem to read.
  expenses_expensable_ids: ['inner_example'], # Array<String> | The IDs of the expensables to read per diems for.
  exclude_drafts: false # Boolean | Whether to exclude drafts from the results.
}

begin
  # Reads all Per diems
  result = api_instance.expenses_per_diems_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ExpensesPerDiemApi->expenses_per_diems_get: #{e}"
end
```

#### Using the expenses_per_diems_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ExpensesPerDiemsGet200Response>, Integer, Hash)> expenses_per_diems_get_with_http_info(opts)

```ruby
begin
  # Reads all Per diems
  data, status_code, headers = api_instance.expenses_per_diems_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ExpensesPerDiemsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ExpensesPerDiemApi->expenses_per_diems_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | The IDs of the per diem to read. | [optional] |
| **expenses_expensable_ids** | [**Array&lt;String&gt;**](String.md) | The IDs of the expensables to read per diems for. | [optional] |
| **exclude_drafts** | **Boolean** | Whether to exclude drafts from the results. | [optional] |

### Return type

[**ExpensesPerDiemsGet200Response**](ExpensesPerDiemsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expenses_per_diems_id_get

> <ExpensesPerDiem> expenses_per_diems_id_get(id)

Reads a single Per diem

Reads a single Per diem

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

api_instance = F::ExpensesPerDiemApi.new
id = '1' # String | The IDs of the per diem to read.

begin
  # Reads a single Per diem
  result = api_instance.expenses_per_diems_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ExpensesPerDiemApi->expenses_per_diems_id_get: #{e}"
end
```

#### Using the expenses_per_diems_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ExpensesPerDiem>, Integer, Hash)> expenses_per_diems_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Per diem
  data, status_code, headers = api_instance.expenses_per_diems_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ExpensesPerDiem>
rescue F::ApiError => e
  puts "Error when calling ExpensesPerDiemApi->expenses_per_diems_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The IDs of the per diem to read. |  |

### Return type

[**ExpensesPerDiem**](ExpensesPerDiem.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

