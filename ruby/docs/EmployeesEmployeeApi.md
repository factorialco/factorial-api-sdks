# F::EmployeesEmployeeApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**employees_employees_create_with_contract_post**](EmployeesEmployeeApi.md#employees_employees_create_with_contract_post) | **POST** /api/2026-07-01/resources/employees/employees/create_with_contract | Create with contracts an Employee |
| [**employees_employees_get**](EmployeesEmployeeApi.md#employees_employees_get) | **GET** /api/2026-07-01/resources/employees/employees | Reads all Employees |
| [**employees_employees_id_get**](EmployeesEmployeeApi.md#employees_employees_id_get) | **GET** /api/2026-07-01/resources/employees/employees/{id} | Reads a single Employee |
| [**employees_employees_id_put**](EmployeesEmployeeApi.md#employees_employees_id_put) | **PUT** /api/2026-07-01/resources/employees/employees/{id} | Updates an Employee |
| [**employees_employees_invite_post**](EmployeesEmployeeApi.md#employees_employees_invite_post) | **POST** /api/2026-07-01/resources/employees/employees/invite | Invites an Employee |
| [**employees_employees_set_regular_access_start_date_post**](EmployeesEmployeeApi.md#employees_employees_set_regular_access_start_date_post) | **POST** /api/2026-07-01/resources/employees/employees/set_regular_access_start_date | Set regular access start dates an Employee |
| [**employees_employees_terminate_post**](EmployeesEmployeeApi.md#employees_employees_terminate_post) | **POST** /api/2026-07-01/resources/employees/employees/terminate | Terminates an Employee |
| [**employees_employees_unterminate_post**](EmployeesEmployeeApi.md#employees_employees_unterminate_post) | **POST** /api/2026-07-01/resources/employees/employees/unterminate | Unterminates an Employee |


## employees_employees_create_with_contract_post

> <EmployeesEmployee> employees_employees_create_with_contract_post(opts)

Create with contracts an Employee

Create an employee with a contract

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

api_instance = F::EmployeesEmployeeApi.new
opts = {
  employees_employees_create_with_contract_post_request: F::EmployeesEmployeesCreateWithContractPostRequest.new({company_id: '1', first_name: 'Ana', last_name: 'Blanco Perez', email: 'ana@factorial.com'}) # EmployeesEmployeesCreateWithContractPostRequest | 
}

begin
  # Create with contracts an Employee
  result = api_instance.employees_employees_create_with_contract_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_create_with_contract_post: #{e}"
end
```

#### Using the employees_employees_create_with_contract_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeesEmployee>, Integer, Hash)> employees_employees_create_with_contract_post_with_http_info(opts)

```ruby
begin
  # Create with contracts an Employee
  data, status_code, headers = api_instance.employees_employees_create_with_contract_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeesEmployee>
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_create_with_contract_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employees_employees_create_with_contract_post_request** | [**EmployeesEmployeesCreateWithContractPostRequest**](EmployeesEmployeesCreateWithContractPostRequest.md) |  | [optional] |

### Return type

[**EmployeesEmployee**](EmployeesEmployee.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## employees_employees_get

> <EmployeesEmployeesGet200Response> employees_employees_get(only_active, only_managers, opts)

Reads all Employees

Only admins can see all the employees' information, regular users will get a restricted version of the payload as a response based on the permission set by the admin

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

api_instance = F::EmployeesEmployeeApi.new
only_active = true # Boolean | get only active employees
only_managers = true # Boolean | get only manager employees.
opts = {
  ids: ['inner_example'], # Array<String> | filter by employee ids.
  access_ids: ['inner_example'], # Array<String> | filter by employee access ids.
  emails: ['inner_example'], # Array<String> | filter by employee emails.
  full_text_name: 'Ana Lopez Perez', # String | filter by employee name.
  updated_at_gteq: '2024-01-01', # String | Filter employees by their latest update timestamp (`updated_at`), on or after this date. Only the date is considered; any time component is ignored (matching starts at 00:00:00 of the given date). Note: `updated_at` only stores the most recent update, so an employee updated multiple times is matched solely by its latest update, not by earlier ones.
  legal_entity_ids: ['inner_example'], # Array<String> | filter by legal entity id (refereces to companies/legal_entities).
  company_identifier: 'bb9d281e', # String | filter by employee company identifier.
  team_ids: ['inner_example'], # Array<String> | filter employees by team id (references to core/teams).
  location_ids: ['inner_example'], # Array<String> | filter employees by location id (references to locations/location).
  name_starts_with: 'Ana' # String | filter by employee names that start with the given text.
}

begin
  # Reads all Employees
  result = api_instance.employees_employees_get(only_active, only_managers, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_get: #{e}"
end
```

#### Using the employees_employees_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeesEmployeesGet200Response>, Integer, Hash)> employees_employees_get_with_http_info(only_active, only_managers, opts)

```ruby
begin
  # Reads all Employees
  data, status_code, headers = api_instance.employees_employees_get_with_http_info(only_active, only_managers, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeesEmployeesGet200Response>
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **only_active** | **Boolean** | get only active employees |  |
| **only_managers** | **Boolean** | get only manager employees. |  |
| **ids** | [**Array&lt;String&gt;**](String.md) | filter by employee ids. | [optional] |
| **access_ids** | [**Array&lt;String&gt;**](String.md) | filter by employee access ids. | [optional] |
| **emails** | [**Array&lt;String&gt;**](String.md) | filter by employee emails. | [optional] |
| **full_text_name** | **String** | filter by employee name. | [optional] |
| **updated_at_gteq** | **String** | Filter employees by their latest update timestamp (&#x60;updated_at&#x60;), on or after this date. Only the date is considered; any time component is ignored (matching starts at 00:00:00 of the given date). Note: &#x60;updated_at&#x60; only stores the most recent update, so an employee updated multiple times is matched solely by its latest update, not by earlier ones. | [optional] |
| **legal_entity_ids** | [**Array&lt;String&gt;**](String.md) | filter by legal entity id (refereces to companies/legal_entities). | [optional] |
| **company_identifier** | **String** | filter by employee company identifier. | [optional] |
| **team_ids** | [**Array&lt;String&gt;**](String.md) | filter employees by team id (references to core/teams). | [optional] |
| **location_ids** | [**Array&lt;String&gt;**](String.md) | filter employees by location id (references to locations/location). | [optional] |
| **name_starts_with** | **String** | filter by employee names that start with the given text. | [optional] |

### Return type

[**EmployeesEmployeesGet200Response**](EmployeesEmployeesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## employees_employees_id_get

> <EmployeesEmployee> employees_employees_id_get(id)

Reads a single Employee

Only admins can see all the employees' information, regular users will get a restricted version of the payload as a response based on the permission set by the admin

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

api_instance = F::EmployeesEmployeeApi.new
id = '1' # String | filter by employee ids.

begin
  # Reads a single Employee
  result = api_instance.employees_employees_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_id_get: #{e}"
end
```

#### Using the employees_employees_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeesEmployee>, Integer, Hash)> employees_employees_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Employee
  data, status_code, headers = api_instance.employees_employees_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeesEmployee>
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | filter by employee ids. |  |

### Return type

[**EmployeesEmployee**](EmployeesEmployee.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## employees_employees_id_put

> <EmployeesEmployee> employees_employees_id_put(id, opts)

Updates an Employee

Updates an Employee

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

api_instance = F::EmployeesEmployeeApi.new
id = '1' # String | id of the employee.
opts = {
  employees_employees_id_put_request: F::EmployeesEmployeesIdPutRequest.new({id: '1'}) # EmployeesEmployeesIdPutRequest | 
}

begin
  # Updates an Employee
  result = api_instance.employees_employees_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_id_put: #{e}"
end
```

#### Using the employees_employees_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeesEmployee>, Integer, Hash)> employees_employees_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates an Employee
  data, status_code, headers = api_instance.employees_employees_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeesEmployee>
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | id of the employee. |  |
| **employees_employees_id_put_request** | [**EmployeesEmployeesIdPutRequest**](EmployeesEmployeesIdPutRequest.md) |  | [optional] |

### Return type

[**EmployeesEmployee**](EmployeesEmployee.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## employees_employees_invite_post

> <EmployeesEmployee> employees_employees_invite_post(opts)

Invites an Employee

Send an email invitation to an unconfirmed employee to join Factorial

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

api_instance = F::EmployeesEmployeeApi.new
opts = {
  employees_employees_invite_post_request: F::EmployeesEmployeesInvitePostRequest.new({id: '1', company_id: '1'}) # EmployeesEmployeesInvitePostRequest | 
}

begin
  # Invites an Employee
  result = api_instance.employees_employees_invite_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_invite_post: #{e}"
end
```

#### Using the employees_employees_invite_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeesEmployee>, Integer, Hash)> employees_employees_invite_post_with_http_info(opts)

```ruby
begin
  # Invites an Employee
  data, status_code, headers = api_instance.employees_employees_invite_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeesEmployee>
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_invite_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employees_employees_invite_post_request** | [**EmployeesEmployeesInvitePostRequest**](EmployeesEmployeesInvitePostRequest.md) |  | [optional] |

### Return type

[**EmployeesEmployee**](EmployeesEmployee.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## employees_employees_set_regular_access_start_date_post

> <EmployeesEmployee> employees_employees_set_regular_access_start_date_post(opts)

Set regular access start dates an Employee

Set regular access start dates an Employee

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

api_instance = F::EmployeesEmployeeApi.new
opts = {
  employees_employees_set_regular_access_start_date_post_request: F::EmployeesEmployeesSetRegularAccessStartDatePostRequest.new({id: '1'}) # EmployeesEmployeesSetRegularAccessStartDatePostRequest | 
}

begin
  # Set regular access start dates an Employee
  result = api_instance.employees_employees_set_regular_access_start_date_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_set_regular_access_start_date_post: #{e}"
end
```

#### Using the employees_employees_set_regular_access_start_date_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeesEmployee>, Integer, Hash)> employees_employees_set_regular_access_start_date_post_with_http_info(opts)

```ruby
begin
  # Set regular access start dates an Employee
  data, status_code, headers = api_instance.employees_employees_set_regular_access_start_date_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeesEmployee>
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_set_regular_access_start_date_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employees_employees_set_regular_access_start_date_post_request** | [**EmployeesEmployeesSetRegularAccessStartDatePostRequest**](EmployeesEmployeesSetRegularAccessStartDatePostRequest.md) |  | [optional] |

### Return type

[**EmployeesEmployee**](EmployeesEmployee.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## employees_employees_terminate_post

> <EmployeesEmployee> employees_employees_terminate_post(opts)

Terminates an Employee

Terminates an Employee

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

api_instance = F::EmployeesEmployeeApi.new
opts = {
  employees_employees_terminate_post_request: F::EmployeesEmployeesTerminatePostRequest.new({id: '1', terminated_on: '2024-10-06'}) # EmployeesEmployeesTerminatePostRequest | 
}

begin
  # Terminates an Employee
  result = api_instance.employees_employees_terminate_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_terminate_post: #{e}"
end
```

#### Using the employees_employees_terminate_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeesEmployee>, Integer, Hash)> employees_employees_terminate_post_with_http_info(opts)

```ruby
begin
  # Terminates an Employee
  data, status_code, headers = api_instance.employees_employees_terminate_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeesEmployee>
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_terminate_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employees_employees_terminate_post_request** | [**EmployeesEmployeesTerminatePostRequest**](EmployeesEmployeesTerminatePostRequest.md) |  | [optional] |

### Return type

[**EmployeesEmployee**](EmployeesEmployee.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## employees_employees_unterminate_post

> <EmployeesEmployee> employees_employees_unterminate_post(opts)

Unterminates an Employee

Unterminates an Employee

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

api_instance = F::EmployeesEmployeeApi.new
opts = {
  ats_evaluation_forms_save_as_template_post_request: F::AtsEvaluationFormsSaveAsTemplatePostRequest.new({id: '1'}) # AtsEvaluationFormsSaveAsTemplatePostRequest | 
}

begin
  # Unterminates an Employee
  result = api_instance.employees_employees_unterminate_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_unterminate_post: #{e}"
end
```

#### Using the employees_employees_unterminate_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EmployeesEmployee>, Integer, Hash)> employees_employees_unterminate_post_with_http_info(opts)

```ruby
begin
  # Unterminates an Employee
  data, status_code, headers = api_instance.employees_employees_unterminate_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EmployeesEmployee>
rescue F::ApiError => e
  puts "Error when calling EmployeesEmployeeApi->employees_employees_unterminate_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_evaluation_forms_save_as_template_post_request** | [**AtsEvaluationFormsSaveAsTemplatePostRequest**](AtsEvaluationFormsSaveAsTemplatePostRequest.md) |  | [optional] |

### Return type

[**EmployeesEmployee**](EmployeesEmployee.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

