# F::TasksTask

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the task |  |
| **name** | **String** | Name of the task |  |
| **company_id** | **String** | Company identifier of the author of the task |  |
| **content** | **String** | Content of the task | [optional] |
| **due_on** | **String** | Due on date of the task | [optional] |
| **assignee_ids** | **Array&lt;String&gt;** | Employees assigned to the task, assignee_id references to access_id |  |
| **author_employee_id** | **String** | Employee id of the author of the task | [optional] |
| **completed_at** | **String** | Completed at date of the task | [optional] |
| **completed_by_id** | **String** | Completed by identifier | [optional] |
| **created_at** | **String** |  |  |
| **updated_at** | **String** | Updated at date of the task |  |
| **status** | **String** | Status of the task | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TasksTask.new(
  id: 1,
  name: My task,
  company_id: 1,
  content: Complete your performance review before Friday,
  due_on: 2024-06-06,
  assignee_ids: [1],
  author_employee_id: 1,
  completed_at: 2024-01-01T00:00:00Z,
  completed_by_id: 1,
  created_at: 2024-01-20T18:05:45.000Z,
  updated_at: 2024-01-20T18:05:45.000Z,
  status: todo
)
```

