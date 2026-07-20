# F::ShiftManagementShiftsBulkDeletePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | **Array&lt;String&gt;** | Filter shifts by their unique identifiers. Deletes only shifts matching the provided IDs. If not provided, uses other filters to determine which shifts to delete | [optional] |
| **start_at** | **String** | Filter shifts that end on or after this date. Only the date (calendar day) is used; the time part is ignored (treated as start of day, 00:00:00). Shifts are included if their end time is at or after the start of the specified day | [optional] |
| **end_at** | **String** | Filter shifts that start before this date. Only the date (calendar day) is used; the time part is ignored (treated as end of day, 23:59:59). Shifts are included if their start time is before the end of the specified day | [optional] |
| **employee_ids** | **Array&lt;String&gt;** | Filter shifts by employee identifiers. Deletes only shifts assigned to the specified employees. Can be combined with start_at and end_at for precise bulk deletion | [optional] |
| **destroy_backup_shifts** | **Boolean** | Also destroys shifts with status backup when true, which by default are being kept | [optional] |
| **author_id** | **String** | Identifier of the user/access who is performing the bulk delete operation. Used for audit purposes and tracking who deleted the shifts |  |

## Example

```ruby
require 'factorial_api'

instance = F::ShiftManagementShiftsBulkDeletePostRequest.new(
  ids: [&quot;1&quot;],
  start_at: 2020-01-01T15:00:00.000+00:00,
  end_at: 2020-12-31T15:00:00.000+00:00,
  employee_ids: [&quot;1&quot;],
  destroy_backup_shifts: true,
  author_id: 1781
)
```

