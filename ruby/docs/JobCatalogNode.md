# F::JobCatalogNode

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **type** | **String** | Type of the node. |  |
| **uuid** | **String** | UUIDs of the node. |  |
| **ancestor_uuid** | **String** | UUID of the parent node. | [optional] |
| **name** | **String** | Name of the node. | [optional] |
| **description** | **String** | Description of the node in the Job Catalog. | [optional] |
| **created_at** | **String** | Creation date of the node. |  |
| **updated_at** | **String** | Update date of the node. |  |
| **full_path_to_root** | **Array&lt;Object&gt;** | Array with the list of nodes tha compose full path from the current node to the root node. | [optional] |
| **job_catalog_title** | **String** | Full title that represents the job position. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::JobCatalogNode.new(
  type: jobcatalog_treelevel,
  uuid: jobcatalog_treelevel-331,
  ancestor_uuid: jobcatalog_treefamily-018,
  name: Engineering,
  description: Engineering Manager family,
  created_at: 2024-01-15,
  updated_at: 2024-01-15,
  full_path_to_root: [jobcatalog_treelevel-331, jobcatalog_treerole-456, jobcatalog_treefunction-123, jobcatalog_treefamily-018, jobcatalog_treeroot-1],
  job_catalog_title: Engineering Manager, Senior
)
```

