# F::TasksTaskFileApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**tasks_task_files_get**](TasksTaskFileApi.md#tasks_task_files_get) | **GET** /api/2026-07-01/resources/tasks/task_files | Reads all Task files |
| [**tasks_task_files_id_delete**](TasksTaskFileApi.md#tasks_task_files_id_delete) | **DELETE** /api/2026-07-01/resources/tasks/task_files/{id} | Deletes a Task file |
| [**tasks_task_files_id_get**](TasksTaskFileApi.md#tasks_task_files_id_get) | **GET** /api/2026-07-01/resources/tasks/task_files/{id} | Reads a single Task file |
| [**tasks_task_files_post**](TasksTaskFileApi.md#tasks_task_files_post) | **POST** /api/2026-07-01/resources/tasks/task_files | Creates a Task file |


## tasks_task_files_get

> <TasksTaskFilesGet200Response> tasks_task_files_get(task_id, opts)

Reads all Task files

Reads all Task files

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

api_instance = F::TasksTaskFileApi.new
task_id = '1' # String | identifier of the task
opts = {
  ids: ['inner_example'] # Array<String> | identifiers of the files
}

begin
  # Reads all Task files
  result = api_instance.tasks_task_files_get(task_id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TasksTaskFileApi->tasks_task_files_get: #{e}"
end
```

#### Using the tasks_task_files_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TasksTaskFilesGet200Response>, Integer, Hash)> tasks_task_files_get_with_http_info(task_id, opts)

```ruby
begin
  # Reads all Task files
  data, status_code, headers = api_instance.tasks_task_files_get_with_http_info(task_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TasksTaskFilesGet200Response>
rescue F::ApiError => e
  puts "Error when calling TasksTaskFileApi->tasks_task_files_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **task_id** | **String** | identifier of the task |  |
| **ids** | [**Array&lt;String&gt;**](String.md) | identifiers of the files | [optional] |

### Return type

[**TasksTaskFilesGet200Response**](TasksTaskFilesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasks_task_files_id_delete

> <TasksTaskFile> tasks_task_files_id_delete(id)

Deletes a Task file

Deletes a Task file

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

api_instance = F::TasksTaskFileApi.new
id = '2' # String | identifier of the file

begin
  # Deletes a Task file
  result = api_instance.tasks_task_files_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TasksTaskFileApi->tasks_task_files_id_delete: #{e}"
end
```

#### Using the tasks_task_files_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TasksTaskFile>, Integer, Hash)> tasks_task_files_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Task file
  data, status_code, headers = api_instance.tasks_task_files_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TasksTaskFile>
rescue F::ApiError => e
  puts "Error when calling TasksTaskFileApi->tasks_task_files_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the file |  |

### Return type

[**TasksTaskFile**](TasksTaskFile.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasks_task_files_id_get

> <TasksTaskFile> tasks_task_files_id_get(id)

Reads a single Task file

Reads a single Task file

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

api_instance = F::TasksTaskFileApi.new
id = '1' # String | identifiers of the files

begin
  # Reads a single Task file
  result = api_instance.tasks_task_files_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TasksTaskFileApi->tasks_task_files_id_get: #{e}"
end
```

#### Using the tasks_task_files_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TasksTaskFile>, Integer, Hash)> tasks_task_files_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Task file
  data, status_code, headers = api_instance.tasks_task_files_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TasksTaskFile>
rescue F::ApiError => e
  puts "Error when calling TasksTaskFileApi->tasks_task_files_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifiers of the files |  |

### Return type

[**TasksTaskFile**](TasksTaskFile.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasks_task_files_post

> <TasksTaskFile> tasks_task_files_post(task_id, file)

Creates a Task file

Creates a Task file

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

api_instance = F::TasksTaskFileApi.new
task_id = 'task_id_example' # String | identifier of the task
file = File.new('/path/to/some/file') # File | file to attach to the task

begin
  # Creates a Task file
  result = api_instance.tasks_task_files_post(task_id, file)
  p result
rescue F::ApiError => e
  puts "Error when calling TasksTaskFileApi->tasks_task_files_post: #{e}"
end
```

#### Using the tasks_task_files_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TasksTaskFile>, Integer, Hash)> tasks_task_files_post_with_http_info(task_id, file)

```ruby
begin
  # Creates a Task file
  data, status_code, headers = api_instance.tasks_task_files_post_with_http_info(task_id, file)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TasksTaskFile>
rescue F::ApiError => e
  puts "Error when calling TasksTaskFileApi->tasks_task_files_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **task_id** | **String** | identifier of the task |  |
| **file** | **File** | file to attach to the task |  |

### Return type

[**TasksTaskFile**](TasksTaskFile.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

