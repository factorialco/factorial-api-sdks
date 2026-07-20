# F::TimeoffPoliciesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | The name of the policy. |  |
| **main** | **Boolean** | If the policy is the main policy. | [optional] |
| **description** | **String** | Policy description. | [optional] |
| **company_id** | **String** | Company ID. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffPoliciesPostRequest.new(
  name: Policy for remotes,
  main: false,
  description: This policy will apply only for remote employees,
  company_id: 1
)
```

