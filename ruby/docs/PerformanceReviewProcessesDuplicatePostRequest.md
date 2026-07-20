# F::PerformanceReviewProcessesDuplicatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Review process ID to duplicate |  |
| **author_access_id** | **String** | Access ID to be set as author of the new review process |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewProcessesDuplicatePostRequest.new(
  id: 1,
  author_access_id: 1
)
```

