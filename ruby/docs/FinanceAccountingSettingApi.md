# F::FinanceAccountingSettingApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**finance_accounting_settings_get**](FinanceAccountingSettingApi.md#finance_accounting_settings_get) | **GET** /api/2026-07-01/resources/finance/accounting_settings | Reads all Accounting settings |
| [**finance_accounting_settings_id_get**](FinanceAccountingSettingApi.md#finance_accounting_settings_id_get) | **GET** /api/2026-07-01/resources/finance/accounting_settings/{id} | Reads a single Accounting setting |
| [**finance_accounting_settings_upsert_post**](FinanceAccountingSettingApi.md#finance_accounting_settings_upsert_post) | **POST** /api/2026-07-01/resources/finance/accounting_settings/upsert | Upserts an Accounting setting |


## finance_accounting_settings_get

> <FinanceAccountingSettingsGet200Response> finance_accounting_settings_get(opts)

Reads all Accounting settings

Reads all Accounting settings

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

api_instance = F::FinanceAccountingSettingApi.new
opts = {
  ids: ['inner_example'], # Array<String> | List of AccountingSetting IDs to filter.
  legal_entity_ids: ['inner_example'], # Array<String> | Filter by an array of legal entity IDs.
  updated_from: '2025-01-01' # String | Start date for filtering accounting settings records based on their last update.
}

begin
  # Reads all Accounting settings
  result = api_instance.finance_accounting_settings_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceAccountingSettingApi->finance_accounting_settings_get: #{e}"
end
```

#### Using the finance_accounting_settings_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceAccountingSettingsGet200Response>, Integer, Hash)> finance_accounting_settings_get_with_http_info(opts)

```ruby
begin
  # Reads all Accounting settings
  data, status_code, headers = api_instance.finance_accounting_settings_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceAccountingSettingsGet200Response>
rescue F::ApiError => e
  puts "Error when calling FinanceAccountingSettingApi->finance_accounting_settings_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | List of AccountingSetting IDs to filter. | [optional] |
| **legal_entity_ids** | [**Array&lt;String&gt;**](String.md) | Filter by an array of legal entity IDs. | [optional] |
| **updated_from** | **String** | Start date for filtering accounting settings records based on their last update. | [optional] |

### Return type

[**FinanceAccountingSettingsGet200Response**](FinanceAccountingSettingsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_accounting_settings_id_get

> <FinanceAccountingSetting> finance_accounting_settings_id_get(id)

Reads a single Accounting setting

Reads a single Accounting setting

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

api_instance = F::FinanceAccountingSettingApi.new
id = '1234' # String | List of AccountingSetting IDs to filter.

begin
  # Reads a single Accounting setting
  result = api_instance.finance_accounting_settings_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceAccountingSettingApi->finance_accounting_settings_id_get: #{e}"
end
```

#### Using the finance_accounting_settings_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceAccountingSetting>, Integer, Hash)> finance_accounting_settings_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Accounting setting
  data, status_code, headers = api_instance.finance_accounting_settings_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceAccountingSetting>
rescue F::ApiError => e
  puts "Error when calling FinanceAccountingSettingApi->finance_accounting_settings_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | List of AccountingSetting IDs to filter. |  |

### Return type

[**FinanceAccountingSetting**](FinanceAccountingSetting.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_accounting_settings_upsert_post

> <FinanceAccountingSetting> finance_accounting_settings_upsert_post(opts)

Upserts an Accounting setting

Upserts an Accounting setting

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

api_instance = F::FinanceAccountingSettingApi.new
opts = {
  finance_accounting_settings_upsert_post_request: F::FinanceAccountingSettingsUpsertPostRequest.new({legal_entity_id: '101'}) # FinanceAccountingSettingsUpsertPostRequest | 
}

begin
  # Upserts an Accounting setting
  result = api_instance.finance_accounting_settings_upsert_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceAccountingSettingApi->finance_accounting_settings_upsert_post: #{e}"
end
```

#### Using the finance_accounting_settings_upsert_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceAccountingSetting>, Integer, Hash)> finance_accounting_settings_upsert_post_with_http_info(opts)

```ruby
begin
  # Upserts an Accounting setting
  data, status_code, headers = api_instance.finance_accounting_settings_upsert_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceAccountingSetting>
rescue F::ApiError => e
  puts "Error when calling FinanceAccountingSettingApi->finance_accounting_settings_upsert_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **finance_accounting_settings_upsert_post_request** | [**FinanceAccountingSettingsUpsertPostRequest**](FinanceAccountingSettingsUpsertPostRequest.md) |  | [optional] |

### Return type

[**FinanceAccountingSetting**](FinanceAccountingSetting.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

