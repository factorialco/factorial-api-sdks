# F::ProjectManagementProjectsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | Mandatory to pass a name of the project. |  |
| **code** | **String** | Optional unique code for the project to be identifiable and searchable. | [optional] |
| **description** | **String** | Description of the project. | [optional] |
| **start_date** | **String** | Optional start date for the project. If given must be in iso-8601 format (YYYY-MM-DD). | [optional] |
| **due_date** | **String** | Optional due date for the project. If given must be in iso-8601 format (YYYY-MM-DD). | [optional] |
| **status** | **String** | Project status. Can be &#x60;active&#x60; or &#x60;closed&#x60; | [optional] |
| **employees_assignment** | **String** | Optional param to define the kind of assignation the project has. Can be &#x60;manual&#x60; or &#x60;company&#x60; | [optional] |
| **project_admins** | **Array&lt;String&gt;** | Array of employee IDs who are project administrators | [optional] |
| **project_managers** | **Array&lt;String&gt;** | Array of employee IDs who are project managers | [optional] |
| **is_billable** | **Boolean** | Whether the project is billable to clients | [optional] |
| **fixed_cost_cents** | **Integer** | Fixed cost of the project in cents | [optional] |
| **budget_allocation** | **Integer** | Budget allocation in minutes for the project, it&#39;s exclusive of the budget_allocation_cents | [optional] |
| **legal_entity_id** | **String** | The legal entity ID associated with the project | [optional] |
| **budget_allocation_cents** | **Integer** | Budget allocation amount in cents, it&#39;s exclusive of the budget_allocation | [optional] |
| **fee_amount_cents** | **Integer** | Fee amount in cents for the project | [optional] |
| **client_id** | **String** | Client associated to the project, refers to finance/contacts. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementProjectsPostRequest.new(
  name: Project Name,
  code: PRO,
  description: A comprehensive project to develop and implement a new customer relationship management system,
  start_date: 2024-10-30,
  due_date: 2026-01-01,
  status: active,
  employees_assignment: company,
  project_admins: [&quot;314159&quot;],
  project_managers: [&quot;271828&quot;],
  is_billable: true,
  fixed_cost_cents: 50000,
  budget_allocation: 1200,
  legal_entity_id: 123,
  budget_allocation_cents: 100000,
  fee_amount_cents: 25000,
  client_id: 1
)
```

