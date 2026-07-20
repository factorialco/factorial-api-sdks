# F::ProjectManagementProjectApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**project_management_projects_activate_post**](ProjectManagementProjectApi.md#project_management_projects_activate_post) | **POST** /api/2026-07-01/resources/project_management/projects/activate | Activates a Project |
| [**project_management_projects_change_assignment_post**](ProjectManagementProjectApi.md#project_management_projects_change_assignment_post) | **POST** /api/2026-07-01/resources/project_management/projects/change_assignment | Change assignments a Project |
| [**project_management_projects_change_status_post**](ProjectManagementProjectApi.md#project_management_projects_change_status_post) | **POST** /api/2026-07-01/resources/project_management/projects/change_status | Change statuses a Project |
| [**project_management_projects_close_post**](ProjectManagementProjectApi.md#project_management_projects_close_post) | **POST** /api/2026-07-01/resources/project_management/projects/close | Closes a Project |
| [**project_management_projects_get**](ProjectManagementProjectApi.md#project_management_projects_get) | **GET** /api/2026-07-01/resources/project_management/projects | Reads all Projects |
| [**project_management_projects_id_get**](ProjectManagementProjectApi.md#project_management_projects_id_get) | **GET** /api/2026-07-01/resources/project_management/projects/{id} | Reads a single Project |
| [**project_management_projects_id_put**](ProjectManagementProjectApi.md#project_management_projects_id_put) | **PUT** /api/2026-07-01/resources/project_management/projects/{id} | Updates a Project |
| [**project_management_projects_post**](ProjectManagementProjectApi.md#project_management_projects_post) | **POST** /api/2026-07-01/resources/project_management/projects | Creates a Project |
| [**project_management_projects_soft_delete_post**](ProjectManagementProjectApi.md#project_management_projects_soft_delete_post) | **POST** /api/2026-07-01/resources/project_management/projects/soft_delete | Soft deletes a Project |


## project_management_projects_activate_post

> <ProjectManagementProject> project_management_projects_activate_post(opts)

Activates a Project

###### **What does it do?** This endpoint can be used to set a project as `Active`. ###### **What body params do you need?**   - `id`: mandatory. The id of the project aimed to be activated.  ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with a role in the project.

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

api_instance = F::ProjectManagementProjectApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Activates a Project
  result = api_instance.project_management_projects_activate_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_activate_post: #{e}"
end
```

#### Using the project_management_projects_activate_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProject>, Integer, Hash)> project_management_projects_activate_post_with_http_info(opts)

```ruby
begin
  # Activates a Project
  data, status_code, headers = api_instance.project_management_projects_activate_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProject>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_activate_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**ProjectManagementProject**](ProjectManagementProject.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_projects_change_assignment_post

> <ProjectManagementProject> project_management_projects_change_assignment_post(opts)

Change assignments a Project

###### **What does it do?** **DEPRECATED**; this endpoint will be removed soon. This changes assignment type to a project. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission of assign employees.

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

api_instance = F::ProjectManagementProjectApi.new
opts = {
  project_management_projects_change_assignment_post_request: F::ProjectManagementProjectsChangeAssignmentPostRequest.new({id: 'id_example', employees_assignment: 'employees_assignment_example'}) # ProjectManagementProjectsChangeAssignmentPostRequest | 
}

begin
  # Change assignments a Project
  result = api_instance.project_management_projects_change_assignment_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_change_assignment_post: #{e}"
end
```

#### Using the project_management_projects_change_assignment_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProject>, Integer, Hash)> project_management_projects_change_assignment_post_with_http_info(opts)

```ruby
begin
  # Change assignments a Project
  data, status_code, headers = api_instance.project_management_projects_change_assignment_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProject>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_change_assignment_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_management_projects_change_assignment_post_request** | [**ProjectManagementProjectsChangeAssignmentPostRequest**](ProjectManagementProjectsChangeAssignmentPostRequest.md) |  | [optional] |

### Return type

[**ProjectManagementProject**](ProjectManagementProject.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_projects_change_status_post

> <ProjectManagementProject> project_management_projects_change_status_post(opts)

Change statuses a Project

###### **What does it do?** This update the project status. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with owner permission.

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

api_instance = F::ProjectManagementProjectApi.new
opts = {
  project_management_projects_change_status_post_request: F::ProjectManagementProjectsChangeStatusPostRequest.new({id: '314159', status: 'active'}) # ProjectManagementProjectsChangeStatusPostRequest | 
}

begin
  # Change statuses a Project
  result = api_instance.project_management_projects_change_status_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_change_status_post: #{e}"
end
```

#### Using the project_management_projects_change_status_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProject>, Integer, Hash)> project_management_projects_change_status_post_with_http_info(opts)

```ruby
begin
  # Change statuses a Project
  data, status_code, headers = api_instance.project_management_projects_change_status_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProject>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_change_status_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_management_projects_change_status_post_request** | [**ProjectManagementProjectsChangeStatusPostRequest**](ProjectManagementProjectsChangeStatusPostRequest.md) |  | [optional] |

### Return type

[**ProjectManagementProject**](ProjectManagementProject.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_projects_close_post

> <ProjectManagementProject> project_management_projects_close_post(opts)

Closes a Project

###### **What does it do?** This endpoint can be used to set a project as `Closed`. ###### **What body params do you need?**   - `id`: mandatory. The id of the project aimed to be closed.  ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with a role in the project.

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

api_instance = F::ProjectManagementProjectApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Closes a Project
  result = api_instance.project_management_projects_close_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_close_post: #{e}"
end
```

#### Using the project_management_projects_close_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProject>, Integer, Hash)> project_management_projects_close_post_with_http_info(opts)

```ruby
begin
  # Closes a Project
  data, status_code, headers = api_instance.project_management_projects_close_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProject>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_close_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**ProjectManagementProject**](ProjectManagementProject.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_projects_get

> <ProjectManagementProjectsGet200Response> project_management_projects_get(include_inputed_minutes, opts)

Reads all Projects

###### **What does it do?** This reads the data of projects, and retrieves the information based on the permissions:    - If the user has the `team_leader` permission, he will only be able to read the projects that he is the team leader.   - If the user has the `reportees` permission, he will only be able to read the projects that he is the team leader or the projects that he is a team member.   - If the user has `everyone` permission, he will be able to read all projects.   - If the user has the `owned` permission, he will only be able to read the projects that he is the assigned.  ###### **Is it related to other entities?** A project is always related to a company, so you can use the query params to list only the projects that are related to a specific company. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission of read projects.

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

api_instance = F::ProjectManagementProjectApi.new
include_inputed_minutes = true # Boolean | If true we will perform the minutes calculations and will be return the total inputed_minutes. If false, 0 will be returned and no minutes calculations will be performed.
opts = {
  ids: ['inner_example'], # Array<String> | Retrieve only the projects that matches the ids provided in the request.
  name: 'Project Name', # String | Retrieve only the projects that match the name passed in the request. (deprecated)
  name_or_code: 'Project Name', # String | Retrieve only the projects that match the name or code passed in the request.
  include_costs: true, # Boolean | If true we will perform the costs calculations and will be return the total cost. If false, 0 will be returned and no costs calculations will be performed.
  updated_after: '1993-08-23', # String | Retrieve only the projects that were created or updated after the date provided in the request.
  legal_entity_id: '123', # String | Retrieve only the projects that are related to the legal entity passed in the request.
  client_ids: ['inner_example'], # Array<String> | Retrieve only the projects that are related to the clients passed in the request, refers to finance/contacts.
  no_clients: false, # Boolean | Retrieve only the projects that are not related to any client, refers to finance/contacts.
  total_currency: 'USD' # String | Retrieve only the projects that have the total cost in the currency passed in the request.
}

begin
  # Reads all Projects
  result = api_instance.project_management_projects_get(include_inputed_minutes, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_get: #{e}"
end
```

#### Using the project_management_projects_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProjectsGet200Response>, Integer, Hash)> project_management_projects_get_with_http_info(include_inputed_minutes, opts)

```ruby
begin
  # Reads all Projects
  data, status_code, headers = api_instance.project_management_projects_get_with_http_info(include_inputed_minutes, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProjectsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include_inputed_minutes** | **Boolean** | If true we will perform the minutes calculations and will be return the total inputed_minutes. If false, 0 will be returned and no minutes calculations will be performed. |  |
| **ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the projects that matches the ids provided in the request. | [optional] |
| **name** | **String** | Retrieve only the projects that match the name passed in the request. (deprecated) | [optional] |
| **name_or_code** | **String** | Retrieve only the projects that match the name or code passed in the request. | [optional] |
| **include_costs** | **Boolean** | If true we will perform the costs calculations and will be return the total cost. If false, 0 will be returned and no costs calculations will be performed. | [optional] |
| **updated_after** | **String** | Retrieve only the projects that were created or updated after the date provided in the request. | [optional] |
| **legal_entity_id** | **String** | Retrieve only the projects that are related to the legal entity passed in the request. | [optional] |
| **client_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the projects that are related to the clients passed in the request, refers to finance/contacts. | [optional] |
| **no_clients** | **Boolean** | Retrieve only the projects that are not related to any client, refers to finance/contacts. | [optional] |
| **total_currency** | **String** | Retrieve only the projects that have the total cost in the currency passed in the request. | [optional] |

### Return type

[**ProjectManagementProjectsGet200Response**](ProjectManagementProjectsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_projects_id_get

> <ProjectManagementProject> project_management_projects_id_get(id)

Reads a single Project

###### **What does it do?** This reads the data of projects, and retrieves the information based on the permissions:    - If the user has the `team_leader` permission, he will only be able to read the projects that he is the team leader.   - If the user has the `reportees` permission, he will only be able to read the projects that he is the team leader or the projects that he is a team member.   - If the user has `everyone` permission, he will be able to read all projects.   - If the user has the `owned` permission, he will only be able to read the projects that he is the assigned.  ###### **Is it related to other entities?** A project is always related to a company, so you can use the query params to list only the projects that are related to a specific company. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission of read projects.

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

api_instance = F::ProjectManagementProjectApi.new
id = '314159' # String | Retrieve only the projects that matches the ids provided in the request.

begin
  # Reads a single Project
  result = api_instance.project_management_projects_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_id_get: #{e}"
end
```

#### Using the project_management_projects_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProject>, Integer, Hash)> project_management_projects_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Project
  data, status_code, headers = api_instance.project_management_projects_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProject>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Retrieve only the projects that matches the ids provided in the request. |  |

### Return type

[**ProjectManagementProject**](ProjectManagementProject.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_projects_id_put

> <ProjectManagementProject> project_management_projects_id_put(id, opts)

Updates a Project

###### **What does it do?** This updates a project with the given params. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with a role in the project.

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

api_instance = F::ProjectManagementProjectApi.new
id = '314159' # String | Id project.
opts = {
  project_management_projects_id_put_request: F::ProjectManagementProjectsIdPutRequest.new({id: '314159', name: 'Project Name'}) # ProjectManagementProjectsIdPutRequest | 
}

begin
  # Updates a Project
  result = api_instance.project_management_projects_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_id_put: #{e}"
end
```

#### Using the project_management_projects_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProject>, Integer, Hash)> project_management_projects_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Project
  data, status_code, headers = api_instance.project_management_projects_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProject>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id project. |  |
| **project_management_projects_id_put_request** | [**ProjectManagementProjectsIdPutRequest**](ProjectManagementProjectsIdPutRequest.md) |  | [optional] |

### Return type

[**ProjectManagementProject**](ProjectManagementProject.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_projects_post

> <ProjectManagementProject> project_management_projects_post(opts)

Creates a Project

###### **What does it do?** This creates a new project. By default, the project will be created with the status `active`. ###### **What body params do you need?**    - `name`: is mandatory to pass a name of the project.   - `code`: optional unique code for the project to be identifiable and searchable.   - `start_date`: optional start date for the project. If given must be in iso-8601 format (YYYY-MM-DD).   - `due_date`: optional due date for the project. If given must be in iso-8601 format (YYYY-MM-DD).   - `status`: a project can have the status `active` or `closed`. By default, the project will be created with the status `active`.   - `employees_assignment`: optional param to define the kind of assignation the project has. Its possible values are: [`manual`, `company`]. A project can have `manual` assignation or can be defined to be assigned to the whole `company`. Defaults to `manual`. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission of create projects.

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

api_instance = F::ProjectManagementProjectApi.new
opts = {
  project_management_projects_post_request: F::ProjectManagementProjectsPostRequest.new({name: 'Project Name'}) # ProjectManagementProjectsPostRequest | 
}

begin
  # Creates a Project
  result = api_instance.project_management_projects_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_post: #{e}"
end
```

#### Using the project_management_projects_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProject>, Integer, Hash)> project_management_projects_post_with_http_info(opts)

```ruby
begin
  # Creates a Project
  data, status_code, headers = api_instance.project_management_projects_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProject>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_management_projects_post_request** | [**ProjectManagementProjectsPostRequest**](ProjectManagementProjectsPostRequest.md) |  | [optional] |

### Return type

[**ProjectManagementProject**](ProjectManagementProject.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_projects_soft_delete_post

> <ProjectManagementProject> project_management_projects_soft_delete_post(opts)

Soft deletes a Project

###### **What does it do?** This soft deletes a project. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission of delete projects.

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

api_instance = F::ProjectManagementProjectApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Soft deletes a Project
  result = api_instance.project_management_projects_soft_delete_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_soft_delete_post: #{e}"
end
```

#### Using the project_management_projects_soft_delete_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementProject>, Integer, Hash)> project_management_projects_soft_delete_post_with_http_info(opts)

```ruby
begin
  # Soft deletes a Project
  data, status_code, headers = api_instance.project_management_projects_soft_delete_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementProject>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementProjectApi->project_management_projects_soft_delete_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**ProjectManagementProject**](ProjectManagementProject.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

