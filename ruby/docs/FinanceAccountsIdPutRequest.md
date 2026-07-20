# F::FinanceAccountsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier in factorial for the ledger account |  |
| **name** | **String** | Name of the ledger account | [optional] |
| **number** | **String** | Number of the ledger account | [optional] |
| **type** | **String** | Type of the ledger account | [optional] |
| **currency** | **String** | Currency of the ledger account | [optional] |
| **legal_entity_id** | **String** | Legal entity ID of the ledger account | [optional] |
| **external_id** | **String** | Id of the ledger account on the external system | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceAccountsIdPutRequest.new(
  id: 1,
  name: Bank Account,
  number: 1000,
  type: bank,
  currency: EUR,
  legal_entity_id: 11,
  external_id: ext_123
)
```

