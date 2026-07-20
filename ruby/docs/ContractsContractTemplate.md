# F::ContractsContractTemplate

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier for the contract template |  |
| **company_id** | **String** | ID of the company this template belongs to | [optional] |
| **contract_version_type** | **String** | Type of contract version (e.g., es for Spain, fr for France) | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsContractTemplate.new(
  id: 1,
  company_id: 1,
  contract_version_type: es
)
```

