# F::TimeoffAllowancesDeleteWithAltAllowancePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **alt_allowance_id** | **String** | Allowance id sent to migrate existing incidences from the deleted allowance to the alternative allowance |  |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffAllowancesDeleteWithAltAllowancePostRequest.new(
  id: null,
  alt_allowance_id: 1
)
```

