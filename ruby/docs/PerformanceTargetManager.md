# F::PerformanceTargetManager

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Manager employee ID |  |
| **performance_review_process_id** | **String** | Review process ID |  |
| **manager_access_id** | **String** | Manager access ID |  |
| **manager_full_name** | **String** | Manager full name |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceTargetManager.new(
  id: 1,
  performance_review_process_id: 1,
  manager_access_id: 3,
  manager_full_name: John Doe
)
```

