# F::ContractsSpanishWorkingDayType

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Working day type identifier |  |
| **name** | **String** | Working day type name |  |
| **default** | **Boolean** | Whether the Working day type is a predefined value | [optional] |
| **contracts_contract_template_id** | **String** | Contract template identifier, refers to contracts/contract_templates | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsSpanishWorkingDayType.new(
  id: 1,
  name: Fulltime,
  default: false,
  contracts_contract_template_id: 1
)
```

