# F::FinanceJournalEntry

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Journal entry ID |  |
| **number** | **Integer** | Incremental number assigned to the journal entry |  |
| **published_at** | **String** | Timestamp when the journal entry was published. |  |
| **type** | **String** | Journal entry type (e.g. bank, invoice, tax) |  |
| **source_id** | **String** | Source id related with this journal entry | [optional] |
| **source_type** | **String** | Source type related with this journal entry | [optional] |
| **reference_date** | **String** | Date of the associate source |  |
| **description** | **String** | Description of the journal entry | [optional] |
| **legal_entity_id** | **String** | The associated Legal Entity ID |  |
| **external_id** | **String** | External identifier for the journal entry | [optional] |
| **status** | **String** | The status of the journal entry (draft, published, etc.) |  |
| **updated_at** | **String** | Timestamp when the journal entry was last updated. |  |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceJournalEntry.new(
  id: 4321,
  number: 1,
  published_at: 2025-01-01T00:00:00.000Z,
  type: bank,
  source_id: 15,
  source_type: bank_transaction,
  reference_date: 2025-01-01,
  description: Payment for invoice,
  legal_entity_id: 1001,
  external_id: EXT-001,
  status: published,
  updated_at: 2025-01-01T00:00:00.000Z
)
```

