# F::TrainingsTrainingMembershipsBulkDestroyPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | **Array&lt;String&gt;** | IDs of training memberships to delete. When &#39;all&#39; is true, these IDs are excluded from deletion. |  |
| **training_id** | **String** | Training ID. Required when &#39;all&#39; is true to identify which training&#39;s memberships to delete. | [optional] |
| **all** | **Boolean** | When true, deletes all memberships for the given training_id, excluding those in the &#39;ids&#39; array. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsTrainingMembershipsBulkDestroyPostRequest.new(
  ids: [&quot;1&quot;,&quot;2&quot;],
  training_id: 1,
  all: false
)
```

