# F::ProjectManagementProjectTaskApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**project_management_project_tasks_bulk_destroy_post**](ProjectManagementProjectTaskApi.md#project_management_project_tasks_bulk_destroy_post) | **POST** /api/2026-07-01/resources/project_management/project_tasks/bulk_destroy | Bulk destroys a Project task |
| [**project_management_project_tasks_bulk_duplicate_post**](ProjectManagementProjectTaskApi.md#project_management_project_tasks_bulk_duplicate_post) | **POST** /api/2026-07-01/resources/project_management/project_tasks/bulk_duplicate | Bulk duplicates a Project task |
| [**project_management_project_tasks_get**](ProjectManagementProjectTaskApi.md#project_management_project_tasks_get) | **GET** /api/2026-07-01/resources/project_management/project_tasks | Reads all Project tasks |
| [**project_management_project_tasks_id_get**](ProjectManagementProjectTaskApi.md#project_management_project_tasks_id_get) | **GET** /api/2026-07-01/resources/project_management/project_tasks/{id} | Reads a single Project task |
| [**project_management_project_tasks_id_put**](ProjectManagementProjectTaskApi.md#project_management_project_tasks_id_put) | **PUT** /api/2026-07-01/resources/project_management/project_tasks/{id} | Updates a Project task |
| [**project_management_project_tasks_post**](ProjectManagementProjectTaskApi.md#project_management_project_tasks_post) | **POST** /api/2026-07-01/resources/project_management/project_tasks | Creates a Project task |


## project_management_project_tasks_bulk_destroy_post

> <Array<ProjectManagementProjectTask>> project_management_project_tasks_bulk_destroy_post(opts)

Bulk destroys a Project task

###### **What does it do?** This will delete the project tasks with the ids passed as an argument. ###### **What params does it accept?**    - `ids`: Project task ids  ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission of read projects.

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

api_instance = F::ProjectManagementProjectTaskApi.new
opts = {
  expenses_expensables_bulk_set_to_paid_post_request: F::ExpensesExpensablesBulkSetToPaidPostRequest.new({ids: ["1"]}) # ExpensesExpensablesBulkSetToPaidPostRequest | 
}

begin
  # Bulk destroys a Project task
  result = api_instance.project_management_project_tasks_bulk_destroy_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectTaskApi->project_management_project_tasks_bulk_destroy_post: #{e}"
end
```

#### Using the project_management_project_tasks_bulk_destroy_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<ProjectManagementProjectTask>>, Integer, Hash)> project_management_project_tasks_bulk_destroy_post_with_http_info(opts)

```ruby
begin
  # Bulk destroys a Project task
  data, status_code, headers = api_instance.project_management_project_tasks_bulk_destroy_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<ProjectManagementProjectTask>>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectTaskApi->project_management_project_tasks_bulk_destroy_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **expenses_expensables_bulk_set_to_paid_post_request** | [**ExpensesExpensablesBulkSetToPaidPostRequest**](ExpensesExpensablesBulkSetToPaidPostRequest.md) |  | [optional] |

### Return type

[**Array&lt;ProjectManagementProjectTask&gt;**](ProjectManagementProjectTask.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_project_tasks_bulk_duplicate_post

> <Array<ProjectManagementProjectTask>> project_management_project_tasks_bulk_duplicate_post(opts)

Bulk duplicates a Project task

###### **What does it do?** This will create new project tasks with the same attributes as the project task ids passed as an argument. ###### **What params does it accept?**    - `ids`: Project task ids  ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission of read projects.

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

api_instance = F::ProjectManagementProjectTaskApi.new
opts = {
  project_management_project_tasks_bulk_duplicate_post_request: F::ProjectManagementProjectTasksBulkDuplicatePostRequest.new({ids: ["1", "2", "3"]}) # ProjectManagementProjectTasksBulkDuplicatePostRequest | 
}

begin
  # Bulk duplicates a Project task
  result = api_instance.project_management_project_tasks_bulk_duplicate_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectTaskApi->project_management_project_tasks_bulk_duplicate_post: #{e}"
end
```

#### Using the project_management_project_tasks_bulk_duplicate_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<ProjectManagementProjectTask>>, Integer, Hash)> project_management_project_tasks_bulk_duplicate_post_with_http_info(opts)

```ruby
begin
  # Bulk duplicates a Project task
  data, status_code, headers = api_instance.project_management_project_tasks_bulk_duplicate_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<ProjectManagementProjectTask>>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectTaskApi->project_management_project_tasks_bulk_duplicate_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_management_project_tasks_bulk_duplicate_post_request** | [**ProjectManagementProjectTasksBulkDuplicatePostRequest**](ProjectManagementProjectTasksBulkDuplicatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;ProjectManagementProjectTask&gt;**](ProjectManagementProjectTask.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_project_tasks_get

> <ProjectManagementProjectTasksGet200Response> project_management_project_tasks_get(ids, project_ids, subproject_ids, completed, overdue, search, due_status, client_ids, opts)

Reads all Project tasks

###### **What does it do?** This reads the data of projects tasks, and retrieves the information based on permissions:    - If the user can see all company projects for everybody, the endpoint will return a list with the tasks from the related projects.   - If the user can create projects for everybody, the endpoint will return a list with the tasks from the related projects.   - If the user has any role (editor or owner) on the project, the endpoint will return a list with the tasks from the related projects where the user has that role.   - If those conditions are not matched, the endpoint will return an empty list.  ###### **What params does it accept?**    - `ids`: retrieve only the projects tasks that matches the ids passed in the request.   - `project_ids`: retrieve only the projects tasks from the projects that matched the ids passed in the request.   - `subproject_ids`: retrieve only the projects tasks from the subprojects that matched the ids passed in the request.   - `completed`: boolean - retrieve only the projects tasks with the status completed.   - `overdue`: boolean - retrieve only the projects tasks that are overdue.   - `search`:  retrieve only the projects tasks that their name match with the content passed as argument.   - `due_status`: retrieve only the project tasks that their due status match with the content passed as argument.   - `client_ids`: retrieve only the projects tasks from the clients that matched the ids passed in the request.  ###### **Who can use it?**    Only companies who have enabled the `projects_management` feature and users with the permission of read projects.

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

api_instance = F::ProjectManagementProjectTaskApi.new
ids = ['inner_example'] # Array<String> | Retrieve only the projects tasks that matches the ids passed in the request.
project_ids = ['inner_example'] # Array<String> | Retrieve only the projects tasks from the projects that matched the ids passed in the request.
subproject_ids = ['inner_example'] # Array<String> | Retrieve only the projects tasks from the subprojects that matched the ids passed in the request.
completed = true # Boolean | Retrieve only the projects tasks with the status completed.
overdue = true # Boolean | Retrieve only the projects tasks that are overdue.
search = 'Project Name' # String | Retrieve only the projects tasks that their name match with the content passed as argument.
due_status = 'no_due' # String | Retrieve only the project tasks that their due status match with the content passed as argument.
client_ids = ['inner_example'] # Array<String> | Retrieve only the projects tasks from the clients that matched the ids passed in the request.
opts = {
  task_ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Project tasks
  result = api_instance.project_management_project_tasks_get(ids, project_ids, subproject_ids, completed, overdue, search, due_status, client_ids, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectTaskApi->project_management_project_tasks_get: #{e}"
end
```

#### Using the project_management_project_tasks_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProjectTasksGet200Response>, Integer, Hash)> project_management_project_tasks_get_with_http_info(ids, project_ids, subproject_ids, completed, overdue, search, due_status, client_ids, opts)

```ruby
begin
  # Reads all Project tasks
  data, status_code, headers = api_instance.project_management_project_tasks_get_with_http_info(ids, project_ids, subproject_ids, completed, overdue, search, due_status, client_ids, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProjectTasksGet200Response>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectTaskApi->project_management_project_tasks_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the projects tasks that matches the ids passed in the request. |  |
| **project_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the projects tasks from the projects that matched the ids passed in the request. |  |
| **subproject_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the projects tasks from the subprojects that matched the ids passed in the request. |  |
| **completed** | **Boolean** | Retrieve only the projects tasks with the status completed. |  |
| **overdue** | **Boolean** | Retrieve only the projects tasks that are overdue. |  |
| **search** | **String** | Retrieve only the projects tasks that their name match with the content passed as argument. |  |
| **due_status** | **String** | Retrieve only the project tasks that their due status match with the content passed as argument. |  |
| **client_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the projects tasks from the clients that matched the ids passed in the request. |  |
| **task_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**ProjectManagementProjectTasksGet200Response**](ProjectManagementProjectTasksGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_project_tasks_id_get

> <ProjectManagementProjectTask> project_management_project_tasks_id_get(id)

Reads a single Project task

###### **What does it do?** This reads the data of projects tasks, and retrieves the information based on permissions:    - If the user can see all company projects for everybody, the endpoint will return a list with the tasks from the related projects.   - If the user can create projects for everybody, the endpoint will return a list with the tasks from the related projects.   - If the user has any role (editor or owner) on the project, the endpoint will return a list with the tasks from the related projects where the user has that role.   - If those conditions are not matched, the endpoint will return an empty list.  ###### **What params does it accept?**    - `ids`: retrieve only the projects tasks that matches the ids passed in the request.   - `project_ids`: retrieve only the projects tasks from the projects that matched the ids passed in the request.   - `subproject_ids`: retrieve only the projects tasks from the subprojects that matched the ids passed in the request.   - `completed`: boolean - retrieve only the projects tasks with the status completed.   - `overdue`: boolean - retrieve only the projects tasks that are overdue.   - `search`:  retrieve only the projects tasks that their name match with the content passed as argument.   - `due_status`: retrieve only the project tasks that their due status match with the content passed as argument.   - `client_ids`: retrieve only the projects tasks from the clients that matched the ids passed in the request.  ###### **Who can use it?**    Only companies who have enabled the `projects_management` feature and users with the permission of read projects.

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

api_instance = F::ProjectManagementProjectTaskApi.new
id = '314159' # String | Retrieve only the projects tasks that matches the ids passed in the request.

begin
  # Reads a single Project task
  result = api_instance.project_management_project_tasks_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectTaskApi->project_management_project_tasks_id_get: #{e}"
end
```

#### Using the project_management_project_tasks_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProjectTask>, Integer, Hash)> project_management_project_tasks_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Project task
  data, status_code, headers = api_instance.project_management_project_tasks_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProjectTask>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectTaskApi->project_management_project_tasks_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Retrieve only the projects tasks that matches the ids passed in the request. |  |

### Return type

[**ProjectManagementProjectTask**](ProjectManagementProjectTask.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_project_tasks_id_put

> <ProjectManagementProjectTask> project_management_project_tasks_id_put(id, id2, name, project_id, opts)

Updates a Project task

###### **What does it do?** This update a project task. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission of create projects.

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

api_instance = F::ProjectManagementProjectTaskApi.new
id = '789' # String | The ID of the project task to update
id2 = 'id_example' # String | The ID of the project task to update
name = 'name_example' # String | The name of the project task
project_id = 'project_id_example' # String | The ID of the project where the task belongs
opts = {
  content: 'content_example', # String | The content/description of the project task
  starts_on: 'starts_on_example', # String | The date when the project task starts
  follow_up: true, # Boolean | If true, status changes related to the project will notify the author
  due_on: 'due_on_example', # String | The date when the project task will be due
  assignee_employee_ids: ['inner_example'], # Array<String> | The value of the assignee employee ids of the project task
  subproject_id: 'subproject_id_example', # String | The ID of the subproject where the project task belongs
  files_to_add: [File.new('/path/to/some/file')], # Array<File> | Array of files to add to the project task
  files_to_remove: ['inner_example'], # Array<String> | Array of files to remove from the project task
  status: 'todo' # String | The status of the project task
}

begin
  # Updates a Project task
  result = api_instance.project_management_project_tasks_id_put(id, id2, name, project_id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectTaskApi->project_management_project_tasks_id_put: #{e}"
end
```

#### Using the project_management_project_tasks_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProjectTask>, Integer, Hash)> project_management_project_tasks_id_put_with_http_info(id, id2, name, project_id, opts)

```ruby
begin
  # Updates a Project task
  data, status_code, headers = api_instance.project_management_project_tasks_id_put_with_http_info(id, id2, name, project_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProjectTask>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectTaskApi->project_management_project_tasks_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The ID of the project task to update |  |
| **id2** | **String** | The ID of the project task to update |  |
| **name** | **String** | The name of the project task |  |
| **project_id** | **String** | The ID of the project where the task belongs |  |
| **content** | **String** | The content/description of the project task | [optional] |
| **starts_on** | **String** | The date when the project task starts | [optional] |
| **follow_up** | **Boolean** | If true, status changes related to the project will notify the author | [optional] |
| **due_on** | **String** | The date when the project task will be due | [optional] |
| **assignee_employee_ids** | [**Array&lt;String&gt;**](String.md) | The value of the assignee employee ids of the project task | [optional] |
| **subproject_id** | **String** | The ID of the subproject where the project task belongs | [optional] |
| **files_to_add** | **Array&lt;File&gt;** | Array of files to add to the project task | [optional] |
| **files_to_remove** | [**Array&lt;String&gt;**](String.md) | Array of files to remove from the project task | [optional] |
| **status** | **String** | The status of the project task | [optional] |

### Return type

[**ProjectManagementProjectTask**](ProjectManagementProjectTask.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## project_management_project_tasks_post

> <ProjectManagementProjectTask> project_management_project_tasks_post(name, project_id, status, opts)

Creates a Project task

###### **What does it do?** This creates a new project task. It will also create a new normal task in the system linked with the project task. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission of create projects.

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

api_instance = F::ProjectManagementProjectTaskApi.new
name = 'name_example' # String | The name of the project task
project_id = 'project_id_example' # String | The ID of the project where the task belongs
status = 'todo' # String | The status of the project task
opts = {
  content: 'content_example', # String | The content/description of the project task
  starts_on: 'starts_on_example', # String | The date when the project task starts
  follow_up: true, # Boolean | If true, status changes related to the project will notify the author
  due_on: 'due_on_example', # String | The date when the project task will be due
  assignee_employee_ids: ['inner_example'], # Array<String> | The value of the assignee employee ids of the project task
  subproject_id: 'subproject_id_example', # String | The ID of the subproject where the project task belongs
  files: [File.new('/path/to/some/file')] # Array<File> | Array of files that will be attached to the project task
}

begin
  # Creates a Project task
  result = api_instance.project_management_project_tasks_post(name, project_id, status, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectTaskApi->project_management_project_tasks_post: #{e}"
end
```

#### Using the project_management_project_tasks_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProjectTask>, Integer, Hash)> project_management_project_tasks_post_with_http_info(name, project_id, status, opts)

```ruby
begin
  # Creates a Project task
  data, status_code, headers = api_instance.project_management_project_tasks_post_with_http_info(name, project_id, status, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProjectTask>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectTaskApi->project_management_project_tasks_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | The name of the project task |  |
| **project_id** | **String** | The ID of the project where the task belongs |  |
| **status** | **String** | The status of the project task |  |
| **content** | **String** | The content/description of the project task | [optional] |
| **starts_on** | **String** | The date when the project task starts | [optional] |
| **follow_up** | **Boolean** | If true, status changes related to the project will notify the author | [optional] |
| **due_on** | **String** | The date when the project task will be due | [optional] |
| **assignee_employee_ids** | [**Array&lt;String&gt;**](String.md) | The value of the assignee employee ids of the project task | [optional] |
| **subproject_id** | **String** | The ID of the subproject where the project task belongs | [optional] |
| **files** | **Array&lt;File&gt;** | Array of files that will be attached to the project task | [optional] |

### Return type

[**ProjectManagementProjectTask**](ProjectManagementProjectTask.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

