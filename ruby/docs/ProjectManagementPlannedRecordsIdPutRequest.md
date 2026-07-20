# F::ProjectManagementPlannedRecordsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the planned record to update |  |
| **start_date** | **String** | The start date to update the planned record for |  |
| **end_date** | **String** | The end date to update the planned record for |  |
| **daily_minutes** | **Integer** | The daily minutes to update the planned record for |  |
| **project_worker_id** | **String** | The project worker id to update the planned record for | [optional] |
| **week_days** | **Array&lt;Integer&gt;** | The week days to update the planned record for, start in Sunday 0 and end in Saturday 6 | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementPlannedRecordsIdPutRequest.new(
  id: 314159,
  start_date: 2025-01-01,
  end_date: 2025-01-03,
  daily_minutes: 100,
  project_worker_id: 314159,
  week_days: [1,2,3,4,5]
)
```

