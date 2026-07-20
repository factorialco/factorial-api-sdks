# F::ApprovalsMaterializedApprovalsFlowsApproveResourcePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **resource_id** | **String** | Id of the resource to approve. |  |
| **resource_type** | **String** | Type of the resource to approve (e.g. Timeoff::Leave). |  |

## Example

```ruby
require 'factorial_api'

instance = F::ApprovalsMaterializedApprovalsFlowsApproveResourcePostRequest.new(
  resource_id: 1,
  resource_type: Timeoff::Leave
)
```

