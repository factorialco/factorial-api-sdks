# F::DocumentsFolder

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **active** | **Boolean** | Whether the folder is active or not |  |
| **company_id** | **String** | Company ID of the folder | [optional] |
| **id** | **String** | Folder ID |  |
| **name** | **String** | Folder name |  |
| **parent_folder_id** | **String** | Id of the parent folder | [optional] |
| **space** | **String** | The space of the folder is related to the place where the folder is displayed. |  |

## Example

```ruby
require 'factorial_api'

instance = F::DocumentsFolder.new(
  active: true,
  company_id: 1,
  id: 10,
  name: Payslips,
  parent_folder_id: 23,
  space: null
)
```

