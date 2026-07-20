# F::BankingTransaction

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Factorial unique identifier. |  |
| **bank_account_id** | **String** | Factorial Banking Bank Account unique identifier. |  |
| **amount_cents** | **Integer** | Amount in cents. |  |
| **balance_after_cents** | **Integer** | Balance after the transaction in cents. | [optional] |
| **currency** | **String** | Currency. |  |
| **type** | **String** | Type of transaction. |  |
| **description** | **String** | Description of the transaction. | [optional] |
| **booking_date** | **String** | Booking date of the transaction. |  |
| **value_date** | **String** | Value date of the transaction. |  |
| **card_payment_id** | **String** | Factorial unique identifier of the card payment. |  |
| **updated_at** | **String** | Date when the transaction was last updated. |  |

## Example

```ruby
require 'factorial_api'

instance = F::BankingTransaction.new(
  id: 135,
  bank_account_id: 357,
  amount_cents: 1000,
  balance_after_cents: 2000,
  currency: USD,
  type: topup,
  description: Topup from external account,
  booking_date: 2021-01-01T00:00:00.000Z,
  value_date: 2021-01-01T00:00:00.000Z,
  card_payment_id: 135,
  updated_at: 2021-01-01T00:00:00.000Z
)
```

