# F::EmployeeUpdatesTermination

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | ID of the termination |  |
| **status** | **String** | Status of the termination |  |
| **employee_id** | **String** | Employee ID |  |
| **terminated_on** | **String** | Date terminated on | [optional] |
| **contract_end_date** | **String** | End date of contract (employment end). Users can still have have access to Factorial after this date. To revoke access, use the terminated_on field. | [optional] |
| **termination_reason** | **String** | Reason for the termination | [optional] |
| **termination_observations** | **String** | Observations about the termination | [optional] |
| **legal_entity_id** | **String** | Legal entity ID | [optional] |
| **remaining_holidays** | **Array&lt;Object&gt;** | Remaining holidays |  |
| **termination_reason_type** | **String** | Termination reason type | [optional] |
| **termination_type_description** | **String** | The description of the termination type. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::EmployeeUpdatesTermination.new(
  id: 1,
  status: to-do,
  employee_id: 1,
  terminated_on: 2020-01-01,
  contract_end_date: 2020-01-01,
  termination_reason: Fired,
  termination_observations: none,
  legal_entity_id: 1,
  remaining_holidays: [{name&#x3D;Vacaciones restantes, available_days&#x3D;0 días laborables}],
  termination_reason_type: company,
  termination_type_description: Baja voluntaria/Dimisión
)
```

