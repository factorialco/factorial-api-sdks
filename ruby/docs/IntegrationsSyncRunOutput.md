# F::IntegrationsSyncRunOutput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the sync run output |  |
| **sync_run_id** | **String** | Identifier of the sync run this output belongs to |  |
| **file_name** | **String** | Name of the uploaded file |  |
| **created_at** | **String** | Timestamp when the sync run output was created |  |

## Example

```ruby
require 'factorial_api'

instance = F::IntegrationsSyncRunOutput.new(
  id: 1,
  sync_run_id: 1,
  file_name: sync_output.csv,
  created_at: 2024-01-20T18:05:45.000Z
)
```

