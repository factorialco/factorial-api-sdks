# F::ProjectManagementPlannedRecordApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**project_management_planned_records_bulk_create_post**](ProjectManagementPlannedRecordApi.md#project_management_planned_records_bulk_create_post) | **POST** /api/2026-07-01/resources/project_management/planned_records/bulk_create | Bulk creates a Planned record |
| [**project_management_planned_records_get**](ProjectManagementPlannedRecordApi.md#project_management_planned_records_get) | **GET** /api/2026-07-01/resources/project_management/planned_records | Reads all Planned records |
| [**project_management_planned_records_id_delete**](ProjectManagementPlannedRecordApi.md#project_management_planned_records_id_delete) | **DELETE** /api/2026-07-01/resources/project_management/planned_records/{id} | Deletes a Planned record |
| [**project_management_planned_records_id_get**](ProjectManagementPlannedRecordApi.md#project_management_planned_records_id_get) | **GET** /api/2026-07-01/resources/project_management/planned_records/{id} | Reads a single Planned record |
| [**project_management_planned_records_id_put**](ProjectManagementPlannedRecordApi.md#project_management_planned_records_id_put) | **PUT** /api/2026-07-01/resources/project_management/planned_records/{id} | Updates a Planned record |


## project_management_planned_records_bulk_create_post

> <Array<ProjectManagementPlannedRecord>> project_management_planned_records_bulk_create_post(opts)

Bulk creates a Planned record

Bulk creates a Planned record

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

api_instance = F::ProjectManagementPlannedRecordApi.new
opts = {
  project_management_planned_records_bulk_create_post_request: F::ProjectManagementPlannedRecordsBulkCreatePostRequest.new({project_worker_ids: ["314159"], start_date: '2025-01-01', end_date: '2025-01-03', daily_minutes: 100}) # ProjectManagementPlannedRecordsBulkCreatePostRequest | 
}

begin
  # Bulk creates a Planned record
  result = api_instance.project_management_planned_records_bulk_create_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementPlannedRecordApi->project_management_planned_records_bulk_create_post: #{e}"
end
```

#### Using the project_management_planned_records_bulk_create_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<ProjectManagementPlannedRecord>>, Integer, Hash)> project_management_planned_records_bulk_create_post_with_http_info(opts)

```ruby
begin
  # Bulk creates a Planned record
  data, status_code, headers = api_instance.project_management_planned_records_bulk_create_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<ProjectManagementPlannedRecord>>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementPlannedRecordApi->project_management_planned_records_bulk_create_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_management_planned_records_bulk_create_post_request** | [**ProjectManagementPlannedRecordsBulkCreatePostRequest**](ProjectManagementPlannedRecordsBulkCreatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;ProjectManagementPlannedRecord&gt;**](ProjectManagementPlannedRecord.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_planned_records_get

> <ProjectManagementPlannedRecordsGet200Response> project_management_planned_records_get(opts)

Reads all Planned records

Reads all Planned records

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

api_instance = F::ProjectManagementPlannedRecordApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Retrieve only the planned records that matches the ids provided in the request.
  project_worker_ids: ['inner_example'], # Array<String> | Retrieve only the planned records that matches the project worker ids provided in the request.
  start_date: '2025-01-01', # String | Retrieve only the planned records that matches the start date provided in the request.
  end_date: '2025-01-03', # String | Retrieve only the planned records that matches the end date provided in the request.
  subproject_ids: ['inner_example'] # Array<String> | Retrieve only the planned records that matches the subproject ids provided in the request.
}

begin
  # Reads all Planned records
  result = api_instance.project_management_planned_records_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementPlannedRecordApi->project_management_planned_records_get: #{e}"
end
```

#### Using the project_management_planned_records_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementPlannedRecordsGet200Response>, Integer, Hash)> project_management_planned_records_get_with_http_info(opts)

```ruby
begin
  # Reads all Planned records
  data, status_code, headers = api_instance.project_management_planned_records_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementPlannedRecordsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementPlannedRecordApi->project_management_planned_records_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the planned records that matches the ids provided in the request. | [optional] |
| **project_worker_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the planned records that matches the project worker ids provided in the request. | [optional] |
| **start_date** | **String** | Retrieve only the planned records that matches the start date provided in the request. | [optional] |
| **end_date** | **String** | Retrieve only the planned records that matches the end date provided in the request. | [optional] |
| **subproject_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the planned records that matches the subproject ids provided in the request. | [optional] |

### Return type

[**ProjectManagementPlannedRecordsGet200Response**](ProjectManagementPlannedRecordsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_planned_records_id_delete

> <ProjectManagementPlannedRecord> project_management_planned_records_id_delete(id)

Deletes a Planned record

Deletes a Planned record

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

api_instance = F::ProjectManagementPlannedRecordApi.new
id = '314159' # String | The id of the planned record to delete

begin
  # Deletes a Planned record
  result = api_instance.project_management_planned_records_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementPlannedRecordApi->project_management_planned_records_id_delete: #{e}"
end
```

#### Using the project_management_planned_records_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementPlannedRecord>, Integer, Hash)> project_management_planned_records_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Planned record
  data, status_code, headers = api_instance.project_management_planned_records_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementPlannedRecord>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementPlannedRecordApi->project_management_planned_records_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the planned record to delete |  |

### Return type

[**ProjectManagementPlannedRecord**](ProjectManagementPlannedRecord.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_planned_records_id_get

> <ProjectManagementPlannedRecord> project_management_planned_records_id_get(id)

Reads a single Planned record

Reads a single Planned record

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

api_instance = F::ProjectManagementPlannedRecordApi.new
id = '314159' # String | Retrieve only the planned records that matches the ids provided in the request.

begin
  # Reads a single Planned record
  result = api_instance.project_management_planned_records_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementPlannedRecordApi->project_management_planned_records_id_get: #{e}"
end
```

#### Using the project_management_planned_records_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementPlannedRecord>, Integer, Hash)> project_management_planned_records_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Planned record
  data, status_code, headers = api_instance.project_management_planned_records_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementPlannedRecord>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementPlannedRecordApi->project_management_planned_records_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Retrieve only the planned records that matches the ids provided in the request. |  |

### Return type

[**ProjectManagementPlannedRecord**](ProjectManagementPlannedRecord.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_planned_records_id_put

> <ProjectManagementPlannedRecord> project_management_planned_records_id_put(id, opts)

Updates a Planned record

Updates a Planned record

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

api_instance = F::ProjectManagementPlannedRecordApi.new
id = '314159' # String | The id of the planned record to update
opts = {
  project_management_planned_records_id_put_request: F::ProjectManagementPlannedRecordsIdPutRequest.new({id: '314159', start_date: '2025-01-01', end_date: '2025-01-03', daily_minutes: 100}) # ProjectManagementPlannedRecordsIdPutRequest | 
}

begin
  # Updates a Planned record
  result = api_instance.project_management_planned_records_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementPlannedRecordApi->project_management_planned_records_id_put: #{e}"
end
```

#### Using the project_management_planned_records_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementPlannedRecord>, Integer, Hash)> project_management_planned_records_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Planned record
  data, status_code, headers = api_instance.project_management_planned_records_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementPlannedRecord>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementPlannedRecordApi->project_management_planned_records_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the planned record to update |  |
| **project_management_planned_records_id_put_request** | [**ProjectManagementPlannedRecordsIdPutRequest**](ProjectManagementPlannedRecordsIdPutRequest.md) |  | [optional] |

### Return type

[**ProjectManagementPlannedRecord**](ProjectManagementPlannedRecord.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

