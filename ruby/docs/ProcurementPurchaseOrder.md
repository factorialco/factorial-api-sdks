# F::ProcurementPurchaseOrder

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier of the purchase order |  |
| **po_number** | **Integer** | Purchase order number assigned to this order |  |
| **description** | **String** | Description or notes about the purchase order |  |
| **status** | **String** | Current status of the purchase order |  |
| **cost** | **Object** | Total cost of the purchase order |  |
| **date** | **String** | Date when the purchase order was created |  |
| **vendor_id** | **String** | Identifier of the vendor (contact) associated with this purchase order | [optional] |
| **purchase_request_id** | **String** | Identifier of the purchase request that generated this purchase order |  |
| **legal_entity_id** | **String** | Identifier of the legal entity that owns this purchase order |  |
| **company_id** | **String** | Identifier of the company that owns this purchase order |  |
| **formatted_po_number** | **String** | Formatted purchase order number with prefix (e.g., PO-00001) |  |

## Example

```ruby
require 'factorial_api'

instance = F::ProcurementPurchaseOrder.new(
  id: 678432,
  po_number: 2131,
  description: Office supplies for Q1 2025,
  status: pending,
  cost: {cents&#x3D;10000, currency&#x3D;EUR},
  date: 2025-01-15,
  vendor_id: 9012,
  purchase_request_id: 5678,
  legal_entity_id: 3456,
  company_id: 1,
  formatted_po_number: PO-02131
)
```

