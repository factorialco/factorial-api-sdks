# F::AtsAnswer

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the answer |  |
| **ats_question_id** | **String** | Identifier of the question | [optional] |
| **ats_application_id** | **String** | Identifier of the application |  |
| **original_question_label** | **String** | Question label of the answer |  |
| **value** | **String** | Value of the answer | [optional] |
| **original_question_type** | **String** | Original type of the question |  |
| **created_at** | **String** | Created date of the answer |  |
| **updated_at** | **String** | Last updated date of the answer |  |

## Example

```ruby
require 'factorial_api'

instance = F::AtsAnswer.new(
  id: 1,
  ats_question_id: 1,
  ats_application_id: 1,
  original_question_label: How was your application ranked?,
  value: One of the best I have ever seen,
  original_question_type: text,
  created_at: 2021-01-01T00:00:00.000Z,
  updated_at: 2021-01-01T00:00:00.000Z
)
```

