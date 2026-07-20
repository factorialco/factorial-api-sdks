# F::ApprovalsMaterializedApprovalsFlow

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **author_id** | **String** |  |  |
| **author_employee_id** | **String** |  | [optional] |
| **owner_id** | **String** |  |  |
| **owner_employee_id** | **String** |  | [optional] |
| **resource_type** | **String** |  |  |
| **resource_id** | **String** |  |  |
| **resource_url** | **String** |  |  |
| **status** | **String** |  |  |
| **expires_at** | **String** |  |  |
| **final_decision_at** | **String** |  | [optional] |
| **approval_flow_id** | **String** |  |  |
| **approvers** | **Array&lt;Object&gt;** |  |  |
| **email_detail_blocks** | **Array&lt;String&gt;** |  |  |
| **override_approver_id** | **String** |  | [optional] |
| **override_approver_employee_id** | **String** |  | [optional] |
| **rules_decision** | **String** |  | [optional] |
| **auto_approval_description** | **String** |  | [optional] |
| **action_type** | **String** |  | [optional] |
| **reason** | **String** |  | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ApprovalsMaterializedApprovalsFlow.new(
  id: null,
  author_id: null,
  author_employee_id: null,
  owner_id: null,
  owner_employee_id: null,
  resource_type: null,
  resource_id: null,
  resource_url: null,
  status: null,
  expires_at: null,
  final_decision_at: null,
  approval_flow_id: null,
  approvers: null,
  email_detail_blocks: null,
  override_approver_id: null,
  override_approver_employee_id: null,
  rules_decision: null,
  auto_approval_description: null,
  action_type: null,
  reason: null
)
```

