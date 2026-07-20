# F::ExpensesExpensable

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier for the expensable |  |
| **type** | **String** | Type of the expensable. Can be either \&quot;expense\&quot; or \&quot;mileage\&quot; or \&quot;perdiem\&quot; |  |
| **company_id** | **String** | The ID of the company that owns the expensable |  |
| **employee_id** | **String** | The ID of the employee that owns the expensable |  |
| **group_id** | **String** | The ID of the expense report (group of expensables submitted together) this expensable was submitted in, if any | [optional] |
| **legal_entity_id** | **String** | The optional ID of the legal entity that the expensable belongs to | [optional] |
| **created_at** | **String** | The date and time when the expensable was created |  |
| **amount** | **Integer** | The optional amount in cents | [optional] |
| **currency** | **String** | The currency code in ISO 4217 format |  |
| **status** | **String** | The lifecycle status of the expensable in the review/payment flow |  |
| **description** | **String** | The optional description of the expensable | [optional] |
| **reporter_id** | **String** | The optional ID of the employee that reported the expensable | [optional] |
| **status_updated_at** | **String** | The optional date and time when the status was last updated |  |
| **effective_on** | **String** | The optional date and time when the expensable was effective | [optional] |
| **review_request_at** | **String** | The optional date and time when the expensable was requested for review | [optional] |
| **paid_at** | **String** | The optional date and time when the expensable was set as paid | [optional] |
| **updated_at** | **String** | The date and time when the expensable was last updated |  |
| **reimbursable_amount** | **Integer** | The optional reimbursable amount in cents | [optional] |
| **reimbursable_currency** | **String** | The optional reimbursable currency code in ISO 4217 format | [optional] |
| **reimbursement_method** | **String** | The optional reimbursement method | [optional] |
| **internal_reference** | **String** | The optional internal reference of the expensable | [optional] |
| **expense_id** | **String** | The ID of the receipt-backed expense detail record; set only when &#x60;type&#x60; is \&quot;expense\&quot; | [optional] |
| **mileage_id** | **String** | The ID of the mileage claim detail record; set only when &#x60;type&#x60; is \&quot;mileage\&quot; | [optional] |
| **per_diem_id** | **String** | The ID of the per-diem allowance detail record; set only when &#x60;type&#x60; is \&quot;perdiem\&quot; | [optional] |
| **budget_id** | **String** | The ID of the budget this expensable draws from, when one is linked | [optional] |
| **project_id** | **String** | The ID of the project this expensable is charged to, when one is linked | [optional] |
| **cost_center_ids** | **Array&lt;String&gt;** | The IDs of the cost centers the expensable&#39;s cost is allocated to |  |

## Example

```ruby
require 'factorial_api'

instance = F::ExpensesExpensable.new(
  id: 1,
  type: expense,
  company_id: 1,
  employee_id: 1,
  group_id: 1,
  legal_entity_id: 1,
  created_at: 2024-06-06T12:00:00.000Z,
  amount: 1000,
  currency: EUR,
  status: approved,
  description: Dinner with clients,
  reporter_id: 1,
  status_updated_at: 2024-06-06T12:00:00.000Z,
  effective_on: 2024-06-06T12:00:00.000Z,
  review_request_at: 2024-06-06T12:00:00.000Z,
  paid_at: 2024-06-06T12:00:00.000Z,
  updated_at: 2024-06-06T12:00:00.000Z,
  reimbursable_amount: 1000,
  reimbursable_currency: EUR,
  reimbursement_method: sepa_transfer,
  internal_reference: REF123,
  expense_id: 1,
  mileage_id: 1,
  per_diem_id: 1,
  budget_id: 1,
  project_id: 1,
  cost_center_ids: [1, 2]
)
```

