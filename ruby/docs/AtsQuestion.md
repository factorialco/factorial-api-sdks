# F::AtsQuestion

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | question identifier |  |
| **ats_job_posting_id** | **String** | job posting identifier. |  |
| **label** | **String** | text of the question. |  |
| **position** | **Integer** | position of the question in the list. |  |
| **mandatory** | **Boolean** | is the question mandatory or not |  |
| **auto_disqualify** | **Boolean** | if the question autodisqualifies the candidate depending on it&#39;s response. |  |
| **question_type** | **String** | type of the question. |  |
| **created_at** | **String** | creation date |  |
| **updated_at** | **String** | last update date |  |
| **options** | **Array&lt;Object&gt;** | options for the question. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsQuestion.new(
  id: 1,
  ats_job_posting_id: 1,
  label: Are you open to relocate?,
  position: 1,
  mandatory: true,
  auto_disqualify: false,
  question_type: text,
  created_at: 2025-01-01T00:00:00.000Z,
  updated_at: 2025-01-01T00:00:00.000Z,
  options: [{text&#x3D;Yes, disqualifies&#x3D;false}, {text&#x3D;No, disqualifies&#x3D;false}]
)
```

