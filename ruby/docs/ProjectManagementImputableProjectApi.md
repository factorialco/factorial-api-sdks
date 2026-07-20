# F::ProjectManagementImputableProjectApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**project_management_imputable_projects_get**](ProjectManagementImputableProjectApi.md#project_management_imputable_projects_get) | **GET** /api/2026-07-01/resources/project_management/imputable_projects | Reads all Imputable projects |
| [**project_management_imputable_projects_id_get**](ProjectManagementImputableProjectApi.md#project_management_imputable_projects_id_get) | **GET** /api/2026-07-01/resources/project_management/imputable_projects/{id} | Reads a single Imputable project |


## project_management_imputable_projects_get

> <ProjectManagementImputableProjectsGet200Response> project_management_imputable_projects_get(opts)

Reads all Imputable projects

Reads all Imputable projects

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

api_instance = F::ProjectManagementImputableProjectApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Retrieve only the imputable projects that match the ids provided in the request.
  name_or_code: 'DS', # String | Retrieve only the imputable projects that match the name or code passed in the request.
  only_active: true, # Boolean | If true, retrieve only active imputable projects.
  assigned: true, # Boolean | If true, retrieve only imputable projects that have at least one assigned project worker.
  employee_ids: ['inner_example'] # Array<String> | Retrieve only the imputable projects in which the employees passed in the request are project workers.
}

begin
  # Reads all Imputable projects
  result = api_instance.project_management_imputable_projects_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementImputableProjectApi->project_management_imputable_projects_get: #{e}"
end
```

#### Using the project_management_imputable_projects_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementImputableProjectsGet200Response>, Integer, Hash)> project_management_imputable_projects_get_with_http_info(opts)

```ruby
begin
  # Reads all Imputable projects
  data, status_code, headers = api_instance.project_management_imputable_projects_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementImputableProjectsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementImputableProjectApi->project_management_imputable_projects_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the imputable projects that match the ids provided in the request. | [optional] |
| **name_or_code** | **String** | Retrieve only the imputable projects that match the name or code passed in the request. | [optional] |
| **only_active** | **Boolean** | If true, retrieve only active imputable projects. | [optional] |
| **assigned** | **Boolean** | If true, retrieve only imputable projects that have at least one assigned project worker. | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the imputable projects in which the employees passed in the request are project workers. | [optional] |

### Return type

[**ProjectManagementImputableProjectsGet200Response**](ProjectManagementImputableProjectsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_imputable_projects_id_get

> <ProjectManagementImputableProject> project_management_imputable_projects_id_get(id)

Reads a single Imputable project

Reads a single Imputable project

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

api_instance = F::ProjectManagementImputableProjectApi.new
id = '314159' # String | Retrieve only the imputable projects that match the ids provided in the request.

begin
  # Reads a single Imputable project
  result = api_instance.project_management_imputable_projects_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementImputableProjectApi->project_management_imputable_projects_id_get: #{e}"
end
```

#### Using the project_management_imputable_projects_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementImputableProject>, Integer, Hash)> project_management_imputable_projects_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Imputable project
  data, status_code, headers = api_instance.project_management_imputable_projects_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementImputableProject>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementImputableProjectApi->project_management_imputable_projects_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Retrieve only the imputable projects that match the ids provided in the request. |  |

### Return type

[**ProjectManagementImputableProject**](ProjectManagementImputableProject.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

