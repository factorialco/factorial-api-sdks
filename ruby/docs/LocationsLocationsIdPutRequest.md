# F::LocationsLocationsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the location |  |
| **name** | **String** | name of the location | [optional] |
| **country** | **String** | country code of the location | [optional] |
| **main** | **Boolean** | whether the location is the main one | [optional] |
| **city** | **String** | City of the location | [optional] |
| **state** | **String** | State of the location | [optional] |
| **phone_number** | **String** | phone number of the location | [optional] |
| **postal_code** | **String** | Postal code of the location | [optional] |
| **address_line_one** | **String** | Address line 1 of the location | [optional] |
| **address_line_two** | **String** | Address line 2 of the location | [optional] |
| **timezone** | **String** | timezone of the location | [optional] |
| **latitude** | **Float** | latitude of the location | [optional] |
| **longitude** | **Float** | longitude of the location | [optional] |
| **radius** | **Float** | radius of the location | [optional] |
| **siret** | **String** | siret of the location (only for France) | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::LocationsLocationsIdPutRequest.new(
  id: 1,
  name: Barcelona Office,
  country: es,
  main: false,
  city: Barcelona,
  state: Barcelona,
  phone_number: 657483987,
  postal_code: 08005,
  address_line_one: Carrer Mallorca,
  address_line_two: 61 2A,
  timezone: Europe/Madrid,
  latitude: 52.378,
  longitude: 4.898,
  radius: 5.0,
  siret: FR00123456789
)
```

