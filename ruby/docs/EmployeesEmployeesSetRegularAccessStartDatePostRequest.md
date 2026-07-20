# F::EmployeesEmployeesSetRegularAccessStartDatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | id of the employee. |  |
| **starts_on** | **String** | the date the employee will start working in the company. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::EmployeesEmployeesSetRegularAccessStartDatePostRequest.new(
  id: 1,
  starts_on: 2024-10-06
)
```

