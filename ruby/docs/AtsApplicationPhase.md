# F::AtsApplicationPhase

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the application Phase |  |
| **ats_job_posting_id** | **String** | Job posting of the application phase |  |
| **name** | **String** | Name of the application phase |  |
| **position** | **Integer** | Position of the application phase |  |
| **editable** | **Boolean** | If the application phase is editable |  |
| **phase_type** | **String** | Application phase type |  |
| **applications_count** | **Integer** | Active application count | [optional] |
| **active_applications_count** | **Integer** |  | [optional] |
| **ats_hiring_stage_id** | **String** | Hiring stage identifier | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsApplicationPhase.new(
  id: 1,
  ats_job_posting_id: 1,
  name: In review,
  position: 1,
  editable: true,
  phase_type: Screening,
  applications_count: 1,
  active_applications_count: null,
  ats_hiring_stage_id: 1
)
```

