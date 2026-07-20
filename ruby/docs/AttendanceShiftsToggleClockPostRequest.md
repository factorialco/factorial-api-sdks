# F::AttendanceShiftsToggleClockPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_id** | **String** | Employee identifier |  |
| **clock_time** | **String** | Clock in or out Timestamp |  |
| **location_type** | **String** | Place where user has clocked in | [optional] |
| **observations** | **String** | Notes on the shift record | [optional] |
| **time_settings_break_configuration_id** | **String** | Specific break configuration id when toggling the shift into a break and out of a break | [optional] |
| **project_id** | **String** | Project identifier to associate the shift with a project. The employee must be assigned to the project, otherwise a 404 error is returned. Only used on clock-in; on clock-out this field is ignored, but the project association is preserved on the shift. Breaks are not associated with any project. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceShiftsToggleClockPostRequest.new(
  employee_id: 1,
  clock_time: 2024-06-23T11:00:00.000+00:00,
  location_type: office,
  observations: I clocked in 10 minutes before,
  time_settings_break_configuration_id: 1,
  project_id: 1
)
```

