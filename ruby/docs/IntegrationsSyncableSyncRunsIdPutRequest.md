# F::IntegrationsSyncableSyncRunsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the syncable sync run |  |
| **status** | **String** | Status of the syncable sync run |  |
| **error_messages** | **Object** | Error or validation messages of the syncable sync run | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::IntegrationsSyncableSyncRunsIdPutRequest.new(
  id: 1,
  status: failed,
  error_messages: {&quot;sync_api_error&quot;:&quot;Api sync error&quot;,&quot;sync_validation_error&quot;:&quot;Missing payroll concept code&quot;}
)
```

