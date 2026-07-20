# F::PerformanceEmployeeScoreScale

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Employee score scale ID |  |
| **scale** | **Array&lt;Object&gt;** | Scale to be used when scoring the employee performance |  |
| **is_default** | **Boolean** |  |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceEmployeeScoreScale.new(
  id: 1,
  scale: [{value&#x3D;1, text&#x3D;Unsatisfactory}, {value&#x3D;2, text&#x3D;Missed expectations}, {value&#x3D;3, text&#x3D;Meets expectations}, {value&#x3D;4, text&#x3D;Exceeds expectations}, {value&#x3D;5, text&#x3D;Outstanding}],
  is_default: null
)
```

