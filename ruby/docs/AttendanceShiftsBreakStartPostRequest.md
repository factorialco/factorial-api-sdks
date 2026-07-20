# F::AttendanceShiftsBreakStartPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_id** | **String** | Employee id of the break | [optional] |
| **now** | **String** | Current time of the break |  |
| **observations** | **String** | Observations of the break | [optional] |
| **time_settings_break_configuration_id** | **String** | Time settings configuration id of the break | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceShiftsBreakStartPostRequest.new(
  employee_id: 1,
  now: 2022-06-23T11:00:00.000+00:00,
  observations: break observation,
  time_settings_break_configuration_id: 1
)
```

