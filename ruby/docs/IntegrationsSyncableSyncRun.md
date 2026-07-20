# F::IntegrationsSyncableSyncRun

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the syncable sync run |  |
| **status** | **String** | Status of the syncable sync run |  |
| **error_messages** | **Array&lt;Object&gt;** | Error or validation messages of the syncable sync run |  |
| **sync_run_id** | **String** | Identifier of the sync run |  |
| **company_id** | **String** | Identifier of the company |  |

## Example

```ruby
require 'factorial_api'

instance = F::IntegrationsSyncableSyncRun.new(
  id: 1,
  status: failed,
  error_messages: [{key&#x3D;sync_api_error, value&#x3D;Api sync error}, {key&#x3D;sync_validation_error, value&#x3D;Missing payroll concept code}],
  sync_run_id: 1,
  company_id: 1
)
```

