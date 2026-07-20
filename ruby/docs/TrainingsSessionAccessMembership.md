# F::TrainingsSessionAccessMembership

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | ID of this membership |  |
| **access_id** | **String** | ID of the access associated with this membership |  |
| **employee_id** | **String** | ID of the employee associated with this membership | [optional] |
| **session_id** | **String** | ID of the session associated with this membership |  |
| **first_name** | **String** | First name of the user associated with this membership | [optional] |
| **last_name** | **String** | Last name of the user associated with this membership | [optional] |
| **job_title** | **String** | Job title of the user associated with this membership | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsSessionAccessMembership.new(
  id: 1,
  access_id: 1,
  employee_id: 1,
  session_id: 1,
  first_name: John,
  last_name: Doe,
  job_title: Manager
)
```

