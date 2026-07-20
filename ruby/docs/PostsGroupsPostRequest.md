# F::PostsGroupsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **title** | **String** | title of the group. |  |
| **description** | **String** | description of the group. |  |
| **company_id** | **String** | Identifier of the company, this value can be retrieved from core/me endpoint |  |

## Example

```ruby
require 'factorial_api'

instance = F::PostsGroupsPostRequest.new(
  title: Company announcements,
  description: The place to find all company announcements.,
  company_id: 1
)
```

