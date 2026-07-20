# F::FinanceJournalEntriesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **external_id** | **String** | External identifier for the journal entry | [optional] |
| **legal_entity_id** | **String** | The associated Legal Entity ID |  |
| **type** | **String** | Journal entry type (e.g. bank, invoice, tax) | [optional] |
| **lines** | **Array&lt;Object&gt;** | Array of journal lines for this entry, example: [{\&quot;account_id\&quot;: 9876, \&quot;debit_amount_cents\&quot;: 0, \&quot;credit_amount_cents\&quot;: 100, \&quot;external_id\&quot;: \&quot;LINE-001\&quot;}, {\&quot;account_id\&quot;: 9876, \&quot;debit_amount_cents\&quot;: 100, \&quot;credit_amount_cents\&quot;: 0, \&quot;external_id\&quot;: \&quot;LINE-002\&quot;}] |  |
| **reference_date** | **String** | Date of the associate source |  |
| **description** | **String** | Description of the journal entry | [optional] |
| **status** | **String** | Status of the journal entry (reversed, published, etc.) | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceJournalEntriesPostRequest.new(
  external_id: EXT-001,
  legal_entity_id: 1001,
  type: external,
  lines: [{&quot;account_id&quot;:9876,&quot;debit_amount_cents&quot;:0,&quot;credit_amount_cents&quot;:100,&quot;external_id&quot;:&quot;LINE-001&quot;},{&quot;account_id&quot;:9876,&quot;debit_amount_cents&quot;:100,&quot;credit_amount_cents&quot;:0,&quot;external_id&quot;:&quot;LINE-002&quot;}],
  reference_date: 2025-01-01,
  description: Payment for invoice,
  status: published
)
```

