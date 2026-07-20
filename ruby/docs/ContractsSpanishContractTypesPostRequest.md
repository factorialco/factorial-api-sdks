# F::ContractsSpanishContractTypesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | Contract type name |  |
| **contracts_contract_template_id** | **String** | Contract template identifier. Refers to contracts/contract_templates. |  |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsSpanishContractTypesPostRequest.new(
  name: Indefinido,
  contracts_contract_template_id: 1
)
```

