# F::PostsGroupsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the group. |  |
| **title** | **String** | title of the group. | [optional] |
| **description** | **String** | description of the group. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PostsGroupsIdPutRequest.new(
  id: 1,
  title: Company announcements,
  description: The place to find all company announcements.
)
```

