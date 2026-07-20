# F::PerformanceReviewEvaluationsReplaceReviewerPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Evaluation ID |  |
| **new_reviewer_access_id** | **String** | New reviewer access ID |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewEvaluationsReplaceReviewerPostRequest.new(
  id: 1,
  new_reviewer_access_id: 5
)
```

