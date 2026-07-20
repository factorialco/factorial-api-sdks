# F::ContractsSpanishProfessionalCategory

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Professional category identifier |  |
| **name** | **String** | Professional category name |  |
| **default** | **Boolean** | Whether the professional category is a predefined value | [optional] |
| **contracts_contract_template_id** | **String** | Contract template identifier, refers to contracts/contract_templates | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsSpanishProfessionalCategory.new(
  id: 1,
  name: Administration Manager,
  default: false,
  contracts_contract_template_id: 1
)
```

