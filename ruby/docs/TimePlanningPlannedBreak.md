# F::TimePlanningPlannedBreak

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Planned break identifier |  |
| **start_at** | **String** | Break start time | [optional] |
| **end_at** | **String** | Break end time | [optional] |
| **duration** | **Integer** | Duration of the break in minutes | [optional] |
| **break_type** | **String** | Type of the break |  |
| **break_configuration_id** | **String** | Break configuration identifier |  |
| **break_configuration_name** | **String** | Name of the break configuration |  |
| **break_configuration_paid** | **Boolean** | Whether the break is paid |  |
| **default_shift_id** | **String** | Default shift identifier | [optional] |
| **shift_configuration_id** | **String** | Shift configuration identifier | [optional] |
| **shift_id** | **String** | Shift identifier | [optional] |
| **day_configuration_id** | **String** | Day configuration identifier | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimePlanningPlannedBreak.new(
  id: 1,
  start_at: 2020-09-07T06:00:00.000+00:00,
  end_at: 2020-09-07T15:00:00.000+00:00,
  duration: 30,
  break_type: flexible,
  break_configuration_id: 1,
  break_configuration_name: Rest,
  break_configuration_paid: true,
  default_shift_id: null,
  shift_configuration_id: null,
  shift_id: 1,
  day_configuration_id: null
)
```

