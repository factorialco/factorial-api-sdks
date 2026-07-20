# F::AtsApplicationsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **author_id** | **String** | Application author id | [optional] |
| **author_type** | **String** | Application author type | [optional] |
| **id** | **String** | Application id |  |
| **qualified** | **Boolean** | Application is qualified | [optional] |
| **ats_application_phase_id** | **String** | Application phase id | [optional] |
| **disqualified_reason** | **String** | Application disqualified reason | [optional] |
| **phone** | **String** | Application candidate phone | [optional] |
| **ats_rejection_reason_id** | **String** | Application rejection reason id | [optional] |
| **source** | **String** | Application source | [optional] |
| **source_id** | **String** | Application source id | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsApplicationsIdPutRequest.new(
  author_id: 1,
  author_type: company,
  id: 1,
  qualified: true,
  ats_application_phase_id: 1,
  disqualified_reason: Unfit for the role,
  phone: 34612345678,
  ats_rejection_reason_id: 1,
  source: source,
  source_id: 1
)
```

