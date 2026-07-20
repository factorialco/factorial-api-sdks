# F::PayrollSupplementsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The supplement id |  |
| **employee_id** | **String** | The employee id of the supplement | [optional] |
| **contracts_compensation_id** | **String** | The supplement contract compensation id | [optional] |
| **contracts_taxonomy_id** | **String** | The supplement contract taxonomy id | [optional] |
| **amount_in_cents** | **Integer** | Supplement amount in cents | [optional] |
| **effective_on** | **String** | Supplement effective on date following the format YYYY-MM-DD | [optional] |
| **unit** | **String** | Supplement unit | [optional] |
| **payroll_policy_period_id** | **String** | Supplement payroll policy period  id | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PayrollSupplementsIdPutRequest.new(
  id: 1,
  employee_id: 1,
  contracts_compensation_id: 1,
  contracts_taxonomy_id: 2,
  amount_in_cents: 50000,
  effective_on: 2024-01-01,
  unit: money,
  payroll_policy_period_id: 1
)
```

