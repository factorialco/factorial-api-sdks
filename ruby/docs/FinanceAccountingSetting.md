# F::FinanceAccountingSetting

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier for the AccountingSetting. |  |
| **external_id** | **String** | External ID for the accounting setting. | [optional] |
| **company_id** | **String** | ID of the associated Company. |  |
| **legal_entity_id** | **String** | ID of the associated Legal Entity. |  |
| **updated_at** | **String** | Timestamp when the accounting setting was last updated. |  |
| **default_account_for_purchase_invoices_id** | **String** | Default account for purchase invoices. | [optional] |
| **default_account_for_vendors_id** | **String** | Default account for vendors. | [optional] |
| **default_account_for_banks_id** | **String** | Default account for banks. | [optional] |
| **default_account_for_suspense_id** | **String** | Default suspense account. | [optional] |
| **default_account_for_expenses_id** | **String** | Default account for expenses. | [optional] |
| **default_account_for_employees_id** | **String** | Default account for employees. | [optional] |
| **default_account_for_sale_invoices_id** | **String** | Default account for sale invoices. | [optional] |
| **default_account_for_clients_id** | **String** | Default account for clients. | [optional] |
| **default_account_for_benefits_id** | **String** | Default account for benefits. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceAccountingSetting.new(
  id: 1234,
  external_id: ext_135,
  company_id: 1,
  legal_entity_id: 101,
  updated_at: 2025-01-01T00:00:00.000Z,
  default_account_for_purchase_invoices_id: 5001,
  default_account_for_vendors_id: 5002,
  default_account_for_banks_id: 5003,
  default_account_for_suspense_id: 5004,
  default_account_for_expenses_id: 5005,
  default_account_for_employees_id: 5006,
  default_account_for_sale_invoices_id: 5007,
  default_account_for_clients_id: 5008,
  default_account_for_benefits_id: 5009
)
```

