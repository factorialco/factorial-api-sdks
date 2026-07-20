# F::BankingBankAccountNumber

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Employee id. |  |
| **company_id** | **String** | Company identifier |  |
| **account_number** | **String** | Account number |  |
| **complementary_data** | **String** | Additional banking information, depending on the selected format. | [optional] |
| **format** | **String** | The format of the account number. |  |

## Example

```ruby
require 'factorial_api'

instance = F::BankingBankAccountNumber.new(
  id: 135,
  company_id: 1,
  account_number: ES7520807723367311468673,
  complementary_data: null,
  format: null
)
```

