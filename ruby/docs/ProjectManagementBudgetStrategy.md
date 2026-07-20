# F::ProjectManagementBudgetStrategy

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Factorial id of the budget strategy |  |
| **budget_type** | **String** | Type of budget strategy. One of project_fixed_cost &#x3D;&gt; ProjectFixedCost, total_budget &#x3D;&gt; TimeAndMaterials, without_budget &#x3D;&gt; WithoutBudget |  |
| **planned_cents** | **Integer** | Planned amount in cents (for project_fixed_cost / total_budget) | [optional] |
| **planned_minutes** | **Integer** | Planned time in minutes (for total_budget) | [optional] |
| **fee_amount_cents** | **Integer** | Fee amount in cents (for project_fixed_cost / total_budget when is billable) | [optional] |
| **project_id** | **String** | Id of the project this budget strategy belongs to |  |
| **subproject_id** | **String** | Id of the subproject this budget strategy belongs to, if any | [optional] |
| **delegated** | **Boolean** | Whether the budget strategy is delegated |  |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementBudgetStrategy.new(
  id: 1234,
  budget_type: total_budget,
  planned_cents: 100000,
  planned_minutes: 6000,
  fee_amount_cents: 5000,
  project_id: 1234,
  subproject_id: 5678,
  delegated: false
)
```

