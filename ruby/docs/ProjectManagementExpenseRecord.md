# F::ProjectManagementExpenseRecord

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **project_worker_id** | **String** |  |  |
| **expense_id** | **String** |  |  |
| **subproject_id** | **String** |  | [optional] |
| **original_amount_currency** | **String** |  | [optional] |
| **original_amount_cents** | **Integer** |  | [optional] |
| **legal_entity_amount_currency** | **String** |  | [optional] |
| **legal_entity_amount_cents** | **String** |  | [optional] |
| **effective_on** | **String** |  | [optional] |
| **exchange_rate** | **Float** |  | [optional] |
| **status** | **String** |  | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementExpenseRecord.new(
  id: null,
  project_worker_id: null,
  expense_id: null,
  subproject_id: null,
  original_amount_currency: null,
  original_amount_cents: null,
  legal_entity_amount_currency: null,
  legal_entity_amount_cents: null,
  effective_on: null,
  exchange_rate: null,
  status: null
)
```

