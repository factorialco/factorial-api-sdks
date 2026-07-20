# F::PerformanceReviewOwner

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review owner ID |  |
| **access_id** | **String** | Review owner access ID |  |
| **performance_review_process_id** | **String** | Review process ID |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewOwner.new(
  id: 1,
  access_id: 2,
  performance_review_process_id: 1
)
```

