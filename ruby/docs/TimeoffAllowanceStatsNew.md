# F::TimeoffAllowanceStatsNew

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | A virtual ID for the allowance stat, composed of employee_id/allowance_id/reference_date. Cannot be used to fetch this resource. |  |
| **allowance_id** | **String** | ID of the allowance these stats belong to. |  |
| **employee_id** | **String** | ID of the employee these stats belong to. |  |
| **year** | **Integer** | Calendar year used to scope cycle calculations. |  |
| **cycles** | **Array&lt;Object&gt;** | Array of cycle objects describing each accrual period for the allowance. |  |
| **cycle_carry_overs** | **Array&lt;Object&gt;** | Carry over entries between cycles, typed as an array of CycleCarryOver value objects. |  |
| **accumulated_carry_over** | **String** | Total carried over units accumulated from previous cycles. |  |
| **available_days** | **String** | Remaining usable allowance units at the reference date, after usage, carry-over, and incidence adjustments. |  |
| **total_accrued_units** | **String** | Total accrued/generated allowance units up to the reference date. |  |
| **total** | **String** | Total entitlement for the cycle used by the Total row in counters (accrued + carry over + incidences, with backend cap/rounding rules applied before incidences). |  |
| **incidences** | **String** | Sum of incidence units (adjustments) applied to this allowance. |  |
| **accrued_incidences** | **String** | Sum of incidence units scoped to &#39;accrued&#39; target balance for the current cycle, filtered by cycle coverage rules. |  |
| **available_incidences** | **String** | Sum of incidence units scoped to non-accrued target balances for the current cycle, filtered by cycle coverage rules. |  |
| **max_balance_cap** | **String** | Maximum balance cap enforced by policy (null if unlimited or no cap). | [optional] |
| **policy_allowance** | **String** | Base policy entitlement for the cycle in allowance units (days or hours depending on allowance setup), before proration and adjustments. |  |
| **prorated_allowance_days** | **String** | Allowance days after proration based on employee tenure or configuration. |  |
| **total_in_decimal** | **String** | Total allowance units in decimal form (null if not computed for the reference date yet). | [optional] |
| **used_carry_over** | **String** | Units from carry over already consumed. |  |
| **used_days** | **String** | Total used days (converted from units) up to the reference date. |  |
| **used_units_until_reference_date** | **String** | Units consumed strictly until the given reference date (excludes future approved leaves). |  |
| **outstanding_units** | **String** | Pending units scheduled (approved in the future) not yet counted as used until the reference date. |  |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffAllowanceStatsNew.new(
  id: 1/2/2023-10-01,
  allowance_id: 10,
  employee_id: 42,
  year: 2025,
  cycles: [{id&#x3D;10/2025-01-01/2025-12-31, start_at&#x3D;2025-01-01, end_at&#x3D;2025-12-31, regular_start_at&#x3D;2025-01-01, regular_end_at&#x3D;2025-12-31, allowance_id&#x3D;10}],
  cycle_carry_overs: [{from_cycle_ending_on&#x3D;2024-12-31, expire_in_months&#x3D;3, non_expire&#x3D;false, total&#x3D;5.0, used&#x3D;[{date&#x3D;2024-06-15, amount&#x3D;1.0}], accumulated&#x3D;5.0, expired&#x3D;0.0, taken&#x3D;2.0}],
  accumulated_carry_over: 3.5,
  available_days: 8.0,
  total_accrued_units: 15.0,
  total: 19.0,
  incidences: 1.0,
  accrued_incidences: 0.5,
  available_incidences: 0.5,
  max_balance_cap: 25.0,
  policy_allowance: 20.0,
  prorated_allowance_days: 18.5,
  total_in_decimal: 20.0,
  used_carry_over: 1.5,
  used_days: 7.0,
  used_units_until_reference_date: 6.5,
  outstanding_units: 2.0
)
```

