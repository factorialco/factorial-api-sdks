# F::PayrollIntegrationsBaseCode

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Code identifier |  |
| **company_id** | **String** | Company ID where the code belongs to |  |
| **code** | **String** | Code value |  |
| **codeable_id** | **String** | Related object ID. Used together with codeable_type |  |
| **codeable_type** | **String** | Related object type. Used together with codeable_id |  |
| **integration** | **String** | Integration name |  |

## Example

```ruby
require 'factorial_api'

instance = F::PayrollIntegrationsBaseCode.new(
  id: 1,
  company_id: 2,
  code: COD-51,
  codeable_id: 5,
  codeable_type: Employee | Company | LegalEntity | Location | TimeoffLeaveType,
  integration: a3innuva
)
```

