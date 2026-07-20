# F::ContractsCompensation

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **contract_version_id** | **String** |  |  |
| **contracts_taxonomy_id** | **String** |  |  |
| **description** | **String** |  | [optional] |
| **compensation_type** | **String** | Required field. You can only use the following options: fixed, undefined, up_to, per_worked_day, per_worked_hour | [optional] |
| **amount** | **Integer** | Value paid on each recurrence, stored in the smallest currency unit (for example cents). Required unless the compensation type is &#x60;undefined&#x60; | [optional] |
| **unit** | **String** | In which unit compensation is paid |  |
| **sync_with_supplements** | **Boolean** |  | [optional] |
| **payroll_policy_id** | **String** |  | [optional] |
| **recurrence_count** | **Integer** | How much time will pass between payments. If recurrence is empty, assume months. For example, 12 here means compensation is paid yearly | [optional] |
| **starts_on** | **String** |  | [optional] |
| **recurrence** | **String** | Frequency (monthly, yearly, one_time) to determine how often the employee is paid. Could be empty, use &#x60;recurrence_count&#x60; in that case | [optional] |
| **first_payment_on** | **String** | Date of the first payout; differs from &#x60;starts_on&#x60; when payroll scheduling or accrual rules delay payment | [optional] |
| **calculation** | **String** | Human-readable hint about the payroll formula used (for example \&quot;current period\&quot; or \&quot;average of last 3 months\&quot;) | [optional] |
| **currency** | **String** |  | [optional] |
| **time_condition** | **String** |  | [optional] |
| **minimum_amount_of_hours** | **Integer** |  | [optional] |
| **minimum_amount_of_hours_in_cents** | **Integer** | Compensation expected minimum amount of hours in cents | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsCompensation.new(
  id: null,
  contract_version_id: null,
  contracts_taxonomy_id: null,
  description: Yearly variable,
  compensation_type: fixed,
  amount: null,
  unit: Money,
  sync_with_supplements: null,
  payroll_policy_id: null,
  recurrence_count: null,
  starts_on: null,
  recurrence: null,
  first_payment_on: null,
  calculation: null,
  currency: null,
  time_condition: null,
  minimum_amount_of_hours: null,
  minimum_amount_of_hours_in_cents: null
)
```

