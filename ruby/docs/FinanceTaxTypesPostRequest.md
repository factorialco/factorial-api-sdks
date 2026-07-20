# F::FinanceTaxTypesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | The name assigned to the tax type. |  |
| **type** | **String** | The tax category used to distinguish different tax kinds. |  |
| **country_code** | **String** | The country code where this tax type applies. | [optional] |
| **external_id** | **String** | The external id of the tax type. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceTaxTypesPostRequest.new(
  name: general IVA,
  type: vat,
  country_code: ES,
  external_id: EXT-TYPE-001
)
```

