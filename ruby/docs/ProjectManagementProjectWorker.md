# F::ProjectManagementProjectWorker

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | id of the project worker. |  |
| **project_id** | **String** | id of the project. |  |
| **employee_id** | **String** | id of the employee. |  |
| **assigned** | **Boolean** | true if the employee is assigned to the project, false otherwise. |  |
| **inputed_minutes** | **Integer** | total inmputed minutes of the employee in the project. | [optional] |
| **labor_cost_cents** | **Integer** | total project currency labor cost of the employee in the project. | [optional] |
| **company_labor_cost_cents** | **Integer** | total company currency labor cost of the employee in the project. | [optional] |
| **spending_cost_cents** | **Integer** | total spending cost of the employee in the project. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementProjectWorker.new(
  id: 92732,
  project_id: 314159,
  employee_id: 21,
  assigned: true,
  inputed_minutes: 100,
  labor_cost_cents: 100,
  company_labor_cost_cents: 100,
  spending_cost_cents: 100
)
```

