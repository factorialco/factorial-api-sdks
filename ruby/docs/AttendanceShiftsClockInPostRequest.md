# F::AttendanceShiftsClockInPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_id** | **String** | Employee identifier | [optional] |
| **now** | **String** | Clock in time |  |
| **latitude** | **Float** | Latitude from where user clocked in | [optional] |
| **longitude** | **Float** | Longitude from where user clocked in | [optional] |
| **accuracy** | **Float** | Location identifier | [optional] |
| **observations** | **String** | Notes on the shift record | [optional] |
| **location_type** | **String** | Place where user has clocked in | [optional] |
| **workplace_id** | **String** | Location identifier | [optional] |
| **time_settings_break_configuration_id** | **String** | Break configuration identifier | [optional] |
| **project_worker_id** | **String** | Project worker identifier | [optional] |
| **subproject_id** | **String** | Subproject identifier | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceShiftsClockInPostRequest.new(
  employee_id: 1,
  now: 2024-06-23T11:00:00.000+00:00,
  latitude: 52.377956,
  longitude: 4.89707,
  accuracy: 5,
  observations: I clocked in 10 minutes before,
  location_type: office,
  workplace_id: null,
  time_settings_break_configuration_id: 2,
  project_worker_id: 3,
  subproject_id: 4
)
```

