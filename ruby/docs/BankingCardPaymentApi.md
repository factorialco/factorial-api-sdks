# F::BankingCardPaymentApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**banking_card_payments_get**](BankingCardPaymentApi.md#banking_card_payments_get) | **GET** /api/2026-07-01/resources/banking/card_payments | Reads all Card payments |
| [**banking_card_payments_id_get**](BankingCardPaymentApi.md#banking_card_payments_id_get) | **GET** /api/2026-07-01/resources/banking/card_payments/{id} | Reads a single Card payment |


## banking_card_payments_get

> <BankingCardPaymentsGet200Response> banking_card_payments_get(opts)

Reads all Card payments

Reads all Card payments

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

api_instance = F::BankingCardPaymentApi.new
opts = {
  ids: ['inner_example'], # Array<String> | An array of card payment IDs to filter by.
  account_ids: ['inner_example'], # Array<String> | An array of banking accounts ID to filter
  status: 'pending', # String | The status of the card payment.
  from: '2021-01-01', # String | Date from which the card payment was created in factorial.
  to: '2025-01-01' # String | Date until which the card payment was created in factorial.
}

begin
  # Reads all Card payments
  result = api_instance.banking_card_payments_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling BankingCardPaymentApi->banking_card_payments_get: #{e}"
end
```

#### Using the banking_card_payments_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BankingCardPaymentsGet200Response>, Integer, Hash)> banking_card_payments_get_with_http_info(opts)

```ruby
begin
  # Reads all Card payments
  data, status_code, headers = api_instance.banking_card_payments_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BankingCardPaymentsGet200Response>
rescue F::ApiError => e
  puts "Error when calling BankingCardPaymentApi->banking_card_payments_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | An array of card payment IDs to filter by. | [optional] |
| **account_ids** | [**Array&lt;String&gt;**](String.md) | An array of banking accounts ID to filter | [optional] |
| **status** | **String** | The status of the card payment. | [optional] |
| **from** | **String** | Date from which the card payment was created in factorial. | [optional] |
| **to** | **String** | Date until which the card payment was created in factorial. | [optional] |

### Return type

[**BankingCardPaymentsGet200Response**](BankingCardPaymentsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## banking_card_payments_id_get

> <BankingCardPayment> banking_card_payments_id_get(id)

Reads a single Card payment

Reads a single Card payment

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

api_instance = F::BankingCardPaymentApi.new
id = '135' # String | An array of card payment IDs to filter by.

begin
  # Reads a single Card payment
  result = api_instance.banking_card_payments_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling BankingCardPaymentApi->banking_card_payments_id_get: #{e}"
end
```

#### Using the banking_card_payments_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BankingCardPayment>, Integer, Hash)> banking_card_payments_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Card payment
  data, status_code, headers = api_instance.banking_card_payments_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BankingCardPayment>
rescue F::ApiError => e
  puts "Error when calling BankingCardPaymentApi->banking_card_payments_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | An array of card payment IDs to filter by. |  |

### Return type

[**BankingCardPayment**](BankingCardPayment.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

