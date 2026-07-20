# F::AttendanceReview

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **employee_id** | **String** | Employee identifier |  |
| **date** | **String** | Date reviewed |  |
| **reviewed_at** | **String** | Reviewed at (ISO 8601 format string) |  |
| **author_id** | **String** | Author of the review |  |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceReview.new(
  id: null,
  employee_id: 1,
  date: 2025-01-01,
  reviewed_at: 2025-01-02T00:00:00Z,
  author_id: 1
)
```

