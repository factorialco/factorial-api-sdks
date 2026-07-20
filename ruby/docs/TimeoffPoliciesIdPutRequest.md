# F::TimeoffPoliciesIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id of the policy to update. |  |
| **name** | **String** | The name of the policy. | [optional] |
| **description** | **String** | Policy description. | [optional] |
| **main** | **Boolean** | If the policy is the main policy. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffPoliciesIdPutRequest.new(
  id: 1,
  name: Policy for remotes,
  description: This policy will apply only for remote employees,
  main: false
)
```

