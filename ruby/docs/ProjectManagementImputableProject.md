# F::ProjectManagementImputableProject

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the imputable project |  |
| **name** | **String** | The name of the imputable project |  |
| **code** | **String** | The code of the imputable project | [optional] |
| **start_date** | **String** | The start date of the imputable project | [optional] |
| **due_date** | **String** | The due date of the imputable project | [optional] |
| **status** | **String** | The status of the imputable project |  |
| **currency** | **String** | The currency of the imputable project |  |
| **client_id** | **String** |  | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementImputableProject.new(
  id: 314159,
  name: Destroy the death star,
  code: DS,
  start_date: 2025-01-01,
  due_date: 2025-01-01,
  status: active,
  currency: EUR,
  client_id: null
)
```

