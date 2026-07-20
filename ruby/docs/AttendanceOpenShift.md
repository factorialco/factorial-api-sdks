# F::AttendanceOpenShift

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Open Shift identifier. |  |
| **employee_id** | **String** | Employee identifier from the open shift. |  |
| **date** | **String** | Date of the open shift. |  |
| **reference_date** | **String** | Reference date for the shift |  |
| **clock_in** | **String** | Clock in time from the shift. Ignore the date part. |  |
| **clock_out** | **String** | For open shifts, this field is null. | [optional] |
| **status** | **String** | Status of the shift |  |
| **workable** | **Boolean** | Indicates if the shift is a break or a workable shift. |  |
| **automatic_clock_in** | **Boolean** | Indicates if the shift is automatic or not |  |
| **location_type** | **String** | String representing the location type of the shift. Examples work_from_home, office, etc. | [optional] |
| **workplace_id** | **String** | Identifier for the workplace assinged to the shift. | [optional] |
| **time_settings_break_configuration_id** | **String** | If the shift is a break, this field will have the break configuration id. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceOpenShift.new(
  id: 1,
  employee_id: 1,
  date: 2024-06-06,
  reference_date: 2024-06-06,
  clock_in: 2000-01-01T02:35:25.000Z,
  clock_out: null,
  status: opened,
  workable: true,
  automatic_clock_in: false,
  location_type: work_from_home,
  workplace_id: 1,
  time_settings_break_configuration_id: 1
)
```

