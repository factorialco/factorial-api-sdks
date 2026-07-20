# F::FinanceLedgerAccountResourceApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**finance_ledger_account_resources_get**](FinanceLedgerAccountResourceApi.md#finance_ledger_account_resources_get) | **GET** /api/2026-07-01/resources/finance/ledger_account_resources | Reads all Ledger account resources |
| [**finance_ledger_account_resources_id_get**](FinanceLedgerAccountResourceApi.md#finance_ledger_account_resources_id_get) | **GET** /api/2026-07-01/resources/finance/ledger_account_resources/{id} | Reads a single Ledger account resource |
| [**finance_ledger_account_resources_upsert_post**](FinanceLedgerAccountResourceApi.md#finance_ledger_account_resources_upsert_post) | **POST** /api/2026-07-01/resources/finance/ledger_account_resources/upsert | Upserts a Ledger account resource |


## finance_ledger_account_resources_get

> <FinanceLedgerAccountResourcesGet200Response> finance_ledger_account_resources_get(opts)

Reads all Ledger account resources

Fetch one or all ledger account resource for the company.

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

api_instance = F::FinanceLedgerAccountResourceApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Search ledger account resources by ID
  resource_ids: ['inner_example'], # Array<String> | Filter ledger account resources by resource ID
  resource_type: 'bankaccount', # String | Filter ledger account resources by resource type
  legal_entity_ids: ['inner_example'], # Array<String> | Filter ledger account resources by legal entity ID
  updated_from: '2021-01-01', # String | Filter ledger account resources by updated at
  finance_account_ids: ['inner_example'] # Array<String> | Filter ledger account resources by finance account ID
}

begin
  # Reads all Ledger account resources
  result = api_instance.finance_ledger_account_resources_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceLedgerAccountResourceApi->finance_ledger_account_resources_get: #{e}"
end
```

#### Using the finance_ledger_account_resources_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceLedgerAccountResourcesGet200Response>, Integer, Hash)> finance_ledger_account_resources_get_with_http_info(opts)

```ruby
begin
  # Reads all Ledger account resources
  data, status_code, headers = api_instance.finance_ledger_account_resources_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceLedgerAccountResourcesGet200Response>
rescue F::ApiError => e
  puts "Error when calling FinanceLedgerAccountResourceApi->finance_ledger_account_resources_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Search ledger account resources by ID | [optional] |
| **resource_ids** | [**Array&lt;String&gt;**](String.md) | Filter ledger account resources by resource ID | [optional] |
| **resource_type** | **String** | Filter ledger account resources by resource type | [optional] |
| **legal_entity_ids** | [**Array&lt;String&gt;**](String.md) | Filter ledger account resources by legal entity ID | [optional] |
| **updated_from** | **String** | Filter ledger account resources by updated at | [optional] |
| **finance_account_ids** | [**Array&lt;String&gt;**](String.md) | Filter ledger account resources by finance account ID | [optional] |

### Return type

[**FinanceLedgerAccountResourcesGet200Response**](FinanceLedgerAccountResourcesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_ledger_account_resources_id_get

> <FinanceLedgerAccountResource> finance_ledger_account_resources_id_get(id)

Reads a single Ledger account resource

Fetch one or all ledger account resource for the company.

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

api_instance = F::FinanceLedgerAccountResourceApi.new
id = '135' # String | Search ledger account resources by ID

begin
  # Reads a single Ledger account resource
  result = api_instance.finance_ledger_account_resources_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceLedgerAccountResourceApi->finance_ledger_account_resources_id_get: #{e}"
end
```

#### Using the finance_ledger_account_resources_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceLedgerAccountResource>, Integer, Hash)> finance_ledger_account_resources_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Ledger account resource
  data, status_code, headers = api_instance.finance_ledger_account_resources_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceLedgerAccountResource>
rescue F::ApiError => e
  puts "Error when calling FinanceLedgerAccountResourceApi->finance_ledger_account_resources_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Search ledger account resources by ID |  |

### Return type

[**FinanceLedgerAccountResource**](FinanceLedgerAccountResource.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_ledger_account_resources_upsert_post

> <FinanceLedgerAccountResource> finance_ledger_account_resources_upsert_post(opts)

Upserts a Ledger account resource

Create or update a ledger account resource.

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

api_instance = F::FinanceLedgerAccountResourceApi.new
opts = {
  finance_ledger_account_resources_upsert_post_request: F::FinanceLedgerAccountResourcesUpsertPostRequest.new({legal_entity_id: '13', resource_type: 'customcategory'}) # FinanceLedgerAccountResourcesUpsertPostRequest | 
}

begin
  # Upserts a Ledger account resource
  result = api_instance.finance_ledger_account_resources_upsert_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceLedgerAccountResourceApi->finance_ledger_account_resources_upsert_post: #{e}"
end
```

#### Using the finance_ledger_account_resources_upsert_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceLedgerAccountResource>, Integer, Hash)> finance_ledger_account_resources_upsert_post_with_http_info(opts)

```ruby
begin
  # Upserts a Ledger account resource
  data, status_code, headers = api_instance.finance_ledger_account_resources_upsert_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceLedgerAccountResource>
rescue F::ApiError => e
  puts "Error when calling FinanceLedgerAccountResourceApi->finance_ledger_account_resources_upsert_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **finance_ledger_account_resources_upsert_post_request** | [**FinanceLedgerAccountResourcesUpsertPostRequest**](FinanceLedgerAccountResourcesUpsertPostRequest.md) |  | [optional] |

### Return type

[**FinanceLedgerAccountResource**](FinanceLedgerAccountResource.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

