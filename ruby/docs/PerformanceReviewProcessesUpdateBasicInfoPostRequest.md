# F::PerformanceReviewProcessesUpdateBasicInfoPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process ID |  |
| **name** | **String** | New name of the review process | [optional] |
| **description** | **String** | New description of the review process | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewProcessesUpdateBasicInfoPostRequest.new(
  id: 1,
  name: Performance Review - Q2 2024,
  description: The performance review for the first quarter of 2024 has started!
)
```

