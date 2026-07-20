# F::TimeoffPolicyAssignmentsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **timeoff_policy_id** | **String** | The time off policy id |  |
| **employee_id** | **String** | The employee id |  |
| **effective_at** | **String** | The effective date of the policy assignment |  |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffPolicyAssignmentsPostRequest.new(
  timeoff_policy_id: 1,
  employee_id: 1,
  effective_at: 2024-01-01
)
```

