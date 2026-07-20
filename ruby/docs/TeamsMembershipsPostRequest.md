# F::TeamsMembershipsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **team_id** | **String** | Team id. |  |
| **employee_id** | **String** | Employee id. |  |
| **lead** | **Boolean** | Makes the employee a lead of the team. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TeamsMembershipsPostRequest.new(
  team_id: 1,
  employee_id: 5,
  lead: true
)
```

