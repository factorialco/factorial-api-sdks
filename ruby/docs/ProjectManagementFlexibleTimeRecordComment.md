# F::ProjectManagementFlexibleTimeRecordComment

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The unique identifier of the flexible time record comment. |  |
| **content** | **String** | The text content of the comment. |  |
| **flexible_time_record_id** | **String** | The ID of the flexible time record this comment belongs to. |  |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementFlexibleTimeRecordComment.new(
  id: 1,
  content: Worked on backend integration.,
  flexible_time_record_id: 42
)
```

