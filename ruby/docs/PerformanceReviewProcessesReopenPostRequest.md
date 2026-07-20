# F::PerformanceReviewProcessesReopenPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process ID |  |
| **ends_at** | **String** | New deadline of the review process |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewProcessesReopenPostRequest.new(
  id: 1,
  ends_at: 2024-04-01T00:00:00Z
)
```

