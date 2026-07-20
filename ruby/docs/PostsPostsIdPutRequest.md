# F::PostsPostsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the post |  |
| **title** | **String** | title of the post | [optional] |
| **description** | **String** | description of the post | [optional] |
| **post_group_id** | **String** | group identifier of the post, references to posts/groups endpoint | [optional] |
| **allow_comments_and_reactions** | **Boolean** | allow comments and reactions on the post | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PostsPostsIdPutRequest.new(
  id: 1,
  title: Are you ready for the perfomance review?,
  description: As you know today we start the performance review process.,
  post_group_id: 1,
  allow_comments_and_reactions: true
)
```

