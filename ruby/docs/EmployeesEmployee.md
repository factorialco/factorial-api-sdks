# F::EmployeesEmployee

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | id of the employee. |  |
| **access_id** | **String** | access_id associated to the employee. |  |
| **first_name** | **String** | name of the employee. |  |
| **last_name** | **String** | last name of the employee. |  |
| **full_name** | **String** | full name of the employee. |  |
| **preferred_name** | **String** | nickname of the employee or a name that defines the employee better. | [optional] |
| **birth_name** | **String** | Birthname of the employee. | [optional] |
| **gender** | **String** | gender of the employee (male | female). | [optional] |
| **identifier** | **String** | national identifier number. | [optional] |
| **identifier_type** | **String** | type of identifier (ex passport). | [optional] |
| **email** | **String** | personal email of the employee. | [optional] |
| **login_email** | **String** | email associated to the session. | [optional] |
| **birthday_on** | **String** | birthday of the employee. | [optional] |
| **nationality** | **String** | nationality country code of the employee (Spain ES, United Kingdom GB). | [optional] |
| **address_line_1** | **String** | address of the employee. | [optional] |
| **address_line_2** | **String** | secondary address of the employee. | [optional] |
| **postal_code** | **String** | postal code of the employee. | [optional] |
| **city** | **String** | city of the employee. | [optional] |
| **state** | **String** | state/province/region of the employee. | [optional] |
| **country** | **String** | country code of the employee (Spain ES, United Kingdom GB). | [optional] |
| **bank_number** | **String** | bank account number of the employee. | [optional] |
| **swift_bic** | **String** | code to identify banks and financial institutions globally. | [optional] |
| **bank_number_format** | **String** | bank number format. | [optional] |
| **company_id** | **String** | id of the company to which the employee belongs (not editable). |  |
| **legal_entity_id** | **String** | legal entity of the employee, references to companies/legal_entities. | [optional] |
| **location_id** | **String** | location id of the employee, references to locations/locations. |  |
| **default_work_area_id** | **String** | Default work area ID for the employee at the default workplace. References locations/work_areas. | [optional] |
| **created_at** | **String** | creation date of the employee. |  |
| **updated_at** | **String** | date of last modification of the employee |  |
| **social_security_number** | **String** | social security number of the employee. | [optional] |
| **is_terminating** | **Boolean** | is the employee being terminated? |  |
| **terminated_on** | **String** | termination date of the employee. | [optional] |
| **termination_reason_type** | **String** | termination reason type of the employee | [optional] |
| **termination_reason** | **String** | A reason for the termination. | [optional] |
| **termination_observations** | **String** | observations about the termination. | [optional] |
| **manager_id** | **String** | manager id of the employee, you can get the manager id from employees endpoint. | [optional] |
| **timeoff_manager_id** | **String** | Timeoff manager id of the employee. | [optional] |
| **phone_number** | **String** | phone number of the employee. | [optional] |
| **company_identifier** | **String** | identity number or string used inside a company to internally identify the employee. | [optional] |
| **age_number** | **Integer** | age of the employee. | [optional] |
| **termination_type_description** | **String** | The description of the termination type. | [optional] |
| **contact_name** | **String** | name of the employee contact. | [optional] |
| **contact_number** | **String** | phone number of the employee contact . | [optional] |
| **personal_email** | **String** | personal email of the employee. | [optional] |
| **seniority_calculation_date** | **String** | date since when the employee is working in the company. | [optional] |
| **communications_email** | **String** | Confirmed email address for company communications and notifications. Separate from login email, used for internal company announcements. | [optional] |
| **unconfirmed_communications_email** | **String** | unconfirmed communications email address for the employee. | [optional] |
| **pronouns** | **String** | pronouns that an employee uses to define themselves. | [optional] |
| **active** | **Boolean** | status of the employee, true when active, false when terminated. | [optional] |
| **disability_percentage_cents** | **Integer** | officially certified level of disability granted by public administration for individuals with physical or mental impairments, expressed in cents | [optional] |
| **identifier_expiration_date** | **String** | identifier expiration date | [optional] |
| **attendable** | **Boolean** | employee included in a time tracking policy. |  |
| **country_of_birth** | **String** | Country of birth of the employee. | [optional] |
| **birthplace** | **String** | Birthplace of the employee. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::EmployeesEmployee.new(
  id: 2,
  access_id: 1,
  first_name: Ana,
  last_name: Blanco Perez,
  full_name: Ana Blanco Perez,
  preferred_name: Anita,
  birth_name: Anna,
  gender: female,
  identifier: QKG587532Y,
  identifier_type: passport,
  email: ana@factorial.com,
  login_email: ana@factorial.com,
  birthday_on: 1990-06-06,
  nationality: es,
  address_line_1: Calle Adaro 10 1 A,
  address_line_2: Calle Adaro 10 1 A,
  postal_code: 27004,
  city: Santander,
  state: Cantabria,
  country: es,
  bank_number: ES6220809324751871912999,
  swift_bic: CAGLES2M510,
  bank_number_format: iban,
  company_id: 1,
  legal_entity_id: 1,
  location_id: 1,
  default_work_area_id: 1,
  created_at: 2010-10-06T00:00:00.000Z,
  updated_at: 2024-10-06T00:00:00.000Z,
  social_security_number: 150126298420,
  is_terminating: false,
  terminated_on: 2024-10-06,
  termination_reason_type: others,
  termination_reason: The employee has left the company,
  termination_observations: Ana has been working on this project before she left,
  manager_id: 1,
  timeoff_manager_id: 1,
  phone_number: 657483987,
  company_identifier: bb9d281e,
  age_number: 30,
  termination_type_description: Baja voluntaria/Dimisión,
  contact_name: Laura Delgado,
  contact_number: 647384950,
  personal_email: ana@factorial.com,
  seniority_calculation_date: 2024-10-07,
  communications_email: employee@company.com,
  unconfirmed_communications_email: new-email@example.com,
  pronouns: She/Her,
  active: true,
  disability_percentage_cents: 1200,
  identifier_expiration_date: 2023-12-31,
  attendable: true,
  country_of_birth: Spain,
  birthplace: Barcelona
)
```

