# F::FinanceTaxRatesIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the tax rate. |  |
| **description** | **String** | An optional text describing the tax rate&#39;s purpose or context. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceTaxRatesIdPutRequest.new(
  id: 123,
  description: VAT for general goods
)
```

