# F::PerformanceReviewProcessCustomTemplate

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process template ID |  |
| **author_id** | **String** | Author of the custom template. | [optional] |
| **company_id** | **String** | Company ID |  |
| **name** | **String** | Review process name |  |
| **description** | **String** | A brief description of the review process | [optional] |
| **template_description** | **String** | A brief description of the review process template | [optional] |
| **target_strategy** | **Object** | Condition that defines the employees that will be evaluated (participants). Calculated when the review process starts | [optional] |
| **reviewer_strategies** | **Array&lt;String&gt;** | Review types that will be assigned to the review process. It&#39;ll be used to create the evaluations when the process starts | [optional] |
| **agreements_enabled** | **Boolean** | Action plans help track goal progress, and facilitate performance review discussions. | [optional] |
| **employee_potential_score_enabled** | **Boolean** | Include one question at the end of the review to rate participants&#39; potential. This rating will be reflected in the 9 box grid. | [optional] |
| **competencies_assessments_enabled** | **Boolean** | Assess employees based on their assigned competencies through both manager and self-reviews. Ensure roles with designated competencies are properly set up. | [optional] |
| **visibility_settings** | **Object** | Visibility settings for the custom template | [optional] |
| **created_at** | **String** | Creation date of the template |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewProcessCustomTemplate.new(
  id: 1,
  author_id: 1,
  company_id: 1,
  name: Performance Review - Q1 2024,
  description: Quarterly 360 review process,
  template_description: This template evaluates the performance of employees,
  target_strategy: {arguments&#x3D;[], strategy&#x3D;all_employees},
  reviewer_strategies: [self, manager],
  agreements_enabled: true,
  employee_potential_score_enabled: true,
  competencies_assessments_enabled: false,
  visibility_settings: {early_access_to_answers_for_managers&#x3D;true, restrict_answers_visibility_to_reportees&#x3D;false, anonymous_peer_evaluation_for_target&#x3D;false},
  created_at: 2025-01-01T00:00:00.000Z
)
```

