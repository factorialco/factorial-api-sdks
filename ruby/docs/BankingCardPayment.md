# F::BankingCardPayment

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The ID of the card payment. |  |
| **card_id** | **String** | The ID of the card. |  |
| **amount_cents** | **Integer** | The amount of the card payment. |  |
| **currency** | **String** | The currency of the card payment. |  |
| **merchant_name** | **String** | The name of the merchant. |  |
| **merchant_amount_cents** | **Integer** | The amount of the merchant. |  |
| **merchant_currency** | **String** | The currency of the merchant. |  |
| **approved** | **Boolean** | Whether the card payment was approved. |  |
| **external_created_at** | **String** | The date and time the card payment was created in the external system. |  |
| **status** | **String** | The status of the card payment. |  |
| **type** | **String** | The type of the card payment. |  |
| **exchange_rate** | **Float** | The exchange rate of the card payment. |  |
| **rejected_reason** | **String** | The reason the card payment was rejected. | [optional] |
| **created_at** | **String** | The date and time the card payment was created in factorial |  |

## Example

```ruby
require 'factorial_api'

instance = F::BankingCardPayment.new(
  id: 135,
  card_id: 123,
  amount_cents: -1000,
  currency: EUR,
  merchant_name: Test Merchant,
  merchant_amount_cents: -1000,
  merchant_currency: EUR,
  approved: true,
  external_created_at: 2025-01-01T00:00:00.000Z,
  status: closed,
  type: payment,
  exchange_rate: 1.0,
  rejected_reason: insufficient_funds,
  created_at: 2025-01-01T00:00:00.000Z
)
```

