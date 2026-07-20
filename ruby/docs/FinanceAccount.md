# F::FinanceAccount

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier in factorial for the ledger account |  |
| **name** | **String** | Name of the ledger account | [optional] |
| **legal_entity_id** | **String** | Legal entity ID of the ledger account |  |
| **number** | **String** | Number of the ledger account |  |
| **disabled** | **Boolean** | Whether the ledger account is disabled |  |
| **type** | **String** | Type of the ledger account |  |
| **external_id** | **String** | Id of the ledger account on the external system | [optional] |
| **updated_at** | **String** | Last updated date of the ledger account |  |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceAccount.new(
  id: 1,
  name: Bank Account,
  legal_entity_id: 11,
  number: 1000,
  disabled: false,
  type: bank,
  external_id: ext_123,
  updated_at: 2021-01-01T00:00:00.000Z
)
```

