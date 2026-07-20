# F::FinanceTaxTypesIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the tax type. |  |
| **name** | **String** | The name assigned to the tax type. | [optional] |
| **type** | **String** | The tax category used to distinguish different tax kinds. |  |
| **country_code** | **String** | The country code where this tax type applies. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceTaxTypesIdPutRequest.new(
  id: 1234,
  name: general IVA,
  type: vat,
  country_code: ES
)
```

