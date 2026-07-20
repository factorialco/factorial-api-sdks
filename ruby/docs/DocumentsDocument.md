# F::DocumentsDocument

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **author_id** | **String** | access identifier of the author, refers to /employees/employees endpoint. | [optional] |
| **company_id** | **String** | company identifier, refers to /api/me endpoint. | [optional] |
| **content_type** | **String** | document content type. | [optional] |
| **created_at** | **String** | creation date of the document. |  |
| **employee_id** | **String** | employee identifier associated to the document. | [optional] |
| **extension** | **String** | document extension. | [optional] |
| **file_size** | **Integer** | document file size in bytes. | [optional] |
| **filename** | **String** | name of the document. |  |
| **folder_id** | **String** | folder identifier, references to documents/folders endpoint. | [optional] |
| **id** | **String** | document identifier. |  |
| **is_company_document** | **Boolean** | flag that indicates if the document is a company document. | [optional] |
| **is_management_document** | **Boolean** | flag that indicates if the document is a management document. | [optional] |
| **is_pending_assignment** | **Boolean** | flag that indicates if the document is pending assignment. | [optional] |
| **leave_id** | **String** | leave identifier associated to the document, refers to /timeoff/leaves endpoint. | [optional] |
| **public** | **Boolean** | flag to indicate if the document is public. |  |
| **signature_status** | **String** | document signature status. | [optional] |
| **signees** | **Array&lt;String&gt;** | list of signee access identifiers associated to the document, refers to /employees/employees endpoint. | [optional] |
| **space** | **String** | document space. |  |
| **updated_at** | **String** | last update date of the document. |  |
| **deleted_at** | **String** | deletion date of the document. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::DocumentsDocument.new(
  author_id: 1,
  company_id: 1,
  content_type: application/pdf,
  created_at: 2020-01-01T00:00:00Z,
  employee_id: 1,
  extension: pdf,
  file_size: 1024,
  filename: document.pdf,
  folder_id: 1,
  id: 1,
  is_company_document: true,
  is_management_document: true,
  is_pending_assignment: true,
  leave_id: 1,
  public: true,
  signature_status: pending,
  signees: null,
  space: company_public,
  updated_at: 2020-01-01T00:00:00Z,
  deleted_at: 2020-01-01T00:00:00Z
)
```

