# F::EmployeeUpdatesNewHire

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the new hire incidence |  |
| **status** | **String** | The status of the new hire incidence |  |
| **employee_id** | **String** | The employee id of the new hire |  |
| **first_name** | **String** | name of the employee. |  |
| **last_name** | **String** | last name of the employee. |  |
| **birth_name** | **String** | The birth name of the new hire | [optional] |
| **identifier** | **String** | national identifier number. | [optional] |
| **identifier_type** | **String** | type of identifier (ex passport). | [optional] |
| **payroll_identifier** | **String** | payroll identifier. | [optional] |
| **work_email** | **String** | personal email of the employee. | [optional] |
| **phone_number** | **String** | phone number of the employee. | [optional] |
| **gender** | **String** | gender of the employee (male | female). | [optional] |
| **job_title** | **String** | job title of the employee. | [optional] |
| **address** | **String** | address of the employee. |  |
| **city** | **String** | city of the employee. | [optional] |
| **country** | **String** | country code of the employee (Spain ES, United Kingdom GB). | [optional] |
| **state** | **String** | state/province/region of the employee. | [optional] |
| **postal_code** | **String** | postal code of the employee. | [optional] |
| **date_of_birth** | **String** | birthday of the employee. | [optional] |
| **nationality** | **String** | nationality country code of the employee (Spain ES, United Kingdom GB). | [optional] |
| **start_date** | **String** |  | [optional] |
| **contract_effective_date** | **String** |  | [optional] |
| **contract_end_date** | **String** |  | [optional] |
| **bank_account** | **String** | bank account number of the employee. | [optional] |
| **salary_amount_in_cents** | **Integer** | salary amount in cents. | [optional] |
| **salary_frequency** | **String** |  | [optional] |
| **working_hours** | **Integer** |  | [optional] |
| **working_hours_frequency** | **String** |  | [optional] |
| **social_security_number** | **String** | social security number of the employee. | [optional] |
| **manager_id** | **String** | manager id of the employee, you can get the manager id from employees endpoint. | [optional] |
| **tax_id** | **String** |  | [optional] |
| **legal_entity_id** | **String** | The legal entity id of the new hire | [optional] |
| **workplace_id** | **String** | workplace id of the employee. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::EmployeeUpdatesNewHire.new(
  id: 1,
  status: done,
  employee_id: 1,
  first_name: Ana,
  last_name: Blanco Perez,
  birth_name: John Doe,
  identifier: QKG587532Y,
  identifier_type: passport,
  payroll_identifier: 123456,
  work_email: ana@factorial.com,
  phone_number: 123456789,
  gender: female,
  job_title: Software Engineer,
  address: Calle Rosalía de Castro 10, 1º 1ª,
  city: Santander,
  country: ES,
  state: Cataluña,
  postal_code: 27004,
  date_of_birth: 1990-06-06,
  nationality: ES,
  start_date: null,
  contract_effective_date: null,
  contract_end_date: null,
  bank_account: ES6220809324751871912999,
  salary_amount_in_cents: 200000,
  salary_frequency: null,
  working_hours: null,
  working_hours_frequency: null,
  social_security_number: 238038194000,
  manager_id: 1,
  tax_id: null,
  legal_entity_id: 1,
  workplace_id: 1
)
```

