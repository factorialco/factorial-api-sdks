# F::PostsCommentsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **post_id** | **String** | identifier of the post |  |
| **text** | **String** | Text of the comment |  |

## Example

```ruby
require 'factorial_api'

instance = F::PostsCommentsPostRequest.new(
  post_id: 1,
  text: How is the week going Ana?
)
```

