# F::FinanceCostCenter

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **name** | **String** |  |  |
| **company_id** | **String** |  |  |
| **legal_entity_id** | **String** |  | [optional] |
| **code** | **String** |  | [optional] |
| **description** | **String** |  | [optional] |
| **active_employees_count** | **Integer** |  |  |
| **historical_employees_count** | **Integer** |  |  |
| **status** | **String** |  |  |
| **deactivation_date** | **String** |  | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceCostCenter.new(
  id: null,
  name: null,
  company_id: null,
  legal_entity_id: null,
  code: null,
  description: null,
  active_employees_count: null,
  historical_employees_count: null,
  status: null,
  deactivation_date: null
)
```

