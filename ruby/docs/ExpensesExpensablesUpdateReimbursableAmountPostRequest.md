# F::ExpensesExpensablesUpdateReimbursableAmountPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The ID of the expensable |  |
| **reimbursable_amount** | **Integer** | The reimbursable amount in cents |  |

## Example

```ruby
require 'factorial_api'

instance = F::ExpensesExpensablesUpdateReimbursableAmountPostRequest.new(
  id: 1,
  reimbursable_amount: 2000
)
```

