# F::TimeoffAllowanceIncidencesIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **days_in_cents** | **Integer** | How many units multiplied by 100 do you want to add/substract. Can be positive or negative | [optional] |
| **timeoff_allowance_id** | **String** | Allowance Id | [optional] |
| **description** | **String** | A free text field to add a description to the incidence | [optional] |
| **effective_on** | **String** | When does the incidence take effect. This is related to the allowance cycle. | [optional] |
| **target_balance** | **String** | Which counter does the incidence affect. Can be \&quot;accrued\&quot; or \&quot;available\&quot; | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffAllowanceIncidencesIdPutRequest.new(
  id: null,
  days_in_cents: 100,
  timeoff_allowance_id: 1,
  description: Working on a bank holiday a different day,
  effective_on: 2024-01-05,
  target_balance: accrued
)
```

