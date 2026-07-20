# F::PerformanceReviewOwnersBulkCreatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **review_process_id** | **String** | Review process ID |  |
| **owner_access_ids** | **Array&lt;String&gt;** | List of access IDs to be added as owners |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewOwnersBulkCreatePostRequest.new(
  review_process_id: 1,
  owner_access_ids: [&quot;1&quot;,&quot;2&quot;,&quot;3&quot;]
)
```

