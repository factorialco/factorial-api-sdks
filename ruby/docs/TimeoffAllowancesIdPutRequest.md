# F::TimeoffAllowancesIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **accrued_denominator_in_cents** | **Integer** | Only for Allowances based on worked time. It represents how many units you need to work to be granted allowance units | [optional] |
| **accrued_factor_in_cents** | **Integer** | Only for Allowances based on worked time. It represents how many units you are given per unit of time worked | [optional] |
| **available_days** | **String** | Indicates how the allowance units are accrued. For example all_days means all allowance days are given on the first day of the cycle. | [optional] |
| **carry_over_units_in_cents** | **Integer** | How many units can carry over between cycles multiplied by 100 | [optional] |
| **count_holiday_as_workable** | **Boolean** | This setting flags if units taken during a bank holiday should be deducted or not from allowance. | [optional] |
| **days_type** | **String** | Indicates if the allowance is based on working on calendar days. | [optional] |
| **expire_in_months** | **Integer** | When does the carryover expire in months. | [optional] |
| **frequency** | **String** | Defines duration of the allowance cycles. Can be \&quot;yearly\&quot;, \&quot;monthly_flexible\&quot; or \&quot;lifetime\&quot; | [optional] |
| **holiday_allowance_in_cents** | **Integer** | Base amount of holiday allowance units multiplied by 100 | [optional] |
| **leave_type_ids** | **Array&lt;String&gt;** | An array of leave type ids associated with that allowance | [optional] |
| **maximum_amount_in_cents** | **Integer** | Maximum the allowance can reach on accrued | [optional] |
| **name** | **String** | Allowance name set by the user | [optional] |
| **negative_counter_type** | **String** | Whether the allowance allows to request more days than available. | [optional] |
| **position** | **Integer** | Indicates the position in the allowance when rendering them in UI | [optional] |
| **proration_type** | **String** | Whether the allowance has proration enabled or not. | [optional] |
| **pto_proratio_enabled** | **Boolean** | Whether the allowance days are prorated or not | [optional] |
| **range_type** | **String** | Configures how leaves duration is handled. | [optional] |
| **rounding** | **String** | How the accrued units of the allowance are rounded. It depends if the allowance is set in hours or days. | [optional] |
| **tenure_period_transition** | **String** | In case the allowance has tenure periods, when is this tenure applied. | [optional] |
| **tenure_periods_enabled** | **Boolean** | Whether the allowance has tenure periods enabled or not. | [optional] |
| **tenure_periods** | **Array&lt;Object&gt;** | The tenure periods associated with the allowance. | [optional] |
| **unlimited_accrued_hours** | **Boolean** | Flag to indicate if there is unlimited accrual. | [optional] |
| **unlimited_carry_over** | **Boolean** | Flag to indicate if there is unlimited carry over. | [optional] |
| **unlimited_carry_over_expiration** | **Boolean** | Boolean to flag if carryover does not expire | [optional] |
| **unlimited_holidays** | **Boolean** | Flag to indicate that the allowance has unlimited available days | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffAllowancesIdPutRequest.new(
  id: null,
  accrued_denominator_in_cents: 1000,
  accrued_factor_in_cents: 10,
  available_days: all_days,
  carry_over_units_in_cents: 1500,
  count_holiday_as_workable: false,
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
  tenure_period_transition: beginning_of_cycle,
  tenure_periods_enabled: false,
  tenure_periods: [{period_type&#x3D;years, period_length&#x3D;1, adjustment_in_cents&#x3D;100, timeoff_allowance_id&#x3D;23, max_cap_in_cents&#x3D;100, time_worked_based_hours_accrued_in_cents&#x3D;100, time_worked_based_per_hours_worked_in_cents&#x3D;100, balance_type&#x3D;fixed_balance}],
  unlimited_accrued_hours: false,
  unlimited_carry_over: false,
  unlimited_carry_over_expiration: false,
  unlimited_holidays: false
)
```

