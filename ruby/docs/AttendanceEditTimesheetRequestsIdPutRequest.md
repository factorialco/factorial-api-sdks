# F::AttendanceEditTimesheetRequestsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_shift_id** | **String** |  | [optional] |
| **clock_in** | **String** |  | [optional] |
| **clock_out** | **String** |  | [optional] |
| **date** | **String** |  | [optional] |
| **reference_date** | **String** |  | [optional] |
| **employee_id** | **String** |  |  |
| **id** | **String** |  |  |
| **location_type** | **String** |  | [optional] |
| **observations** | **String** |  | [optional] |
| **reason** | **String** |  | [optional] |
| **time_settings_break_configuration_id** | **String** |  | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceEditTimesheetRequestsIdPutRequest.new(
  attendance_shift_id: null,
  clock_in: null,
  clock_out: null,
  date: null,
  reference_date: null,
  employee_id: null,
  id: null,
  location_type: null,
  observations: null,
  reason: null,
  time_settings_break_configuration_id: null
)
```

