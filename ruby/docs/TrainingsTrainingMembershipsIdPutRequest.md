# F::TrainingsTrainingMembershipsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier for the training membership. Only used to identify the training membership to update. |  |
| **training_completed_at** | **String** | This field is used to record the date a training was completed for trainings that have an expiry date. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsTrainingMembershipsIdPutRequest.new(
  id: 1,
  training_completed_at: 2022-01-01
)
```

