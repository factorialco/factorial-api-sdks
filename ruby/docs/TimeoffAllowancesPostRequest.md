# F::TimeoffAllowancesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **accrued_denominator_in_cents** | **Integer** | Only for Allowances based on worked time. It represents how many units you need to work to be granted allowance units | [optional] |
| **accrued_factor_in_cents** | **Integer** | Only for Allowances based on worked time. It represents how many units you are given per unit of time worked | [optional] |
| **accrued_units_availability** | **String** | When can the accrued units be spent. |  |
| **allowance_type** | **String** | Sets the allowance units. Can be \&quot;days\&quot; or \&quot;hours\&quot; |  |
| **available_days** | **String** | Indicates how the allowance units are accrued. For example all_days means all allowance days are given on the first day of the cycle. |  |
| **carry_over_units_in_cents** | **Integer** | How many units can carry over between cycles multiplied by 100 | [optional] |
| **count_holiday_as_workable** | **Boolean** | This setting flags if units taken during a bank holiday should be deducted or not from allowance. |  |
| **cycle_length** | **Integer** | How many months does each allowance cycle last | [optional] |
| **cycle_start** | **String** | When does the cycle start. |  |
| **days_type** | **String** | Indicates if the allowance is based on working on calendar days. |  |
| **expire_in_months** | **Integer** | When does the carryover expire in months. | [optional] |
| **frequency** | **String** | Defines duration of the allowance cycles. Can be \&quot;yearly\&quot;, \&quot;monthly_flexible\&quot; or \&quot;lifetime\&quot; | [optional] |
| **holiday_allowance_in_cents** | **Integer** | Base amount of holiday allowance units multiplied by 100 |  |
| **leave_type_ids** | **Array&lt;String&gt;** | An array of leave type ids associated with that allowance |  |
| **maximum_amount_in_cents** | **Integer** | Maximum the allowance can reach on accrued | [optional] |
| **name** | **String** | Allowance name set by the user |  |
| **negative_counter_type** | **String** | Whether the allowance allows to request more days than available. |  |
| **position** | **Integer** | Indicates the position in the allowance when rendering them in UI | [optional] |
| **proration_type** | **String** | Whether the allowance has proration enabled or not. |  |
| **pto_proratio_enabled** | **Boolean** | Whether the allowance days are prorated or not |  |
| **range_type** | **String** | Configures how leaves duration is handled. | [optional] |
| **rounding** | **String** | How the accrued units of the allowance are rounded. It depends if the allowance is set in hours or days. |  |
| **source_units** | **String** | This field configures the type of allowance (fixed balance, based on worked time) |  |
| **tenure_period_transition** | **String** | In case the allowance has tenure periods, when is this tenure applied. | [optional] |
| **tenure_periods_enabled** | **Boolean** | Whether the allowance has tenure periods enabled or not. | [optional] |
| **tenure_periods** | **Array&lt;Object&gt;** | The tenure periods associated with the allowance. |  |
| **timeoff_policy_id** | **String** | The Id of the policy to which the allowance belongs to |  |
| **unlimited_accrued_hours** | **Boolean** | Flag to indicate if there is unlimited accrual. |  |
| **unlimited_carry_over** | **Boolean** | Flag to indicate if there is unlimited carry over. |  |
| **unlimited_carry_over_expiration** | **Boolean** | Boolean to flag if carryover does not expire |  |
| **unlimited_holidays** | **Boolean** | Flag to indicate that the allowance has unlimited available days |  |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffAllowancesPostRequest.new(
  accrued_denominator_in_cents: 1000,
  accrued_factor_in_cents: 10,
  accrued_units_availability: current_cycle,
  allowance_type: days,
  available_days: all_days,
  carry_over_units_in_cents: 1500,
  count_holiday_as_workable: false,
  cycle_length: 12,
  cycle_start: jan,
  days_type: working_days,
  expire_in_months: 6,
  frequency: yearly,
  holiday_allowance_in_cents: 2300,
  leave_type_ids: [1, 2, 3, 4],
  maximum_amount_in_cents: 2800,
  name: Holiday Allowance,
  negative_counter_type: negative_counter_disabled,
  position: 0,
  proration_type: proration_enabled,
  pto_proratio_enabled: false,
  range_type: working_days,
  rounding: half_day,
  source_units: base_units,
  tenure_period_transition: beginning_of_cycle,
  tenure_periods_enabled: false,
  tenure_periods: [{&quot;period_type&quot;:&quot;years&quot;,&quot;period_length&quot;:1,&quot;adjustment_in_cents&quot;:100,&quot;timeoff_allowance_id&quot;:23,&quot;max_cap_in_cents&quot;:100,&quot;time_worked_based_hours_accrued_in_cents&quot;:100,&quot;time_worked_based_per_hours_worked_in_cents&quot;:100,&quot;balance_type&quot;:&quot;fixed_balance&quot;}],
  timeoff_policy_id: 1,
  unlimited_accrued_hours: false,
  unlimited_carry_over: false,
  unlimited_carry_over_expiration: false,
  unlimited_holidays: false
)
```

