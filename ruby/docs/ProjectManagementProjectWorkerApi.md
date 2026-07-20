# F::ProjectManagementProjectWorkerApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**project_management_project_workers_bulk_assign_post**](ProjectManagementProjectWorkerApi.md#project_management_project_workers_bulk_assign_post) | **POST** /api/2026-07-01/resources/project_management/project_workers/bulk_assign | Bulk assigns a Project worker |
| [**project_management_project_workers_bulk_create_post**](ProjectManagementProjectWorkerApi.md#project_management_project_workers_bulk_create_post) | **POST** /api/2026-07-01/resources/project_management/project_workers/bulk_create | Bulk creates a Project worker |
| [**project_management_project_workers_get**](ProjectManagementProjectWorkerApi.md#project_management_project_workers_get) | **GET** /api/2026-07-01/resources/project_management/project_workers | Reads all Project workers |
| [**project_management_project_workers_id_get**](ProjectManagementProjectWorkerApi.md#project_management_project_workers_id_get) | **GET** /api/2026-07-01/resources/project_management/project_workers/{id} | Reads a single Project worker |
| [**project_management_project_workers_post**](ProjectManagementProjectWorkerApi.md#project_management_project_workers_post) | **POST** /api/2026-07-01/resources/project_management/project_workers | Creates a Project worker |
| [**project_management_project_workers_unassign_post**](ProjectManagementProjectWorkerApi.md#project_management_project_workers_unassign_post) | **POST** /api/2026-07-01/resources/project_management/project_workers/unassign | Unassigns a Project worker |


## project_management_project_workers_bulk_assign_post

> <Array<ProjectManagementProjectWorker>> project_management_project_workers_bulk_assign_post(opts)

Bulk assigns a Project worker

###### **What does it do?** This method is used to specify a set of employees that should be assigned as a result of the execution. All the employees in the list will be assigned and all others will be unassigned. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with a role in the given project.

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

api_instance = F::ProjectManagementProjectWorkerApi.new
opts = {
  project_management_project_workers_bulk_assign_post_request: F::ProjectManagementProjectWorkersBulkAssignPostRequest.new({employee_ids: ["21", "22", "23"]}) # ProjectManagementProjectWorkersBulkAssignPostRequest | 
}

begin
  # Bulk assigns a Project worker
  result = api_instance.project_management_project_workers_bulk_assign_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectWorkerApi->project_management_project_workers_bulk_assign_post: #{e}"
end
```

#### Using the project_management_project_workers_bulk_assign_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<ProjectManagementProjectWorker>>, Integer, Hash)> project_management_project_workers_bulk_assign_post_with_http_info(opts)

```ruby
begin
  # Bulk assigns a Project worker
  data, status_code, headers = api_instance.project_management_project_workers_bulk_assign_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<ProjectManagementProjectWorker>>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectWorkerApi->project_management_project_workers_bulk_assign_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_management_project_workers_bulk_assign_post_request** | [**ProjectManagementProjectWorkersBulkAssignPostRequest**](ProjectManagementProjectWorkersBulkAssignPostRequest.md) |  | [optional] |

### Return type

[**Array&lt;ProjectManagementProjectWorker&gt;**](ProjectManagementProjectWorker.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_project_workers_bulk_create_post

> <Array<ProjectManagementProjectWorker>> project_management_project_workers_bulk_create_post(opts)

Bulk creates a Project worker

Bulk creates a Project worker

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

api_instance = F::ProjectManagementProjectWorkerApi.new
opts = {
  project_management_project_workers_bulk_create_post_request: F::ProjectManagementProjectWorkersBulkCreatePostRequest.new({project_id: '314159', employee_ids: ["21", "22"]}) # ProjectManagementProjectWorkersBulkCreatePostRequest | 
}

begin
  # Bulk creates a Project worker
  result = api_instance.project_management_project_workers_bulk_create_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectWorkerApi->project_management_project_workers_bulk_create_post: #{e}"
end
```

#### Using the project_management_project_workers_bulk_create_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<ProjectManagementProjectWorker>>, Integer, Hash)> project_management_project_workers_bulk_create_post_with_http_info(opts)

```ruby
begin
  # Bulk creates a Project worker
  data, status_code, headers = api_instance.project_management_project_workers_bulk_create_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<ProjectManagementProjectWorker>>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectWorkerApi->project_management_project_workers_bulk_create_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_management_project_workers_bulk_create_post_request** | [**ProjectManagementProjectWorkersBulkCreatePostRequest**](ProjectManagementProjectWorkersBulkCreatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;ProjectManagementProjectWorker&gt;**](ProjectManagementProjectWorker.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_project_workers_get

> <ProjectManagementProjectWorkersGet200Response> project_management_project_workers_get(opts)

Reads all Project workers

###### **What does it do?** This endpoint reads and retrieves a list of project workers. You can utilize URL parameters to filter the results. ###### **Is it related to other entities?** A project_worker is always related to a project and a employee. Only a `project worker` is able to add time to a project using the `time_record` entity. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission to read project workers.

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

api_instance = F::ProjectManagementProjectWorkerApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Retrieve only the project workers that matches the ids provided in the request.
  project_ids: ['inner_example'], # Array<String> | Retrieve only the project workers that matches the project_ids provided in the request.
  subproject_ids: ['inner_example'], # Array<String> | Retrieve only the project workers that matches the subproject_ids provided in the request.
  no_subproject: true, # Boolean | Retrieve the project workers that are not assigned to any subproject (can be combined with subproject_ids).
  employee_ids: ['inner_example'], # Array<String> | Retrieve only the project workers that are related to the employee_ids provided in the request.
  assigned: true, # Boolean | Retrieve project workers that are assigned if true or in not-assigned status if false.
  project_active: true, # Boolean | Retrieve the project workers that are assigned to active projects if turew or closed projects if false.
  employee_name: 'John D', # String | Retrieve only the project workers that matches the given employee's name provided in the request.
  include_inputed_minutes: true, # Boolean | If true we will perform the minutes calculations and will be return the total inputed_minutes. If false, 0 will be returned and no minutes calculations will be performed.
  include_cost: true, # Boolean | If true, costs of the project worker will be included to the response.
  updated_after: '1993-08-23', # String | Retrieve only the project workers that were created or updated after the date provided in the request.
  include_labor_cost: true # Boolean | 
}

begin
  # Reads all Project workers
  result = api_instance.project_management_project_workers_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectWorkerApi->project_management_project_workers_get: #{e}"
end
```

#### Using the project_management_project_workers_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProjectWorkersGet200Response>, Integer, Hash)> project_management_project_workers_get_with_http_info(opts)

```ruby
begin
  # Reads all Project workers
  data, status_code, headers = api_instance.project_management_project_workers_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProjectWorkersGet200Response>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectWorkerApi->project_management_project_workers_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the project workers that matches the ids provided in the request. | [optional] |
| **project_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the project workers that matches the project_ids provided in the request. | [optional] |
| **subproject_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the project workers that matches the subproject_ids provided in the request. | [optional] |
| **no_subproject** | **Boolean** | Retrieve the project workers that are not assigned to any subproject (can be combined with subproject_ids). | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the project workers that are related to the employee_ids provided in the request. | [optional] |
| **assigned** | **Boolean** | Retrieve project workers that are assigned if true or in not-assigned status if false. | [optional] |
| **project_active** | **Boolean** | Retrieve the project workers that are assigned to active projects if turew or closed projects if false. | [optional] |
| **employee_name** | **String** | Retrieve only the project workers that matches the given employee&#39;s name provided in the request. | [optional] |
| **include_inputed_minutes** | **Boolean** | If true we will perform the minutes calculations and will be return the total inputed_minutes. If false, 0 will be returned and no minutes calculations will be performed. | [optional] |
| **include_cost** | **Boolean** | If true, costs of the project worker will be included to the response. | [optional] |
| **updated_after** | **String** | Retrieve only the project workers that were created or updated after the date provided in the request. | [optional] |
| **include_labor_cost** | **Boolean** |  | [optional] |

### Return type

[**ProjectManagementProjectWorkersGet200Response**](ProjectManagementProjectWorkersGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_project_workers_id_get

> <ProjectManagementProjectWorker> project_management_project_workers_id_get(id)

Reads a single Project worker

###### **What does it do?** This endpoint reads and retrieves a list of project workers. You can utilize URL parameters to filter the results. ###### **Is it related to other entities?** A project_worker is always related to a project and a employee. Only a `project worker` is able to add time to a project using the `time_record` entity. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission to read project workers.

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

api_instance = F::ProjectManagementProjectWorkerApi.new
id = '92732' # String | Retrieve only the project workers that matches the ids provided in the request.

begin
  # Reads a single Project worker
  result = api_instance.project_management_project_workers_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectWorkerApi->project_management_project_workers_id_get: #{e}"
end
```

#### Using the project_management_project_workers_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProjectWorker>, Integer, Hash)> project_management_project_workers_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Project worker
  data, status_code, headers = api_instance.project_management_project_workers_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProjectWorker>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectWorkerApi->project_management_project_workers_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Retrieve only the project workers that matches the ids provided in the request. |  |

### Return type

[**ProjectManagementProjectWorker**](ProjectManagementProjectWorker.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_project_workers_post

> <ProjectManagementProjectWorker> project_management_project_workers_post(opts)

Creates a Project worker

###### **What does it do?** This creates a new project worker. By default, the project worker will be created with the status `assigned`. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with a role in the given project.

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

api_instance = F::ProjectManagementProjectWorkerApi.new
opts = {
  project_management_project_workers_post_request: F::ProjectManagementProjectWorkersPostRequest.new({project_id: '314159', employee_id: '21'}) # ProjectManagementProjectWorkersPostRequest | 
}

begin
  # Creates a Project worker
  result = api_instance.project_management_project_workers_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectWorkerApi->project_management_project_workers_post: #{e}"
end
```

#### Using the project_management_project_workers_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProjectWorker>, Integer, Hash)> project_management_project_workers_post_with_http_info(opts)

```ruby
begin
  # Creates a Project worker
  data, status_code, headers = api_instance.project_management_project_workers_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProjectWorker>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectWorkerApi->project_management_project_workers_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_management_project_workers_post_request** | [**ProjectManagementProjectWorkersPostRequest**](ProjectManagementProjectWorkersPostRequest.md) |  | [optional] |

### Return type

[**ProjectManagementProjectWorker**](ProjectManagementProjectWorker.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_project_workers_unassign_post

> <ProjectManagementProjectWorker> project_management_project_workers_unassign_post(opts)

Unassigns a Project worker

Unassigns a Project worker

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

api_instance = F::ProjectManagementProjectWorkerApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Unassigns a Project worker
  result = api_instance.project_management_project_workers_unassign_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectWorkerApi->project_management_project_workers_unassign_post: #{e}"
end
```

#### Using the project_management_project_workers_unassign_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProjectWorker>, Integer, Hash)> project_management_project_workers_unassign_post_with_http_info(opts)

```ruby
begin
  # Unassigns a Project worker
  data, status_code, headers = api_instance.project_management_project_workers_unassign_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProjectWorker>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectWorkerApi->project_management_project_workers_unassign_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**ProjectManagementProjectWorker**](ProjectManagementProjectWorker.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

