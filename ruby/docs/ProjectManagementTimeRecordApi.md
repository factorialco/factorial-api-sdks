# F::ProjectManagementTimeRecordApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**project_management_time_records_bulk_delete_post**](ProjectManagementTimeRecordApi.md#project_management_time_records_bulk_delete_post) | **POST** /api/2026-07-01/resources/project_management/time_records/bulk_delete | Bulk deletes a Time record |
| [**project_management_time_records_bulk_process_post**](ProjectManagementTimeRecordApi.md#project_management_time_records_bulk_process_post) | **POST** /api/2026-07-01/resources/project_management/time_records/bulk_process | Bulk processes a Time record |
| [**project_management_time_records_get**](ProjectManagementTimeRecordApi.md#project_management_time_records_get) | **GET** /api/2026-07-01/resources/project_management/time_records | Reads all Time records |
| [**project_management_time_records_id_delete**](ProjectManagementTimeRecordApi.md#project_management_time_records_id_delete) | **DELETE** /api/2026-07-01/resources/project_management/time_records/{id} | Deletes a Time record |
| [**project_management_time_records_id_get**](ProjectManagementTimeRecordApi.md#project_management_time_records_id_get) | **GET** /api/2026-07-01/resources/project_management/time_records/{id} | Reads a single Time record |
| [**project_management_time_records_post**](ProjectManagementTimeRecordApi.md#project_management_time_records_post) | **POST** /api/2026-07-01/resources/project_management/time_records | Creates a Time record |
| [**project_management_time_records_update_project_worker_post**](ProjectManagementTimeRecordApi.md#project_management_time_records_update_project_worker_post) | **POST** /api/2026-07-01/resources/project_management/time_records/update_project_worker | Update project workers a Time record |


## project_management_time_records_bulk_delete_post

> <Array<ProjectManagementTimeRecord>> project_management_time_records_bulk_delete_post(opts)

Bulk deletes a Time record

###### **What does it do?** This endpoint is used to bulk delete all the time records in a particular `date` for a specific `project_worker_id`.

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

api_instance = F::ProjectManagementTimeRecordApi.new
opts = {
  project_management_time_records_bulk_delete_post_request: F::ProjectManagementTimeRecordsBulkDeletePostRequest.new({date: 'date_example', project_worker_id: 'project_worker_id_example'}) # ProjectManagementTimeRecordsBulkDeletePostRequest | 
}

begin
  # Bulk deletes a Time record
  result = api_instance.project_management_time_records_bulk_delete_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementTimeRecordApi->project_management_time_records_bulk_delete_post: #{e}"
end
```

#### Using the project_management_time_records_bulk_delete_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<ProjectManagementTimeRecord>>, Integer, Hash)> project_management_time_records_bulk_delete_post_with_http_info(opts)

```ruby
begin
  # Bulk deletes a Time record
  data, status_code, headers = api_instance.project_management_time_records_bulk_delete_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<ProjectManagementTimeRecord>>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementTimeRecordApi->project_management_time_records_bulk_delete_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_management_time_records_bulk_delete_post_request** | [**ProjectManagementTimeRecordsBulkDeletePostRequest**](ProjectManagementTimeRecordsBulkDeletePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;ProjectManagementTimeRecord&gt;**](ProjectManagementTimeRecord.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_time_records_bulk_process_post

> <Array<ProjectManagementTimeRecord>> project_management_time_records_bulk_process_post(opts)

Bulk processes a Time record

###### **What does it do?** This versatile endpoint allows for the creation, update, or deletion of a time record associated with an `attendance_shift_id`. To achieve this, provide an array of items with the following structure:    ```json     [{       \"time_record_id\": number | null,       \"attendance_shift_id\": number | null,       \"project_worker_id\": number | null,       \"subproject_id\": number | null     }]   ```    - If no `time_record_id` provided, a created will be performed with the other data that will be required (except for `subproject_id`, that is always optional).   - If `time_record_id but no other data provided, then the action will be a **delete**.   - If `time_record_id` and more data, then it's an **update**.  Please note: The relationship between `time_record` and `attendance_shift` is unique. In the provided array of items, if two items have exactly the same `attendance_shift_id`, only the last action specified will be executed, **unless the first action is a delete and the second one an update**. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature.

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

api_instance = F::ProjectManagementTimeRecordApi.new
opts = {
  project_management_time_records_bulk_process_post_request: F::ProjectManagementTimeRecordsBulkProcessPostRequest.new({items: [3.56]}) # ProjectManagementTimeRecordsBulkProcessPostRequest | 
}

begin
  # Bulk processes a Time record
  result = api_instance.project_management_time_records_bulk_process_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementTimeRecordApi->project_management_time_records_bulk_process_post: #{e}"
end
```

#### Using the project_management_time_records_bulk_process_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<ProjectManagementTimeRecord>>, Integer, Hash)> project_management_time_records_bulk_process_post_with_http_info(opts)

```ruby
begin
  # Bulk processes a Time record
  data, status_code, headers = api_instance.project_management_time_records_bulk_process_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<ProjectManagementTimeRecord>>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementTimeRecordApi->project_management_time_records_bulk_process_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_management_time_records_bulk_process_post_request** | [**ProjectManagementTimeRecordsBulkProcessPostRequest**](ProjectManagementTimeRecordsBulkProcessPostRequest.md) |  | [optional] |

### Return type

[**Array&lt;ProjectManagementTimeRecord&gt;**](ProjectManagementTimeRecord.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_time_records_get

> <ProjectManagementTimeRecordsGet200Response> project_management_time_records_get(opts)

Reads all Time records

###### **What does it do?** This endpoint reads and retrieves a list of time records. You can utilize URL parameters to filter the results. ###### **What params does it accept?**    - `ids`: retrieve only the time records that matches the `ids` passed in the request.   - `project_workers_ids`: Retrieve only the time records assigned to any `project_workers_ids` passed in the request.   - `subproject_ids`: retrieve only the time records related with any `subproject_ids` passed in the request.   - `attendance_shift_ids`: retrieve only the time records related with any `attendance_shift_ids` passed in the request.   - `employee_ids`: ⚠️ This param, will be deprecated soon. **Please use `project_worker_ids` param instead.**   - `month`: Filter time records created in a specific month of the year.   - `year`: To be used with the `month` parameter to filter time records created in a particular period.   - `updated_after`: this parameter is needed to filter time records created or updated after a date.  ###### **Is it related to other entities?** A `time_record` is mandatory related to a `project_worker_id` and an `attendance_shift_id`. Optionally, it can be related to a subproject. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission to read time_records.

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

api_instance = F::ProjectManagementTimeRecordApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Time record ids to retrieve
  project_worker_ids: ['inner_example'], # Array<String> | Project worker ids to retrieve
  subproject_ids: ['inner_example'], # Array<String> | Subproject ids to retrieve
  attendance_shift_ids: ['inner_example'], # Array<String> | Attendance shift ids to retrieve
  employee_ids: ['inner_example'], # Array<String> | Employee ids to retrieve
  month: 1, # Integer | Month to filter
  year: 2021, # Integer | Year to filter
  updated_after: 'updated_after_example' # String | 
}

begin
  # Reads all Time records
  result = api_instance.project_management_time_records_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementTimeRecordApi->project_management_time_records_get: #{e}"
end
```

#### Using the project_management_time_records_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementTimeRecordsGet200Response>, Integer, Hash)> project_management_time_records_get_with_http_info(opts)

```ruby
begin
  # Reads all Time records
  data, status_code, headers = api_instance.project_management_time_records_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementTimeRecordsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementTimeRecordApi->project_management_time_records_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Time record ids to retrieve | [optional] |
| **project_worker_ids** | [**Array&lt;String&gt;**](String.md) | Project worker ids to retrieve | [optional] |
| **subproject_ids** | [**Array&lt;String&gt;**](String.md) | Subproject ids to retrieve | [optional] |
| **attendance_shift_ids** | [**Array&lt;String&gt;**](String.md) | Attendance shift ids to retrieve | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Employee ids to retrieve | [optional] |
| **month** | **Integer** | Month to filter | [optional] |
| **year** | **Integer** | Year to filter | [optional] |
| **updated_after** | **String** |  | [optional] |

### Return type

[**ProjectManagementTimeRecordsGet200Response**](ProjectManagementTimeRecordsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_time_records_id_delete

> <ProjectManagementTimeRecord> project_management_time_records_id_delete(id)

Deletes a Time record

Deletes a Time record

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

api_instance = F::ProjectManagementTimeRecordApi.new
id = '1' # String | 

begin
  # Deletes a Time record
  result = api_instance.project_management_time_records_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementTimeRecordApi->project_management_time_records_id_delete: #{e}"
end
```

#### Using the project_management_time_records_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementTimeRecord>, Integer, Hash)> project_management_time_records_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Time record
  data, status_code, headers = api_instance.project_management_time_records_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementTimeRecord>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementTimeRecordApi->project_management_time_records_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**ProjectManagementTimeRecord**](ProjectManagementTimeRecord.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_time_records_id_get

> <ProjectManagementTimeRecord> project_management_time_records_id_get(id)

Reads a single Time record

###### **What does it do?** This endpoint reads and retrieves a list of time records. You can utilize URL parameters to filter the results. ###### **What params does it accept?**    - `ids`: retrieve only the time records that matches the `ids` passed in the request.   - `project_workers_ids`: Retrieve only the time records assigned to any `project_workers_ids` passed in the request.   - `subproject_ids`: retrieve only the time records related with any `subproject_ids` passed in the request.   - `attendance_shift_ids`: retrieve only the time records related with any `attendance_shift_ids` passed in the request.   - `employee_ids`: ⚠️ This param, will be deprecated soon. **Please use `project_worker_ids` param instead.**   - `month`: Filter time records created in a specific month of the year.   - `year`: To be used with the `month` parameter to filter time records created in a particular period.   - `updated_after`: this parameter is needed to filter time records created or updated after a date.  ###### **Is it related to other entities?** A `time_record` is mandatory related to a `project_worker_id` and an `attendance_shift_id`. Optionally, it can be related to a subproject. ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission to read time_records.

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

api_instance = F::ProjectManagementTimeRecordApi.new
id = '1' # String | Time record ids to retrieve

begin
  # Reads a single Time record
  result = api_instance.project_management_time_records_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementTimeRecordApi->project_management_time_records_id_get: #{e}"
end
```

#### Using the project_management_time_records_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementTimeRecord>, Integer, Hash)> project_management_time_records_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Time record
  data, status_code, headers = api_instance.project_management_time_records_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementTimeRecord>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementTimeRecordApi->project_management_time_records_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Time record ids to retrieve |  |

### Return type

[**ProjectManagementTimeRecord**](ProjectManagementTimeRecord.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_time_records_post

> <ProjectManagementTimeRecord> project_management_time_records_post(opts)

Creates a Time record

###### **What does it do?** \"This endpoint is used to create time records. A time record is an entity that establishes a mandatory relationship between `project_worker` and `attendance_shift_id`, and optionally with `subproject`. For a successful creation of a `time_record`, the `project_worker` must be **assigned**, and the associated `project` must be **active**.\" ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission to create `time_records`.

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

api_instance = F::ProjectManagementTimeRecordApi.new
opts = {
  project_management_time_records_post_request: F::ProjectManagementTimeRecordsPostRequest.new({project_worker_id: 'project_worker_id_example'}) # ProjectManagementTimeRecordsPostRequest | 
}

begin
  # Creates a Time record
  result = api_instance.project_management_time_records_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementTimeRecordApi->project_management_time_records_post: #{e}"
end
```

#### Using the project_management_time_records_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementTimeRecord>, Integer, Hash)> project_management_time_records_post_with_http_info(opts)

```ruby
begin
  # Creates a Time record
  data, status_code, headers = api_instance.project_management_time_records_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementTimeRecord>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementTimeRecordApi->project_management_time_records_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_management_time_records_post_request** | [**ProjectManagementTimeRecordsPostRequest**](ProjectManagementTimeRecordsPostRequest.md) |  | [optional] |

### Return type

[**ProjectManagementTimeRecord**](ProjectManagementTimeRecord.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_time_records_update_project_worker_post

> <ProjectManagementTimeRecord> project_management_time_records_update_project_worker_post(opts)

Update project workers a Time record

###### **What does it do?** This endpoint is used to change the project that an employee (`project_worker`) has assigned to an `attendance_shift`.

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

api_instance = F::ProjectManagementTimeRecordApi.new
opts = {
  project_management_time_records_update_project_worker_post_request: F::ProjectManagementTimeRecordsUpdateProjectWorkerPostRequest.new({id: 'id_example', project_worker_id: 'project_worker_id_example'}) # ProjectManagementTimeRecordsUpdateProjectWorkerPostRequest | 
}

begin
  # Update project workers a Time record
  result = api_instance.project_management_time_records_update_project_worker_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementTimeRecordApi->project_management_time_records_update_project_worker_post: #{e}"
end
```

#### Using the project_management_time_records_update_project_worker_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementTimeRecord>, Integer, Hash)> project_management_time_records_update_project_worker_post_with_http_info(opts)

```ruby
begin
  # Update project workers a Time record
  data, status_code, headers = api_instance.project_management_time_records_update_project_worker_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementTimeRecord>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementTimeRecordApi->project_management_time_records_update_project_worker_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_management_time_records_update_project_worker_post_request** | [**ProjectManagementTimeRecordsUpdateProjectWorkerPostRequest**](ProjectManagementTimeRecordsUpdateProjectWorkerPostRequest.md) |  | [optional] |

### Return type

[**ProjectManagementTimeRecord**](ProjectManagementTimeRecord.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

