# F::ProjectManagementExportableProject

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the project |  |
| **date** | **String** | The date of imputed time | [optional] |
| **project_name** | **String** | The name of the project |  |
| **project_code** | **String** | The code of the project | [optional] |
| **project_start_date** | **String** | The start date of the project | [optional] |
| **project_due_date** | **String** | The due date of the project | [optional] |
| **project_status** | **String** | The status of the project |  |
| **subproject_name** | **String** | The name of the subproject | [optional] |
| **employee_name** | **String** | The name of the employee | [optional] |
| **employee_id** | **String** | The id of the employee | [optional] |
| **inputed_time** | **String** | The time imputed by the employee |  |
| **client_id** | **String** | The client id of the project | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ProjectManagementExportableProject.new(
  id: id,
  date: 2021-01-01,
  project_name: Project name,
  project_code: 123,
  project_start_date: 2021-01-01,
  project_due_date: 2022-01-01,
  project_status: active,
  subproject_name: Subproject name,
  employee_name: Bob The Boss,
  employee_id: 123,
  inputed_time: 60.00,
  client_id: 123
)
```

