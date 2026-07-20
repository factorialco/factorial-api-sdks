# F::EmployeeUpdatesAbsence

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the absence employee update |  |
| **status** | **String** | The status of the employee update. |  |
| **employee_id** | **String** | Employee id of the absence | [optional] |
| **employee_full_name** | **String** | Full name of the employee | [optional] |
| **approved** | **Boolean** | Indicates if the absence is approved | [optional] |
| **description** | **String** | A description of the absence | [optional] |
| **start_on** | **String** | The start date of the absence | [optional] |
| **prev_start_on** | **String** | The previous start date of the absence | [optional] |
| **finish_on** | **String** | The end date of the absence | [optional] |
| **prev_finish_on** | **String** | The previous end date of the absence | [optional] |
| **half_day** | **String** | Indicates if the absence is taken as a half-day | [optional] |
| **hours_amount_in_cents** | **Integer** | The total number of hours taken for the absence, represented in cents | [optional] |
| **leave_type_id** | **String** | The id of the leave type | [optional] |
| **leave_type_name** | **String** | The name of the leave type | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::EmployeeUpdatesAbsence.new(
  id: 1,
  status: done,
  employee_id: 1,
  employee_full_name: Bob The Boss,
  approved: true,
  description: Trip to Norway,
  start_on: 2021-06-07,
  prev_start_on: 2021-06-07,
  finish_on: 2021-06-09,
  prev_finish_on: 2021-06-07,
  half_day: end_of_day,
  hours_amount_in_cents: 80000,
  leave_type_id: 1,
  leave_type_name: Annual leave
)
```

