# F::ContractsSpanishEducationLevel

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Education level identifier |  |
| **name** | **String** | education level name |  |
| **default** | **Boolean** | Whether the education level is a predefined value | [optional] |
| **contracts_contract_template_id** | **String** | Contract template identifier, refers to contracts/contract_templates | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsSpanishEducationLevel.new(
  id: 1,
  name: Without studies,
  default: false,
  contracts_contract_template_id: 1
)
```

