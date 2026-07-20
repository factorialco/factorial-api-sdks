# F::FinanceTaxRatesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **description** | **String** | An optional text describing the tax rate&#39;s purpose or context. | [optional] |
| **rate** | **Float** | Specifies the numerical percentage for the tax rate between -1 and 1. | [optional] |
| **tax_type_id** | **String** | The identifier of the related TaxType record. | [optional] |
| **external_id** | **String** | The external id of the tax rate. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceTaxRatesPostRequest.new(
  description: VAT for general goods,
  rate: 0.07,
  tax_type_id: 1234,
  external_id: EXT-RATE-001
)
```

