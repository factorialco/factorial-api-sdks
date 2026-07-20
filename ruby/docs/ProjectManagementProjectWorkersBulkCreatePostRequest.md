# F::ProjectManagementProjectWorkersBulkCreatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | **String** | The id of the project to assign the given employees. |  |
| **employee_ids** | **Array&lt;String&gt;** | The id of the employee to be assigned to the projects. |  |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementProjectWorkersBulkCreatePostRequest.new(
  project_id: 314159,
  employee_ids: [&quot;21&quot;,&quot;22&quot;]
)
```

