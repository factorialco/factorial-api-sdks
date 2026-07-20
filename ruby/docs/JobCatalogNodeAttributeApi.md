# F::JobCatalogNodeAttributeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**job_catalog_node_attributes_get**](JobCatalogNodeAttributeApi.md#job_catalog_node_attributes_get) | **GET** /api/2026-07-01/resources/job_catalog/node_attributes | Reads all Node attributes |


## job_catalog_node_attributes_get

> <JobCatalogNodeAttributesGet200Response> job_catalog_node_attributes_get(node_uuid, attribute_types)

Reads all Node attributes

Fetch Attributes for a node (Family, Function, role or level) in the Job Catalog Tree

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

api_instance = F::JobCatalogNodeAttributeApi.new
node_uuid = 'jobcatalog_treelevel-331' # String | Preferred identifier of the node to fetch attributes for. Required unless `node_id` + `node_type` are provided.
attribute_types = ['inner_example'] # Array<String> | Restrict the response to attributes of these classes (e.g., competency, salary_range).

begin
  # Reads all Node attributes
  result = api_instance.job_catalog_node_attributes_get(node_uuid, attribute_types)
  p result
rescue F::ApiError => e
  puts "Error when calling JobCatalogNodeAttributeApi->job_catalog_node_attributes_get: #{e}"
end
```

#### Using the job_catalog_node_attributes_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<JobCatalogNodeAttributesGet200Response>, Integer, Hash)> job_catalog_node_attributes_get_with_http_info(node_uuid, attribute_types)

```ruby
begin
  # Reads all Node attributes
  data, status_code, headers = api_instance.job_catalog_node_attributes_get_with_http_info(node_uuid, attribute_types)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <JobCatalogNodeAttributesGet200Response>
rescue F::ApiError => e
  puts "Error when calling JobCatalogNodeAttributeApi->job_catalog_node_attributes_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **node_uuid** | **String** | Preferred identifier of the node to fetch attributes for. Required unless &#x60;node_id&#x60; + &#x60;node_type&#x60; are provided. |  |
| **attribute_types** | [**Array&lt;String&gt;**](String.md) | Restrict the response to attributes of these classes (e.g., competency, salary_range). |  |

### Return type

[**JobCatalogNodeAttributesGet200Response**](JobCatalogNodeAttributesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

