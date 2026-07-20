# F::AtsAnswersPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_question_id** | **String** | Identifier of the question |  |
| **ats_application_id** | **String** | Identifier of the application |  |
| **value** | **String** | Value of the answer |  |
| **original_question_label** | **String** | Label of the question |  |
| **original_question_type** | **String** | Type of the question |  |

## Example

```ruby
require 'factorial_api'

instance = F::AtsAnswersPostRequest.new(
  ats_question_id: 1,
  ats_application_id: 1,
  value: One of the best I have ever seen,
  original_question_label: How was your application ranked?,
  original_question_type: text
)
```

