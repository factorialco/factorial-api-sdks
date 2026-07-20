# F::DocumentsFolderApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**documents_folders_get**](DocumentsFolderApi.md#documents_folders_get) | **GET** /api/2026-07-01/resources/documents/folders | Reads all Folders |
| [**documents_folders_id_get**](DocumentsFolderApi.md#documents_folders_id_get) | **GET** /api/2026-07-01/resources/documents/folders/{id} | Reads a single Folder |
| [**documents_folders_id_put**](DocumentsFolderApi.md#documents_folders_id_put) | **PUT** /api/2026-07-01/resources/documents/folders/{id} | Updates a Folder |
| [**documents_folders_post**](DocumentsFolderApi.md#documents_folders_post) | **POST** /api/2026-07-01/resources/documents/folders | Creates a Folder |


## documents_folders_get

> <DocumentsFoldersGet200Response> documents_folders_get(opts)

Reads all Folders

Get all folders.

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

api_instance = F::DocumentsFolderApi.new
opts = {
  active: true, # Boolean | Active folder.
  employee_id: '15', # String | Employee id
  ids: ['inner_example'], # Array<String> | ids of the folders.
  name: 'Payslips' # String | Name of the folder.
}

begin
  # Reads all Folders
  result = api_instance.documents_folders_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling DocumentsFolderApi->documents_folders_get: #{e}"
end
```

#### Using the documents_folders_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DocumentsFoldersGet200Response>, Integer, Hash)> documents_folders_get_with_http_info(opts)

```ruby
begin
  # Reads all Folders
  data, status_code, headers = api_instance.documents_folders_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DocumentsFoldersGet200Response>
rescue F::ApiError => e
  puts "Error when calling DocumentsFolderApi->documents_folders_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **active** | **Boolean** | Active folder. | [optional] |
| **employee_id** | **String** | Employee id | [optional] |
| **ids** | [**Array&lt;String&gt;**](String.md) | ids of the folders. | [optional] |
| **name** | **String** | Name of the folder. | [optional] |

### Return type

[**DocumentsFoldersGet200Response**](DocumentsFoldersGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## documents_folders_id_get

> <DocumentsFolder> documents_folders_id_get(id)

Reads a single Folder

Get all folders.

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

api_instance = F::DocumentsFolderApi.new
id = '10' # String | ids of the folders.

begin
  # Reads a single Folder
  result = api_instance.documents_folders_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling DocumentsFolderApi->documents_folders_id_get: #{e}"
end
```

#### Using the documents_folders_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DocumentsFolder>, Integer, Hash)> documents_folders_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Folder
  data, status_code, headers = api_instance.documents_folders_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DocumentsFolder>
rescue F::ApiError => e
  puts "Error when calling DocumentsFolderApi->documents_folders_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | ids of the folders. |  |

### Return type

[**DocumentsFolder**](DocumentsFolder.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## documents_folders_id_put

> <DocumentsFolder> documents_folders_id_put(id, opts)

Updates a Folder

Update a folder.

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

api_instance = F::DocumentsFolderApi.new
id = '3' # String | Folder id
opts = {
  documents_folders_id_put_request: F::DocumentsFoldersIdPutRequest.new({company_id: '1', id: '3', name: 'New folder name'}) # DocumentsFoldersIdPutRequest | 
}

begin
  # Updates a Folder
  result = api_instance.documents_folders_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling DocumentsFolderApi->documents_folders_id_put: #{e}"
end
```

#### Using the documents_folders_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DocumentsFolder>, Integer, Hash)> documents_folders_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Folder
  data, status_code, headers = api_instance.documents_folders_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DocumentsFolder>
rescue F::ApiError => e
  puts "Error when calling DocumentsFolderApi->documents_folders_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Folder id |  |
| **documents_folders_id_put_request** | [**DocumentsFoldersIdPutRequest**](DocumentsFoldersIdPutRequest.md) |  | [optional] |

### Return type

[**DocumentsFolder**](DocumentsFolder.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## documents_folders_post

> <DocumentsFolder> documents_folders_post(opts)

Creates a Folder

Create a folder.

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

api_instance = F::DocumentsFolderApi.new
opts = {
  documents_folders_post_request: F::DocumentsFoldersPostRequest.new({company_id: '1', name: 'Payslips', space: 'employee_my_documents'}) # DocumentsFoldersPostRequest | 
}

begin
  # Creates a Folder
  result = api_instance.documents_folders_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling DocumentsFolderApi->documents_folders_post: #{e}"
end
```

#### Using the documents_folders_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DocumentsFolder>, Integer, Hash)> documents_folders_post_with_http_info(opts)

```ruby
begin
  # Creates a Folder
  data, status_code, headers = api_instance.documents_folders_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DocumentsFolder>
rescue F::ApiError => e
  puts "Error when calling DocumentsFolderApi->documents_folders_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **documents_folders_post_request** | [**DocumentsFoldersPostRequest**](DocumentsFoldersPostRequest.md) |  | [optional] |

### Return type

[**DocumentsFolder**](DocumentsFolder.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

