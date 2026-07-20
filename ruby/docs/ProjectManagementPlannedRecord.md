# F::ProjectManagementPlannedRecord

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the planned record |  |
| **daily_minutes** | **Integer** | The daily minutes of the planned record |  |
| **start_date** | **String** | The start date of the planned record |  |
| **end_date** | **String** | The end date of the planned record |  |
| **project_worker_id** | **String** | The project worker id of the planned record |  |
| **subproject_id** | **String** | The subproject id of the planned record | [optional] |
| **week_days** | **Array&lt;Integer&gt;** | The week days of the planned record, start in Sunday 0 and end in Saturday 6 |  |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementPlannedRecord.new(
  id: 314159,
  daily_minutes: 100,
  start_date: 2025-01-01,
  end_date: 2025-01-03,
  project_worker_id: 314159,
  subproject_id: 314159,
  week_days: [1, 2, 3, 4, 5]
)
```

