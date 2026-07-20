# F::TimeoffLeave

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the Leave |  |
| **company_id** | **String** | Company identifier of the employee of the leave |  |
| **employee_id** | **String** | Employee identifier of the leave |  |
| **start_on** | **String** | The start date of the leave |  |
| **finish_on** | **String** | The end date of the leave | [optional] |
| **half_day** | **String** | Indicates if the leave is taken as a half-day | [optional] |
| **description** | **String** | A description of the leave | [optional] |
| **reason** | **String** | The reason provided by the employee for taking the leave | [optional] |
| **leave_type_id** | **String** | The identifier for the type of leave | [optional] |
| **leave_type_name** | **String** | The name of the leave type | [optional] |
| **approved** | **Boolean** | Indicates whether the leave has been approved | [optional] |
| **employee_full_name** | **String** | The full name of the employee taking the leave | [optional] |
| **start_time** | **String** | The start time of the leave | [optional] |
| **hours_amount_in_cents** | **Integer** | The total number of hours taken for the leave, represented in cents | [optional] |
| **updated_at** | **String** | The updated at date of the leave |  |
| **created_at** | **String** | The created at date of the leave | [optional] |
| **deleted_at** | **String** | The date when the leave was deleted | [optional] |
| **duration_attributes** | **String** | The duration attributes of the leave | [optional] |
| **days_taken** | **Float** | Number of days taken for paid leave |  |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffLeave.new(
  id: 1,
  company_id: 1,
  employee_id: 1,
  start_on: 2028-09-05,
  finish_on: 2028-09-05,
  half_day: null,
  description: Annual family vacation,
  reason: Medical appointment,
  leave_type_id: 36,
  leave_type_name: null,
  approved: true,
  employee_full_name: Bob The Boss,
  start_time: 09:00,
  hours_amount_in_cents: 800,
  updated_at: 2028-03-11T17:03:12.000Z,
  created_at: 2028-03-11T17:03:12.000Z,
  deleted_at: 2028-03-11T17:03:12.000Z,
  duration_attributes: {accrues_list&#x3D;{2028&#x3D;1.0}, workable_units&#x3D;{days&#x3D;{2028&#x3D;1.0}, hours&#x3D;{2028&#x3D;8.0}}, used_units&#x3D;{days&#x3D;{2028&#x3D;1.0}, hours&#x3D;{2028&#x3D;8.0}}, french_calendar_flag_enabled&#x3D;false, finish_on_natural&#x3D;2028-09-05},
  days_taken: 1.0
)
```

