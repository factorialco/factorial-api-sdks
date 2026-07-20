# F::TimeoffAllowanceIncidence

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier of the allowance incidence |  |
| **employee_id** | **String** | Employee id of the affected employee |  |
| **description** | **String** | Optional comment regarding the incidence | [optional] |
| **days_in_cents** | **Integer** | How many units * 100 does the incidence add/substract. Can be positive or negative. Example is one unit |  |
| **timeoff_allowance_id** | **String** | To what allowance does the incidence affect. It will dictate if its days or hours |  |
| **effective_on** | **String** | When does the incidence take effect; this is for time off cycles calculations. |  |
| **target_balance** | **String** | Whether the incidence affects the Accrued or the Available counter. | [optional] |
| **created_at** | **Integer** | Unix timestamp when the DB record was created |  |
| **updated_at** | **Integer** | Unix timestamp when the DB record was last updated |  |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffAllowanceIncidence.new(
  id: 1,
  employee_id: 1,
  description: Added because working on a holiday,
  days_in_cents: 100,
  timeoff_allowance_id: 2,
  effective_on: 2024-01-02,
  target_balance: accrued,
  created_at: 1723623354,
  updated_at: 1723623354
)
```

