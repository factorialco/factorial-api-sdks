# F::TimeoffPolicyAssignmentsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier of the policy assignment |  |
| **timeoff_policy_id** | **String** | The time off policy id |  |
| **effective_at** | **String** | The effective date of the policy assignment |  |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffPolicyAssignmentsIdPutRequest.new(
  id: 1,
  timeoff_policy_id: 1,
  effective_at: 2024-01-01
)
```

