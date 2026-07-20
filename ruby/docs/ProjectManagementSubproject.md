# F::ProjectManagementSubproject

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the subproject | [optional] |
| **name** | **String** | The name of the subproject |  |
| **project_id** | **String** | The id of the project |  |
| **inputed_minutes** | **Integer** | The total minutes tracked in the subproject (if requested) | [optional] |
| **labor_cost_cents** | **Integer** | The total labor cost of the subproject in cents (if requested) | [optional] |
| **description** | **String** | The description of the subproject | [optional] |
| **status** | **String** | The status of the subproject | [optional] |
| **code** | **String** | The code of the subproject | [optional] |
| **start_date** | **String** | The start date of the subproject | [optional] |
| **due_date** | **String** | The due date of the subproject | [optional] |
| **is_billable** | **Boolean** | Whether the subproject is billable | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementSubproject.new(
  id: 314,
  name: Subproject name,
  project_id: 11,
  inputed_minutes: 0,
  labor_cost_cents: 540000,
  description: Subproject description,
  status: active,
  code: SUB123,
  start_date: 2025-01-01,
  due_date: 2025-12-31,
  is_billable: true
)
```

