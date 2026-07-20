# F::AttendanceShiftsBreakEndPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_id** | **String** | Employee id of the break | [optional] |
| **now** | **String** | Current time of the break |  |
| **observations** | **String** | Observations of the break | [optional] |
| **project_worker_id** | **String** |  | [optional] |
| **subproject_id** | **String** |  | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceShiftsBreakEndPostRequest.new(
  employee_id: 1,
  now: 2022-06-23T11:00:00.000+00:00,
  observations: break observation,
  project_worker_id: null,
  subproject_id: null
)
```

