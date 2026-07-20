# F::BankingBankAccount

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Factorial unique identifier. |  |
| **external_id** | **String** | External ID for the bank account. |  |
| **currency** | **String** | Currency. |  |
| **country** | **String** | Country. |  |
| **account_number** | **String** | Account number. |  |
| **account_number_type** | **String** | Account number type. |  |
| **sort_code** | **String** | Sort code. | [optional] |
| **bic** | **String** | Bank Identifier Code. | [optional] |
| **iban** | **String** | International Bank Account Number. | [optional] |
| **routing_number** | **String** | Routing number. | [optional] |
| **account_balance_cents** | **Integer** | Account balance in cents. |  |
| **available_balance_cents** | **Integer** | Available balance in cents. |  |
| **pending_balance_cents** | **Integer** | Pending balance in cents. |  |
| **beneficiary_name** | **String** | Beneficiary name. | [optional] |
| **bank_name** | **String** | Bank name. | [optional] |
| **account_alias** | **String** | Account alias. | [optional] |
| **updated_at** | **String** | Last updated date. |  |
| **legal_entity_id** | **String** | Factorial unique identifier of the legal entity. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::BankingBankAccount.new(
  id: 1,
  external_id: ext_135,
  currency: EUR,
  country: es,
  account_number: ES28209582976036485969781,
  account_number_type: iban,
  sort_code: 123456,
  bic: FAKEBB33,
  iban: ES28209582976036485969781,
  routing_number: 12345678,
  account_balance_cents: 0,
  available_balance_cents: 0,
  pending_balance_cents: 0,
  beneficiary_name: factorial INC. - B66854530,
  bank_name: Fake Bank,
  account_alias: My Bank Account,
  updated_at: 2021-01-01T00:00:00.000Z,
  legal_entity_id: 11
)
```

