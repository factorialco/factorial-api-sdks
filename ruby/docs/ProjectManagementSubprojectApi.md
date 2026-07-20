# F::ProjectManagementSubprojectApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**project_management_subprojects_get**](ProjectManagementSubprojectApi.md#project_management_subprojects_get) | **GET** /api/2026-07-01/resources/project_management/subprojects | Reads all Subprojects |
| [**project_management_subprojects_id_delete**](ProjectManagementSubprojectApi.md#project_management_subprojects_id_delete) | **DELETE** /api/2026-07-01/resources/project_management/subprojects/{id} | Deletes a Subproject |
| [**project_management_subprojects_id_get**](ProjectManagementSubprojectApi.md#project_management_subprojects_id_get) | **GET** /api/2026-07-01/resources/project_management/subprojects/{id} | Reads a single Subproject |
| [**project_management_subprojects_id_put**](ProjectManagementSubprojectApi.md#project_management_subprojects_id_put) | **PUT** /api/2026-07-01/resources/project_management/subprojects/{id} | Updates a Subproject |
| [**project_management_subprojects_post**](ProjectManagementSubprojectApi.md#project_management_subprojects_post) | **POST** /api/2026-07-01/resources/project_management/subprojects | Creates a Subproject |
| [**project_management_subprojects_rename_post**](ProjectManagementSubprojectApi.md#project_management_subprojects_rename_post) | **POST** /api/2026-07-01/resources/project_management/subprojects/rename | Renames a Subproject |


## project_management_subprojects_get

> <ProjectManagementSubprojectsGet200Response> project_management_subprojects_get(opts)

Reads all Subprojects

###### **What does it do?** This reads all subprojects created ###### **What params does it accept?**    - `ids`: retrieve only the subprojects that matches the ids passed in the request.\\n   - `include_inputed_minutes`: if `true` we will perform the minutes calculations and will be return the total `inputed_minutes`. If the param is not passed in the request, its default value is `FALSE` so it will return `inputed_minutes: 0` and no minutes calculations will be performed.   - `updated_after`: this parameter is needed to filter subprojects created or updated after a date.  ###### **Is it related to other entities?** A subproject is always related to a project, so you can use the query params to list only the subprojects that are related to a specific project. ###### **Who can use it?** Only companies who have enabled the `projects_with_subprojects` feature and users with the permission of read subprojects.

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

api_instance = F::ProjectManagementSubprojectApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Retrieve only the subprojects that matches the ids passed in the request.
  project_ids: ['inner_example'], # Array<String> | Retrieve only the subprojects that belongs to the project ids passed in the request.
  name: 'Subproject name', # String | Retrieve only the subprojects that matches the name passed in the request.
  include_no_subproject: true, # Boolean | 
  include_inputed_minutes: true, # Boolean | If `true` we will perform the minutes calculations and will be return the total `inputed_minutes`. If the param is not passed in the request, its default value is `FALSE` so it will return `inputed_minutes: 0` and no minutes calculations will be performed.
  include_cost: true, # Boolean | If `true` we will perform the cost calculations and will be return the total `labor_cost_cents`. If the param is not passed in the request, its default value is `FALSE` so it will return `labor_cost_cents: 0` and no cost calculations will be performed.
  updated_after: '1993-08-23' # String | Retrieve only the subprojects that were updated after the date passed in the request.
}

begin
  # Reads all Subprojects
  result = api_instance.project_management_subprojects_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementSubprojectApi->project_management_subprojects_get: #{e}"
end
```

#### Using the project_management_subprojects_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementSubprojectsGet200Response>, Integer, Hash)> project_management_subprojects_get_with_http_info(opts)

```ruby
begin
  # Reads all Subprojects
  data, status_code, headers = api_instance.project_management_subprojects_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementSubprojectsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementSubprojectApi->project_management_subprojects_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the subprojects that matches the ids passed in the request. | [optional] |
| **project_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the subprojects that belongs to the project ids passed in the request. | [optional] |
| **name** | **String** | Retrieve only the subprojects that matches the name passed in the request. | [optional] |
| **include_no_subproject** | **Boolean** |  | [optional] |
| **include_inputed_minutes** | **Boolean** | If &#x60;true&#x60; we will perform the minutes calculations and will be return the total &#x60;inputed_minutes&#x60;. If the param is not passed in the request, its default value is &#x60;FALSE&#x60; so it will return &#x60;inputed_minutes: 0&#x60; and no minutes calculations will be performed. | [optional] |
| **include_cost** | **Boolean** | If &#x60;true&#x60; we will perform the cost calculations and will be return the total &#x60;labor_cost_cents&#x60;. If the param is not passed in the request, its default value is &#x60;FALSE&#x60; so it will return &#x60;labor_cost_cents: 0&#x60; and no cost calculations will be performed. | [optional] |
| **updated_after** | **String** | Retrieve only the subprojects that were updated after the date passed in the request. | [optional] |

### Return type

[**ProjectManagementSubprojectsGet200Response**](ProjectManagementSubprojectsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_subprojects_id_delete

> <ProjectManagementSubproject> project_management_subprojects_id_delete(id)

Deletes a Subproject

###### **What does it do?** This deletes a subproject. ###### **Who can use it?** Only companies who have enabled the `projects_with_subprojects` feature and users with a role in the project owning the subproject.

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

api_instance = F::ProjectManagementSubprojectApi.new
id = '1' # String | 

begin
  # Deletes a Subproject
  result = api_instance.project_management_subprojects_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementSubprojectApi->project_management_subprojects_id_delete: #{e}"
end
```

#### Using the project_management_subprojects_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementSubproject>, Integer, Hash)> project_management_subprojects_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Subproject
  data, status_code, headers = api_instance.project_management_subprojects_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementSubproject>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementSubprojectApi->project_management_subprojects_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**ProjectManagementSubproject**](ProjectManagementSubproject.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_subprojects_id_get

> <ProjectManagementSubproject> project_management_subprojects_id_get(id)

Reads a single Subproject

###### **What does it do?** This reads all subprojects created ###### **What params does it accept?**    - `ids`: retrieve only the subprojects that matches the ids passed in the request.\\n   - `include_inputed_minutes`: if `true` we will perform the minutes calculations and will be return the total `inputed_minutes`. If the param is not passed in the request, its default value is `FALSE` so it will return `inputed_minutes: 0` and no minutes calculations will be performed.   - `updated_after`: this parameter is needed to filter subprojects created or updated after a date.  ###### **Is it related to other entities?** A subproject is always related to a project, so you can use the query params to list only the subprojects that are related to a specific project. ###### **Who can use it?** Only companies who have enabled the `projects_with_subprojects` feature and users with the permission of read subprojects.

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

api_instance = F::ProjectManagementSubprojectApi.new
id = '314' # String | Retrieve only the subprojects that matches the ids passed in the request.

begin
  # Reads a single Subproject
  result = api_instance.project_management_subprojects_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementSubprojectApi->project_management_subprojects_id_get: #{e}"
end
```

#### Using the project_management_subprojects_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementSubproject>, Integer, Hash)> project_management_subprojects_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Subproject
  data, status_code, headers = api_instance.project_management_subprojects_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementSubproject>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementSubprojectApi->project_management_subprojects_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Retrieve only the subprojects that matches the ids passed in the request. |  |

### Return type

[**ProjectManagementSubproject**](ProjectManagementSubproject.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_subprojects_id_put

> <ProjectManagementSubproject> project_management_subprojects_id_put(id, opts)

Updates a Subproject

###### **What does it do?** This updates the subproject details.

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

api_instance = F::ProjectManagementSubprojectApi.new
id = '314' # String | The id of the subproject.
opts = {
  project_management_subprojects_id_put_request: F::ProjectManagementSubprojectsIdPutRequest.new({id: '314'}) # ProjectManagementSubprojectsIdPutRequest | 
}

begin
  # Updates a Subproject
  result = api_instance.project_management_subprojects_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementSubprojectApi->project_management_subprojects_id_put: #{e}"
end
```

#### Using the project_management_subprojects_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementSubproject>, Integer, Hash)> project_management_subprojects_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Subproject
  data, status_code, headers = api_instance.project_management_subprojects_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementSubproject>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementSubprojectApi->project_management_subprojects_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the subproject. |  |
| **project_management_subprojects_id_put_request** | [**ProjectManagementSubprojectsIdPutRequest**](ProjectManagementSubprojectsIdPutRequest.md) |  | [optional] |

### Return type

[**ProjectManagementSubproject**](ProjectManagementSubproject.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_subprojects_post

> <ProjectManagementSubproject> project_management_subprojects_post(opts)

Creates a Subproject

###### **What does it do?** This creates a new subproject. ###### **Is it related to other entities?** A subproject is always related to a project. ###### **Who can use it?** Only companies who have enabled the `projects_with_subprojects` feature and users with a role in the project owning the subproject.

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

api_instance = F::ProjectManagementSubprojectApi.new
opts = {
  project_management_subprojects_post_request: F::ProjectManagementSubprojectsPostRequest.new({name: 'name_example', project_id: 'project_id_example'}) # ProjectManagementSubprojectsPostRequest | 
}

begin
  # Creates a Subproject
  result = api_instance.project_management_subprojects_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementSubprojectApi->project_management_subprojects_post: #{e}"
end
```

#### Using the project_management_subprojects_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementSubproject>, Integer, Hash)> project_management_subprojects_post_with_http_info(opts)

```ruby
begin
  # Creates a Subproject
  data, status_code, headers = api_instance.project_management_subprojects_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementSubproject>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementSubprojectApi->project_management_subprojects_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_management_subprojects_post_request** | [**ProjectManagementSubprojectsPostRequest**](ProjectManagementSubprojectsPostRequest.md) |  | [optional] |

### Return type

[**ProjectManagementSubproject**](ProjectManagementSubproject.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_subprojects_rename_post

> <ProjectManagementSubproject> project_management_subprojects_rename_post(opts)

Renames a Subproject

###### **What does it do?** This renames a subproject. ###### **Who can use it?** Only companies who have enabled the `projects_with_subprojects` feature and users with a role in the project owning the subproject.

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

api_instance = F::ProjectManagementSubprojectApi.new
opts = {
  locations_work_areas_id_put_request: F::LocationsWorkAreasIdPutRequest.new({id: 'id_example', name: 'name_example'}) # LocationsWorkAreasIdPutRequest | 
}

begin
  # Renames a Subproject
  result = api_instance.project_management_subprojects_rename_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementSubprojectApi->project_management_subprojects_rename_post: #{e}"
end
```

#### Using the project_management_subprojects_rename_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementSubproject>, Integer, Hash)> project_management_subprojects_rename_post_with_http_info(opts)

```ruby
begin
  # Renames a Subproject
  data, status_code, headers = api_instance.project_management_subprojects_rename_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementSubproject>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementSubprojectApi->project_management_subprojects_rename_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **locations_work_areas_id_put_request** | [**LocationsWorkAreasIdPutRequest**](LocationsWorkAreasIdPutRequest.md) |  | [optional] |

### Return type

[**ProjectManagementSubproject**](ProjectManagementSubproject.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

