# F::BankingBankAccountsCreateManualPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **legal_entity_id** | **String** | Factorial unique identifier of the legal entity. |  |
| **currency** | **String** | Currency of bank account. |  |
| **account_number** | **String** | Account number. |  |
| **account_number_type** | **String** | Account number type. |  |
| **account_alias** | **String** | Alias for the bank account. | [optional] |
| **ledger_account_id** | **String** | Factorial unique identifier of the ledger account. | [optional] |
| **bank_account_membership_employee_ids** | **Array&lt;String&gt;** | An array of bank account membership employee IDs. | [optional] |
| **external_id** | **String** | External ID for the bank account. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::BankingBankAccountsCreateManualPostRequest.new(
  legal_entity_id: 11,
  currency: EUR,
  account_number: ES28209582976036485969781,
  account_number_type: iban,
  account_alias: My Bank Account,
  ledger_account_id: 135,
  bank_account_membership_employee_ids: [&quot;11&quot;],
  external_id: ext_135
)
```

