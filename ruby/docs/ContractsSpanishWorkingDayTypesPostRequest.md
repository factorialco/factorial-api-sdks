# F::ContractsSpanishWorkingDayTypesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | Working day type name |  |
| **contracts_contract_template_id** | **String** | Contract template identifier, refers to contracts/contract_templates | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsSpanishWorkingDayTypesPostRequest.new(
  name: Fulltime,
  contracts_contract_template_id: 1
)
```

