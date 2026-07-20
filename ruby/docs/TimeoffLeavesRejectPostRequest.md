# F::TimeoffLeavesRejectPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the Leave |  |
| **reason** | **String** | Reason for rejecting the leave | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffLeavesRejectPostRequest.new(
  id: 1,
  reason: Not enough notice
)
```

