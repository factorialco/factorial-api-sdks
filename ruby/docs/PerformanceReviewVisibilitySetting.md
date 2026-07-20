# F::PerformanceReviewVisibilitySetting

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process ID |  |
| **performance_review_process_id** | **String** | Review process ID |  |
| **restrict_answers_visibility_to_reportees** | **Boolean** | Employees don&#39;t have access to their results when enabled |  |
| **early_access_to_answers_for_managers** | **Boolean** | Managers can access the results of their reports before deadline when enabled |  |
| **anonymous_peer_evaluation_for_target** | **Boolean** | Peer evaluations are anonymous when enabled, so employees don&#39;t know who reviewed them |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewVisibilitySetting.new(
  id: 1,
  performance_review_process_id: 1,
  restrict_answers_visibility_to_reportees: false,
  early_access_to_answers_for_managers: true,
  anonymous_peer_evaluation_for_target: false
)
```

