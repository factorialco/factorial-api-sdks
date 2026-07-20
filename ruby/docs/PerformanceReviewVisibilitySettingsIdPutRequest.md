# F::PerformanceReviewVisibilitySettingsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process ID | [optional] |
| **performance_review_process_id** | **String** | Review process ID | [optional] |
| **restrict_answers_visibility_to_reportees** | **Boolean** | When enabled, employees don&#39;t have access to their results |  |
| **early_access_to_answers_for_managers** | **Boolean** | When enabled, managers can access the results of their reports before deadline |  |
| **anonymous_peer_evaluation_for_target** | **Boolean** | When enabled, peer evaluations are anonymous so employees don&#39;t know who reviewed them |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewVisibilitySettingsIdPutRequest.new(
  id: 1,
  performance_review_process_id: 1,
  restrict_answers_visibility_to_reportees: false,
  early_access_to_answers_for_managers: true,
  anonymous_peer_evaluation_for_target: false
)
```

