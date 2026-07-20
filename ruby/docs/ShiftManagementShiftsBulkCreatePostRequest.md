# F::ShiftManagementShiftsBulkCreatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **shifts** | **Array&lt;Object&gt;** | Array of shift objects to create. Each shift object represents a scheduled work period for an employee |  |
| **planned_breaks** | **Array&lt;Object&gt;** | An array of planned breaks to be added to the shifts created. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ShiftManagementShiftsBulkCreatePostRequest.new(
  shifts: null,
  planned_breaks: null
)
```

