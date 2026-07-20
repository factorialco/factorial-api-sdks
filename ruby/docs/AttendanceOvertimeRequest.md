# F::AttendanceOvertimeRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **employee_id** | **String** |  |  |
| **approver_id** | **String** |  | [optional] |
| **author_id** | **String** |  |  |
| **status** | **String** |  |  |
| **description** | **String** |  | [optional] |
| **reason** | **String** |  | [optional] |
| **date** | **String** |  |  |
| **hours_amount_in_cents** | **Integer** |  |  |
| **created_at** | **String** |  | [optional] |
| **approver** | **Boolean** |  |  |
| **approver_full_name** | **String** |  | [optional] |
| **is_editable** | **Boolean** | Defines if the overtime request can be edited |  |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceOvertimeRequest.new(
  id: null,
  employee_id: null,
  approver_id: null,
  author_id: null,
  status: null,
  description: null,
  reason: null,
  date: null,
  hours_amount_in_cents: null,
  created_at: null,
  approver: null,
  approver_full_name: null,
  is_editable: null
)
```

