# F::TimeoffAllowanceIncidencesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_id** | **String** | Employee Id |  |
| **timeoff_allowance_id** | **String** | Allowance Id |  |
| **days_in_cents** | **Integer** | How many units multiplied by 100 do you want to add/substract. Can be positive or negative |  |
| **description** | **String** | A free text field to add a description to the incidence | [optional] |
| **effective_on** | **String** | When does the incidence take effect. This is related to the allowance cycle. |  |
| **target_balance** | **String** | Which counter does the incidence affect. Can be \&quot;accrued\&quot; or \&quot;available\&quot; |  |
| **_skip_notifications** | **Boolean** | When set to true, it prevents notifications being sent to employee when this incidence is created | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffAllowanceIncidencesPostRequest.new(
  employee_id: 6,
  timeoff_allowance_id: 1,
  days_in_cents: 100,
  description: Working on a bank holiday a different day,
  effective_on: 2024-01-05,
  target_balance: accrued,
  _skip_notifications: null
)
```

