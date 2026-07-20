# F::ContractsCompensationsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **contract_version_id** | **String** |  |  |
| **contracts_taxonomy_id** | **String** |  |  |
| **description** | **String** |  | [optional] |
| **compensation_type** | **String** |  | [optional] |
| **amount** | **Integer** |  | [optional] |
| **unit** | **String** |  | [optional] |
| **sync_with_supplements** | **Boolean** |  | [optional] |
| **payroll_policy_id** | **String** |  | [optional] |
| **recurrence_count** | **Integer** |  | [optional] |
| **starts_on** | **String** |  | [optional] |
| **recurrence** | **String** |  | [optional] |
| **first_payment_on** | **String** |  | [optional] |
| **calculation** | **String** |  | [optional] |
| **time_condition** | **String** |  | [optional] |
| **minimum_amount_of_hours** | **Integer** |  | [optional] |
| **minimum_amount_of_hours_in_cents** | **Integer** |  | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsCompensationsPostRequest.new(
  contract_version_id: null,
  contracts_taxonomy_id: null,
  description: null,
  compensation_type: null,
  amount: null,
  unit: null,
  sync_with_supplements: null,
  payroll_policy_id: null,
  recurrence_count: null,
  starts_on: null,
  recurrence: null,
  first_payment_on: null,
  calculation: null,
  time_condition: null,
  minimum_amount_of_hours: null,
  minimum_amount_of_hours_in_cents: null
)
```

