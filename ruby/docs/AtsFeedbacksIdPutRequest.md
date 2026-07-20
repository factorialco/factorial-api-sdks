# F::AtsFeedbacksIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | the ID of the feedback entry to be updated. | [optional] |
| **rating** | **Integer** | the overall rating from 1 to 5 for the candidate&#39;s application. | [optional] |
| **description** | **String** | the description of the feedback provided. | [optional] |
| **ats_application_phase_id** | **String** | the ID of the phase within the application related to the feedback. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsFeedbacksIdPutRequest.new(
  id: 1,
  rating: 5,
  description: The candidate has a great attitude and is a good fit for the team.,
  ats_application_phase_id: 1
)
```

