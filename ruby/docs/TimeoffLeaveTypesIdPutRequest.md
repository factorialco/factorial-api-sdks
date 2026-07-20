# F::TimeoffLeaveTypesIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the leave type to update | [optional] |
| **accrues** | **Boolean** | Whether the leave type accrues over time | [optional] |
| **approval_required** | **Boolean** | Whether approval is required for this leave type | [optional] |
| **identifier** | **String** | A unique identifier for the leave type | [optional] |
| **attachment** | **Boolean** | Whether an attachment is required for this leave type | [optional] |
| **color** | **String** | The color associated with this leave type (hex code) | [optional] |
| **name** | **String** | The name of the leave type | [optional] |
| **visibility** | **Boolean** | Whether the leave type is visible to employees | [optional] |
| **workable** | **Boolean** | Whether the leave type is workable (can be worked on during leave) | [optional] |
| **payable** | **Boolean** | Whether the leave type is payable | [optional] |
| **is_attachment_mandatory** | [**Unknown**](Unknown.md) | Whether the attachment is mandatory or a status description (boolean or string) | [optional] |
| **half_days_units_enabled** | **Boolean** | Whether half-day units are enabled for this leave type | [optional] |
| **max_days_in_cents** | **Integer** | Maximum days in cents that can be taken | [optional] |
| **min_days_in_cents** | **Integer** | Minimum days in cents that must be taken | [optional] |
| **active** | **Boolean** | Whether the leave type is active | [optional] |
| **allow_endless** | **Boolean** | Whether endless leave is allowed | [optional] |
| **restricted** | **Boolean** | Whether the leave type is restricted | [optional] |
| **description** | **String** | Description of the leave type | [optional] |
| **details_required** | **Boolean** | Whether additional details are required for the leave type | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffLeaveTypesIdPutRequest.new(
  id: 5,
  accrues: true,
  approval_required: true,
  identifier: custom,
  attachment: true,
  color: red,
  name: Sick Leave,
  visibility: true,
  workable: false,
  payable: true,
  is_attachment_mandatory: null,
  half_days_units_enabled: true,
  max_days_in_cents: 5000,
  min_days_in_cents: 1000,
  active: true,
  allow_endless: false,
  restricted: false,
  description: Leave for sick days,
  details_required: false
)
```

