# F::ContractsSpanishContractType

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier for the contract type |  |
| **name** | **String** | The name of the contract type |  |
| **default** | **Boolean** | This contract type is a predefined one | [optional] |
| **contracts_contract_template_id** | **String** | The contract template identifier. Refers to contracts/contract_templates. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsSpanishContractType.new(
  id: 1,
  name: Indefinido,
  default: false,
  contracts_contract_template_id: 1
)
```

