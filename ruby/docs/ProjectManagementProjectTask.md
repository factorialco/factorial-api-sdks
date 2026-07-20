# F::ProjectManagementProjectTask

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **project_id** | **String** | The ID of the project linked to the project task |  |
| **subproject_id** | **String** | The ID of the subproject linked to the project task | [optional] |
| **task_id** | **String** | The ID of the task linked to the project task |  |
| **follow_up** | **Boolean** | If true, status changes related to the project will notify the author |  |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementProjectTask.new(
  id: 789,
  project_id: 123,
  subproject_id: 456,
  task_id: 780,
  follow_up: true
)
```

