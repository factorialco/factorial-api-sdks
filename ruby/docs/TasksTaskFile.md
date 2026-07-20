# F::TasksTaskFile

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the file. |  |
| **task_id** | **String** | identifier of the task. |  |
| **filename** | **String** | name of the file. |  |
| **content_type** | **String** | content type of the file. | [optional] |
| **path** | **String** | path of the file, for downloading the file you need to concat api_url/path. |  |
| **created_at** | **String** | creation date of the file. |  |

## Example

```ruby
require 'factorial_api'

instance = F::TasksTaskFile.new(
  id: 1,
  task_id: 1,
  filename: expenses.png,
  content_type: image/png,
  path: /tasks/tasks_files/405,
  created_at: 2024-10-06
)
```

