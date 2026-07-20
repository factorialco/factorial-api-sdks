# F::FinanceAccountApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**finance_accounts_get**](FinanceAccountApi.md#finance_accounts_get) | **GET** /api/2026-07-01/resources/finance/accounts | Reads all Accounts |
| [**finance_accounts_id_get**](FinanceAccountApi.md#finance_accounts_id_get) | **GET** /api/2026-07-01/resources/finance/accounts/{id} | Reads a single Account |
| [**finance_accounts_id_put**](FinanceAccountApi.md#finance_accounts_id_put) | **PUT** /api/2026-07-01/resources/finance/accounts/{id} | Updates an Account |
| [**finance_accounts_post**](FinanceAccountApi.md#finance_accounts_post) | **POST** /api/2026-07-01/resources/finance/accounts | Creates an Account |


## finance_accounts_get

> <FinanceAccountsGet200Response> finance_accounts_get(opts)

Reads all Accounts

Fetch one or all ledger accounts for the company legal_entities.

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

api_instance = F::FinanceAccountApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Search ledger accounts by ID
  legal_entity_ids: ['inner_example'], # Array<String> | Search ledger accounts by legal_entity_id
  types: ['inner_example'], # Array<String> | Search ledger accounts by type
  number: '1000', # String | Search ledger accounts by number
  updated_from: '2021-01-01' # String | Start date for filtering ledger accounts based on their last update.
}

begin
  # Reads all Accounts
  result = api_instance.finance_accounts_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceAccountApi->finance_accounts_get: #{e}"
end
```

#### Using the finance_accounts_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceAccountsGet200Response>, Integer, Hash)> finance_accounts_get_with_http_info(opts)

```ruby
begin
  # Reads all Accounts
  data, status_code, headers = api_instance.finance_accounts_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceAccountsGet200Response>
rescue F::ApiError => e
  puts "Error when calling FinanceAccountApi->finance_accounts_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Search ledger accounts by ID | [optional] |
| **legal_entity_ids** | [**Array&lt;String&gt;**](String.md) | Search ledger accounts by legal_entity_id | [optional] |
| **types** | [**Array&lt;String&gt;**](String.md) | Search ledger accounts by type | [optional] |
| **number** | **String** | Search ledger accounts by number | [optional] |
| **updated_from** | **String** | Start date for filtering ledger accounts based on their last update. | [optional] |

### Return type

[**FinanceAccountsGet200Response**](FinanceAccountsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_accounts_id_get

> <FinanceAccount> finance_accounts_id_get(id)

Reads a single Account

Fetch one or all ledger accounts for the company legal_entities.

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

api_instance = F::FinanceAccountApi.new
id = '1' # String | Search ledger accounts by ID

begin
  # Reads a single Account
  result = api_instance.finance_accounts_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceAccountApi->finance_accounts_id_get: #{e}"
end
```

#### Using the finance_accounts_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceAccount>, Integer, Hash)> finance_accounts_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Account
  data, status_code, headers = api_instance.finance_accounts_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceAccount>
rescue F::ApiError => e
  puts "Error when calling FinanceAccountApi->finance_accounts_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Search ledger accounts by ID |  |

### Return type

[**FinanceAccount**](FinanceAccount.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_accounts_id_put

> <FinanceAccount> finance_accounts_id_put(id, opts)

Updates an Account

Update a ledger account.

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

api_instance = F::FinanceAccountApi.new
id = '1' # String | Unique identifier in factorial for the ledger account
opts = {
  finance_accounts_id_put_request: F::FinanceAccountsIdPutRequest.new({id: '1'}) # FinanceAccountsIdPutRequest | 
}

begin
  # Updates an Account
  result = api_instance.finance_accounts_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceAccountApi->finance_accounts_id_put: #{e}"
end
```

#### Using the finance_accounts_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceAccount>, Integer, Hash)> finance_accounts_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates an Account
  data, status_code, headers = api_instance.finance_accounts_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceAccount>
rescue F::ApiError => e
  puts "Error when calling FinanceAccountApi->finance_accounts_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier in factorial for the ledger account |  |
| **finance_accounts_id_put_request** | [**FinanceAccountsIdPutRequest**](FinanceAccountsIdPutRequest.md) |  | [optional] |

### Return type

[**FinanceAccount**](FinanceAccount.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## finance_accounts_post

> <FinanceAccount> finance_accounts_post(opts)

Creates an Account

Create a ledger account for the company legal_entity. To avoid duplicates use the external_id field to set the ID of the ledger account in the external system.

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

api_instance = F::FinanceAccountApi.new
opts = {
  finance_accounts_post_request: F::FinanceAccountsPostRequest.new({number: '1000', type: 'equity', currency: 'EUR', legal_entity_id: '11'}) # FinanceAccountsPostRequest | 
}

begin
  # Creates an Account
  result = api_instance.finance_accounts_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceAccountApi->finance_accounts_post: #{e}"
end
```

#### Using the finance_accounts_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceAccount>, Integer, Hash)> finance_accounts_post_with_http_info(opts)

```ruby
begin
  # Creates an Account
  data, status_code, headers = api_instance.finance_accounts_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceAccount>
rescue F::ApiError => e
  puts "Error when calling FinanceAccountApi->finance_accounts_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **finance_accounts_post_request** | [**FinanceAccountsPostRequest**](FinanceAccountsPostRequest.md) |  | [optional] |

### Return type

[**FinanceAccount**](FinanceAccount.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

