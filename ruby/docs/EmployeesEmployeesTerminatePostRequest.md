# F::EmployeesEmployeesTerminatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | id of the employee. |  |
| **terminated_on** | **String** | when the employee will be terminated. |  |
| **termination_reason** | **String** | A reason for the termination. | [optional] |
| **termination_assigned_manager_id** | **String** | id of manager that terminates the employee, you can get the manager_id from employees endpoint. | [optional] |
| **open_backfill** | **Boolean** | When true, automatically opens a backfill position (vacancy or requisition) for the terminated employee. Requires ATS to be enabled with an automatic backfill setting configured. When false or omitted, no backfill is created. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::EmployeesEmployeesTerminatePostRequest.new(
  id: 1,
  terminated_on: 2024-10-06,
  termination_reason: The employee has left the company,
  termination_assigned_manager_id: 1,
  open_backfill: false
)
```

