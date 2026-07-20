# F::ShiftManagementShift

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier for the shift |  |
| **company_id** | **String** | Identifier of the company that owns this shift |  |
| **name** | **String** | Display name of the shift. If not explicitly set, falls back to the default shift title or template week name | [optional] |
| **state** | **String** | Current state of the shift. &#39;draft&#39; means the shift is not yet visible to employees, &#39;published&#39; means it&#39;s visible and confirmed, &#39;backup&#39; indicates a backup shift that can be replaced |  |
| **location_id** | **String** | Identifier of the location where the shift takes place. Can be null if the shift uses the employee&#39;s default location | [optional] |
| **locations_work_area_id** | **String** | Identifier of the specific work area within the location where the shift occurs. Work areas allow further subdivision of locations | [optional] |
| **employee_id** | **String** | Identifier of the employee assigned to this shift |  |
| **start_at** | **String** | Timestamp indicating when the shift starts |  |
| **end_at** | **String** | Timestamp indicating when the shift ends |  |
| **notes** | **String** | Optional notes or comments about the shift, visible to managers and schedulers | [optional] |
| **extra_hours** | **Boolean** | Indicates whether this shift counts as extra hours beyond the employee&#39;s regular schedule. Used for overtime calculations |  |
| **default_shift_title** | **String** | Title from the default shift template that was used to create this shift, if applicable | [optional] |
| **timezone** | **String** | IANA timezone identifier (e.g., &#39;Europe/Madrid&#39;, &#39;America/New_York&#39;) used to display the shift times in the local timezone |  |
| **local_start_at** | **String** | Start time of the shift converted to the local timezone. This is what employees see in their schedule |  |
| **local_end_at** | **String** | End time of the shift converted to the local timezone. This is what employees see in their schedule |  |

## Example

```ruby
require 'factorial_api'

instance = F::ShiftManagementShift.new(
  id: 1,
  company_id: 1,
  name: Morning shift,
  state: draft,
  location_id: 3,
  locations_work_area_id: 5,
  employee_id: 1,
  start_at: 2020-09-07T06:00:00.000+00:00,
  end_at: 2020-09-07T15:00:00.000+00:00,
  notes: This is a shift note,
  extra_hours: false,
  default_shift_title: Morning shift,
  timezone: Europe/Madrid,
  local_start_at: 2020-09-07T08:00:00.000+00:00,
  local_end_at: 2020-09-07T17:00:00.000+00:00
)
```

