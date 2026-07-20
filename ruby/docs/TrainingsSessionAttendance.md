# F::TrainingsSessionAttendance

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier of the session attendance |  |
| **status** | **String** | Status of the session attendance |  |
| **session_access_membership_id** | **String** | Identifier of the session access membership |  |
| **access_id** | **String** | Identifier of the access associated with the employee |  |
| **employee_id** | **String** | Identifier of the employee | [optional] |
| **completed_duration** | **String** | Completed duration in hours (decimal format, e.g. 1.5 means 1h 30m). Null when session attendance status is not completed. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsSessionAttendance.new(
  id: 1,
  status: completed,
  session_access_membership_id: 1,
  access_id: 20,
  employee_id: 20,
  completed_duration: 1.5
)
```

