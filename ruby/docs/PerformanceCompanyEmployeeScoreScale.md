# F::PerformanceCompanyEmployeeScoreScale

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Company ID |  |
| **scale_id** | **String** | Employee score scale ID |  |
| **is_default** | **Boolean** | Default employee score scale |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceCompanyEmployeeScoreScale.new(
  id: 1,
  scale_id: 1,
  is_default: true
)
```

