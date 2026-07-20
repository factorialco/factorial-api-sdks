# F::FinanceTaxRate

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Factorial id |  |
| **rate** | **Float** | Specifies the numerical percentage for the tax rate between -1 and 1. |  |
| **description** | **String** | An optional text describing the tax rate&#39;s purpose or context. | [optional] |
| **tax_type_id** | **String** | The identifier of the related TaxType record. |  |
| **external_id** | **String** | The external id of the tax rate. | [optional] |
| **updated_at** | **String** | Last update date of the tax rate. |  |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceTaxRate.new(
  id: 123,
  rate: 0.07,
  description: VAT for general goods,
  tax_type_id: 1234,
  external_id: EXT-RATE-001,
  updated_at: 2025-01-01T00:00:00.000Z
)
```

