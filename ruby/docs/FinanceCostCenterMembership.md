# F::FinanceCostCenterMembership

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The unique identifier of the cost center membership |  |
| **employee_id** | **String** | The identifier of the associated employee |  |
| **cost_center_id** | **String** | The identifier of the associated cost center |  |
| **start_date** | **String** | The date the employee started being assigned to the cost center |  |
| **end_date** | **String** | The date the em&#39;ployee stopped being assigned to the cost center | [optional] |
| **percentage** | **Float** | The percentage allocation of the employee to the cost center |  |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceCostCenterMembership.new(
  id: 1,
  employee_id: 1,
  cost_center_id: 1,
  start_date: 2020-01-01,
  end_date: 2020-12-31,
  percentage: 0.5
)
```

