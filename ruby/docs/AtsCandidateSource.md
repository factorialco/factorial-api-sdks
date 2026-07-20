# F::AtsCandidateSource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the source. |  |
| **company_id** | **String** | identifier of the company. |  |
| **category** | **String** | category of the source. |  |
| **name** | **String** | name of the source. |  |
| **label** | **String** | Translated label of the source if it is a default one, or name otherwise |  |

## Example

```ruby
require 'factorial_api'

instance = F::AtsCandidateSource.new(
  id: 1,
  company_id: 1,
  category: social_media,
  name: manually_added,
  label: Manually added
)
```

