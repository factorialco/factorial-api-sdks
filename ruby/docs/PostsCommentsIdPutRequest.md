# F::PostsCommentsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the comment |  |
| **post_id** | **String** | identifier of the post |  |
| **text** | **String** | Text of the comment |  |

## Example

```ruby
require 'factorial_api'

instance = F::PostsCommentsIdPutRequest.new(
  id: 1,
  post_id: 1,
  text: How is the week going Ana?
)
```

