# F::AtsApplicationsMoveToPhasePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Application id to move |  |
| **ats_application_phase_id** | **String** | Target application phase id. Must belong to the same job posting as the application. Refers to ats/application_phases. |  |

## Example

```ruby
require 'factorial_api'

instance = F::AtsApplicationsMoveToPhasePostRequest.new(
  id: 1,
  ats_application_phase_id: 1
)
```

