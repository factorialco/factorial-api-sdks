# F::PerformanceReviewEvaluation

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Evaluation ID |  |
| **performance_review_process_id** | **String** | Review process ID | [optional] |
| **target_access_id** | **String** | Participant access ID | [optional] |
| **reviewer_access_id** | **String** | Reviewer access ID | [optional] |
| **evaluation_type** | **String** | Evaluation type |  |
| **published** | **Boolean** | Whether the evaluation is published |  |
| **status** | **String** | Evaluation status |  |
| **review_process_target_id** | **String** |  |  |
| **published_at** | **String** | Date when the evaluation was published | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewEvaluation.new(
  id: 1,
  performance_review_process_id: 1,
  target_access_id: 1,
  reviewer_access_id: 1,
  evaluation_type: manager,
  published: true,
  status: published,
  review_process_target_id: null,
  published_at: 2024-01-01T00:00:00Z
)
```

