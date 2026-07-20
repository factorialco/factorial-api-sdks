# F::EmployeeUpdatesPersonalChangeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**employee_updates_personal_changes_get**](EmployeeUpdatesPersonalChangeApi.md#employee_updates_personal_changes_get) | **GET** /api/2026-07-01/resources/employee_updates/personal_changes | Reads all Personal changes |
| [**employee_updates_personal_changes_id_get**](EmployeeUpdatesPersonalChangeApi.md#employee_updates_personal_changes_id_get) | **GET** /api/2026-07-01/resources/employee_updates/personal_changes/{id} | Reads a single Personal change |


## employee_updates_personal_changes_get

> <EmployeeUpdatesPersonalChangesGet200Response> employee_updates_personal_changes_get(opts)

Reads all Personal changes

This endpoint can be used to retrieve a list of personal changes `employee updates`.

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

api_instance = F::EmployeeUpdatesPersonalChangeApi.new
opts = {
  ids: ['inner_example'] # Array<String> | filter by personal change incidence ids.
}

begin
  # Reads all Personal changes
  result = api_instance.employee_updates_personal_changes_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesPersonalChangeApi->employee_updates_personal_changes_get: #{e}"
end
```

#### Using the employee_updates_personal_changes_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeeUpdatesPersonalChangesGet200Response>, Integer, Hash)> employee_updates_personal_changes_get_with_http_info(opts)

```ruby
begin
  # Reads all Personal changes
  data, status_code, headers = api_instance.employee_updates_personal_changes_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeeUpdatesPersonalChangesGet200Response>
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesPersonalChangeApi->employee_updates_personal_changes_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | filter by personal change incidence ids. | [optional] |

### Return type

[**EmployeeUpdatesPersonalChangesGet200Response**](EmployeeUpdatesPersonalChangesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## employee_updates_personal_changes_id_get

> <EmployeeUpdatesPersonalChange> employee_updates_personal_changes_id_get(id)

Reads a single Personal change

This endpoint can be used to retrieve a list of personal changes `employee updates`.

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

api_instance = F::EmployeeUpdatesPersonalChangeApi.new
id = '1' # String | filter by personal change incidence ids.

begin
  # Reads a single Personal change
  result = api_instance.employee_updates_personal_changes_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesPersonalChangeApi->employee_updates_personal_changes_id_get: #{e}"
end
```

#### Using the employee_updates_personal_changes_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeeUpdatesPersonalChange>, Integer, Hash)> employee_updates_personal_changes_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Personal change
  data, status_code, headers = api_instance.employee_updates_personal_changes_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeeUpdatesPersonalChange>
rescue F::ApiError => e
  puts "Error when calling EmployeeUpdatesPersonalChangeApi->employee_updates_personal_changes_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | filter by personal change incidence ids. |  |

### Return type

[**EmployeeUpdatesPersonalChange**](EmployeeUpdatesPersonalChange.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

