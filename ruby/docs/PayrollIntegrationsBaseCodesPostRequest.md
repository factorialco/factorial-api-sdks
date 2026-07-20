# F::PayrollIntegrationsBaseCodesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **String** | Code Value |  |
| **codeable_id** | **String** | Related object ID. Used together with codeable_type |  |
| **codeable_type** | **String** | Related object type. Used together with codeable_id |  |
| **integration** | **String** | Integration name |  |

## Example

```ruby
require 'factorial_api'

instance = F::PayrollIntegrationsBaseCodesPostRequest.new(
  code: COD-51,
  codeable_id: 1,
  codeable_type: Employee | Company | LegalEntity | Location | TimeoffLeaveType,
  integration: a3innuva
)
```

