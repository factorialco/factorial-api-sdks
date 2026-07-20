# F::AtsCandidate

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the candidate. |  |
| **company_id** | **String** | company identifier. | [optional] |
| **first_name** | **String** | name of the candidate. |  |
| **last_name** | **String** | last name of the candidate. |  |
| **full_name** | **String** | full name of the candidate. |  |
| **email** | **String** | email of the candidate. | [optional] |
| **talent_pool** | **Boolean** | is the candidate part of talent pool? |  |
| **phone_number** | **String** | phone number of the candidate. | [optional] |
| **created_at** | **String** | creation date of the candidate. |  |
| **updated_at** | **String** | last update of the candidate. |  |
| **consent_given_at** | **String** | date when the consent was given. | [optional] |
| **inactive_since** | **String** | date when the candidate became inactive. | [optional] |
| **ats_job_posting_ids** | **Array&lt;String&gt;** | list of job posting identifiers. | [optional] |
| **personal_url** | **String** | personal web resource from the candidate. | [optional] |
| **consent_expiration_date** | **String** | date when the consent expires. | [optional] |
| **consent_to_talent_pool** | **Boolean** | consent to talent pool. | [optional] |
| **medium** | **String** | specifies additional details related to the source of the candidate, such as the referrer name for example if the source is referred. | [optional] |
| **source_id** | **String** | candidate source identifier, refers to ats/candidate_sources endpoint. | [optional] |
| **gender** | **String** | gender of the candidate. | [optional] |
| **score** | **Float** | score of the candidate. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsCandidate.new(
  id: 1,
  company_id: 1,
  first_name: Ana,
  last_name: Fernandez Perez,
  full_name: Ana Fernandez Perez,
  email: ana@factorial.com,
  talent_pool: true,
  phone_number: 645786980,
  created_at: 2021-01-01T00:00:00Z,
  updated_at: 2021-01-01T00:00:00Z,
  consent_given_at: 2021-01-01T00:00:00Z,
  inactive_since: 2021-01-01T00:00:00Z,
  ats_job_posting_ids: [1, 2, 3],
  personal_url: https://anaperez.factorial.com,
  consent_expiration_date: 2021-01-01T00:00:00Z,
  consent_to_talent_pool: true,
  medium: email,
  source_id: 1,
  gender: female,
  score: 7
)
```

