# F::ContractsMaterializedTemplateApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**contracts_materialized_templates_get**](ContractsMaterializedTemplateApi.md#contracts_materialized_templates_get) | **GET** /api/2026-07-01/resources/contracts/materialized_templates | Reads all Materialized templates |


## contracts_materialized_templates_get

> <ContractsMaterializedTemplatesGet200Response> contracts_materialized_templates_get(company_id, template_type, include_archived, opts)

Reads all Materialized templates

Reads all Materialized templates

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

api_instance = F::ContractsMaterializedTemplateApi.new
company_id = '1' # String | The identifier of the company whose templates you want to retrieve. All results are scoped to this company. 
template_type = 'company' # String | The template level to retrieve. Use company to get the organization-wide base field definitions. Use country to get country-specific overrides merged with company defaults. Use legal_entity to get the final effective template for a specific legal entity, which is the most common use case when building contract creation or editing flows. 
include_archived = false # Boolean | When true, archived options are included in the response alongside active ones. Defaults to false, which returns only active options. Set to true when you need to display contracts that reference options that have since been archived. 
opts = {
  legal_entity_ids: ['inner_example'], # Array<String> | Optional list of legal entity identifiers to filter results. When provided alongside template_type: legal_entity, returns only the materialized templates for those legal entities. Ignored for company and country template types. 
  countries: ['inner_example'], # Array<String> | Optional list of ISO 3166-1 alpha-2 country codes to filter results. When provided alongside template_type: country, returns only templates for those countries. When used with template_type: legal_entity, narrows results to legal entities operating in those countries. 
  field_ids: ['inner_example'] # Array<String> | Optional list of field identifiers to filter the template fields returned. When provided, each materialized template will only include fields whose field_id matches one of the values in this list. Use this to retrieve a specific subset of fields (e.g. [\"contract_type\"]) without fetching the full template structure. 
}

begin
  # Reads all Materialized templates
  result = api_instance.contracts_materialized_templates_get(company_id, template_type, include_archived, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ContractsMaterializedTemplateApi->contracts_materialized_templates_get: #{e}"
end
```

#### Using the contracts_materialized_templates_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ContractsMaterializedTemplatesGet200Response>, Integer, Hash)> contracts_materialized_templates_get_with_http_info(company_id, template_type, include_archived, opts)

```ruby
begin
  # Reads all Materialized templates
  data, status_code, headers = api_instance.contracts_materialized_templates_get_with_http_info(company_id, template_type, include_archived, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ContractsMaterializedTemplatesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ContractsMaterializedTemplateApi->contracts_materialized_templates_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **company_id** | **String** | The identifier of the company whose templates you want to retrieve. All results are scoped to this company.  |  |
| **template_type** | **String** | The template level to retrieve. Use company to get the organization-wide base field definitions. Use country to get country-specific overrides merged with company defaults. Use legal_entity to get the final effective template for a specific legal entity, which is the most common use case when building contract creation or editing flows.  |  |
| **include_archived** | **Boolean** | When true, archived options are included in the response alongside active ones. Defaults to false, which returns only active options. Set to true when you need to display contracts that reference options that have since been archived.  |  |
| **legal_entity_ids** | [**Array&lt;String&gt;**](String.md) | Optional list of legal entity identifiers to filter results. When provided alongside template_type: legal_entity, returns only the materialized templates for those legal entities. Ignored for company and country template types.  | [optional] |
| **countries** | [**Array&lt;String&gt;**](String.md) | Optional list of ISO 3166-1 alpha-2 country codes to filter results. When provided alongside template_type: country, returns only templates for those countries. When used with template_type: legal_entity, narrows results to legal entities operating in those countries.  | [optional] |
| **field_ids** | [**Array&lt;String&gt;**](String.md) | Optional list of field identifiers to filter the template fields returned. When provided, each materialized template will only include fields whose field_id matches one of the values in this list. Use this to retrieve a specific subset of fields (e.g. [\&quot;contract_type\&quot;]) without fetching the full template structure.  | [optional] |

### Return type

[**ContractsMaterializedTemplatesGet200Response**](ContractsMaterializedTemplatesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

