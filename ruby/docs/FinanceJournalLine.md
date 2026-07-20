# F::FinanceJournalLine

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Factorial id |  |
| **number** | **Integer** | Sequential number assigned to the line |  |
| **debit_amount_cents** | **Integer** | The debit amount in cents |  |
| **credit_amount_cents** | **Integer** | The credit amount in cents |  |
| **journal_entry_id** | **String** | ID of the parent journal entry |  |
| **account_id** | **String** | ID of the associated account |  |
| **fully_reconciled_at** | **String** | Timestamp when the journal line was reconciled | [optional] |
| **external_id** | **String** | External identifier for the journal line | [optional] |
| **updated_at** | **String** | Timestamp when the journal line was last updated. |  |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceJournalLine.new(
  id: 1234,
  number: 1,
  debit_amount_cents: 0,
  credit_amount_cents: 100,
  journal_entry_id: 4321,
  account_id: 9876,
  fully_reconciled_at: 2025-01-01T00:00:00.000Z,
  external_id: EXT-LINE-001,
  updated_at: 2025-01-01T00:00:00.000Z
)
```

