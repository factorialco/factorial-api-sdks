# F::AtsApplicationsApplyPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **company_id** | **String** | Company id of the application | [optional] |
| **first_name** | **String** | Application first name |  |
| **last_name** | **String** | Application last name |  |
| **ats_job_posting_id** | **String** | Application job posting id |  |
| **email** | **String** | Application candidate email |  |
| **phone** | **String** | Application candidate phone | [optional] |
| **source** | **String** | Application source | [optional] |
| **medium** | **String** | Application medium | [optional] |
| **cover_letter** | **String** | Application cover letter | [optional] |
| **gender** | **String** | gender of the candidate. | [optional] |
| **consent_to_talent_pool** | **Boolean** | Application consent talent pool | [optional] |
| **answers** | **Array&lt;Object&gt;** | answers | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsApplicationsApplyPostRequest.new(
  company_id: 1,
  first_name: Jane,
  last_name: Doe,
  ats_job_posting_id: 1,
  email: jane.doe@service.com,
  phone: 34612345678,
  source: source,
  medium: medium,
  cover_letter: This is my cover letter for the position,
  gender: female,
  consent_to_talent_pool: true,
  answers: null
)
```

