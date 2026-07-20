# F::CompaniesLegalEntitiesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **company_id** | **String** | company identifier |  |
| **country** | **String** | country code of the legal entity |  |
| **legal_name** | **String** | Legal name of the legal entity |  |
| **currency** | **String** | The currency code in ISO 4217 format |  |
| **tin** | **String** | Tax identification number | [optional] |
| **city** | **String** | City of the legal entity | [optional] |
| **state** | **String** | State of the legal entity | [optional] |
| **postal_code** | **String** | Postal code of the legal entity | [optional] |
| **address_line_1** | **String** | Address line 1 of the legal entity | [optional] |
| **address_line_2** | **String** | Address line 2 of the legal entity | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::CompaniesLegalEntitiesPostRequest.new(
  company_id: 1,
  country: es,
  legal_name: Acme Inc.,
  currency: EUR,
  tin: H41192410,
  city: Barcelona,
  state: Barcelona,
  postal_code: 08005,
  address_line_1: Carrer Mallorca,
  address_line_2: 61 2A
)
```

