# F::PostsComment

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the comment |  |
| **post_id** | **String** | identifier of the post |  |
| **author_id** | **String** | author identifier refers to the employee access, you can get the employee from the employee endpoint |  |
| **text** | **String** | text of the comment |  |
| **created_at** | **String** | date of the comment |  |

## Example

```ruby
require 'factorial_api'

instance = F::PostsComment.new(
  id: 1,
  post_id: 1,
  author_id: 1,
  text: How is the week going Ana?,
  created_at: 2024-07-17T00:00:00Z
)
```

