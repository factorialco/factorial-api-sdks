# F::AtsFeedbacksPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_candidate_id** | **String** | the ID of the candidate to whom the new feedback will be associated. |  |
| **rating** | **Integer** | the overall rating from 1 to 5 to be given to the candidate&#39;s application. | [optional] |
| **ats_application_id** | **String** | the ID of the application related to the feedback. | [optional] |
| **ats_application_phase_id** | **String** | the ID of the phase within the application related to the feedback. | [optional] |
| **description** | **String** | a string describing the feedback provided. | [optional] |
| **mention_ids** | **Array&lt;String&gt;** | the IDs of the accesses for sending notifications if they have it enabled. They must have permissions to see the assosiated application. | [optional] |
| **ats_evaluation_forms_id** | **String** | IDs of the form to which the feedback belongs if the evaluation forms feature is active. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsFeedbacksPostRequest.new(
  ats_candidate_id: 1,
  rating: 4,
  ats_application_id: 1,
  ats_application_phase_id: 1,
  description: The candidate has a great attitude and is a good fit for the team.,
  mention_ids: [&quot;1&quot;,&quot;2&quot;,&quot;3&quot;],
  ats_evaluation_forms_id: [1, 2, 3]
)
```

