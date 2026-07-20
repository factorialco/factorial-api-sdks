# F::PerformanceReviewProcessTarget

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process target ID (composed with performance_review_process_id and access_id) |  |
| **access_id** | **String** | Participant access ID |  |
| **performance_review_process_id** | **String** | Review process ID |  |
| **materialized_process_target_id** | **String** | Materialized review process target ID |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewProcessTarget.new(
  id: 1-3,
  access_id: 3,
  performance_review_process_id: 1,
  materialized_process_target_id: 5
)
```

