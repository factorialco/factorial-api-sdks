# F::ExpensesPerDiem

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The ID of the per diem. |  |
| **employee_id** | **String** | The ID of the employee the per diem is for. | [optional] |
| **company_id** | **String** | The ID of the company the per diem is for. |  |
| **expenses_expensable_id** | **String** | The ID of the expensable the per diem is for. | [optional] |
| **end_date** | **String** | The last day of the trip the allowance covers. | [optional] |
| **start_date** | **String** | The first day of the trip the allowance covers. | [optional] |
| **from** | **String** | The location the per diem is from. | [optional] |
| **to** | **String** | The location the per diem is to. | [optional] |
| **trip_name** | **String** | The name of the trip. | [optional] |
| **ledger_account_id** | **String** | The ID of the ledger account the per diem is for. | [optional] |
| **amount** | **Integer** | The total allowance amount in cents. | [optional] |
| **currency** | **String** | The currency code in ISO 4217 format. |  |
| **reimbursable_amount** | **Integer** | The amount to be reimbursed by the per diem in cents. | [optional] |
| **reimbursable_currency** | **String** | The currency for the reimbursable amount. | [optional] |
| **payment** | **String** | The payment method for the per diem. |  |
| **paid_at** | **String** | The date the per diem was paid. | [optional] |
| **files** | **Array&lt;Object&gt;** | The files attached to the per diem. |  |
| **review_request_at** | **String** | The date the per diem was requested for review. | [optional] |
| **effective_on** | **String** | The date the per diem is effective on. | [optional] |
| **description** | **String** | The description of the per diem. | [optional] |
| **category** | **Object** | The category of the per diem. | [optional] |
| **subcategory** | **String** | The subcategory of the per diem. | [optional] |
| **status** | **String** | The status of the per diem. |  |
| **budget_id** | **String** | The id of the budget associated with this per diem | [optional] |
| **project_id** | **String** | The id of the project associated with this per diem | [optional] |
| **cost_center_ids** | **Array&lt;String&gt;** | Array of cost center IDs associated with this per diem |  |
| **rates** | **Array&lt;Object&gt;** | The rates for the per diem. |  |

## Example

```ruby
require 'factorial_api'

instance = F::ExpensesPerDiem.new(
  id: 1,
  employee_id: 1,
  company_id: 1,
  expenses_expensable_id: 1,
  end_date: 2020-01-01,
  start_date: 2020-01-01,
  from: New York,
  to: San Francisco,
  trip_name: Berlin - Barcelona, 12-19 Mar 2026,
  ledger_account_id: 1,
  amount: 1000,
  currency: USD,
  reimbursable_amount: 250,
  reimbursable_currency: USD,
  payment: reimbursable,
  paid_at: 2020-01-01T12:00:00.000Z,
  files: null,
  review_request_at: 2020-01-01T12:00:00.000Z,
  effective_on: 2020-01-01T12:00:00.000Z,
  description: Per diem for trip to San Francisco,
  category: travel,
  subcategory: national,
  status: approved,
  budget_id: 1,
  project_id: 1,
  cost_center_ids: [1, 2],
  rates: null
)
```

