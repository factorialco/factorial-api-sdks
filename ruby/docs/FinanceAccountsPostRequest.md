# F::FinanceAccountsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | Name of the ledger account | [optional] |
| **number** | **String** | Number of the ledger account |  |
| **type** | **String** | Type of the ledger account |  |
| **currency** | **String** | Currency of the ledger account |  |
| **legal_entity_id** | **String** | Legal entity ID of the ledger account |  |
| **external_id** | **String** | Id of the ledger account on the external system. This field is important to avoid having duplicated ledger accounts | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceAccountsPostRequest.new(
  name: Bank Account,
  number: 1000,
  type: bank,
  currency: EUR,
  legal_entity_id: 11,
  external_id: ext_123
)
```

