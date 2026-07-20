# F::ProjectManagementProjectWorkersPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | **String** | The id of the project to assign the employee project worker. |  |
| **employee_id** | **String** | The id of the employee to be assigned to the project. |  |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementProjectWorkersPostRequest.new(
  project_id: 314159,
  employee_id: 21
)
```

