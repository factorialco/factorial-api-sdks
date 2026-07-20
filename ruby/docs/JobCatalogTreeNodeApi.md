# F::JobCatalogTreeNodeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**job_catalog_tree_nodes_get**](JobCatalogTreeNodeApi.md#job_catalog_tree_nodes_get) | **GET** /api/2026-07-01/resources/job_catalog/tree_nodes | Reads all Tree nodes |


## job_catalog_tree_nodes_get

> <JobCatalogTreeNodesGet200Response> job_catalog_tree_nodes_get(node_type, opts)

Reads all Tree nodes

Fetch Job Catalog Tree Node. For now only admins can see all the nodes' information, regular users won't have access to the nodes' information. In general there are four node types level, function, role and family.

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

api_instance = F::JobCatalogTreeNodeApi.new
node_type = 'jobcatalog_treeroot' # String | Node type scope for the query. Required with IDs, ancestor filters, or name search. Accepted values: jobcatalog_treelevel, jobcatalog_treefunction, jobcatalog_treerole, jobcatalog_treefamily.
opts = {
  uuids: ['inner_example'], # Array<String> | List of Job Catalog node UUIDs to fetch. Must reference nodes of a single type.
  ancestor_uuids: ['inner_example'], # Array<String> | Return nodes that descend from any of these ancestor UUIDs (single node type only).
  include_full_path: true # Boolean | When true, includes each node's ordered ancestor path up to the root.
}

begin
  # Reads all Tree nodes
  result = api_instance.job_catalog_tree_nodes_get(node_type, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling JobCatalogTreeNodeApi->job_catalog_tree_nodes_get: #{e}"
end
```

#### Using the job_catalog_tree_nodes_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<JobCatalogTreeNodesGet200Response>, Integer, Hash)> job_catalog_tree_nodes_get_with_http_info(node_type, opts)

```ruby
begin
  # Reads all Tree nodes
  data, status_code, headers = api_instance.job_catalog_tree_nodes_get_with_http_info(node_type, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <JobCatalogTreeNodesGet200Response>
rescue F::ApiError => e
  puts "Error when calling JobCatalogTreeNodeApi->job_catalog_tree_nodes_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **node_type** | **String** | Node type scope for the query. Required with IDs, ancestor filters, or name search. Accepted values: jobcatalog_treelevel, jobcatalog_treefunction, jobcatalog_treerole, jobcatalog_treefamily. |  |
| **uuids** | [**Array&lt;String&gt;**](String.md) | List of Job Catalog node UUIDs to fetch. Must reference nodes of a single type. | [optional] |
| **ancestor_uuids** | [**Array&lt;String&gt;**](String.md) | Return nodes that descend from any of these ancestor UUIDs (single node type only). | [optional] |
| **include_full_path** | **Boolean** | When true, includes each node&#39;s ordered ancestor path up to the root. | [optional] |

### Return type

[**JobCatalogTreeNodesGet200Response**](JobCatalogTreeNodesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

