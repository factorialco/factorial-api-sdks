# F::AttendanceEditTimesheetRequestsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_id** | **String** |  |  |
| **request_type** | **String** |  |  |
| **reason** | **String** |  | [optional] |
| **date** | **String** |  | [optional] |
| **clock_in** | **String** |  | [optional] |
| **clock_out** | **String** |  | [optional] |
| **workable** | **Boolean** |  | [optional] |
| **attendance_shift_id** | **String** |  | [optional] |
| **reference_date** | **String** |  | [optional] |
| **time_settings_break_configuration_id** | **String** |  | [optional] |
| **location_type** | **String** |  | [optional] |
| **observations** | **String** |  | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceEditTimesheetRequestsPostRequest.new(
  employee_id: null,
  request_type: null,
  reason: null,
  date: null,
  clock_in: null,
  clock_out: null,
  workable: null,
  attendance_shift_id: null,
  reference_date: null,
  time_settings_break_configuration_id: null,
  location_type: null,
  observations: null
)
```

