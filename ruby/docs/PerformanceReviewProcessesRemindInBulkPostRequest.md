# F::PerformanceReviewProcessesRemindInBulkPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process ID |  |
| **evaluation_types** | **Array&lt;String&gt;** | Reviewer strategies to remind about | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewProcessesRemindInBulkPostRequest.new(
  id: 1,
  evaluation_types: [&quot;self&quot;,&quot;manager&quot;]
)
```

