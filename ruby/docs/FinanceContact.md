# F::FinanceContact

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier for the Contact. |  |
| **name** | **String** | The commercial name of the Contact. |  |
| **legal_name** | **String** | The official or legal name of the Contact. | [optional] |
| **tax_id** | **String** | Tax identification number assigned to the Contact. | [optional] |
| **address** | **Object** | The address object containing street, city, etc. |  |
| **external_id** | **String** | The external id of the contact. | [optional] |
| **updated_at** | **String** | Timestamp when the Contact was last updated. |  |
| **iban** | **String** | International Bank Account Number if provided. | [optional] |
| **bank_code** | **String** | Bank or branch code for the Contact if relevant. | [optional] |
| **preferred_payment_method** | **String** | Preferred payment method for the Contact (e.g. wire_transfer, paypal). | [optional] |
| **website** | **String** | The website of the Contact. | [optional] |
| **email** | **String** | The email of the Contact. | [optional] |
| **phone_number** | **String** | The phone number of the Contact. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceContact.new(
  id: 123,
  name: Google,
  legal_name: Google engineering vendor,
  tax_id: X1234567,
  address: {city&#x3D;East Ariana, country_code&#x3D;SC, line1&#x3D;93402 Spencer Points, line2&#x3D;Apt. 555, postal_code&#x3D;61471, state&#x3D;Oklahoma},
  external_id: EXT-CONTACT-001,
  updated_at: 2025-01-01T00:00:00.000Z,
  iban: GB25ZFXH46063029945396,
  bank_code: BABCESMM,
  preferred_payment_method: banktransfer,
  website: https://www.example.com,
  email: contact@example.com,
  phone_number: +1234567890
)
```

