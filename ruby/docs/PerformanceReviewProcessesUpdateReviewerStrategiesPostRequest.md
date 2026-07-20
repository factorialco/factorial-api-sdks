# F::PerformanceReviewProcessesUpdateReviewerStrategiesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process ID |  |
| **reviewer_strategies** | **Array&lt;String&gt;** | New review types to be applied |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewProcessesUpdateReviewerStrategiesPostRequest.new(
  id: 1,
  reviewer_strategies: [&quot;self&quot;,&quot;manager&quot;]
)
```

