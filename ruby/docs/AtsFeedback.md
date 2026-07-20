# F::AtsFeedback

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | the ID of the feedback entry. |  |
| **rating** | **Integer** | the overall rating from 1 to 5 for the candidate&#39;s application. | [optional] |
| **description** | **String** | the description of the feedback provided. | [optional] |
| **ats_application_id** | **String** | the ID of the application related to the feedback. | [optional] |
| **ats_application_phase_id** | **String** | the ID of the phase within the application related to the feedback. | [optional] |
| **created_at** | **String** | the date and time when the feedback entry was created. |  |
| **ats_candidate_id** | **String** | the ID of the candidate to whom the feedback is associated. |  |
| **ats_evaluation_forms_id** | **String** | the ID of the evaluation form to which the feedback belongs if the evaluation forms feature is active. | [optional] |
| **evaluation_form_answers** | **Array&lt;Object&gt;** | the answers from the evaluation form, if this feedback is related to an evaluation form. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsFeedback.new(
  id: 1,
  rating: 4,
  description: The candidate has a great attitude and is a good fit for the team.,
  ats_application_id: 1,
  ats_application_phase_id: 1,
  created_at: 2022-01-01T00:00:00Z,
  ats_candidate_id: 1,
  ats_evaluation_forms_id: 1,
  evaluation_form_answers: [{id&#x3D;1, score&#x3D;3, note&#x3D;Good communication skills.}]
)
```

