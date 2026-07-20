# F::ExpensesMileageApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**expenses_mileages_get**](ExpensesMileageApi.md#expenses_mileages_get) | **GET** /api/2026-07-01/resources/expenses/mileages | Reads all Mileages |
| [**expenses_mileages_id_get**](ExpensesMileageApi.md#expenses_mileages_id_get) | **GET** /api/2026-07-01/resources/expenses/mileages/{id} | Reads a single Mileage |


## expenses_mileages_get

> <ExpensesMileagesGet200Response> expenses_mileages_get(include_manual_drafts, include_attachments, opts)

Reads all Mileages

Reads all Mileages

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

api_instance = F::ExpensesMileageApi.new
include_manual_drafts = true # Boolean | 
include_attachments = true # Boolean | 
opts = {
  ids: ['inner_example'], # Array<String> | 
  expenses_expensable_ids: ['inner_example'], # Array<String> | 
  employee_ids: ['inner_example'], # Array<String> | 
  external_authorization_ids: ['inner_example'], # Array<String> | 
  card_ids: ['inner_example'], # Array<String> | 
  card_payment_ids: ['inner_example'], # Array<String> | 
  from: 'from_example', # String | 
  to: 'to_example', # String | 
  dispute_ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Mileages
  result = api_instance.expenses_mileages_get(include_manual_drafts, include_attachments, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ExpensesMileageApi->expenses_mileages_get: #{e}"
end
```

#### Using the expenses_mileages_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ExpensesMileagesGet200Response>, Integer, Hash)> expenses_mileages_get_with_http_info(include_manual_drafts, include_attachments, opts)

```ruby
begin
  # Reads all Mileages
  data, status_code, headers = api_instance.expenses_mileages_get_with_http_info(include_manual_drafts, include_attachments, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ExpensesMileagesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ExpensesMileageApi->expenses_mileages_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include_manual_drafts** | **Boolean** |  |  |
| **include_attachments** | **Boolean** |  |  |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **expenses_expensable_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **external_authorization_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **card_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **card_payment_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **from** | **String** |  | [optional] |
| **to** | **String** |  | [optional] |
| **dispute_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**ExpensesMileagesGet200Response**](ExpensesMileagesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expenses_mileages_id_get

> <ExpensesMileage> expenses_mileages_id_get(id)

Reads a single Mileage

Reads a single Mileage

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

api_instance = F::ExpensesMileageApi.new
id = '1' # String | 

begin
  # Reads a single Mileage
  result = api_instance.expenses_mileages_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ExpensesMileageApi->expenses_mileages_id_get: #{e}"
end
```

#### Using the expenses_mileages_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ExpensesMileage>, Integer, Hash)> expenses_mileages_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Mileage
  data, status_code, headers = api_instance.expenses_mileages_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ExpensesMileage>
rescue F::ApiError => e
  puts "Error when calling ExpensesMileageApi->expenses_mileages_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**ExpensesMileage**](ExpensesMileage.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

