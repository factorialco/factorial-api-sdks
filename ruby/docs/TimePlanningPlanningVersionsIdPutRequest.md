# F::TimePlanningPlanningVersionsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Planning version identifier |  |
| **effective_at** | **String** | Planning version start date |  |
| **number_of_rest_days_in_cents** | **Integer** | Amount of rest days per week if applicable (in cents) | [optional] |
| **planning_tool** | **String** | Type of planning tool (shift_management, work_schedules, contract_hours) |  |
| **schedule_id** | **String** | Work schedule identifier to include if applicable | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimePlanningPlanningVersionsIdPutRequest.new(
  id: 1,
  effective_at: 2020-09-07,
  number_of_rest_days_in_cents: 200,
  planning_tool: shift_management,
  schedule_id: 1
)
```

