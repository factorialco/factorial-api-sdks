# F::ApprovalsMaterializedApprovalsFlowsRejectResourcePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **resource_id** | **String** | Id of the resource to reject. |  |
| **resource_type** | **String** | Type of the resource to reject (e.g. Timeoff::Leave). |  |
| **reason** | **String** | Optional reason for the rejection. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ApprovalsMaterializedApprovalsFlowsRejectResourcePostRequest.new(
  resource_id: 1,
  resource_type: Timeoff::Leave,
  reason: Does not comply with policy
)
```

