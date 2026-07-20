# F::DocumentsDocumentsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | document identifiers. |  |
| **public** | **Boolean** | flag to indicate if the document is public. |  |
| **employee_id** | **String** | employee identifier associated to the document. | [optional] |
| **folder_id** | **String** | folder identifier, references to documents/folders endpoint. | [optional] |
| **request_esignature** | **Boolean** | flag to indicate if the document requires an electronic signature. |  |
| **signee_ids** | **Array&lt;String&gt;** | list of user access identifiers associated to the document, refers to /employees/employees endpoint. |  |

## Example

```ruby
require 'factorial_api'

instance = F::DocumentsDocumentsIdPutRequest.new(
  id: 1,
  public: true,
  employee_id: 1,
  folder_id: 1,
  request_esignature: true,
  signee_ids: [1, 2, 3]
)
```

