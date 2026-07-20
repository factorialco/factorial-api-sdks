# F::ShiftManagementShiftsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | Display name of the shift. If not explicitly set, falls back to the default shift title or template week name | [optional] |
| **start_at** | **String** | Timestamp indicating when the shift starts. Required parameter |  |
| **end_at** | **String** | Timestamp indicating when the shift ends. Required parameter |  |
| **notes** | **String** | Optional notes or comments about the shift, visible to managers and schedulers | [optional] |
| **employee_id** | **String** | Identifier of the employee assigned to this shift. Required parameter |  |
| **location_id** | **String** | Identifier of the location where the shift takes place. Can be null if the shift uses the employee&#39;s default location | [optional] |
| **work_area_id** | **String** | Identifier of the specific work area within the location where the shift occurs. Work areas allow further subdivision of locations | [optional] |
| **company_id** | **String** | Identifier of the company that owns this shift. Required parameter |  |

## Example

```ruby
require 'factorial_api'

instance = F::ShiftManagementShiftsPostRequest.new(
  name: Morning shift,
  start_at: 2020-09-07T06:00:00.000+00:00,
  end_at: 2020-09-07T15:00:00.000+00:00,
  notes: This is a shift note,
  employee_id: 1,
  location_id: 3,
  work_area_id: 5,
  company_id: 1
)
```

