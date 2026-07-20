# F::AttendanceShiftsAutofillPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_ids** | **Array&lt;String&gt;** | Ids of the employees to be autofilled |  |
| **start_on** | **String** | Date to start autofilling |  |
| **end_on** | **String** | Date to end autofilling |  |
| **source** | **String** | Source of the shift creation | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceShiftsAutofillPostRequest.new(
  employee_ids: [&quot;1&quot;,&quot;2&quot;,&quot;3&quot;],
  start_on: 2022-01-01,
  end_on: 2022-01-01,
  source: desktop
)
```

