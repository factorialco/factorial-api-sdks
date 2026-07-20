# F::TrainingsTrainingMembershipsBulkCreatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_ids** | **Array&lt;String&gt;** | ids for the accesses to be assigned in a training |  |
| **training_id** | **String** | Training id to be assigned |  |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsTrainingMembershipsBulkCreatePostRequest.new(
  employee_ids: [&quot;20&quot;],
  training_id: 1
)
```

