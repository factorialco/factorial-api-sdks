# F::ProjectManagementFlexibleTimeRecord

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The unique identifier of the flexible time record. |  |
| **date** | **String** | The date on which the time was imputed. |  |
| **imputed_minutes** | **Integer** | The amount of time imputed to the project, in minutes. |  |
| **project_worker_id** | **String** | The ID of the project worker associated with this flexible time record. |  |
| **subproject_id** | **String** | The ID of the subproject worked on, if any. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementFlexibleTimeRecord.new(
  id: 1,
  date: 2025-01-15,
  imputed_minutes: 120,
  project_worker_id: 42,
  subproject_id: 7
)
```

