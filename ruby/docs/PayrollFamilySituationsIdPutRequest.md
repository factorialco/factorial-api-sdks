# F::PayrollFamilySituationsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Family situation id. |  |
| **employee_id** | **String** | Employee id. |  |
| **civil_status** | **String** | Civil status of the employee. | [optional] |
| **number_of_dependants** | **Integer** | Number of dependants of the employee. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PayrollFamilySituationsIdPutRequest.new(
  id: 3,
  employee_id: 10,
  civil_status: married,
  number_of_dependants: 2
)
```

