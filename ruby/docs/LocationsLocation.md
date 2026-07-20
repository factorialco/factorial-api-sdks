# F::LocationsLocation

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the location |  |
| **company_id** | **String** | company identifier |  |
| **name** | **String** | name of the location |  |
| **timezone** | **String** | timezone of the location | [optional] |
| **country** | **String** | country code of the location | [optional] |
| **state** | **String** | State of the location | [optional] |
| **city** | **String** | City of the location | [optional] |
| **address_line_1** | **String** | Address line 1 of the location | [optional] |
| **address_line_2** | **String** | Address line 2 of the location | [optional] |
| **postal_code** | **String** | Postal code of the location | [optional] |
| **phone_number** | **String** | phone number of the location | [optional] |
| **main** | **Boolean** | whether the location is the main one |  |
| **latitude** | **Float** | latitude of the location | [optional] |
| **longitude** | **Float** | longitude of the location | [optional] |
| **radius** | **Float** | radius of the location | [optional] |
| **siret** | **String** | siret of the location (only for France) | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::LocationsLocation.new(
  id: 1,
  company_id: 1,
  name: Barcelona Office,
  timezone: Europe/Madrid,
  country: es,
  state: Barcelona,
  city: Barcelona,
  address_line_1: Carrer Mallorca,
  address_line_2: 61 2A,
  postal_code: 08005,
  phone_number: 657483987,
  main: false,
  latitude: 52.378,
  longitude: 4.898,
  radius: 5.0,
  siret: FR00123456789
)
```

