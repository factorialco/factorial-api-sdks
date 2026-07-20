# F::TimePlanningPlanningVersion

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Planning version identifier | [optional] |
| **effective_at** | **String** | Planning version start date |  |
| **planning_tool** | **String** | Type of planning tool (shift_management, work_schedules, contract_hours) |  |
| **number_of_rest_days_in_cents** | **Integer** | Amount of rest days per week if applicable (in cents) | [optional] |
| **employee_id** | **String** | Employee identifier |  |
| **work_schedule_schedule_id** | **String** | Work schedule identifier to include if applicable | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimePlanningPlanningVersion.new(
  id: 1,
  effective_at: 2020-09-07,
  planning_tool: shift_management,
  number_of_rest_days_in_cents: 200,
  employee_id: 1,
  work_schedule_schedule_id: 1
)
```

