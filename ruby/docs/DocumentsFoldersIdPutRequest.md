# F::DocumentsFoldersIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **company_id** | **String** | Company ID |  |
| **id** | **String** | Folder id |  |
| **name** | **String** | Folder name |  |

## Example

```ruby
require 'factorial_api'

instance = F::DocumentsFoldersIdPutRequest.new(
  company_id: 1,
  id: 3,
  name: New folder name
)
```

