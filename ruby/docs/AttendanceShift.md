# F::AttendanceShift

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier for the shift |  |
| **employee_id** | **String** | Identifier for the employee assigned to the shift |  |
| **date** | **String** | Date of the shift |  |
| **reference_date** | **String** | Reference date for the shift |  |
| **clock_in** | **String** | Time when the employee clocked in | [optional] |
| **clock_out** | **String** | Time when the employee clocked out | [optional] |
| **in_source** | **String** | Source of the clock-in time | [optional] |
| **out_source** | **String** | Source of the clock-out time | [optional] |
| **observations** | **String** | Additional observations about the shift | [optional] |
| **location_type** | **String** | Type of location for the shift | [optional] |
| **half_day** | **String** | Indicates which worked part of the day | [optional] |
| **in_location_latitude** | **Float** | Latitude of the clock-in location | [optional] |
| **in_location_longitude** | **Float** | Longitude of the clock-in location | [optional] |
| **in_location_accuracy** | **Float** | Accuracy of the clock-in location | [optional] |
| **out_location_latitude** | **Float** | Latitude of the clock-out location | [optional] |
| **out_location_longitude** | **Float** | Longitude of the clock-out location | [optional] |
| **out_location_accuracy** | **Float** | Accuracy of the clock-out location | [optional] |
| **workable** | **Boolean** | Indicates if the shift is workable | [optional] |
| **created_at** | **String** | Timestamp when the shift record was created |  |
| **workplace_id** | **String** | Identifier for the location | [optional] |
| **time_settings_break_configuration_id** | **String** | Identifier for the break configuration | [optional] |
| **company_id** | **String** | Identifier for the company |  |
| **updated_at** | **String** | Timestamp when the shift record was updated |  |
| **minutes** | **Integer** | Number in minutes of the shift |  |
| **clock_in_with_seconds** | **String** | Clock in time with seconds | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceShift.new(
  id: 1,
  employee_id: 1,
  date: 2023-10-01,
  reference_date: 2023-09-30,
  clock_in: 08:30,
  clock_out: 12:30,
  in_source: automatic,
  out_source: automatic,
  observations: Employee arrived late due to traffic,
  location_type: office,
  half_day: beginning_of_day,
  in_location_latitude: 37.7749,
  in_location_longitude: -122.419,
  in_location_accuracy: 5.0,
  out_location_latitude: 37.7749,
  out_location_longitude: -122.419,
  out_location_accuracy: 5.7,
  workable: true,
  created_at: 2023-10-01T08:00:00.000Z,
  workplace_id: 1,
  time_settings_break_configuration_id: 1,
  company_id: 1,
  updated_at: 2023-10-01T08:00:00.000Z,
  minutes: 240,
  clock_in_with_seconds: 08:30:15
)
```

