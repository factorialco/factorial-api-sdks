# F::AttendanceShiftsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id of the shift |  |
| **clock_in** | **String** | Time of the clock in | [optional] |
| **clock_out** | **String** | Time of the clock out | [optional] |
| **date** | **String** | Date of the shift | [optional] |
| **reference_date** | **String** | reference date of the shift | [optional] |
| **observations** | **String** | Comments added to the shift | [optional] |
| **location_type** | **String** | Type of the location | [optional] |
| **workplace_id** | **String** | Id of the location related | [optional] |
| **time_settings_break_configuration_id** | **String** | Id of the break configuration | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceShiftsIdPutRequest.new(
  id: 1,
  clock_in: 2024-01-01T12:12:01-02:00,
  clock_out: 2024-01-01T12:12:01-02:00,
  date: 2024-01-01,
  reference_date: 2024-01-01,
  observations: This is an observation,
  location_type: office,
  workplace_id: 1,
  time_settings_break_configuration_id: 1
)
```

