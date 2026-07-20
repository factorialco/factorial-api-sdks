# F::AtsEvaluationForm

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id of the evaluation form. |  |
| **company_id** | **String** | Id of the company that the evaluation form belongs to. |  |
| **ats_job_posting_id** | **String** | Id of the job posting that the evaluation form is associated with. | [optional] |
| **name** | **String** | Name of the evaluation form. |  |
| **based_on_id** | **String** | Id of the evaluation form that this evaluation form is related. | [optional] |
| **questions** | **Array&lt;Object&gt;** | List of questions in the evaluation form. |  |
| **created_at** | **String** | date and time when the evaluation form was created. |  |
| **updated_at** | **String** | date and time when the evaluation form was last updated. |  |

## Example

```ruby
require 'factorial_api'

instance = F::AtsEvaluationForm.new(
  id: 1,
  company_id: 1,
  ats_job_posting_id: 1,
  name: Technical Evaluation,
  based_on_id: 1,
  questions: [{id&#x3D;1, text&#x3D;What is your experience with Ruby on Rails?, description&#x3D;experience in years}],
  created_at: 2021-01-01T00:00:00Z,
  updated_at: 2021-01-01T00:00:00Z
)
```

