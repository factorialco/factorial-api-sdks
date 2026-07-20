# F::FinanceLedgerAccountResourcesUpsertPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Factorial unique identifier. | [optional] |
| **name** | **String** | Name of the ledger account resource. | [optional] |
| **number** | **String** | Number of the ledger account resource. | [optional] |
| **external_id** | **String** | External identifier. | [optional] |
| **legal_entity_id** | **String** | Legal entity identifier. |  |
| **account_id** | **String** | Finance account identifier. | [optional] |
| **resource_id** | **String** | Factorial unique identifier of the resource associated to the ledger account resource. | [optional] |
| **resource_type** | **String** | Ledger account resource type. |  |
| **balance_type** | **String** | Ledger account balance type. | [optional] |
| **operation_type** | **String** | Ledger account operation type. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceLedgerAccountResourcesUpsertPostRequest.new(
  id: 135,
  name: Tax Type,
  number: 1234567890,
  external_id: ext_123,
  legal_entity_id: 13,
  account_id: 15,
  resource_id: 155,
  resource_type: taxtype,
  balance_type: debit,
  operation_type: purchase
)
```

