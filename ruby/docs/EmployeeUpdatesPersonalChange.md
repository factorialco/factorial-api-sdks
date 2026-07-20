# F::EmployeeUpdatesPersonalChange

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the new hire incidence |  |
| **status** | **String** | The status of the new hire incidence |  |
| **employee_id** | **String** | The employee id of the new hire |  |
| **work_email** | **String** | personal email of the employee. | [optional] |
| **phone_number** | **String** | phone number of the employee. | [optional] |
| **identifier_type** | **String** | type of identifier (ex passport). | [optional] |
| **identifier** | **String** | national identifier number. | [optional] |
| **social_security_number** | **String** | social security number of the employee. | [optional] |
| **tax_id** | **String** |  | [optional] |
| **first_name** | **String** | name of the employee. |  |
| **last_name** | **String** | last name of the employee. |  |
| **gender** | **String** | gender of the employee (male | female). | [optional] |
| **date_of_birth** | **String** | birthday of the employee. | [optional] |
| **nationality** | **String** | nationality country code of the employee (Spain ES, United Kingdom GB). | [optional] |
| **address_line_1** | **String** | address line 1 of the employee. | [optional] |
| **address_line_2** | **String** | address line 1 of the employee. | [optional] |
| **postal_code** | **String** | postal code of the employee. | [optional] |
| **city** | **String** | city of the employee. | [optional] |
| **state** | **String** | state/province/region of the employee. | [optional] |
| **country** | **String** | country code of the employee (Spain ES, United Kingdom GB). | [optional] |
| **bank_number** | **String** | bank account number of the employee. | [optional] |
| **job_title** | **String** | job title of the employee. | [optional] |
| **workplace_id** | **String** | workplace id of the employee. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::EmployeeUpdatesPersonalChange.new(
  id: 1,
  status: done,
  employee_id: 1,
  work_email: ana@factorial.com,
  phone_number: 123456789,
  identifier_type: passport,
  identifier: QKG587532Y,
  social_security_number: 238038194000,
  tax_id: null,
  first_name: Ana,
  last_name: Blanco Perez,
  gender: female,
  date_of_birth: 1990-06-06,
  nationality: ES,
  address_line_1: Calle Rosalía de Castro 10, 1º 1ª,
  address_line_2: Calle Rosalía de Castro 10, 1º 1ª,
  postal_code: 27004,
  city: Santander,
  state: Cataluña,
  country: ES,
  bank_number: ES6220809324751871912999,
  job_title: Software Engineer,
  workplace_id: 1
)
```

