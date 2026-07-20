# F::AtsApplicationsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **author_id** | **String** | Application author id | [optional] |
| **author_type** | **String** | Application author type | [optional] |
| **phone** | **String** | Application candidate phone | [optional] |
| **ats_candidate_id** | **String** | Application candidate id | [optional] |
| **ats_job_posting_id** | **String** | Application job posting id |  |
| **ats_application_phase_id** | **String** | Application phase id | [optional] |
| **consent_to_talent_pool** | **Boolean** | Whether or not the candidate has given consent to be added to the talent pool | [optional] |
| **cover_letter** | **String** | Application cover letter | [optional] |
| **source** | **String** | Application source | [optional] |
| **medium** | **String** | Application medium | [optional] |
| **answers** | **Array&lt;Object&gt;** | answers | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsApplicationsPostRequest.new(
  author_id: 1,
  author_type: company,
  phone: 34612345678,
  ats_candidate_id: 1,
  ats_job_posting_id: 1,
  ats_application_phase_id: 1,
  consent_to_talent_pool: true,
  cover_letter: This is my cover letter for the position,
  source: source,
  medium: medium,
  answers: null
)
```

