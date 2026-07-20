# F::DocumentsFoldersPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **company_id** | **String** | Company ID |  |
| **name** | **String** | Folder name |  |
| **space** | **String** | The space of the folder is related to the type of documents that will be stored in it. You should always use \&quot;employee_my_documents\&quot; |  |

## Example

```ruby
require 'factorial_api'

instance = F::DocumentsFoldersPostRequest.new(
  company_id: 1,
  name: Payslips,
  space: employee_my_documents
)
```

