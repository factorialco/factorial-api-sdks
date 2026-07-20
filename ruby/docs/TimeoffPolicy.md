# F::TimeoffPolicy

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The policy id. |  |
| **name** | **String** | Policy name. |  |
| **main** | **Boolean** | Is the main policy? It will return true if it&#39;s the main policy if not it will return false. | [optional] |
| **company_id** | **String** | The company id. |  |
| **description** | **String** | The policy description. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffPolicy.new(
  id: 1,
  name: Policy for remotes,
  main: true,
  company_id: 1,
  description: This policy will apply only for remote employees
)
```

