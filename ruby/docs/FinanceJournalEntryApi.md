# F::FinanceJournalEntryApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**finance_journal_entries_get**](FinanceJournalEntryApi.md#finance_journal_entries_get) | **GET** /api/2026-07-01/resources/finance/journal_entries | Reads all Journal entries |
| [**finance_journal_entries_id_get**](FinanceJournalEntryApi.md#finance_journal_entries_id_get) | **GET** /api/2026-07-01/resources/finance/journal_entries/{id} | Reads a single Journal entry |
| [**finance_journal_entries_post**](FinanceJournalEntryApi.md#finance_journal_entries_post) | **POST** /api/2026-07-01/resources/finance/journal_entries | Creates a Journal entry |


## finance_journal_entries_get

> <FinanceJournalEntriesGet200Response> finance_journal_entries_get(opts)

Reads all Journal entries

Reads all Journal entries

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

api_instance = F::FinanceJournalEntryApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Filter by JournalEntry IDs
  legal_entity_ids: ['inner_example'], # Array<String> | Filter by Legal Entity IDs
  source_ids: ['inner_example'], # Array<String> | Filter by Source IDs
  source_type: 'bank_transaction', # String | Filter by related source type
  types: ['inner_example'], # Array<String> | Filter by entry type
  status: 'published', # String | Filter by Journal Entry Status
  updated_from: '2025-01-01' # String | Start date for filtering journal entries records based on their last update.
}

begin
  # Reads all Journal entries
  result = api_instance.finance_journal_entries_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceJournalEntryApi->finance_journal_entries_get: #{e}"
end
```

#### Using the finance_journal_entries_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceJournalEntriesGet200Response>, Integer, Hash)> finance_journal_entries_get_with_http_info(opts)

```ruby
begin
  # Reads all Journal entries
  data, status_code, headers = api_instance.finance_journal_entries_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceJournalEntriesGet200Response>
rescue F::ApiError => e
  puts "Error when calling FinanceJournalEntryApi->finance_journal_entries_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter by JournalEntry IDs | [optional] |
| **legal_entity_ids** | [**Array&lt;String&gt;**](String.md) | Filter by Legal Entity IDs | [optional] |
| **source_ids** | [**Array&lt;String&gt;**](String.md) | Filter by Source IDs | [optional] |
| **source_type** | **String** | Filter by related source type | [optional] |
| **types** | [**Array&lt;String&gt;**](String.md) | Filter by entry type | [optional] |
| **status** | **String** | Filter by Journal Entry Status | [optional] |
| **updated_from** | **String** | Start date for filtering journal entries records based on their last update. | [optional] |

### Return type

[**FinanceJournalEntriesGet200Response**](FinanceJournalEntriesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_journal_entries_id_get

> <FinanceJournalEntry> finance_journal_entries_id_get(id)

Reads a single Journal entry

Reads a single Journal entry

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

api_instance = F::FinanceJournalEntryApi.new
id = '4321' # String | Filter by JournalEntry IDs

begin
  # Reads a single Journal entry
  result = api_instance.finance_journal_entries_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceJournalEntryApi->finance_journal_entries_id_get: #{e}"
end
```

#### Using the finance_journal_entries_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceJournalEntry>, Integer, Hash)> finance_journal_entries_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Journal entry
  data, status_code, headers = api_instance.finance_journal_entries_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceJournalEntry>
rescue F::ApiError => e
  puts "Error when calling FinanceJournalEntryApi->finance_journal_entries_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter by JournalEntry IDs |  |

### Return type

[**FinanceJournalEntry**](FinanceJournalEntry.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_journal_entries_post

> <FinanceJournalEntry> finance_journal_entries_post(opts)

Creates a Journal entry

Creates a Journal entry

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

api_instance = F::FinanceJournalEntryApi.new
opts = {
  finance_journal_entries_post_request: F::FinanceJournalEntriesPostRequest.new({legal_entity_id: '1001', lines: [{"account_id": 9876, "debit_amount_cents": 0, "credit_amount_cents": 100, "external_id": "LINE-001"}, {"account_id": 9876, "debit_amount_cents": 100, "credit_amount_cents": 0, "external_id": "LINE-002"}], reference_date: '2025-01-01'}) # FinanceJournalEntriesPostRequest | 
}

begin
  # Creates a Journal entry
  result = api_instance.finance_journal_entries_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceJournalEntryApi->finance_journal_entries_post: #{e}"
end
```

#### Using the finance_journal_entries_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceJournalEntry>, Integer, Hash)> finance_journal_entries_post_with_http_info(opts)

```ruby
begin
  # Creates a Journal entry
  data, status_code, headers = api_instance.finance_journal_entries_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceJournalEntry>
rescue F::ApiError => e
  puts "Error when calling FinanceJournalEntryApi->finance_journal_entries_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **finance_journal_entries_post_request** | [**FinanceJournalEntriesPostRequest**](FinanceJournalEntriesPostRequest.md) |  | [optional] |

### Return type

[**FinanceJournalEntry**](FinanceJournalEntry.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

