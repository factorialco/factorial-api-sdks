# F::ProjectManagementProjectsChangeStatusPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id project. |  |
| **status** | **String** | new status of the projects |  |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementProjectsChangeStatusPostRequest.new(
  id: 314159,
  status: active
)
```

