# F::DocumentsDocumentApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**documents_documents_get**](DocumentsDocumentApi.md#documents_documents_get) | **GET** /api/2026-07-01/resources/documents/documents | Reads all Documents |
| [**documents_documents_id_delete**](DocumentsDocumentApi.md#documents_documents_id_delete) | **DELETE** /api/2026-07-01/resources/documents/documents/{id} | Deletes a Document |
| [**documents_documents_id_get**](DocumentsDocumentApi.md#documents_documents_id_get) | **GET** /api/2026-07-01/resources/documents/documents/{id} | Reads a single Document |
| [**documents_documents_id_put**](DocumentsDocumentApi.md#documents_documents_id_put) | **PUT** /api/2026-07-01/resources/documents/documents/{id} | Updates a Document |
| [**documents_documents_move_to_trash_bin_post**](DocumentsDocumentApi.md#documents_documents_move_to_trash_bin_post) | **POST** /api/2026-07-01/resources/documents/documents/move_to_trash_bin | Move to trash bins a Document |
| [**documents_documents_post**](DocumentsDocumentApi.md#documents_documents_post) | **POST** /api/2026-07-01/resources/documents/documents | Creates a Document |
| [**documents_documents_restore_from_trash_bin_post**](DocumentsDocumentApi.md#documents_documents_restore_from_trash_bin_post) | **POST** /api/2026-07-01/resources/documents/documents/restore_from_trash_bin | Restore from trash bins a Document |


## documents_documents_get

> <DocumentsDocumentsGet200Response> documents_documents_get(by_pending_assignment, by_trash_bin, opts)

Reads all Documents

Reads all Documents

### Examples

```ruby
require 'time'
require 'factorial_api'
# setup authorization
F.configure do |config|
  # Configure API key authorization: apikey
  config.api_key['x-api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x-api-key'] = 'Bearer'

  # Configure OAuth2 access token for authorization: oauth2
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = F::DocumentsDocumentApi.new
by_pending_assignment = true # Boolean | flag to indicate if the document is pending assignment.
by_trash_bin = true # Boolean | flag to indicate if the document is in the trash bin.
opts = {
  by_bookkeeper_documents: true, # Boolean | flag to indicate if the document belongs to a bookkeeper.
  by_without_folder: true, # Boolean | flag to indicate if the document doesn't have a folder.
  employee_ids: ['inner_example'], # Array<String> | list of employee identifiers.
  folder_id: '1', # String | folder identifier.
  ids: ['inner_example'], # Array<String> | list of document identifiers.
  leave_id: '1' # String | leave identifier associated to the document, refers to /timeoff/leaves endpoint.
}

begin
  # Reads all Documents
  result = api_instance.documents_documents_get(by_pending_assignment, by_trash_bin, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling DocumentsDocumentApi->documents_documents_get: #{e}"
end
```

#### Using the documents_documents_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DocumentsDocumentsGet200Response>, Integer, Hash)> documents_documents_get_with_http_info(by_pending_assignment, by_trash_bin, opts)

```ruby
begin
  # Reads all Documents
  data, status_code, headers = api_instance.documents_documents_get_with_http_info(by_pending_assignment, by_trash_bin, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DocumentsDocumentsGet200Response>
rescue F::ApiError => e
  puts "Error when calling DocumentsDocumentApi->documents_documents_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **by_pending_assignment** | **Boolean** | flag to indicate if the document is pending assignment. |  |
| **by_trash_bin** | **Boolean** | flag to indicate if the document is in the trash bin. |  |
| **by_bookkeeper_documents** | **Boolean** | flag to indicate if the document belongs to a bookkeeper. | [optional] |
| **by_without_folder** | **Boolean** | flag to indicate if the document doesn&#39;t have a folder. | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | list of employee identifiers. | [optional] |
| **folder_id** | **String** | folder identifier. | [optional] |
| **ids** | [**Array&lt;String&gt;**](String.md) | list of document identifiers. | [optional] |
| **leave_id** | **String** | leave identifier associated to the document, refers to /timeoff/leaves endpoint. | [optional] |

### Return type

[**DocumentsDocumentsGet200Response**](DocumentsDocumentsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## documents_documents_id_delete

> <DocumentsDocument> documents_documents_id_delete(id)

Deletes a Document

Deletes a Document

### Examples

```ruby
require 'time'
require 'factorial_api'
# setup authorization
F.configure do |config|
  # Configure API key authorization: apikey
  config.api_key['x-api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x-api-key'] = 'Bearer'

  # Configure OAuth2 access token for authorization: oauth2
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = F::DocumentsDocumentApi.new
id = '1' # String | 

begin
  # Deletes a Document
  result = api_instance.documents_documents_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling DocumentsDocumentApi->documents_documents_id_delete: #{e}"
end
```

#### Using the documents_documents_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DocumentsDocument>, Integer, Hash)> documents_documents_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Document
  data, status_code, headers = api_instance.documents_documents_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DocumentsDocument>
rescue F::ApiError => e
  puts "Error when calling DocumentsDocumentApi->documents_documents_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**DocumentsDocument**](DocumentsDocument.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## documents_documents_id_get

> <DocumentsDocument> documents_documents_id_get(id)

Reads a single Document

Reads a single Document

### Examples

```ruby
require 'time'
require 'factorial_api'
# setup authorization
F.configure do |config|
  # Configure API key authorization: apikey
  config.api_key['x-api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x-api-key'] = 'Bearer'

  # Configure OAuth2 access token for authorization: oauth2
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = F::DocumentsDocumentApi.new
id = '1' # String | list of document identifiers.

begin
  # Reads a single Document
  result = api_instance.documents_documents_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling DocumentsDocumentApi->documents_documents_id_get: #{e}"
end
```

#### Using the documents_documents_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DocumentsDocument>, Integer, Hash)> documents_documents_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Document
  data, status_code, headers = api_instance.documents_documents_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DocumentsDocument>
rescue F::ApiError => e
  puts "Error when calling DocumentsDocumentApi->documents_documents_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | list of document identifiers. |  |

### Return type

[**DocumentsDocument**](DocumentsDocument.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## documents_documents_id_put

> <DocumentsDocument> documents_documents_id_put(id, opts)

Updates a Document

Updates a Document

### Examples

```ruby
require 'time'
require 'factorial_api'
# setup authorization
F.configure do |config|
  # Configure API key authorization: apikey
  config.api_key['x-api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x-api-key'] = 'Bearer'

  # Configure OAuth2 access token for authorization: oauth2
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = F::DocumentsDocumentApi.new
id = '1' # String | document identifiers.
opts = {
  documents_documents_id_put_request: F::DocumentsDocumentsIdPutRequest.new({id: '1', public: true, request_esignature: true, signee_ids: [1,  2,  3]}) # DocumentsDocumentsIdPutRequest | 
}

begin
  # Updates a Document
  result = api_instance.documents_documents_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling DocumentsDocumentApi->documents_documents_id_put: #{e}"
end
```

#### Using the documents_documents_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DocumentsDocument>, Integer, Hash)> documents_documents_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Document
  data, status_code, headers = api_instance.documents_documents_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DocumentsDocument>
rescue F::ApiError => e
  puts "Error when calling DocumentsDocumentApi->documents_documents_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | document identifiers. |  |
| **documents_documents_id_put_request** | [**DocumentsDocumentsIdPutRequest**](DocumentsDocumentsIdPutRequest.md) |  | [optional] |

### Return type

[**DocumentsDocument**](DocumentsDocument.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## documents_documents_move_to_trash_bin_post

> <Array<DocumentsDocument>> documents_documents_move_to_trash_bin_post(opts)

Move to trash bins a Document

This endpoint moves the documents to the trash bin, after 30 days they will be deleted from the system.

### Examples

```ruby
require 'time'
require 'factorial_api'
# setup authorization
F.configure do |config|
  # Configure API key authorization: apikey
  config.api_key['x-api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x-api-key'] = 'Bearer'

  # Configure OAuth2 access token for authorization: oauth2
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = F::DocumentsDocumentApi.new
opts = {
  documents_documents_move_to_trash_bin_post_request: F::DocumentsDocumentsMoveToTrashBinPostRequest.new({document_ids: [1,  2,  3]}) # DocumentsDocumentsMoveToTrashBinPostRequest | 
}

begin
  # Move to trash bins a Document
  result = api_instance.documents_documents_move_to_trash_bin_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling DocumentsDocumentApi->documents_documents_move_to_trash_bin_post: #{e}"
end
```

#### Using the documents_documents_move_to_trash_bin_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<DocumentsDocument>>, Integer, Hash)> documents_documents_move_to_trash_bin_post_with_http_info(opts)

```ruby
begin
  # Move to trash bins a Document
  data, status_code, headers = api_instance.documents_documents_move_to_trash_bin_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<DocumentsDocument>>
rescue F::ApiError => e
  puts "Error when calling DocumentsDocumentApi->documents_documents_move_to_trash_bin_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **documents_documents_move_to_trash_bin_post_request** | [**DocumentsDocumentsMoveToTrashBinPostRequest**](DocumentsDocumentsMoveToTrashBinPostRequest.md) |  | [optional] |

### Return type

[**Array&lt;DocumentsDocument&gt;**](DocumentsDocument.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## documents_documents_post

> <DocumentsDocument> documents_documents_post(public, space, is_pending_assignment, file, author_id, company_id, signee_ids, request_esignature, opts)

Creates a Document

Creates a Document

### Examples

```ruby
require 'time'
require 'factorial_api'
# setup authorization
F.configure do |config|
  # Configure API key authorization: apikey
  config.api_key['x-api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x-api-key'] = 'Bearer'

  # Configure OAuth2 access token for authorization: oauth2
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = F::DocumentsDocumentApi.new
public = true # Boolean | flag to indicate if the document is public.
space = 'employee_my_documents' # String | document space, in case of employee_my_documents it's necessary to fill employee_id.
is_pending_assignment = true # Boolean | flag that indicates if the document is pending assignment.
file = File.new('/path/to/some/file') # File | file to upload, the binary file.
author_id = 'author_id_example' # String | access identifier of the author, refers to /employees/employees endpoint.
company_id = 'company_id_example' # String | company identifier, refers to /api/me endpoint.
signee_ids = ['inner_example'] # Array<String> | list of user access identifiers associated to the document, refers to /employees/employees endpoint.
request_esignature = true # Boolean | flag to indicate if the document requires an electronic signature.
opts = {
  folder_id: 'folder_id_example', # String | folder identifier, references to documents/folders endpoint.
  file_filename: 'file_filename_example', # String | final name of the file, even if the file has been uploaded with a different name.
  leave_id: 'leave_id_example', # String | leave identifier associated to the document, refers to /timeoff/leaves endpoint.
  employee_id: 'employee_id_example' # String | employee identifier associated to the document.
}

begin
  # Creates a Document
  result = api_instance.documents_documents_post(public, space, is_pending_assignment, file, author_id, company_id, signee_ids, request_esignature, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling DocumentsDocumentApi->documents_documents_post: #{e}"
end
```

#### Using the documents_documents_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DocumentsDocument>, Integer, Hash)> documents_documents_post_with_http_info(public, space, is_pending_assignment, file, author_id, company_id, signee_ids, request_esignature, opts)

```ruby
begin
  # Creates a Document
  data, status_code, headers = api_instance.documents_documents_post_with_http_info(public, space, is_pending_assignment, file, author_id, company_id, signee_ids, request_esignature, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DocumentsDocument>
rescue F::ApiError => e
  puts "Error when calling DocumentsDocumentApi->documents_documents_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **public** | **Boolean** | flag to indicate if the document is public. |  |
| **space** | **String** | document space, in case of employee_my_documents it&#39;s necessary to fill employee_id. |  |
| **is_pending_assignment** | **Boolean** | flag that indicates if the document is pending assignment. |  |
| **file** | **File** | file to upload, the binary file. |  |
| **author_id** | **String** | access identifier of the author, refers to /employees/employees endpoint. |  |
| **company_id** | **String** | company identifier, refers to /api/me endpoint. |  |
| **signee_ids** | [**Array&lt;String&gt;**](String.md) | list of user access identifiers associated to the document, refers to /employees/employees endpoint. |  |
| **request_esignature** | **Boolean** | flag to indicate if the document requires an electronic signature. |  |
| **folder_id** | **String** | folder identifier, references to documents/folders endpoint. | [optional] |
| **file_filename** | **String** | final name of the file, even if the file has been uploaded with a different name. | [optional] |
| **leave_id** | **String** | leave identifier associated to the document, refers to /timeoff/leaves endpoint. | [optional] |
| **employee_id** | **String** | employee identifier associated to the document. | [optional] |

### Return type

[**DocumentsDocument**](DocumentsDocument.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## documents_documents_restore_from_trash_bin_post

> <Array<DocumentsDocument>> documents_documents_restore_from_trash_bin_post(opts)

Restore from trash bins a Document

This endpoint restores the documents from the trash bin, remember that a document in the trash bin will be deleted from the system after 30 days.

### Examples

```ruby
require 'time'
require 'factorial_api'
# setup authorization
F.configure do |config|
  # Configure API key authorization: apikey
  config.api_key['x-api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x-api-key'] = 'Bearer'

  # Configure OAuth2 access token for authorization: oauth2
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = F::DocumentsDocumentApi.new
opts = {
  documents_documents_move_to_trash_bin_post_request: F::DocumentsDocumentsMoveToTrashBinPostRequest.new({document_ids: [1,  2,  3]}) # DocumentsDocumentsMoveToTrashBinPostRequest | 
}

begin
  # Restore from trash bins a Document
  result = api_instance.documents_documents_restore_from_trash_bin_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling DocumentsDocumentApi->documents_documents_restore_from_trash_bin_post: #{e}"
end
```

#### Using the documents_documents_restore_from_trash_bin_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<DocumentsDocument>>, Integer, Hash)> documents_documents_restore_from_trash_bin_post_with_http_info(opts)

```ruby
begin
  # Restore from trash bins a Document
  data, status_code, headers = api_instance.documents_documents_restore_from_trash_bin_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<DocumentsDocument>>
rescue F::ApiError => e
  puts "Error when calling DocumentsDocumentApi->documents_documents_restore_from_trash_bin_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **documents_documents_move_to_trash_bin_post_request** | [**DocumentsDocumentsMoveToTrashBinPostRequest**](DocumentsDocumentsMoveToTrashBinPostRequest.md) |  | [optional] |

### Return type

[**Array&lt;DocumentsDocument&gt;**](DocumentsDocument.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

