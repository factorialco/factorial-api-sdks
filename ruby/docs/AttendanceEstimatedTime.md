# F::AttendanceEstimatedTime

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **date** | **String** |  |  |
| **company_id** | **String** |  |  |
| **employee_id** | **String** |  |  |
| **expected_minutes** | **Float** | Amount of minutes the employee has to work without taking into consideration time off leaves and bank holidays. |  |
| **regular_minutes** | **Float** | Amount of regular minutes the employee has to work. |  |
| **overtime_minutes** | **Float** | Amount of overtime minutes the employee has to work (only available with Shift Management). |  |
| **breaks** | **Array&lt;Object&gt;** |  |  |
| **time_unit** | **String** |  |  |
| **estimated_half_days** | **Integer** |  |  |
| **shifts** | **Array&lt;Object&gt;** |  |  |
| **source** | **String** | Source of the estimated time. Could be employee&#39;s contract, work schedule or shift management. |  |
| **id** | **String** | ID to specify the estimation time it includes the employee_id and date |  |
| **minutes** | **Float** | Amount of minutes the employee has to work. |  |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceEstimatedTime.new(
  date: null,
  company_id: null,
  employee_id: null,
  expected_minutes: null,
  regular_minutes: null,
  overtime_minutes: null,
  breaks: null,
  time_unit: null,
  estimated_half_days: null,
  shifts: null,
  source: null,
  id: 1_2025-02-01,
  minutes: null
)
```

