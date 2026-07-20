# F::ProjectManagementExpenseRecordApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**project_management_expense_records_get**](ProjectManagementExpenseRecordApi.md#project_management_expense_records_get) | **GET** /api/2026-07-01/resources/project_management/expense_records | Reads all Expense records |
| [**project_management_expense_records_id_get**](ProjectManagementExpenseRecordApi.md#project_management_expense_records_id_get) | **GET** /api/2026-07-01/resources/project_management/expense_records/{id} | Reads a single Expense record |


## project_management_expense_records_get

> <ProjectManagementExpenseRecordsGet200Response> project_management_expense_records_get(opts)

Reads all Expense records

Reads all Expense records

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

api_instance = F::ProjectManagementExpenseRecordApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Retrieve only the expense records that matches the project ids provided in the request.
  start_date: '2025-01-01', # String | Retrieve only the expense records with end date greater than or equal to the start date provided in the request.
  end_date: '2025-01-01', # String | Retrieve only the expense records with start date less than or equal to the end date provided in the request.
  expense_ids: ['inner_example'], # Array<String> | Retrieve only the expense records that matches the expense ids provided in the request.
  project_ids: ['inner_example'], # Array<String> | Retrieve only the expense records that matches the project ids provided in the request.
  subproject_ids: ['inner_example'], # Array<String> | Retrieve only the expense records that matches the subproject ids provided in the request.
  updated_after: '2025-01-01', # String | Retrieve only the expense records that matches the updated after date provided in the request.
  employee_user_name_like: 'John Doe', # String | Retrieve only the expense records that matches the employee user name like provided in the request.
  project_worker_ids: ['inner_example'] # Array<String> | Retrieve only the expense records that matches the project worker ids provided in the request.
}

begin
  # Reads all Expense records
  result = api_instance.project_management_expense_records_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementExpenseRecordApi->project_management_expense_records_get: #{e}"
end
```

#### Using the project_management_expense_records_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementExpenseRecordsGet200Response>, Integer, Hash)> project_management_expense_records_get_with_http_info(opts)

```ruby
begin
  # Reads all Expense records
  data, status_code, headers = api_instance.project_management_expense_records_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementExpenseRecordsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementExpenseRecordApi->project_management_expense_records_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the expense records that matches the project ids provided in the request. | [optional] |
| **start_date** | **String** | Retrieve only the expense records with end date greater than or equal to the start date provided in the request. | [optional] |
| **end_date** | **String** | Retrieve only the expense records with start date less than or equal to the end date provided in the request. | [optional] |
| **expense_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the expense records that matches the expense ids provided in the request. | [optional] |
| **project_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the expense records that matches the project ids provided in the request. | [optional] |
| **subproject_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the expense records that matches the subproject ids provided in the request. | [optional] |
| **updated_after** | **String** | Retrieve only the expense records that matches the updated after date provided in the request. | [optional] |
| **employee_user_name_like** | **String** | Retrieve only the expense records that matches the employee user name like provided in the request. | [optional] |
| **project_worker_ids** | [**Array&lt;String&gt;**](String.md) | Retrieve only the expense records that matches the project worker ids provided in the request. | [optional] |

### Return type

[**ProjectManagementExpenseRecordsGet200Response**](ProjectManagementExpenseRecordsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_expense_records_id_get

> <ProjectManagementExpenseRecord> project_management_expense_records_id_get(id)

Reads a single Expense record

Reads a single Expense record

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

api_instance = F::ProjectManagementExpenseRecordApi.new
id = '123' # String | Retrieve only the expense records that matches the project ids provided in the request.

begin
  # Reads a single Expense record
  result = api_instance.project_management_expense_records_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementExpenseRecordApi->project_management_expense_records_id_get: #{e}"
end
```

#### Using the project_management_expense_records_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementExpenseRecord>, Integer, Hash)> project_management_expense_records_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Expense record
  data, status_code, headers = api_instance.project_management_expense_records_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementExpenseRecord>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementExpenseRecordApi->project_management_expense_records_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Retrieve only the expense records that matches the project ids provided in the request. |  |

### Return type

[**ProjectManagementExpenseRecord**](ProjectManagementExpenseRecord.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

