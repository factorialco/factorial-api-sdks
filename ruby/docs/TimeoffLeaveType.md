# F::TimeoffLeaveType

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the leave type |  |
| **name** | **String** | Name of the leave type |  |
| **translated_name** | **String** | Translated name of the leave type, if available | [optional] |
| **identifier** | **String** | Unique identifier of the leave type |  |
| **color** | **String** | The color associated with this leave type |  |
| **active** | **Boolean** | Whether the leave type is active | [optional] |
| **editable** | **Boolean** | Whether the leave type is editable | [optional] |
| **approval_required** | **Boolean** | Whether approval is required for this leave type | [optional] |
| **accrues** | **Boolean** | Whether the leave type accrues over time | [optional] |
| **attachment** | **Boolean** | Whether an attachment is required for this leave type |  |
| **allow_endless** | **Boolean** | Whether endless leave is allowed | [optional] |
| **restricted** | **Boolean** | Whether the leave type is restricted | [optional] |
| **visibility** | **Boolean** | Whether the leave type is visible to employees |  |
| **workable** | **Boolean** | Whether the leave type is workable |  |
| **payable** | **Boolean** | Whether the leave type is payable | [optional] |
| **company_id** | **String** | Identifier of the company associated with this leave type |  |
| **is_attachment_mandatory** | **Boolean** | Whether the attachment is mandatory | [optional] |
| **allowance_ids** | **Array&lt;String&gt;** | List of allowance identifiers associated with this leave type |  |
| **half_days_units_enabled** | **Boolean** | Whether half-day units are enabled for this leave type | [optional] |
| **max_days_in_cents** | **Integer** | Maximum days in cents that can be taken | [optional] |
| **min_days_in_cents** | **Integer** | Minimum days in cents that must be taken | [optional] |
| **description** | **String** | Description of the leave type | [optional] |
| **details_required** | **Boolean** | Whether additional details are required for the leave type |  |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffLeaveType.new(
  id: 1,
  name: Annual Leave,
  translated_name: Congé Annuel,
  identifier: annual_leave,
  color: red,
  active: true,
  editable: false,
  approval_required: true,
  accrues: true,
  attachment: true,
  allow_endless: false,
  restricted: false,
  visibility: true,
  workable: false,
  payable: true,
  company_id: 1,
  is_attachment_mandatory: false,
  allowance_ids: [1, 2],
  half_days_units_enabled: true,
  max_days_in_cents: 5000,
  min_days_in_cents: 1000,
  description: This leave type is for annual holidays.,
  details_required: false
)
```

