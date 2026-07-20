# F::ContractsContractVersionMetaData

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **contract_version_id** | **String** | identifier for the contract version. |  |
| **action_type** | **String** | the action that has been performed on the contract version ex:promotion / evolution / null. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsContractVersionMetaData.new(
  contract_version_id: 1,
  action_type: promotion
)
```

