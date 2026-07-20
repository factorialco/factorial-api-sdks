# F::ProjectManagementProjectsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id project. |  |
| **name** | **String** | Name of the project. |  |
| **code** | **String** | Code for the project to be identifiable and searchable. | [optional] |
| **description** | **String** | Description of the project. | [optional] |
| **start_date** | **String** | Start date for the project. If given must be in iso-8601 format (YYYY-MM-DD). | [optional] |
| **due_date** | **String** | Due date for the project. If given must be in iso-8601 format (YYYY-MM-DD). | [optional] |
| **client_id** | **String** | Client associated to the project, refers to finance/contacts. | [optional] |
| **legal_entity_id** | **String** | Id of the legal entity for the currency of the project | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementProjectsIdPutRequest.new(
  id: 314159,
  name: Project Name,
  code: PRO,
  description: A comprehensive project to develop and implement a new customer relationship management system,
  start_date: 2025-01-01,
  due_date: 2026-01-01,
  client_id: 123,
  legal_entity_id: 123
)
```

