# F::PerformanceReviewProcessesSchedulePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process ID |  |
| **starts_at** | **String** | Date when the review process should start |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewProcessesSchedulePostRequest.new(
  id: 1,
  starts_at: 2024-01-01T00:00:00Z
)
```

