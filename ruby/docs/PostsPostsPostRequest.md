# F::PostsPostsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **title** | **String** | title of the post |  |
| **description** | **String** | description of the post |  |
| **post_group_id** | **String** | group identifier of the post, references to posts/groups endpoint |  |
| **allow_comments_and_reactions** | **Boolean** | allow comments and reactions on the post | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PostsPostsPostRequest.new(
  title: Are you ready for the perfomance review?,
  description: As you know today we start the performance review process.,
  post_group_id: 1,
  allow_comments_and_reactions: true
)
```

