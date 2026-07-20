# F::PerformanceReviewProcessesUpdateTargetStrategyPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process ID |  |
| **target_strategy** | **String** | Condition that defines the employees that will be evaluated (participants) | [optional] |
| **arguments** | **Array&lt;String&gt;** | IDs of target strategy groups selected | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewProcessesUpdateTargetStrategyPostRequest.new(
  id: 1,
  target_strategy: all_employees,
  arguments: null
)
```

