# F::PayrollFamilySituationsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_id** | **String** | Employee id. |  |
| **civil_status** | **String** | Civil status of the employee. | [optional] |
| **number_of_dependants** | **Integer** | Number of dependants of the employee. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PayrollFamilySituationsPostRequest.new(
  employee_id: 10,
  civil_status: married,
  number_of_dependants: 3
)
```

