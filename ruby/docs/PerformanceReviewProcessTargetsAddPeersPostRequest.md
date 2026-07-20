# F::PerformanceReviewProcessTargetsAddPeersPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process target ID |  |
| **peer_access_ids** | **Array&lt;String&gt;** | List of access IDs to be added as peers for the participant |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewProcessTargetsAddPeersPostRequest.new(
  id: 1-3,
  peer_access_ids: [&quot;1&quot;,&quot;2&quot;,&quot;3&quot;]
)
```

