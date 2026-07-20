# F::FinanceContactsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | The commercial name of the Contact. |  |
| **tax_id** | **String** | Tax identification number assigned to the Contact. | [optional] |
| **legal_name** | **String** | The official or legal name of the Contact. | [optional] |
| **address** | **Object** | The address object containing street, city, etc. |  |
| **iban** | **String** | International Bank Account Number if provided. | [optional] |
| **bank_code** | **String** | Bank or branch code for the Contact if relevant. | [optional] |
| **external_id** | **String** | The external id of the contact. | [optional] |
| **project_ids** | **Array&lt;String&gt;** | List of project IDs associated with the Contact. | [optional] |
| **website** | **String** | The website of the Contact. | [optional] |
| **email** | **String** | The email of the Contact. | [optional] |
| **phone_number** | **String** | The phone number of the Contact. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceContactsPostRequest.new(
  name: Google,
  tax_id: X1234567,
  legal_name: Google engineering vendor,
  address: {city&#x3D;East Ariana, country_code&#x3D;SC, line1&#x3D;93402 Spencer Points, line2&#x3D;Apt. 555, postal_code&#x3D;61471, state&#x3D;Oklahoma},
  iban: GB25ZFXH46063029945396,
  bank_code: BABCESMM,
  external_id: EXT-CONTACT-001,
  project_ids: null,
  website: https://www.example.com,
  email: contact@example.com,
  phone_number: +1234567890
)
```

