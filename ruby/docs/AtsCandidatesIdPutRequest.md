# F::AtsCandidatesIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the candidate. |  |
| **email** | **String** | email of the candidate. | [optional] |
| **first_name** | **String** | first name of the candidate. | [optional] |
| **last_name** | **String** | last name of the candidate. | [optional] |
| **talent_pool** | **Boolean** | is the candidate part of talent pool? | [optional] |
| **consent_given_at** | **String** | date when the consent was given. | [optional] |
| **phone_number** | **String** | phone number of the candidate. | [optional] |
| **personal_url** | **String** | personal web resource from the candidate. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsCandidatesIdPutRequest.new(
  id: 1,
  email: ana@factorial.com,
  first_name: Ana,
  last_name: Fernandez Perez,
  talent_pool: true,
  consent_given_at: 2021-01-01T00:00:00Z,
  phone_number: 645786980,
  personal_url: https://anaperez.factorial.com
)
```

