# F::AttendanceEditTimesheetRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier for the edit timesheet request |  |
| **approved** | **Boolean** | Status of the edit timesheet request | [optional] |
| **request_type** | **String** | Type of the request |  |
| **employee_id** | **String** | Id of the shift&#39;s employee |  |
| **workable** | **Boolean** | Indicates if the shift is workable or a break | [optional] |
| **clock_in** | **String** | Clock in of the shift | [optional] |
| **clock_out** | **String** | Clock out of the shift | [optional] |
| **location_type** | **String** | Location of the shift | [optional] |
| **reason** | **String** | Approve or reject reason | [optional] |
| **attendance_shift_id** | **String** | Id of the shift for the request | [optional] |
| **time_settings_break_configuration_id** | **String** | Id of the type of break for the request | [optional] |
| **observations** | **String** | Additional observations for the shift | [optional] |
| **date** | **String** | Date of the shift | [optional] |
| **reference_date** | **String** | Reference date for the shift | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceEditTimesheetRequest.new(
  id: 1,
  approved: 1,
  request_type: create_shift,
  employee_id: 1,
  workable: true,
  clock_in: 08:30:15,
  clock_out: 10:30:00,
  location_type: office,
  reason: Looks good!,
  attendance_shift_id: 1,
  time_settings_break_configuration_id: 1,
  observations: Employee arrived late due to traffic,
  date: 2023-10-01,
  reference_date: 2023-09-30
)
```

