# F::FinanceTaxType

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Factorial id |  |
| **name** | **String** | The name assigned to the tax type. |  |
| **type** | **String** | The tax category used to distinguish different tax kinds. |  |
| **country_code** | **String** | The country code where this tax type applies. | [optional] |
| **external_id** | **String** | The external id of the tax type. | [optional] |
| **updated_at** | **String** | Last update date of the tax type. |  |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceTaxType.new(
  id: 1234,
  name: general IVA,
  type: vat,
  country_code: ES,
  external_id: EXT-TYPE-001,
  updated_at: 2025-01-01T00:00:00.000Z
)
```

