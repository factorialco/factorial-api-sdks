# F::TimeoffLeavesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_id** | **String** | The employee id of the leave |  |
| **leave_type_id** | **String** | The leave type id | [optional] |
| **description** | **String** | The description of the leave | [optional] |
| **start_on** | **String** | The valid start date of the leave following the format YYYY-MM-DD |  |
| **finish_on** | **String** | The valid end date of the leave following the format YYYY-MM-DD | [optional] |
| **half_day** | **String** | If the leave is in: [beggining_of_day, end_of_day] | [optional] |
| **start_time** | **String** | The start time of a leave | [optional] |
| **hours_amount_in_cents** | **Integer** | The hours amount in cents of a leave | [optional] |
| **medical_leave_type** | **Integer** | The medical leave type | [optional] |
| **effective_on** | **String** | The effective on date of a leave following the format YYYY-MM-DD | [optional] |
| **medical_discharge_reason** | **String** | The medical discharge reason of a leave | [optional] |
| **colegiate_number** | **Integer** | The colegiate number of a leave | [optional] |
| **has_previous_relapse** | **Boolean** | If the leave has previous relapse | [optional] |
| **relapse_leave_id** | **String** | The leave relapse id | [optional] |
| **relapse_on** | **String** | The leave relapse on date following the format YYYY-MM-DD | [optional] |
| **accident_on** | **String** | The leave accident on date following the format YYYY-MM-DD | [optional] |
| **paternity_birth_on** | **String** | The leave paternity birth on date following the format YYYY-MM-DD | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffLeavesPostRequest.new(
  employee_id: 1,
  leave_type_id: 36,
  description: Annual family vacation,
  start_on: 2028-09-05,
  finish_on: 2028-09-05,
  half_day: null,
  start_time: 09:00,
  hours_amount_in_cents: 800,
  medical_leave_type: 4,
  effective_on: 2024-05-05,
  medical_discharge_reason: Illness,
  colegiate_number: 150,
  has_previous_relapse: false,
  relapse_leave_id: 1,
  relapse_on: 2028-09-05,
  accident_on: 2028-09-05,
  paternity_birth_on: 2028-09-05
)
```

