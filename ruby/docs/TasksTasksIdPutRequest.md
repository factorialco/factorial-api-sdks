# F::TasksTasksIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | id of a task. |  |
| **name** | **String** | name of  task. | [optional] |
| **content** | **String** | description of the task. | [optional] |
| **due_on** | **String** | expiration date of the task. | [optional] |
| **assignee_ids** | **Array&lt;String&gt;** | employees assigned to the task, assignee_id references to access_id. | [optional] |
| **status** | **String** | status of the task (todo | in_progress | done | discarded). | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TasksTasksIdPutRequest.new(
  id: 1,
  name: My task,
  content: Complete your performance review before Friday,
  due_on: 2024-06-06,
  assignee_ids: [&quot;1&quot;],
  status: todo
)
```

