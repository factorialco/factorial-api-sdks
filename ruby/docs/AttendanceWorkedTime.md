# F::AttendanceWorkedTime

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_id** | **String** |  |  |
| **date** | **String** |  |  |
| **company_id** | **String** |  |  |
| **tracked_minutes** | **Integer** |  |  |
| **multiplied_minutes** | **Integer** |  |  |
| **pending_minutes** | **Integer** |  |  |
| **minutes** | **Integer** |  |  |
| **time_unit** | **String** |  |  |
| **worked_time_blocks** | **Array&lt;Object&gt;** |  |  |
| **day_type** | **String** |  |  |
| **id** | **String** | ID to specify the worked time it includes the employee_id and date |  |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceWorkedTime.new(
  employee_id: null,
  date: null,
  company_id: null,
  tracked_minutes: null,
  multiplied_minutes: null,
  pending_minutes: null,
  minutes: null,
  time_unit: null,
  worked_time_blocks: null,
  day_type: null,
  id: 1_2024-07-01
)
```

