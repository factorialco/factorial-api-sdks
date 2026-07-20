# F::PerformanceReviewQuestionnairesByStrategy

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process ID |  |
| **performance_review_process_id** | **String** | Review process ID |  |
| **default_rating_scale** | **Array&lt;Object&gt;** | Scoring range used in rating questions |  |
| **self_questionnaire** | **Object** | Questionnaire for self evaluation | [optional] |
| **manager_questionnaire** | **Object** | Questionnaire for manager evaluation | [optional] |
| **direct_report_questionnaire** | **Object** | Questionnaire for direct report evaluation | [optional] |
| **peers_questionnaire** | **Object** | Questionnaire for peers evaluation | [optional] |
| **employee_score_self_questionnaire** | **Object** | Questionnaire included in the end of self evaluation to evaluate the employee performance | [optional] |
| **employee_score_manager_questionnaire** | **Object** | Questionnaire included in the end of manager evaluation to evaluate the employee performance | [optional] |
| **employee_potential_score_manager_questionnaire** | **Object** | Questionnaire included in the end of manager evaluation to evaluate the employee potential | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewQuestionnairesByStrategy.new(
  id: 1,
  performance_review_process_id: 1,
  default_rating_scale: [{value&#x3D;1, text&#x3D;Poor}, {value&#x3D;2, text&#x3D;Inconsistent}, {value&#x3D;3, text&#x3D;Meets expectations}, {value&#x3D;4, text&#x3D;Exceeds expectations}, {value&#x3D;5, text&#x3D;Exceptional}],
  self_questionnaire: {reviewer_strategy&#x3D;self, content&#x3D;[{uuid&#x3D;26f26623-043f-4110-a5cb-1fd54a69626f, type&#x3D;question, questions&#x3D;[{uuid&#x3D;84ba99f3-4e4f-4917-a2af-6d0aa8c2e0f2, mandatory&#x3D;true, with_comment&#x3D;false, title&#x3D;Do you think you are a team player?, answer_type&#x3D;single_choice, choice_options&#x3D;[Yes, No]}]}]},
  manager_questionnaire: {reviewer_strategy&#x3D;manager, content&#x3D;[{uuid&#x3D;b69c9b4d-0aa6-4ada-89d5-5fdcb04c1327, type&#x3D;section, section_title&#x3D;Performance, questions&#x3D;[{uuid&#x3D;a347a2fd-1a0a-4eee-b6c8-f74be63624fb, mandatory&#x3D;true, with_comment&#x3D;true, title&#x3D;How would you rate the commitment of the employee?, answer_type&#x3D;rating}]}]},
  direct_report_questionnaire: null,
  peers_questionnaire: null,
  employee_score_self_questionnaire: null,
  employee_score_manager_questionnaire: null,
  employee_potential_score_manager_questionnaire: null
)
```

