# F::ProjectManagementProject

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the project |  |
| **name** | **String** | The name of the project |  |
| **code** | **String** | The code of the project | [optional] |
| **description** | **String** | The description of the project | [optional] |
| **start_date** | **String** | The start date of the project | [optional] |
| **due_date** | **String** | The end date of the project | [optional] |
| **status** | **String** | The lifecycle status of the project (whether it is still running and can take new charges) |  |
| **employees_assignment** | **String** | How employees get access to the project — &#x60;manual&#x60; (hand-picked members) or &#x60;company&#x60; (everyone in the company) |  |
| **inputed_minutes** | **Integer** | The total minutes tracked in the project (if requested) | [optional] |
| **is_billable** | **Boolean** | Whether the project&#39;s costs can be billed (recharged) to a client |  |
| **fixed_cost_cents** | **Integer** | Total fixed costs in cents | [optional] |
| **labor_cost_cents** | **Integer** | Total labor costs in cents | [optional] |
| **legal_entity_id** | **String** | The legal entity id of the project |  |
| **spending_cost_cents** | **Integer** | Total spending costs in cents | [optional] |
| **client_id** | **String** | The client of the project, refers to finance/contacts. | [optional] |
| **total_cost_cents** | **Integer** | Total Cost in cents | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementProject.new(
  id: 314159,
  name: Project name,
  code: PRO,
  description: A comprehensive project to develop and implement a new customer relationship management system,
  start_date: 2025-01-01,
  due_date: 2026-01-01,
  status: active,
  employees_assignment: manual,
  inputed_minutes: 123,
  is_billable: true,
  fixed_cost_cents: 123,
  labor_cost_cents: 123,
  legal_entity_id: 123,
  spending_cost_cents: 123,
  client_id: 123,
  total_cost_cents: 123
)
```

