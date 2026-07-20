# F::TimePlanningPlanningVersionsBulkCreatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **effective_at** | **String** | Start date of the planning version |  |
| **planning_tool** | **String** | Type of planning tool (shift_management, work_schedules, contract_hours) |  |
| **number_of_rest_days_in_cents** | **Integer** | Amount of rest days per week if applicable (in cents) | [optional] |
| **employee_ids** | **Array&lt;String&gt;** | List of employee identifiers |  |
| **schedule_id** | **String** | Work schedule identifier to include if applicable | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimePlanningPlanningVersionsBulkCreatePostRequest.new(
  effective_at: 2020-09-07,
  planning_tool: shift_management,
  number_of_rest_days_in_cents: 200,
  employee_ids: [1, 2, 3],
  schedule_id: 1
)
```

