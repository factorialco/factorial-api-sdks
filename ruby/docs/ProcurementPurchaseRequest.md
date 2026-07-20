# F::ProcurementPurchaseRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier of the purchase request |  |
| **description** | **String** | Description or notes about the purchase request |  |
| **type_id** | **String** | The id of the referred type |  |
| **company_id** | **String** | Identifier of the company that owns this purchase request | [optional] |
| **cost** | **Object** | Total cost of the purchase request |  |
| **date** | **String** | Date when the purchase request was created |  |
| **requester_employee_id** | **String** | Identifier of the employee who requested this purchase |  |
| **vendor_id** | **String** | Identifier of the vendor (contact) associated with this purchase request | [optional] |
| **status** | **String** | Current status of the purchase request |  |
| **url** | **String** | URL related to the purchase request (e.g., product link) | [optional] |
| **additional_information** | **String** | Additional information or notes about the purchase request | [optional] |
| **deadline** | **String** | Deadline date for the purchase request | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProcurementPurchaseRequest.new(
  id: 678432,
  description: Office supplies request,
  type_id: 12353,
  company_id: 1,
  cost: {cents&#x3D;10000, currency&#x3D;EUR},
  date: 2025-01-15,
  requester_employee_id: 20,
  vendor_id: 9012,
  status: pending,
  url: https://example.com/product,
  additional_information: Urgent delivery required,
  deadline: 2025-02-15
)
```

