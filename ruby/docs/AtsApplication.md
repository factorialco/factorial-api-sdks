# F::AtsApplication

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id of the application |  |
| **company_id** | **String** | Company id of the application |  |
| **ats_job_posting_id** | **String** | Job posting id of the application |  |
| **ats_candidate_id** | **String** | Candidate id of the application |  |
| **employee_id** | **String** | Employee id of the application | [optional] |
| **phone** | **String** | Candidate phone of the application | [optional] |
| **qualified** | **Boolean** | Qualified of the application | [optional] |
| **ats_application_phase_id** | **String** | Application phase id | [optional] |
| **created_at** | **String** | Application created at date |  |
| **cover_letter** | **String** | Application cover letter | [optional] |
| **cv** | **Object** | CV file attachment of the application (includes filename, url, byte_size, content_type, created_at) | [optional] |
| **ats_conversation_id** | **String** | Application conversation id | [optional] |
| **medium** | **String** | Application medium | [optional] |
| **rating_average** | **Integer** | Application average rating | [optional] |
| **ats_rejection_reason_id** | **String** | Application rejection reason id | [optional] |
| **source_id** | **String** | Application source id | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsApplication.new(
  id: 1,
  company_id: 1,
  ats_job_posting_id: 1,
  ats_candidate_id: 1,
  employee_id: 1,
  phone: 34612345678,
  qualified: true,
  ats_application_phase_id: 1,
  created_at: 2024-08-19T14:30:00.000Z,
  cover_letter: This is my cover letter for the position,
  cv: null,
  ats_conversation_id: 1,
  medium: medium,
  rating_average: 1,
  ats_rejection_reason_id: 1,
  source_id: 1
)
```

