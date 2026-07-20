# F::LocationsLocationsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | name of the location |  |
| **country** | **String** | country code of the location |  |
| **main** | **Boolean** | whether the location is the main one | [optional] |
| **city** | **String** | City of the location | [optional] |
| **state** | **String** | State of the location | [optional] |
| **phone_number** | **String** | phone number of the location | [optional] |
| **postal_code** | **String** | Postal code of the location | [optional] |
| **address_line_one** | **String** | Address line 1 of the location | [optional] |
| **address_line_two** | **String** | Address line 2 of the location | [optional] |
| **latitude** | **Float** | latitude of the location | [optional] |
| **longitude** | **Float** | longitude of the location | [optional] |
| **timezone** | **String** | timezone of the location |  |
| **radius** | **Float** | radius of the location | [optional] |
| **company_id** | **String** | company identifier |  |
| **siret** | **String** | siret of the location (only for France) | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::LocationsLocationsPostRequest.new(
  name: Barcelona Office,
  country: es,
  main: false,
  city: Barcelona,
  state: Barcelona,
  phone_number: 657483987,
  postal_code: 08005,
  address_line_one: Carrer Mallorca,
  address_line_two: 61 2A,
  latitude: 52.378,
  longitude: 4.898,
  timezone: Europe/Madrid,
  radius: 5.0,
  company_id: 1,
  siret: FR00123456789
)
```

