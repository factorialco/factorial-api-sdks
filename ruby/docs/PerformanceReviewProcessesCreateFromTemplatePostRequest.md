# F::PerformanceReviewProcessesCreateFromTemplatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **author_access_id** | **String** | Access ID to be set as author of the new review process |  |
| **template_id** | **String** | Review process template ID |  |
| **template_type** | **String** | Type of the template, custom or predefined |  |
| **name** | **String** | Name of the new review process | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceReviewProcessesCreateFromTemplatePostRequest.new(
  author_access_id: 1,
  template_id: 1,
  template_type: predefined,
  name: Performance Review - Q2 2024
)
```

