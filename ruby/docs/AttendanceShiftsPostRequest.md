# F::AttendanceShiftsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_id** | **String** | Id of the employee related | [optional] |
| **date** | **String** | Date of the shift |  |
| **reference_date** | **String** | Reference date of the shift | [optional] |
| **day** | **Integer** | number of days of the shift | [optional] |
| **clock_in** | **String** | Time of the clock in | [optional] |
| **clock_out** | **String** | Time of the clock out | [optional] |
| **observations** | **String** | Comments added to the shift | [optional] |
| **half_day** | **String** | Boolean that indicates if the shift is a half day | [optional] |
| **workable** | **Boolean** | Boolean that indicates if the shift is workable | [optional] |
| **location_type** | **String** | Type of the location | [optional] |
| **source** | **String** | Source of the shift creation | [optional] |
| **time_settings_break_configuration_id** | **String** | Id of the break configuration | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceShiftsPostRequest.new(
  employee_id: 1,
  date: 2022-01-01,
  reference_date: 2022-01-01,
  day: 1,
  clock_in: 2024-01-01T12:12:01-02:00,
  clock_out: 2024-01-01T12:12:01-02:00,
  observations: This is an observation,
  half_day: true,
  workable: true,
  location_type: office,
  source: desktop,
  time_settings_break_configuration_id: 1
)
```

