# F::ProjectManagementExportableExpenseApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**project_management_exportable_expenses_get**](ProjectManagementExportableExpenseApi.md#project_management_exportable_expenses_get) | **GET** /api/2026-07-01/resources/project_management/exportable_expenses | Reads all Exportable expenses |


## project_management_exportable_expenses_get

> <ProjectManagementExportableExpensesGet200Response> project_management_exportable_expenses_get(start_date, end_date, project_ids)

Reads all Exportable expenses

###### **What does it do?**    This will generate an export of the type **\"Project's expenses\"**. You will have to pass the start and end date to determine the range for which htis information will be exported; as well as the projects ids to get the information of specifically given projects.  ###### **What params does it accept?**   - `start_date`: It's mandatory to pass this data, being start date to delimit the range of information exported.   - `end_date`: It's mandatory to pass this data, corresponding to an end date for the date range of data to be exported.   - `project_ids`: Mandatory data to pass to the export, specifying the projects to be exported from.  ###### **Who can use it?** Only companies who have enabled the `projects_management` feature and users with the permission of read projects.

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

api_instance = F::ProjectManagementExportableExpenseApi.new
start_date = 'start_date_example' # String | 
end_date = 'end_date_example' # String | 
project_ids = ['inner_example'] # Array<String> | 

begin
  # Reads all Exportable expenses
  result = api_instance.project_management_exportable_expenses_get(start_date, end_date, project_ids)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementExportableExpenseApi->project_management_exportable_expenses_get: #{e}"
end
```

#### Using the project_management_exportable_expenses_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementExportableExpensesGet200Response>, Integer, Hash)> project_management_exportable_expenses_get_with_http_info(start_date, end_date, project_ids)

```ruby
begin
  # Reads all Exportable expenses
  data, status_code, headers = api_instance.project_management_exportable_expenses_get_with_http_info(start_date, end_date, project_ids)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementExportableExpensesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementExportableExpenseApi->project_management_exportable_expenses_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **start_date** | **String** |  |  |
| **end_date** | **String** |  |  |
| **project_ids** | [**Array&lt;String&gt;**](String.md) |  |  |

### Return type

[**ProjectManagementExportableExpensesGet200Response**](ProjectManagementExportableExpensesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

