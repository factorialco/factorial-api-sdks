# F::PayrollFamilySituation

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | ID of the family situation. |  |
| **employee_id** | **String** | Employee id of the family situation. |  |
| **civil_status** | **String** | Civil status of the employee. | [optional] |
| **number_of_dependants** | **Integer** | Number of dependants of the employee. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PayrollFamilySituation.new(
  id: 1,
  employee_id: 5,
  civil_status: married,
  number_of_dependants: 2
)
```

