# F::PerformanceAgreement

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Action plan ID |  |
| **process_id** | **String** | Review process ID |  |
| **target_id** | **String** | Review process target ID |  |
| **signer_id** | **String** | Manager access ID who signed the action plan | [optional] |
| **reviewer_id** | **String** | Manager employee ID | [optional] |
| **manager_signed_at** | **String** | Date when the manager signed the action plan | [optional] |
| **target_signed_at** | **String** | Date when the employee signed the action plan | [optional] |
| **agreement_signed_at** | **String** | Date when the action plan was last signed | [optional] |
| **last_modified_at** | **String** | Date when the action plan was last modified | [optional] |
| **status** | **String** | Action plan status |  |
| **locked** | **Boolean** | When the action plan cannot be edited anymore. Locked when both manager and employee signed it. |  |
| **conclusions** | **Object** | Conclusions of the action plan | [optional] |
| **self_evaluation_id** | **String** | Self review evaluation ID | [optional] |
| **manager_evaluation_id** | **String** | Manager review evaluation ID | [optional] |
| **self_comments** | **Array&lt;Object&gt;** | Self comments by question |  |
| **manager_comments** | **Array&lt;Object&gt;** | Manager comments by question |  |

## Example

```ruby
require 'factorial_api'

instance = F::PerformanceAgreement.new(
  id: 1,
  process_id: 1,
  target_id: 1-3,
  signer_id: 5,
  reviewer_id: 3,
  manager_signed_at: 2024-01-01T00:00:00Z,
  target_signed_at: 2024-01-01T00:00:00Z,
  agreement_signed_at: 2024-01-01T00:00:00Z,
  last_modified_at: 2024-01-01T00:00:00Z,
  status: signed,
  locked: true,
  conclusions: {text&#x3D;The employee is doing well., last_updated_at&#x3D;2024-01-01T00:00:00Z},
  self_evaluation_id: 1,
  manager_evaluation_id: 2,
  self_comments: [{question_uuid&#x3D;z69c9b4d-0aa6-4ada-89d5-5fdcb04c1327, author_access_id&#x3D;8, text&#x3D;I am a team player., updated_at&#x3D;2024-01-01T00:00:00Z}],
  manager_comments: [{question_uuid&#x3D;a347a2fd-1a0a-4eee-b6c8-f74be63624fb, author_access_id&#x3D;5, text&#x3D;The employee is doing well., updated_at&#x3D;2024-01-01T00:00:00Z}]
)
```

