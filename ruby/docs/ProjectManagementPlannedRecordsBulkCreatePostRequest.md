# F::ProjectManagementPlannedRecordsBulkCreatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_worker_ids** | **Array&lt;String&gt;** | The project worker ids to create the planned records for |  |
| **start_date** | **String** | The start date to create the planned records for |  |
| **end_date** | **String** | The end date to create the planned records for |  |
| **daily_minutes** | **Integer** | The daily minutes to create the planned records for |  |
| **subproject_id** | **String** | The subproject id to create the planned records for | [optional] |
| **week_days** | **Array&lt;Integer&gt;** | The week days to create the planned records for, start in Sunday 0 and end in Saturday 6 | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementPlannedRecordsBulkCreatePostRequest.new(
  project_worker_ids: [&quot;314159&quot;],
  start_date: 2025-01-01,
  end_date: 2025-01-03,
  daily_minutes: 100,
  subproject_id: 314159,
  week_days: [1,2,3,4,5]
)
```

