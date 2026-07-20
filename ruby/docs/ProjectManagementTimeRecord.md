# F::ProjectManagementTimeRecord

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id of the time record |  |
| **project_worker_id** | **String** | Id of the project worker |  |
| **attendance_shift_id** | **String** | Id of the attendance shift | [optional] |
| **subproject_id** | **String** | Id of the subproject | [optional] |
| **date** | **String** | Reference date of the shift | [optional] |
| **imputed_minutes** | **Integer** | Minutes difference between the clock in and clock out | [optional] |
| **clock_in** | **String** | Clock in time | [optional] |
| **clock_out** | **String** | Clock out time | [optional] |
| **observations** | **String** | Comment for the time record | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementTimeRecord.new(
  id: 1,
  project_worker_id: 1,
  attendance_shift_id: 1,
  subproject_id: 1,
  date: 2021-01-01,
  imputed_minutes: 480,
  clock_in: 2021-01-01T08:00:00Z,
  clock_out: 2021-01-01T17:00:00Z,
  observations: Comment for the time record
)
```

