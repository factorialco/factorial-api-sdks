# F::AttendanceReviewsBulkDestroyPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_ids** | **Array&lt;String&gt;** | Employee identifiers |  |
| **start_on** | **String** | Start date of the reviews to delete |  |
| **end_on** | **String** | End date of the reviews to delete |  |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceReviewsBulkDestroyPostRequest.new(
  employee_ids: [1, 2, 3],
  start_on: 2025-01-01,
  end_on: 2025-01-02
)
```

