# F::ProjectManagementProjectTasksBulkDuplicatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | **String** | Project id where the tasks will be duplicated | [optional] |
| **subproject_id** | **String** | Subproject id where the tasks will be duplicated | [optional] |
| **ids** | **Array&lt;String&gt;** | Task ids to be duplicated |  |
| **exclude_assignees** | **Boolean** | Set this to true if you want to exclude assignees from the duplicated tasks | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementProjectTasksBulkDuplicatePostRequest.new(
  project_id: 1,
  subproject_id: 1,
  ids: [&quot;1&quot;,&quot;2&quot;,&quot;3&quot;],
  exclude_assignees: true
)
```

