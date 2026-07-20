# F::AtsQuestionsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_job_posting_id** | **String** | job posting identifier. |  |
| **company_id** | **String** | company identifier, refers to /core/me endpoint. |  |
| **label** | **String** | text of the question. |  |
| **position** | **Integer** | position of the question in the list. |  |
| **mandatory** | **Boolean** | is the question mandatory or not | [optional] |
| **question_type** | **String** | type of the question. |  |
| **auto_disqualify** | **Boolean** | if the question autodisqualifies the candidate depending on it&#39;s response. | [optional] |
| **options** | **Array&lt;Object&gt;** | options for the question. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsQuestionsPostRequest.new(
  ats_job_posting_id: 1,
  company_id: 1,
  label: Are you open to relocate?,
  position: 1,
  mandatory: true,
  question_type: text,
  auto_disqualify: false,
  options: [{text&#x3D;Yes, disqualifies&#x3D;false}, {text&#x3D;No, disqualifies&#x3D;false}]
)
```

