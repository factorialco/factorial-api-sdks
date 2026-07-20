# F::ProjectManagementSubprojectsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the subproject. |  |
| **name** | **String** | The name of the subproject. | [optional] |
| **description** | **String** | The description of the subproject. | [optional] |
| **status** | **String** | The status of the subproject. | [optional] |
| **code** | **String** | The code of the subproject. | [optional] |
| **start_date** | **String** | The start date of the subproject. | [optional] |
| **due_date** | **String** | The due date of the subproject. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementSubprojectsIdPutRequest.new(
  id: 314,
  name: Subproject name,
  description: Subproject description,
  status: active,
  code: SUB123,
  start_date: 2025-01-01,
  due_date: 2025-01-01
)
```

