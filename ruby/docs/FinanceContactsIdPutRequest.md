# F::FinanceContactsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | ID of the Contact to update. |  |
| **tax_id** | **String** | Tax identification number assigned to the Contact. | [optional] |
| **legal_name** | **String** | The official or legal name of the Contact. | [optional] |
| **name** | **String** | The commercial name of the Contact. | [optional] |
| **address** | **Object** | The address object containing street, city, etc. Example: { \&quot;city\&quot;: \&quot;East Ariana\&quot;, \&quot;country_code\&quot;: \&quot;SC\&quot;, \&quot;line1\&quot;: \&quot;93402 Spencer Points\&quot;, \&quot;line2\&quot;: \&quot;Apt. 555\&quot;, \&quot;postal_code\&quot;: \&quot;61471\&quot;, \&quot;state\&quot;: \&quot;Oklahoma\&quot; } |  |
| **website** | **String** | The website of the Contact. | [optional] |
| **email** | **String** | The email of the Contact. | [optional] |
| **phone_number** | **String** | The phone number of the Contact. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceContactsIdPutRequest.new(
  id: 123,
  tax_id: X1234567,
  legal_name: Google engineering vendor,
  name: Google,
  address: {&quot;city&quot;:&quot;East Ariana&quot;,&quot;country_code&quot;:&quot;SC&quot;,&quot;line1&quot;:&quot;93402 Spencer Points&quot;,&quot;line2&quot;:&quot;Apt. 555&quot;,&quot;postal_code&quot;:&quot;61471&quot;,&quot;state&quot;:&quot;Oklahoma&quot;},
  website: https://www.example.com,
  email: contact@example.com,
  phone_number: +1234567890
)
```

