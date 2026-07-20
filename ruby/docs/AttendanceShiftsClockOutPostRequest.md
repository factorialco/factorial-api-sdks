# F::AttendanceShiftsClockOutPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_id** | **String** | Employee identifier | [optional] |
| **now** | **String** | Clock out time |  |
| **latitude** | **Float** | Latitude from where user clocked in | [optional] |
| **longitude** | **Float** | Longitude from where user clocked in | [optional] |
| **accuracy** | **Float** | Location accuracy | [optional] |
| **observations** | **String** | Notes on the shift record | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceShiftsClockOutPostRequest.new(
  employee_id: 1,
  now: 2024-06-23T11:00:00.000+00:00,
  latitude: 52.377956,
  longitude: 4.89707,
  accuracy: 5,
  observations: I clocked in 10 minutes before
)
```

