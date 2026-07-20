# F::ExpensesExpense

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the expense | [optional] |
| **employee_id** | **String** | The id of the expense&#39;s owner | [optional] |
| **company_id** | **String** | The id of the expense&#39;s company |  |
| **card_payment_id** | **String** | The id of the card payment | [optional] |
| **dispute_id** | **String** | The id of the dispute | [optional] |
| **expenses_expensable_id** | **String** | The id of the expensable | [optional] |
| **merchant_name** | **String** | The name of the merchant | [optional] |
| **user_merchant** | **String** | The merchant name as typed by the employee, when they corrected or filled it manually (takes precedence over the extracted &#x60;merchant_name&#x60;) | [optional] |
| **merchant_tin** | **String** | The tax identification number of the merchant | [optional] |
| **category** | **Object** | The category of the expense | [optional] |
| **subcategory** | **String** | The subcategory of the expense | [optional] |
| **creation_type** | **String** | How the expense was created, one of &#39;manual&#39;, &#39;automatic&#39; or &#39;travelperk&#39; |  |
| **reference** | **String** | The reference of the expense | [optional] |
| **amount** | **Integer** | The total amount in cents | [optional] |
| **currency** | **String** | The currency of the expense |  |
| **status** | **String** | The lifecycle status of the expense in the review/payment flow |  |
| **description** | **String** | The description of the expense | [optional] |
| **effective_on** | **String** | The date when the expense was made |  |
| **review_request_at** | **String** | The date and time when the expense was reviewed | [optional] |
| **status_updated_at** | **String** | The date and time when the status was updated |  |
| **files** | **Array&lt;Object&gt;** | The files of the expense |  |
| **external_authorization_id** | **String** | The id of the external authorization | [optional] |
| **expenses_card_id** | **String** | The id of the card | [optional] |
| **card** | **Object** | The card of the expense | [optional] |
| **document_id** | **String** | The id of the document | [optional] |
| **signed_document** | **Object** | The signed document of the expense | [optional] |
| **access_token** | **String** | The access token of the expense | [optional] |
| **paid_at** | **String** | The date and time when the expense was paid | [optional] |
| **document_number** | **String** | Number of the financial document associated to the expense | [optional] |
| **document_type** | **String** | Type of the financial document associated to the expense | [optional] |
| **payment** | **String** | The payment of the expense | [optional] |
| **payment_method** | **String** | The method of the payment | [optional] |
| **exchange_rate** | **Float** | The exchange rate of the payment | [optional] |
| **reimbursable_currency** | **String** | The currency of the reimbursable amount | [optional] |
| **reimbursable_amount** | **Integer** | The optional reimbursable amount in cents | [optional] |
| **taxes** | **Array&lt;Object&gt;** | The taxes of the expense |  |
| **category_id** | **String** | The id of the expense category the expense is classified under (company-configurable catalogue) | [optional] |
| **ledger_account_id** | **String** | The id of the ledger account | [optional] |
| **budget_id** | **String** | The id of the budget associated with this expense | [optional] |
| **project_id** | **String** | The id of the project associated with this expense | [optional] |
| **cost_center_ids** | **Array&lt;String&gt;** | Array of cost center IDs associated with this expense |  |

## Example

```ruby
require 'factorial_api'

instance = F::ExpensesExpense.new(
  id: 1,
  employee_id: 1,
  company_id: 1,
  card_payment_id: 1,
  dispute_id: 1,
  expenses_expensable_id: 1,
  merchant_name: Example Merchant,
  user_merchant: Example User Merchant,
  merchant_tin: 1234567890,
  category: Category,
  subcategory: Subcategory,
  creation_type: null,
  reference: 1414PX,
  amount: 1000,
  currency: EUR,
  status: draft,
  description: Example Description,
  effective_on: 2020-01-01,
  review_request_at: 2020-01-01T00:00:000Z,
  status_updated_at: 2020-01-01T00:00:000Z,
  files: null,
  external_authorization_id: 1,
  expenses_card_id: 1,
  card: null,
  document_id: 1,
  signed_document: null,
  access_token: 1234567890,
  paid_at: 2020-01-01T00:00:000Z,
  document_number: 123456,
  document_type: invoice,
  payment: null,
  payment_method: null,
  exchange_rate: null,
  reimbursable_currency: EUR,
  reimbursable_amount: 1000,
  taxes: null,
  category_id: null,
  ledger_account_id: 1,
  budget_id: 1,
  project_id: 1,
  cost_center_ids: [1, 2]
)
```

