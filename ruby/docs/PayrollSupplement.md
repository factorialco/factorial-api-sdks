# F::PayrollSupplement

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The identifier of the supplement |  |
| **employee_id** | **String** | The identifier of the employee associated with the supplement |  |
| **company_id** | **String** | The identifier of the company associated with the supplement |  |
| **contracts_compensation_id** | **String** | The contract compensation identifier associated with the supplement | [optional] |
| **contracts_taxonomy_id** | **String** | The taxonomy identifier associated with the supplement | [optional] |
| **amount_in_cents** | **Integer** | The amount of the supplement in cents | [optional] |
| **unit** | **String** | The unit of the supplement |  |
| **effective_on** | **String** | The date on which the supplement becomes effective | [optional] |
| **created_at** | [**Unknown**](Unknown.md) | The created at date when the supplement was created | [optional] |
| **updated_at** | [**Unknown**](Unknown.md) | The last updated at date when the supplement was last updated | [optional] |
| **description** | **String** | The description of the supplement | [optional] |
| **payroll_policy_period_id** | **String** | The payroll policy period identifier associated with the supplement | [optional] |
| **employee_observations** | **Array&lt;String&gt;** | Observations on the employee made by the admin or manager | [optional] |
| **raw_minutes_in_cents** | **Integer** | The raw value of minutes in cents associated with the supplement | [optional] |
| **minutes_in_cents** | **Integer** | The value of minutes in cents after adjustments | [optional] |
| **equivalent_minutes_in_cents** | **Integer** | The equivalent value of minutes in cents for payroll processing | [optional] |
| **currency** | **String** | The currency used for the supplement, typically in ISO 4217 format | [optional] |
| **legal_entity_id** | **String** | The legal entity identifier associated with the supplement | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PayrollSupplement.new(
  id: 1,
  employee_id: 1,
  company_id: 1,
  contracts_compensation_id: 1,
  contracts_taxonomy_id: 2,
  amount_in_cents: 50000,
  unit: money,
  effective_on: 2024-01-01,
  created_at: 2024-01-01T12:00:00Z,
  updated_at: 2024-01-05T12:00:00Z,
  description: Cantidad fija,
  payroll_policy_period_id: 1,
  employee_observations: [Worked extra shifts, Bonus for holiday work],
  raw_minutes_in_cents: 5000,
  minutes_in_cents: 4800,
  equivalent_minutes_in_cents: 4600,
  currency: EUR,
  legal_entity_id: 1
)
```

