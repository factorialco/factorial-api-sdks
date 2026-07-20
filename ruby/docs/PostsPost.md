# F::PostsPost

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifiers of the post |  |
| **title** | **String** | title of the post | [optional] |
| **description** | **String** | description of the post | [optional] |
| **allow_comments_and_reactions** | **Boolean** | allow comments and reactions on the post |  |
| **published_at** | **String** | date when the post has been published | [optional] |
| **created_at** | **String** | date when the post has been created |  |
| **updated_at** | **String** | date when the post has been updated |  |
| **visits_count** | **Integer** | number of visits of the post |  |
| **cover_image_url** | **String** | url of the cover image | [optional] |
| **posts_group_id** | **String** | group identifier of the post, references to posts/groups endpoint | [optional] |
| **comments_count** | **Integer** |  |  |

## Example

```ruby
require 'factorial_api'

instance = F::PostsPost.new(
  id: 1,
  title: Are you ready for the perfomance review?,
  description: As you know today we start the performance review process.,
  allow_comments_and_reactions: true,
  published_at: 2024-07-17T00:00:00Z,
  created_at: 2024-07-17T00:00:00Z,
  updated_at: 2024-07-17T00:00:00Z,
  visits_count: 10,
  cover_image_url: https://example.com/image.jpg,
  posts_group_id: 1,
  comments_count: null
)
```

