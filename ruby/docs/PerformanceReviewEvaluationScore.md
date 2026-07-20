# F::PerformanceReviewEvaluationScore

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review evaluation score ID |  |
| **review_process_id** | **String** | Review process ID |  |
| **review_evaluation_id** | **String** | Review evaluation ID |  |
| **target_access_id** | **String** | Employee access ID |  |
| **company_id** | **String** | Company identifier of the review evaluation score |  |
| **reviewer_strategy** | **String** | Who scored the employee |  |
| **review_process_target_id** | **String** | Review process target ID (composed with review_process_id and target_access_id) |  |
| **potential_score** | **Integer** | Employee evaluation potential score within the min and max scale | [optional] |
| **normalized_potential_score** | **Float** | Employee evaluation potential score in percentage (0% to 100%) | [optional] |
| **score** | **Float** | Evaluation score within the min and max scale |  |
| **scale_min** | **Integer** | Minimum score in the scale |  |
| **scale_max** | **Integer** | Maximum score in the scale |  |
| **normalized_score** | **Float** | Evaluation score in percentage (0% to 100%) |  |
| **published_at** | **String** | Date and time when the evaluation score was published |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewEvaluationScore.new(
  id: 1,
  review_process_id: 1,
  review_evaluation_id: 1,
  target_access_id: 1,
  company_id: 1,
  reviewer_strategy: manager,
  review_process_target_id: 1-1,
  potential_score: 3,
  normalized_potential_score: 50.0,
  score: 3.0,
  scale_min: 1,
  scale_max: 5,
  normalized_score: 50.0,
  published_at: 2024-01-01T00:00:00.000+00:00
)
```

