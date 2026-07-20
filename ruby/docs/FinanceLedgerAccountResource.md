# F::FinanceLedgerAccountResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Factorial unique identifier. |  |
| **resource_type** | **String** | Ledger account resource type. |  |
| **resource_id** | **String** | Factorial unique identifier of the resource associated to the ledger account resource. |  |
| **account_id** | **String** | Factorial Ledger Account identifier. |  |
| **balance_type** | **String** | Ledger account balance type. | [optional] |
| **updated_at** | **String** | Last time the resource was updated. |  |
| **external_id** | **String** | External identifier. | [optional] |
| **legal_entity_id** | **String** | Factorial unique identifier of the Legal entity. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceLedgerAccountResource.new(
  id: 135,
  resource_type: taxtype,
  resource_id: 155,
  account_id: 15,
  balance_type: debit,
  updated_at: 2021-01-01T00:00:00.000Z,
  external_id: ext_123,
  legal_entity_id: 13
)
```

