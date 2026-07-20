# F::TasksTasksPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | name of the task. |  |
| **content** | **String** | description of the task | [optional] |
| **due_on** | **String** | expiration date of the task. | [optional] |
| **assignee_ids** | **Array&lt;String&gt;** | Employees assigned to the task, assignee_id references to access_id. | [optional] |
| **status** | **String** | status of the task (todo | in_progress | done | discarded). |  |

## Example

```ruby
require 'factorial_api'

instance = F::TasksTasksPostRequest.new(
  name: My task,
  content: Complete your performance review before Friday,
  due_on: 2024-06-06,
  assignee_ids: [&quot;1&quot;,&quot;2&quot;,&quot;3&quot;],
  status: todo
)
```

