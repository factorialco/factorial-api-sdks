# F::ProjectManagementBudgetStrategiesIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id of the budget strategy to update |  |
| **planned_cents** | **Integer** | Planned amount in cents (for project_fixed_cost / total_budget) | [optional] |
| **planned_minutes** | **Integer** | Planned time in minutes (for total_budget) | [optional] |
| **fee_amount_cents** | **Integer** | Fee amount in cents (for project_fixed_cost / total_budget when is billable) | [optional] |
| **budget_strategy_type** | **String** | Type of budget strategy. One of project_fixed_cost &#x3D;&gt; ProjectFixedCost, total_budget &#x3D;&gt; TimeAndMaterials, without_budget &#x3D;&gt; WithoutBudget | [optional] |
| **delegated** | **Boolean** | Whether the budget strategy is delegated | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementBudgetStrategiesIdPutRequest.new(
  id: 1234,
  planned_cents: 100000,
  planned_minutes: 6000,
  fee_amount_cents: 5000,
  budget_strategy_type: total_budget,
  delegated: false
)
```

