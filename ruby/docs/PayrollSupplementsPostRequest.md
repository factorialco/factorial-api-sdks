# F::PayrollSupplementsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **amount_in_cents** | **Integer** | Supplement amount in cents |  |
| **employee_id** | **String** | The employee id of the suplement |  |
| **effective_on** | **String** | Supplement effective on date following the format YYYY-MM-DD |  |
| **contracts_taxonomy_id** | **String** | Supplement contract taxonomy id |  |
| **contracts_compensation_id** | **String** | Supplement contract compensation id | [optional] |
| **payroll_policy_period_id** | **String** | Supplement payroll policy period id |  |
| **unit** | **String** | Supplement unit | [optional] |
| **worked_days** | **Integer** | Supplement worked days | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PayrollSupplementsPostRequest.new(
  amount_in_cents: 50000,
  employee_id: 1,
  effective_on: 2024-01-01,
  contracts_taxonomy_id: 2,
  contracts_compensation_id: 1,
  payroll_policy_period_id: 1,
  unit: money,
  worked_days: 5
)
```

