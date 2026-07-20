# F::FinanceJournalLineApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**finance_journal_lines_get**](FinanceJournalLineApi.md#finance_journal_lines_get) | **GET** /api/2026-07-01/resources/finance/journal_lines | Reads all Journal lines |
| [**finance_journal_lines_id_get**](FinanceJournalLineApi.md#finance_journal_lines_id_get) | **GET** /api/2026-07-01/resources/finance/journal_lines/{id} | Reads a single Journal line |


## finance_journal_lines_get

> <FinanceJournalLinesGet200Response> finance_journal_lines_get(opts)

Reads all Journal lines

Reads all Journal lines

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

api_instance = F::FinanceJournalLineApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Filter by specific JournalLine IDs
  journal_entry_ids: ['inner_example'], # Array<String> | Filter by specific JournalEntry IDs
  account_ids: ['inner_example'], # Array<String> | Filter by specific Account IDs
  journal_entry_types: ['inner_example'], # Array<String> | Filter by JournalEntry types, accepted values: bank, bill, invoice, credit_note, merged_ledger_account, reconciliation, tax, receipt, payroll_result, external
  reconciliation_status: 'pending', # String | The reconciliation status of the journal line
  description: 'description_example', # String | 
  updated_from: '2025-01-01' # String | Start date for filtering journal line records based on their last update.
}

begin
  # Reads all Journal lines
  result = api_instance.finance_journal_lines_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceJournalLineApi->finance_journal_lines_get: #{e}"
end
```

#### Using the finance_journal_lines_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceJournalLinesGet200Response>, Integer, Hash)> finance_journal_lines_get_with_http_info(opts)

```ruby
begin
  # Reads all Journal lines
  data, status_code, headers = api_instance.finance_journal_lines_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceJournalLinesGet200Response>
rescue F::ApiError => e
  puts "Error when calling FinanceJournalLineApi->finance_journal_lines_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter by specific JournalLine IDs | [optional] |
| **journal_entry_ids** | [**Array&lt;String&gt;**](String.md) | Filter by specific JournalEntry IDs | [optional] |
| **account_ids** | [**Array&lt;String&gt;**](String.md) | Filter by specific Account IDs | [optional] |
| **journal_entry_types** | [**Array&lt;String&gt;**](String.md) | Filter by JournalEntry types, accepted values: bank, bill, invoice, credit_note, merged_ledger_account, reconciliation, tax, receipt, payroll_result, external | [optional] |
| **reconciliation_status** | **String** | The reconciliation status of the journal line | [optional] |
| **description** | **String** |  | [optional] |
| **updated_from** | **String** | Start date for filtering journal line records based on their last update. | [optional] |

### Return type

[**FinanceJournalLinesGet200Response**](FinanceJournalLinesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_journal_lines_id_get

> <FinanceJournalLine> finance_journal_lines_id_get(id)

Reads a single Journal line

Reads a single Journal line

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

api_instance = F::FinanceJournalLineApi.new
id = '1234' # String | Filter by specific JournalLine IDs

begin
  # Reads a single Journal line
  result = api_instance.finance_journal_lines_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceJournalLineApi->finance_journal_lines_id_get: #{e}"
end
```

#### Using the finance_journal_lines_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceJournalLine>, Integer, Hash)> finance_journal_lines_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Journal line
  data, status_code, headers = api_instance.finance_journal_lines_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceJournalLine>
rescue F::ApiError => e
  puts "Error when calling FinanceJournalLineApi->finance_journal_lines_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter by specific JournalLine IDs |  |

### Return type

[**FinanceJournalLine**](FinanceJournalLine.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

