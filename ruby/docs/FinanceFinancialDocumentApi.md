# F::FinanceFinancialDocumentApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**finance_financial_documents_get**](FinanceFinancialDocumentApi.md#finance_financial_documents_get) | **GET** /api/2026-07-01/resources/finance/financial_documents | Reads all Financial documents |
| [**finance_financial_documents_id_get**](FinanceFinancialDocumentApi.md#finance_financial_documents_id_get) | **GET** /api/2026-07-01/resources/finance/financial_documents/{id} | Reads a single Financial document |


## finance_financial_documents_get

> <FinanceFinancialDocumentsGet200Response> finance_financial_documents_get(opts)

Reads all Financial documents

Fetch one or all financial documents for the company.

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

api_instance = F::FinanceFinancialDocumentApi.new
opts = {
  company_id: '1', # String | Search financial documents by company_id
  ids: ['inner_example'], # Array<String> | Search financial documents by ID
  vendor_id: '33', # String | Search financial documents by vendor_id
  currency: 'USD', # String | Search financial documents by currency
  statuses: ['inner_example'], # Array<String> | Search financial documents by status
  legal_entity_ids: ['inner_example'], # Array<String> | Search financial documents by legal_entity_id
  document_types: ['inner_example'], # Array<String> | Search financial documents by document_type
  updated_from: '2020-01-01' # String | Filter financial documents updated from a specific date
}

begin
  # Reads all Financial documents
  result = api_instance.finance_financial_documents_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceFinancialDocumentApi->finance_financial_documents_get: #{e}"
end
```

#### Using the finance_financial_documents_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceFinancialDocumentsGet200Response>, Integer, Hash)> finance_financial_documents_get_with_http_info(opts)

```ruby
begin
  # Reads all Financial documents
  data, status_code, headers = api_instance.finance_financial_documents_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceFinancialDocumentsGet200Response>
rescue F::ApiError => e
  puts "Error when calling FinanceFinancialDocumentApi->finance_financial_documents_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **company_id** | **String** | Search financial documents by company_id | [optional] |
| **ids** | [**Array&lt;String&gt;**](String.md) | Search financial documents by ID | [optional] |
| **vendor_id** | **String** | Search financial documents by vendor_id | [optional] |
| **currency** | **String** | Search financial documents by currency | [optional] |
| **statuses** | [**Array&lt;String&gt;**](String.md) | Search financial documents by status | [optional] |
| **legal_entity_ids** | [**Array&lt;String&gt;**](String.md) | Search financial documents by legal_entity_id | [optional] |
| **document_types** | [**Array&lt;String&gt;**](String.md) | Search financial documents by document_type | [optional] |
| **updated_from** | **String** | Filter financial documents updated from a specific date | [optional] |

### Return type

[**FinanceFinancialDocumentsGet200Response**](FinanceFinancialDocumentsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_financial_documents_id_get

> <FinanceFinancialDocument> finance_financial_documents_id_get(id)

Reads a single Financial document

Fetch one or all financial documents for the company.

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

api_instance = F::FinanceFinancialDocumentApi.new
id = '135' # String | Search financial documents by ID

begin
  # Reads a single Financial document
  result = api_instance.finance_financial_documents_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceFinancialDocumentApi->finance_financial_documents_id_get: #{e}"
end
```

#### Using the finance_financial_documents_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceFinancialDocument>, Integer, Hash)> finance_financial_documents_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Financial document
  data, status_code, headers = api_instance.finance_financial_documents_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceFinancialDocument>
rescue F::ApiError => e
  puts "Error when calling FinanceFinancialDocumentApi->finance_financial_documents_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Search financial documents by ID |  |

### Return type

[**FinanceFinancialDocument**](FinanceFinancialDocument.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

