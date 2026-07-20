# F::PostsGroup

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the group. |  |
| **title** | **String** | title of the group. |  |
| **description** | **String** | description of the group. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PostsGroup.new(
  id: 1,
  title: Company announcements,
  description: The place to find all company announcements.
)
```

