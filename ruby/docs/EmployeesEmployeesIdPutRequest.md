# F::EmployeesEmployeesIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | id of the employee. |  |
| **access_id** | **String** | access_id of the creator. | [optional] |
| **gender** | **String** | gender of the employee (male | female). | [optional] |
| **first_name** | **String** | name of the employee. | [optional] |
| **last_name** | **String** | last name of the employee. | [optional] |
| **identifier** | **String** | national identifier number. | [optional] |
| **identifier_type** | **String** | type of identifier (ex passport). | [optional] |
| **birthday_on** | **String** | birthday of the employee. | [optional] |
| **nationality** | **String** | nationality country code of the employee (Spain ES, United Kingdom GB). | [optional] |
| **address_line_1** | **String** | address of the employee. | [optional] |
| **address_line_2** | **String** | address of the employee. | [optional] |
| **postal_code** | **String** | postal code of the employee. | [optional] |
| **city** | **String** | city of the employee. | [optional] |
| **state** | **String** | state/province/region of the employee. | [optional] |
| **country** | **String** | country code of the employee (Spain ES, United Kingdom GB). | [optional] |
| **bank_number** | **String** | bank account number of the employee. | [optional] |
| **swift_bic** | **String** | code to identify banks and financial institutions globally. | [optional] |
| **manager_id** | **String** | id of manager, you can get the manager_id from employees endpoint. | [optional] |
| **timeoff_manager_id** | **String** | id of manager, you can get the manager_id from employees endpoint. | [optional] |
| **social_security_number** | **String** | social security number of the employee. | [optional] |
| **has_work_permit** | **Boolean** | does the employee have work permit? | [optional] |
| **phone_number** | **String** | phone number of the employee. | [optional] |
| **company_identifier** | **String** | identity number or string used inside a company to internally identify the employee. | [optional] |
| **seniority_calculation_date** | **String** | date since when the employee is working in the company. | [optional] |
| **legal_entity_id** | **String** | legal entity of the employee, references to companies/legal_entities. | [optional] |
| **location_id** | **String** | location id of the employee, references to locations/locations. | [optional] |
| **preferred_name** | **String** | nickname of the employee or a name that defines the employee better. | [optional] |
| **pronouns** | **String** | pronouns that an employee uses to define themselves. | [optional] |
| **contact_name** | **String** | name of the employee contact. | [optional] |
| **contact_number** | **String** | phone number of the employee contact . | [optional] |
| **personal_email** | **String** | personal email of the employee. | [optional] |
| **communications_email** | **String** | Email address for company communications and notifications. Separate from login email. | [optional] |
| **disability_percentage_cents** | **Integer** | officially certified level of disability granted by public administration for individuals with physical or mental impairments, expressed in cents | [optional] |
| **identifier_expiration_date** | **String** | identifier expiration date | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::EmployeesEmployeesIdPutRequest.new(
  id: 1,
  access_id: 1,
  gender: female,
  first_name: Ana,
  last_name: Blanco Perez,
  identifier: QKG587532Y,
  identifier_type: passport,
  birthday_on: 1990-06-06,
  nationality: ES,
  address_line_1: Calle Adaro 10 1 A,
  address_line_2: Calle Adaro 10 1 A,
  postal_code: 27004,
  city: Santander,
  state: Cataluña,
  country: ES,
  bank_number: ES6220809324751871912999,
  swift_bic: CAGLES2M510,
  manager_id: 1,
  timeoff_manager_id: 1,
  social_security_number: 150126298420,
  has_work_permit: true,
  phone_number: 657483987,
  company_identifier: bb9d281e,
  seniority_calculation_date: 2024-10-07,
  legal_entity_id: 1,
  location_id: 1,
  preferred_name: Anita,
  pronouns: She/Her,
  contact_name: Laura Delgado,
  contact_number: 657482908,
  personal_email: ana@factorial.com,
  communications_email: employee@company.com,
  disability_percentage_cents: 1200,
  identifier_expiration_date: 2023-12-31
)
```

