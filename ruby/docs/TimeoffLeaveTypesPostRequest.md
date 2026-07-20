# F::TimeoffLeaveTypesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **accrues** | **Boolean** | Whether the leave type accrues over time |  |
| **approval_required** | **Boolean** | Whether approval is required for this leave type |  |
| **identifier** | **String** | A unique identifier for the leave type |  |
| **attachment** | **Boolean** | Whether an attachment is required for this leave type | [optional] |
| **color** | **String** | The color associated with this leave type |  |
| **name** | **String** | The name of the leave type |  |
| **visibility** | **Boolean** | Whether the leave type is visible to employees | [optional] |
| **workable** | **Boolean** | Whether the leave type is workable (can be worked on during leave) |  |
| **payable** | **Boolean** | Whether the leave type is payable | [optional] |
| **is_attachment_mandatory** | **Boolean** | Whether the attachment is mandatory | [optional] |
| **half_days_units_enabled** | **Boolean** | Whether half-day units are enabled for this leave type | [optional] |
| **max_days_in_cents** | **Integer** | Maximum days in cents that can be taken | [optional] |
| **min_days_in_cents** | **Integer** | Minimum days in cents that must be taken | [optional] |
| **company_id** | **String** | Identifier of the company associated with this leave type |  |
| **editable** | **Boolean** | Whether the leave type is editable | [optional] |
| **allow_endless** | **Boolean** | Whether endless leave is allowed | [optional] |
| **restricted** | **Boolean** | Whether the leave type is restricted | [optional] |
| **description** | **String** | Description of the leave type | [optional] |
| **details_required** | **Boolean** | Whether additional details are required for the leave type |  |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffLeaveTypesPostRequest.new(
  accrues: true,
  approval_required: true,
  identifier: custom,
  attachment: true,
  color: red,
  name: Sick Leave,
  visibility: true,
  workable: false,
  payable: true,
  is_attachment_mandatory: false,
  half_days_units_enabled: true,
  max_days_in_cents: 5000,
  min_days_in_cents: 1000,
  company_id: 1,
  editable: true,
  allow_endless: false,
  restricted: false,
  description: Leave for sick days,
  details_required: false
)
```

