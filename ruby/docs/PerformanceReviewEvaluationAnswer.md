# F::PerformanceReviewEvaluationAnswer

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review evaluation ID |  |
| **performance_review_evaluation_id** | **String** | Review evaluation ID |  |
| **answered_questionnaire_with_sections** | **Object** | List of questions and their respective answers grouped by section. |  |
| **answered_employee_score_questionnaire** | **Object** | Questionnaire for getting employee score. | [optional] |
| **answered_employee_potential_score_questionnaire** | **Object** | Questionnaire for getting the employee potential score. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewEvaluationAnswer.new(
  id: 1,
  performance_review_evaluation_id: 1,
  answered_questionnaire_with_sections: {content&#x3D;[{uuid&#x3D;b69c9b4d-0aa6-4ada-89d5-5fdcb04c1327, type&#x3D;section, section_title&#x3D;Performance, questions&#x3D;[{question&#x3D;{uuid&#x3D;84ba99f3-4e4f-4917-a2af-6d0aa8c2e0f2, mandatory&#x3D;true, with_comment&#x3D;false, title&#x3D;Do you think the employee is a team player?, answer_type&#x3D;multiple_choice, max_choices&#x3D;1, choice_options&#x3D;[Yes, No]}, answer&#x3D;{uuid&#x3D;84ba99f3-4e4f-4917-a2af-6d0aa8c2e0f2, answer_text&#x3D;Example answer, answer_int&#x3D;10, answer_float&#x3D;10.5, answer_choice&#x3D;[Yes], answer_rating&#x3D;{value&#x3D;3, comment&#x3D;The employee is doing well.}}}, {question&#x3D;{uuid&#x3D;a347a2fd-1a0a-4eee-b6c8-f74be63624fb, mandatory&#x3D;true, with_comment&#x3D;true, title&#x3D;How would you rate the commitment of the employee?, answer_type&#x3D;rating}, answer&#x3D;{uuid&#x3D;a347a2fd-1a0a-4eee-b6c8-f74be63624fb, answer_text&#x3D;Example answer, answer_int&#x3D;10, answer_float&#x3D;10.5, answer_choice&#x3D;[Yes], answer_rating&#x3D;{value&#x3D;3, comment&#x3D;The employee is doing well.}}}]}]},
  answered_employee_score_questionnaire: {content&#x3D;[{uuid&#x3D;b69c9b4d-0aa6-4ada-89d5-5fdcb04c1327, type&#x3D;section, section_title&#x3D;Overall performance, questions&#x3D;[{question&#x3D;{uuid&#x3D;a347a2fd-1a0a-4eee-b6c8-f74be63624fb, mandatory&#x3D;true, with_comment&#x3D;true, title&#x3D;How would you rate the evarall performance of the employee?, answer_type&#x3D;rating, scale&#x3D;[{value&#x3D;1, text&#x3D;Unsatisfactory}, {value&#x3D;2, text&#x3D;Needs Improvement}, {value&#x3D;3, text&#x3D;Meets Expectations}, {value&#x3D;4, text&#x3D;Exceeds Expectations}, {value&#x3D;5, text&#x3D;Outstanding}]}, answer&#x3D;{uuid&#x3D;a347a2fd-1a0a-4eee-b6c8-f74be63625fb, answer_text&#x3D;Example answer, answer_int&#x3D;10, answer_float&#x3D;10.5, answer_choice&#x3D;[Yes], answer_rating&#x3D;{value&#x3D;3, comment&#x3D;The employee is doing well.}}}]}]},
  answered_employee_potential_score_questionnaire: null
)
```

