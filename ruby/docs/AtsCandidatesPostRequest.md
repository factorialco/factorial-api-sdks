# F::AtsCandidatesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **first_name** | **String** | first name of the candidate. |  |
| **last_name** | **String** | last name of the candidate. |  |
| **email** | **String** | email of the candidate. | [optional] |
| **company_id** | **String** | company identifier, refers to /core/me endpoint. |  |
| **talent_pool** | **Boolean** | is the candidate part of talent pool? | [optional] |
| **consent_given_at** | **String** | date when the consent was given. | [optional] |
| **source** | **String** | source of the candidate. | [optional] |
| **medium** | **String** | specifies additional details related to the source of the candidate, such as the referrer name for example if the source is referred. | [optional] |
| **phone_number** | **String** | phone number of the candidate. | [optional] |
| **personal_url** | **String** | personal web resource from the candidate. | [optional] |
| **gender** | **String** | gender of the candidate. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsCandidatesPostRequest.new(
  first_name: Ana,
  last_name: Fernandez Perez,
  email: ana@factorial.com,
  company_id: 1,
  talent_pool: true,
  consent_given_at: 2021-01-01T00:00:00Z,
  source: referred,
  medium: email,
  phone_number: 645786980,
  personal_url: https://anaperez.factorial.com,
  gender: female
)
```

