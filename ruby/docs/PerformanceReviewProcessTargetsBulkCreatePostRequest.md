# F::PerformanceReviewProcessTargetsBulkCreatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **performance_review_process_id** | **String** | Review process ID |  |
| **targets_access_ids** | **Array&lt;String&gt;** | List of access IDs to be added as participants |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewProcessTargetsBulkCreatePostRequest.new(
  performance_review_process_id: 1,
  targets_access_ids: [&quot;1&quot;,&quot;2&quot;,&quot;3&quot;]
)
```

