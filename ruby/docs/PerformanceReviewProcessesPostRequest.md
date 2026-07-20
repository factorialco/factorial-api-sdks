# F::PerformanceReviewProcessesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **author_access_id** | **String** | Access identifier of the author of the review process |  |
| **name** | **String** | Name of the review process | [optional] |
| **description** | **String** | A brief description of the review process | [optional] |
| **reviewer_strategies** | **Array&lt;String&gt;** | Review types that will be assigned to the review process. It&#39;ll be used to create the evaluations when the process starts | [optional] |
| **target_strategy** | **String** | Condition that defines the employees that will be evaluated (participants). Calculated when the review process starts | [optional] |
| **arguments** | **Array&lt;String&gt;** | IDs of target strategy groups selected | [optional] |
| **ends_at** | **String** | Date when the review process should end | [optional] |
| **agreements_enabled** | **Boolean** | Action plans help track goal progress, and facilitate performance review discussions. | [optional] |
| **employee_score_enabled** | **Boolean** | Include one question at the end of the review to rate participants&#39; performance. This rating will be reflected on the results page. | [optional] |
| **employee_potential_score_enabled** | **Boolean** | Include one question at the end of the review to rate participants&#39; potential. This rating will be reflected in the 9 box grid. | [optional] |
| **competencies_assessments_enabled** | **Boolean** | Assess employees based on their assigned competencies through both manager and self-reviews. Ensure roles with designated competencies are properly set up. | [optional] |
| **cycle_id** | **String** | Performance cycle ID | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewProcessesPostRequest.new(
  author_access_id: 1,
  name: Performance Review - Q1 2024,
  description: The performance review for the first quarter of 2024 has started!,
  reviewer_strategies: [self, manager],
  target_strategy: all_employees,
  arguments: null,
  ends_at: 2024-04-01T00:00:00Z,
  agreements_enabled: true,
  employee_score_enabled: true,
  employee_potential_score_enabled: true,
  competencies_assessments_enabled: true,
  cycle_id: 5
)
```

