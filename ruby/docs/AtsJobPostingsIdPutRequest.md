# F::AtsJobPostingsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **title** | **String** |  | [optional] |
| **description** | **String** |  | [optional] |
| **contract_type** | **String** |  | [optional] |
| **category** | **String** |  | [optional] |
| **workplace_type** | **String** |  | [optional] |
| **status** | **String** |  | [optional] |
| **schedule_type** | **String** |  | [optional] |
| **team_id** | **String** |  | [optional] |
| **location_id** | **String** |  | [optional] |
| **salary_format** | **String** |  | [optional] |
| **salary_from_amount_in_cents** | **Integer** |  | [optional] |
| **salary_to_amount_in_cents** | **Integer** |  | [optional] |
| **cv_requirement** | **String** |  | [optional] |
| **cover_letter_requirement** | **String** |  | [optional] |
| **phone_requirement** | **String** |  | [optional] |
| **photo_requirement** | **String** |  | [optional] |
| **personal_url_requirement** | **String** |  | [optional] |
| **salary_period** | **String** |  | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsJobPostingsIdPutRequest.new(
  id: 1,
  title: My job title,
  description: My job description,
  contract_type: indefinite,
  category: engineering,
  workplace_type: onsite,
  status: draft,
  schedule_type: full_time,
  team_id: 1,
  location_id: 1,
  salary_format: range,
  salary_from_amount_in_cents: 3000000,
  salary_to_amount_in_cents: 5000000,
  cv_requirement: mandatory,
  cover_letter_requirement: optional,
  phone_requirement: do_not_ask,
  photo_requirement: do_not_ask,
  personal_url_requirement: do_not_ask,
  salary_period: annual
)
```

