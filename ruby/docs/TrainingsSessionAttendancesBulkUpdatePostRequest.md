# F::TrainingsSessionAttendancesBulkUpdatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | **Array&lt;String&gt;** | List of session attendance IDs to update |  |
| **status** | **String** | New status for the session attendances | [optional] |
| **completed_duration** | **String** | Completed duration in hours (decimal format, e.g. 1.5 means 1h 30m) | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsSessionAttendancesBulkUpdatePostRequest.new(
  ids: [&quot;1&quot;],
  status: completed,
  completed_duration: 1.5
)
```

