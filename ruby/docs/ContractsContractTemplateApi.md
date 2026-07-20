# F::ContractsContractTemplateApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**contracts_contract_templates_get**](ContractsContractTemplateApi.md#contracts_contract_templates_get) | **GET** /api/2026-07-01/resources/contracts/contract_templates | Reads all Contract templates |
| [**contracts_contract_templates_id_get**](ContractsContractTemplateApi.md#contracts_contract_templates_id_get) | **GET** /api/2026-07-01/resources/contracts/contract_templates/{id} | Reads a single Contract template |


## contracts_contract_templates_get

> <ContractsContractTemplatesGet200Response> contracts_contract_templates_get(opts)

Reads all Contract templates

Read Contract Template

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

api_instance = F::ContractsContractTemplateApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Filter by contract template IDs
  company_id: '1', # String | Filter by company ID
  contract_version_type: 'es' # String | Filter by contract version type (e.g., es for Spain, fr for France)
}

begin
  # Reads all Contract templates
  result = api_instance.contracts_contract_templates_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsContractTemplateApi->contracts_contract_templates_get: #{e}"
end
```

#### Using the contracts_contract_templates_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsContractTemplatesGet200Response>, Integer, Hash)> contracts_contract_templates_get_with_http_info(opts)

```ruby
begin
  # Reads all Contract templates
  data, status_code, headers = api_instance.contracts_contract_templates_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsContractTemplatesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ContractsContractTemplateApi->contracts_contract_templates_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter by contract template IDs | [optional] |
| **company_id** | **String** | Filter by company ID | [optional] |
| **contract_version_type** | **String** | Filter by contract version type (e.g., es for Spain, fr for France) | [optional] |

### Return type

[**ContractsContractTemplatesGet200Response**](ContractsContractTemplatesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contracts_contract_templates_id_get

> <ContractsContractTemplate> contracts_contract_templates_id_get(id)

Reads a single Contract template

Read Contract Template

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

api_instance = F::ContractsContractTemplateApi.new
id = '1' # String | Filter by contract template IDs

begin
  # Reads a single Contract template
  result = api_instance.contracts_contract_templates_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsContractTemplateApi->contracts_contract_templates_id_get: #{e}"
end
```

#### Using the contracts_contract_templates_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsContractTemplate>, Integer, Hash)> contracts_contract_templates_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Contract template
  data, status_code, headers = api_instance.contracts_contract_templates_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsContractTemplate>
rescue F::ApiError => e
  puts "Error when calling ContractsContractTemplateApi->contracts_contract_templates_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter by contract template IDs |  |

### Return type

[**ContractsContractTemplate**](ContractsContractTemplate.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

