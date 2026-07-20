# F::TasksTaskApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**tasks_tasks_bulk_create_post**](TasksTaskApi.md#tasks_tasks_bulk_create_post) | **POST** /api/2026-07-01/resources/tasks/tasks/bulk_create | Bulk creates a Task |
| [**tasks_tasks_bulk_delete_post**](TasksTaskApi.md#tasks_tasks_bulk_delete_post) | **POST** /api/2026-07-01/resources/tasks/tasks/bulk_delete | Bulk deletes a Task |
| [**tasks_tasks_bulk_update_post**](TasksTaskApi.md#tasks_tasks_bulk_update_post) | **POST** /api/2026-07-01/resources/tasks/tasks/bulk_update | Bulk updates a Task |
| [**tasks_tasks_copy_post**](TasksTaskApi.md#tasks_tasks_copy_post) | **POST** /api/2026-07-01/resources/tasks/tasks/copy | Copies a Task |
| [**tasks_tasks_create_comment_post**](TasksTaskApi.md#tasks_tasks_create_comment_post) | **POST** /api/2026-07-01/resources/tasks/tasks/create_comment | Create comments a Task |
| [**tasks_tasks_get**](TasksTaskApi.md#tasks_tasks_get) | **GET** /api/2026-07-01/resources/tasks/tasks | Reads all Tasks |
| [**tasks_tasks_id_delete**](TasksTaskApi.md#tasks_tasks_id_delete) | **DELETE** /api/2026-07-01/resources/tasks/tasks/{id} | Deletes a Task |
| [**tasks_tasks_id_get**](TasksTaskApi.md#tasks_tasks_id_get) | **GET** /api/2026-07-01/resources/tasks/tasks/{id} | Reads a single Task |
| [**tasks_tasks_id_put**](TasksTaskApi.md#tasks_tasks_id_put) | **PUT** /api/2026-07-01/resources/tasks/tasks/{id} | Updates a Task |
| [**tasks_tasks_post**](TasksTaskApi.md#tasks_tasks_post) | **POST** /api/2026-07-01/resources/tasks/tasks | Creates a Task |


## tasks_tasks_bulk_create_post

> <Array<TasksTask>> tasks_tasks_bulk_create_post(opts)

Bulk creates a Task

This endpoint creates a new task for each assignee.

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

api_instance = F::TasksTaskApi.new
opts = {
  tasks_tasks_post_request: F::TasksTasksPostRequest.new({name: 'My task', status: 'todo'}) # TasksTasksPostRequest | 
}

begin
  # Bulk creates a Task
  result = api_instance.tasks_tasks_bulk_create_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_bulk_create_post: #{e}"
end
```

#### Using the tasks_tasks_bulk_create_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<TasksTask>>, Integer, Hash)> tasks_tasks_bulk_create_post_with_http_info(opts)

```ruby
begin
  # Bulk creates a Task
  data, status_code, headers = api_instance.tasks_tasks_bulk_create_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<TasksTask>>
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_bulk_create_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **tasks_tasks_post_request** | [**TasksTasksPostRequest**](TasksTasksPostRequest.md) |  | [optional] |

### Return type

[**Array&lt;TasksTask&gt;**](TasksTask.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tasks_tasks_bulk_delete_post

> <Array<TasksTask>> tasks_tasks_bulk_delete_post(opts)

Bulk deletes a Task

This endpoint allows to delete a list of tasks given the ids.

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

api_instance = F::TasksTaskApi.new
opts = {
  expenses_expensables_bulk_set_to_paid_post_request: F::ExpensesExpensablesBulkSetToPaidPostRequest.new({ids: ["1"]}) # ExpensesExpensablesBulkSetToPaidPostRequest | 
}

begin
  # Bulk deletes a Task
  result = api_instance.tasks_tasks_bulk_delete_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_bulk_delete_post: #{e}"
end
```

#### Using the tasks_tasks_bulk_delete_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<TasksTask>>, Integer, Hash)> tasks_tasks_bulk_delete_post_with_http_info(opts)

```ruby
begin
  # Bulk deletes a Task
  data, status_code, headers = api_instance.tasks_tasks_bulk_delete_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<TasksTask>>
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_bulk_delete_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **expenses_expensables_bulk_set_to_paid_post_request** | [**ExpensesExpensablesBulkSetToPaidPostRequest**](ExpensesExpensablesBulkSetToPaidPostRequest.md) |  | [optional] |

### Return type

[**Array&lt;TasksTask&gt;**](TasksTask.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tasks_tasks_bulk_update_post

> <Array<TasksTask>> tasks_tasks_bulk_update_post(opts)

Bulk updates a Task

Bulk updates a Task

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

api_instance = F::TasksTaskApi.new
opts = {
  tasks_tasks_bulk_update_post_request: F::TasksTasksBulkUpdatePostRequest.new({tasks: [{"id": 1, "name": "My task", "content": "Complete your performance review before Friday", "due_on": "2024-06-06", "assignee_ids": [1], "status": "todo"}]}) # TasksTasksBulkUpdatePostRequest | 
}

begin
  # Bulk updates a Task
  result = api_instance.tasks_tasks_bulk_update_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_bulk_update_post: #{e}"
end
```

#### Using the tasks_tasks_bulk_update_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<TasksTask>>, Integer, Hash)> tasks_tasks_bulk_update_post_with_http_info(opts)

```ruby
begin
  # Bulk updates a Task
  data, status_code, headers = api_instance.tasks_tasks_bulk_update_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<TasksTask>>
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_bulk_update_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **tasks_tasks_bulk_update_post_request** | [**TasksTasksBulkUpdatePostRequest**](TasksTasksBulkUpdatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;TasksTask&gt;**](TasksTask.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tasks_tasks_copy_post

> <TasksTask> tasks_tasks_copy_post(opts)

Copies a Task

This endpoint duplicates a task.

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

api_instance = F::TasksTaskApi.new
opts = {
  tasks_tasks_copy_post_request: F::TasksTasksCopyPostRequest.new({id: '1'}) # TasksTasksCopyPostRequest | 
}

begin
  # Copies a Task
  result = api_instance.tasks_tasks_copy_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_copy_post: #{e}"
end
```

#### Using the tasks_tasks_copy_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TasksTask>, Integer, Hash)> tasks_tasks_copy_post_with_http_info(opts)

```ruby
begin
  # Copies a Task
  data, status_code, headers = api_instance.tasks_tasks_copy_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TasksTask>
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_copy_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **tasks_tasks_copy_post_request** | [**TasksTasksCopyPostRequest**](TasksTasksCopyPostRequest.md) |  | [optional] |

### Return type

[**TasksTask**](TasksTask.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tasks_tasks_create_comment_post

> <TasksTask> tasks_tasks_create_comment_post(opts)

Create comments a Task

Create comments a Task

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

api_instance = F::TasksTaskApi.new
opts = {
  tasks_tasks_create_comment_post_request: F::TasksTasksCreateCommentPostRequest.new({content: 'content_example', author_id: 'author_id_example', resource_id: 'resource_id_example', company_id: 'company_id_example'}) # TasksTasksCreateCommentPostRequest | 
}

begin
  # Create comments a Task
  result = api_instance.tasks_tasks_create_comment_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_create_comment_post: #{e}"
end
```

#### Using the tasks_tasks_create_comment_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TasksTask>, Integer, Hash)> tasks_tasks_create_comment_post_with_http_info(opts)

```ruby
begin
  # Create comments a Task
  data, status_code, headers = api_instance.tasks_tasks_create_comment_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TasksTask>
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_create_comment_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **tasks_tasks_create_comment_post_request** | [**TasksTasksCreateCommentPostRequest**](TasksTasksCreateCommentPostRequest.md) |  | [optional] |

### Return type

[**TasksTask**](TasksTask.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tasks_tasks_get

> <TasksTasksGet200Response> tasks_tasks_get(opts)

Reads all Tasks

This endpoint retrieves all tasks created.

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

api_instance = F::TasksTaskApi.new
opts = {
  ids: ['inner_example'], # Array<String> | retrieve only the tasks that match the IDs passed in the request.
  company_id: '1', # String | retrieve the tasks that have a company_id associated
  assignee_id: '1', # String | retrieve the tasks that have an assignee_id associated, assignee_id references to access_id.
  due_on: '2024-06-06', # String | filter by tasks that have a due date.
  already_due: true, # Boolean | filter by tasks that have expired or are still due.
  task_status: 'todo', # String | filter by tasks that with an especific status (todo | in_progress | done | discarded).
  involvee_id: '1', # String | retrieve tasks where the user is affectee or assignee
  category: 'benefits' # String | filter by tasks that have a specific category
}

begin
  # Reads all Tasks
  result = api_instance.tasks_tasks_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_get: #{e}"
end
```

#### Using the tasks_tasks_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TasksTasksGet200Response>, Integer, Hash)> tasks_tasks_get_with_http_info(opts)

```ruby
begin
  # Reads all Tasks
  data, status_code, headers = api_instance.tasks_tasks_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TasksTasksGet200Response>
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | retrieve only the tasks that match the IDs passed in the request. | [optional] |
| **company_id** | **String** | retrieve the tasks that have a company_id associated | [optional] |
| **assignee_id** | **String** | retrieve the tasks that have an assignee_id associated, assignee_id references to access_id. | [optional] |
| **due_on** | **String** | filter by tasks that have a due date. | [optional] |
| **already_due** | **Boolean** | filter by tasks that have expired or are still due. | [optional] |
| **task_status** | **String** | filter by tasks that with an especific status (todo | in_progress | done | discarded). | [optional] |
| **involvee_id** | **String** | retrieve tasks where the user is affectee or assignee | [optional] |
| **category** | **String** | filter by tasks that have a specific category | [optional] |

### Return type

[**TasksTasksGet200Response**](TasksTasksGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasks_tasks_id_delete

> <TasksTask> tasks_tasks_id_delete(id)

Deletes a Task

This endpoint deletes a task.

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

api_instance = F::TasksTaskApi.new
id = '1' # String | id of the task.

begin
  # Deletes a Task
  result = api_instance.tasks_tasks_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_id_delete: #{e}"
end
```

#### Using the tasks_tasks_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TasksTask>, Integer, Hash)> tasks_tasks_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Task
  data, status_code, headers = api_instance.tasks_tasks_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TasksTask>
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | id of the task. |  |

### Return type

[**TasksTask**](TasksTask.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasks_tasks_id_get

> <TasksTask> tasks_tasks_id_get(id)

Reads a single Task

This endpoint retrieves all tasks created.

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

api_instance = F::TasksTaskApi.new
id = '1' # String | retrieve only the tasks that match the IDs passed in the request.

begin
  # Reads a single Task
  result = api_instance.tasks_tasks_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_id_get: #{e}"
end
```

#### Using the tasks_tasks_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TasksTask>, Integer, Hash)> tasks_tasks_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Task
  data, status_code, headers = api_instance.tasks_tasks_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TasksTask>
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | retrieve only the tasks that match the IDs passed in the request. |  |

### Return type

[**TasksTask**](TasksTask.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasks_tasks_id_put

> <TasksTask> tasks_tasks_id_put(id, opts)

Updates a Task

This endpoint updates an existing task.

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

api_instance = F::TasksTaskApi.new
id = '1' # String | id of a task.
opts = {
  tasks_tasks_id_put_request: F::TasksTasksIdPutRequest.new({id: '1'}) # TasksTasksIdPutRequest | 
}

begin
  # Updates a Task
  result = api_instance.tasks_tasks_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_id_put: #{e}"
end
```

#### Using the tasks_tasks_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TasksTask>, Integer, Hash)> tasks_tasks_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Task
  data, status_code, headers = api_instance.tasks_tasks_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TasksTask>
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | id of a task. |  |
| **tasks_tasks_id_put_request** | [**TasksTasksIdPutRequest**](TasksTasksIdPutRequest.md) |  | [optional] |

### Return type

[**TasksTask**](TasksTask.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tasks_tasks_post

> <TasksTask> tasks_tasks_post(opts)

Creates a Task

This endpoint creates a new task.

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

api_instance = F::TasksTaskApi.new
opts = {
  tasks_tasks_post_request: F::TasksTasksPostRequest.new({name: 'My task', status: 'todo'}) # TasksTasksPostRequest | 
}

begin
  # Creates a Task
  result = api_instance.tasks_tasks_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_post: #{e}"
end
```

#### Using the tasks_tasks_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TasksTask>, Integer, Hash)> tasks_tasks_post_with_http_info(opts)

```ruby
begin
  # Creates a Task
  data, status_code, headers = api_instance.tasks_tasks_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TasksTask>
rescue F::ApiError => e
  puts "Error when calling TasksTaskApi->tasks_tasks_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **tasks_tasks_post_request** | [**TasksTasksPostRequest**](TasksTasksPostRequest.md) |  | [optional] |

### Return type

[**TasksTask**](TasksTask.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

