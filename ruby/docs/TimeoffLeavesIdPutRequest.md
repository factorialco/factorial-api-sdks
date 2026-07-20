# F::TimeoffLeavesIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The leave id |  |
| **employee_id** | **String** | The employee id of the leave | [optional] |
| **leave_type_id** | **String** | The leave type id | [optional] |
| **description** | **String** | The description of the leave | [optional] |
| **start_on** | **String** | The valid start date of the leave following the format YYYY-MM-DD | [optional] |
| **finish_on** | **String** | The valid end date of the leave following the format YYYY-MM-DD | [optional] |
| **half_day** | **String** | If the leave is in: [beggining_of_day, end_of_day] | [optional] |
| **start_time** | **String** | The start time of a leave | [optional] |
| **hours_amount_in_cents** | **Integer** | The hours amount in cents of a leave | [optional] |
| **approved** | **Boolean** | Whether the leave is approved | [optional] |
| **skip_notifications** | **Boolean** | Whether to skip notifications for this update | [optional] |
| **skip_validations** | **Boolean** | Whether to skip validations for this update | [optional] |
| **skip_medical_leave** | **Boolean** | Whether to skip medical leave processing for this update | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffLeavesIdPutRequest.new(
  id: null,
  employee_id: 1,
  leave_type_id: 36,
  description: Annual family vacation,
  start_on: 2028-09-05,
  finish_on: 2028-09-05,
  half_day: null,
  start_time: 09:00,
  hours_amount_in_cents: 800,
  approved: true,
  skip_notifications: false,
  skip_validations: false,
  skip_medical_leave: false
)
```

