# F::TeamsMembership

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Membership ID |  |
| **company_id** | **String** | Company ID of the membership | [optional] |
| **employee_id** | **String** | Employee ID of the membership |  |
| **team_id** | **String** | Team ID of the membership |  |
| **lead** | **Boolean** | Whether the employee is a lead of the team or not |  |

## Example

```ruby
require 'factorial_api'

instance = F::TeamsMembership.new(
  id: 1,
  company_id: 5,
  employee_id: 12,
  team_id: 4,
  lead: true
)
```

