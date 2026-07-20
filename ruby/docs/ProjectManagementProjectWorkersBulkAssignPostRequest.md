# F::ProjectManagementProjectWorkersBulkAssignPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | **String** | **DEPRECATED** in favor of &#x60;project_ids&#x60;. Please use &#x60;project_ids&#x60; instead | [optional] |
| **project_ids** | **Array&lt;String&gt;** | Set of project_ids to assign to the employees specified in the next param. | [optional] |
| **employee_ids** | **Array&lt;String&gt;** | Set of a employee_ids that must be **assigned** after execution. |  |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementProjectWorkersBulkAssignPostRequest.new(
  project_id: 314159,
  project_ids: [&quot;33&quot;,&quot;34&quot;],
  employee_ids: [&quot;21&quot;,&quot;22&quot;,&quot;23&quot;]
)
```

