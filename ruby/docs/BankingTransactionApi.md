# F::BankingTransactionApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**banking_transactions_get**](BankingTransactionApi.md#banking_transactions_get) | **GET** /api/2026-07-01/resources/banking/transactions | Reads all Transactions |
| [**banking_transactions_id_get**](BankingTransactionApi.md#banking_transactions_id_get) | **GET** /api/2026-07-01/resources/banking/transactions/{id} | Reads a single Transaction |


## banking_transactions_get

> <BankingTransactionsGet200Response> banking_transactions_get(opts)

Reads all Transactions

Reads all Transactions

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

api_instance = F::BankingTransactionApi.new
opts = {
  ids: ['inner_example'], # Array<String> | An array of transaction IDs to filter by.
  bank_account_ids: ['inner_example'], # Array<String> | An array of Factorial Banking Bank Account IDs to filter by.
  card_payment_ids: ['inner_example'], # Array<String> | An array of Factorial Card Payment IDs to filter by.
  from: '2021-01-01', # String | Date from which the transactions should be fetched.
  to: '2025-01-01', # String | Date until which the transactions should be fetched.
  updated_from: '2021-01-01' # String | Filter transactions updated from a specific date.
}

begin
  # Reads all Transactions
  result = api_instance.banking_transactions_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling BankingTransactionApi->banking_transactions_get: #{e}"
end
```

#### Using the banking_transactions_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BankingTransactionsGet200Response>, Integer, Hash)> banking_transactions_get_with_http_info(opts)

```ruby
begin
  # Reads all Transactions
  data, status_code, headers = api_instance.banking_transactions_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BankingTransactionsGet200Response>
rescue F::ApiError => e
  puts "Error when calling BankingTransactionApi->banking_transactions_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | An array of transaction IDs to filter by. | [optional] |
| **bank_account_ids** | [**Array&lt;String&gt;**](String.md) | An array of Factorial Banking Bank Account IDs to filter by. | [optional] |
| **card_payment_ids** | [**Array&lt;String&gt;**](String.md) | An array of Factorial Card Payment IDs to filter by. | [optional] |
| **from** | **String** | Date from which the transactions should be fetched. | [optional] |
| **to** | **String** | Date until which the transactions should be fetched. | [optional] |
| **updated_from** | **String** | Filter transactions updated from a specific date. | [optional] |

### Return type

[**BankingTransactionsGet200Response**](BankingTransactionsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## banking_transactions_id_get

> <BankingTransaction> banking_transactions_id_get(id)

Reads a single Transaction

Reads a single Transaction

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

api_instance = F::BankingTransactionApi.new
id = '135' # String | An array of transaction IDs to filter by.

begin
  # Reads a single Transaction
  result = api_instance.banking_transactions_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling BankingTransactionApi->banking_transactions_id_get: #{e}"
end
```

#### Using the banking_transactions_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BankingTransaction>, Integer, Hash)> banking_transactions_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Transaction
  data, status_code, headers = api_instance.banking_transactions_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BankingTransaction>
rescue F::ApiError => e
  puts "Error when calling BankingTransactionApi->banking_transactions_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | An array of transaction IDs to filter by. |  |

### Return type

[**BankingTransaction**](BankingTransaction.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

