# F::AttendanceReviewsBulkCreatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_ids** | **Array&lt;String&gt;** | Employee identifiers to review |  |
| **start_on** | **String** | Start date of the reviews |  |
| **end_on** | **String** | End date of the reviews |  |
| **reviewed_by** | **String** | Reviewed by employee identifier |  |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceReviewsBulkCreatePostRequest.new(
  employee_ids: [&quot;1&quot;,&quot;2&quot;,&quot;3&quot;],
  start_on: 2025-02-01,
  end_on: 2025-02-28,
  reviewed_by: 1
)
```

