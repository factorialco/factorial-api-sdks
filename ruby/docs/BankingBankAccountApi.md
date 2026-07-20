# F::BankingBankAccountApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**banking_bank_accounts_create_manual_post**](BankingBankAccountApi.md#banking_bank_accounts_create_manual_post) | **POST** /api/2026-07-01/resources/banking/bank_accounts/create_manual | Create manuals a Bank account |
| [**banking_bank_accounts_get**](BankingBankAccountApi.md#banking_bank_accounts_get) | **GET** /api/2026-07-01/resources/banking/bank_accounts | Reads all Bank accounts |
| [**banking_bank_accounts_id_get**](BankingBankAccountApi.md#banking_bank_accounts_id_get) | **GET** /api/2026-07-01/resources/banking/bank_accounts/{id} | Reads a single Bank account |


## banking_bank_accounts_create_manual_post

> <BankingBankAccount> banking_bank_accounts_create_manual_post(opts)

Create manuals a Bank account

Create a manual bank account.

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

api_instance = F::BankingBankAccountApi.new
opts = {
  banking_bank_accounts_create_manual_post_request: F::BankingBankAccountsCreateManualPostRequest.new({legal_entity_id: '11', currency: 'EUR', account_number: 'ES28209582976036485969781', account_number_type: 'iban'}) # BankingBankAccountsCreateManualPostRequest | 
}

begin
  # Create manuals a Bank account
  result = api_instance.banking_bank_accounts_create_manual_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling BankingBankAccountApi->banking_bank_accounts_create_manual_post: #{e}"
end
```

#### Using the banking_bank_accounts_create_manual_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BankingBankAccount>, Integer, Hash)> banking_bank_accounts_create_manual_post_with_http_info(opts)

```ruby
begin
  # Create manuals a Bank account
  data, status_code, headers = api_instance.banking_bank_accounts_create_manual_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BankingBankAccount>
rescue F::ApiError => e
  puts "Error when calling BankingBankAccountApi->banking_bank_accounts_create_manual_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **banking_bank_accounts_create_manual_post_request** | [**BankingBankAccountsCreateManualPostRequest**](BankingBankAccountsCreateManualPostRequest.md) |  | [optional] |

### Return type

[**BankingBankAccount**](BankingBankAccount.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## banking_bank_accounts_get

> <BankingBankAccountsGet200Response> banking_bank_accounts_get(opts)

Reads all Bank accounts

Fetch one or all bank accounts for the company.

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

api_instance = F::BankingBankAccountApi.new
opts = {
  ids: ['inner_example'], # Array<String> | An array of bank account IDs to filter by.
  currency: 'EUR', # String | A currency to filter by.
  legal_entity_ids: ['inner_example'], # Array<String> | An array of legal entity IDs to filter by.
  updated_from: '2021-01-01' # String | Filter by accounts updated from a specific date.
}

begin
  # Reads all Bank accounts
  result = api_instance.banking_bank_accounts_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling BankingBankAccountApi->banking_bank_accounts_get: #{e}"
end
```

#### Using the banking_bank_accounts_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BankingBankAccountsGet200Response>, Integer, Hash)> banking_bank_accounts_get_with_http_info(opts)

```ruby
begin
  # Reads all Bank accounts
  data, status_code, headers = api_instance.banking_bank_accounts_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BankingBankAccountsGet200Response>
rescue F::ApiError => e
  puts "Error when calling BankingBankAccountApi->banking_bank_accounts_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | An array of bank account IDs to filter by. | [optional] |
| **currency** | **String** | A currency to filter by. | [optional] |
| **legal_entity_ids** | [**Array&lt;String&gt;**](String.md) | An array of legal entity IDs to filter by. | [optional] |
| **updated_from** | **String** | Filter by accounts updated from a specific date. | [optional] |

### Return type

[**BankingBankAccountsGet200Response**](BankingBankAccountsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## banking_bank_accounts_id_get

> <BankingBankAccount> banking_bank_accounts_id_get(id)

Reads a single Bank account

Fetch one or all bank accounts for the company.

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

api_instance = F::BankingBankAccountApi.new
id = '1' # String | An array of bank account IDs to filter by.

begin
  # Reads a single Bank account
  result = api_instance.banking_bank_accounts_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling BankingBankAccountApi->banking_bank_accounts_id_get: #{e}"
end
```

#### Using the banking_bank_accounts_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BankingBankAccount>, Integer, Hash)> banking_bank_accounts_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Bank account
  data, status_code, headers = api_instance.banking_bank_accounts_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BankingBankAccount>
rescue F::ApiError => e
  puts "Error when calling BankingBankAccountApi->banking_bank_accounts_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | An array of bank account IDs to filter by. |  |

### Return type

[**BankingBankAccount**](BankingBankAccount.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

