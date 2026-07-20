# F::FinanceBudgetOption

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier for the budget option |  |
| **name** | **String** | Name of the budget option |  |
| **description** | **String** | Description of the budget option | [optional] |
| **currency** | **String** | Currency of the budget option |  |
| **legal_entity_id** | **String** | Legal entity ID of the budget option |  |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceBudgetOption.new(
  id: 1,
  name: Marketing Budget,
  description: Budget for marketing activities,
  currency: EUR,
  legal_entity_id: 11
)
```

