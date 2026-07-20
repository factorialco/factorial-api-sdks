# F::AtsRejectionReason

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Rejection reason identifier |  |
| **company_id** | **String** | Company identifier of the rejection reason |  |
| **decision_maker** | **String** | Decision maker of the rejection reason |  |
| **reason** | **String** | Reason of the rejection |  |
| **created_at** | **String** | Rejection reason created date |  |
| **updated_at** | **String** | Rejection reason updated date |  |

## Example

```ruby
require 'factorial_api'

instance = F::AtsRejectionReason.new(
  id: 1,
  company_id: 1,
  decision_maker: candidate,
  reason: Unfit for the role,
  created_at: 2024-08-22T14:30:00-07:00,
  updated_at: 2024-08-22T14:30:00-07:00
)
```

