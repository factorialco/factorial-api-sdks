# F::PerformanceReviewProcess

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process ID |  |
| **company_id** | **String** | Company ID |  |
| **name** | **String** | Review process name | [optional] |
| **description** | **String** | A brief description of the review process | [optional] |
| **status** | **String** | Review process status |  |
| **target_strategy** | **Object** | Condition that defines the employees that will be evaluated (participants). Calculated when the review process starts | [optional] |
| **reviewer_strategies** | **Array&lt;String&gt;** | Review types that will be assigned to the review process. It&#39;ll be used to create the evaluations when the process starts | [optional] |
| **starts_at** | **String** | Date when the review process should start | [optional] |
| **ends_at** | **String** | Date when the review process should end | [optional] |
| **start_validation_errors** | **Array&lt;String&gt;** | Missing or invalid information to be able to start the review process |  |
| **archived** | **Boolean** | Whether the review process is archived or not |  |
| **agreements_configuration** | **Object** | Action plans help track goal progress, and facilitate performance review discussions. |  |
| **competencies_assessments_configuration** | **Object** | Assess employees based on their assigned competencies through both manager and self-reviews. Ensure roles with designated competencies are properly set up. |  |
| **last_bulk_reminder** | **String** | Date when the last bulk reminder was sent | [optional] |
| **cycle_id** | **String** | Performance cycle ID | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewProcess.new(
  id: 1,
  company_id: 1,
  name: Performance Review - Q1 2024,
  description: The performance review for the first quarter of 2024 has started!,
  status: draft,
  target_strategy: {arguments&#x3D;[], strategy&#x3D;all_employees},
  reviewer_strategies: [self, manager],
  starts_at: 2024-01-01T00:00:00.000Z,
  ends_at: 2024-04-01T00:00:00.000Z,
  start_validation_errors: [invalid_deadline, missing_target_strategy_members],
  archived: false,
  agreements_configuration: {enabled&#x3D;true},
  competencies_assessments_configuration: {enabled&#x3D;false},
  last_bulk_reminder: 2024-03-01T00:00:00.000Z,
  cycle_id: 5
)
```

