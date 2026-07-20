# F::PayrollEmployeesIdentifier

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | payroll employee identifier |  |
| **employee_id** | **String** | identifier of the employee |  |
| **social_security_number** | **String** | social security number of the employee | [optional] |
| **tax_id** | **String** | tax id of the employee | [optional] |
| **country** | **String** | country code of the employee pt | it | de |  |

## Example

```ruby
require 'factorial_api'

instance = F::PayrollEmployeesIdentifier.new(
  id: 1,
  employee_id: 1,
  social_security_number: 123456788,
  tax_id: 123456789,
  country: it
)
```

