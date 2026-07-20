# F::EmployeesEmployeesCreateWithContractPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **company_id** | **String** | company id of the employee, you can get it in companies/legal_entities endpoint. |  |
| **first_name** | **String** | name of the employee. |  |
| **last_name** | **String** | last name of the employee. |  |
| **email** | **String** | personal email of the employee. |  |
| **contract_effective_on** | **String** | the day the specific contract starts, in case of hiring the same than contract_starts_on. | [optional] |
| **contract_starts_on** | **String** | the day the employee is hired. | [optional] |
| **ends_on** | **String** | the day the contract ends. | [optional] |
| **gender** | **String** | gender of the employee (male | female). | [optional] |
| **identifier** | **String** | national identifier number. | [optional] |
| **identifier_type** | **String** | type of identifier (ex passport). | [optional] |
| **identifier_expiration_date** | **String** | identifier expiration date. | [optional] |
| **birthday_on** | **String** | birthday of the employee. | [optional] |
| **nationality** | **String** | nationality country code of the employee (Spain ES, United Kingdom GB). | [optional] |
| **address_line1** | **String** | address of the employee. | [optional] |
| **address_line_2** | **String** | address of the employee. | [optional] |
| **postal_code** | **String** | postal code of the employee. | [optional] |
| **city** | **String** | city of the employee. | [optional] |
| **state** | **String** | state/province/region of the employee. | [optional] |
| **country** | **String** | country code of the employee (Spain ES, United Kingdom GB). | [optional] |
| **bank_number** | **String** | bank account number of the employee. | [optional] |
| **swift_bic** | **String** | code to identify banks and financial institutions globally. | [optional] |
| **manager_id** | **String** | id of manager, you can get the manager_id from employees endpoint. | [optional] |
| **timeoff_manager_id** | **String** | id of manager, you can get the manager_id from employees endpoint. | [optional] |
| **legal_entity_id** | **String** | legal entity of the employee, references to companies/legal_entities. | [optional] |
| **company_identifier** | **String** | identity number or string used inside a company to internally identify the employee. | [optional] |
| **seniority_calculation_date** | **String** | date since when the employee is working in the company. | [optional] |
| **job_catalog_tree_node_uuid** | **String** | the uuid of nodes in the job catalog tree. For now it only supports level nodes. From this point in the job catalog tree you can get the full ancestor path to the root node including the role. Refer to job_catalog/tree_nodes endpoint. | [optional] |
| **team_id** | **String** | team id of the employee. | [optional] |
| **location_id** | **String** | location id of the employee, references to locations/locations. | [optional] |
| **social_security_number** | **String** | social security number of the employee. | [optional] |
| **has_trial_period** | **Boolean** | does the employee have a trial period? | [optional] |
| **trial_period_ends_on** | **String** | when the trial period ends. | [optional] |
| **contact_name** | **String** | name of the emergency contact. | [optional] |
| **contact_number** | **String** | phone number of the emergency contact. | [optional] |
| **phone_number** | **String** | phone number of the employee. | [optional] |
| **a3_innuva_code** | **String** | A3Innuva employee code. | [optional] |
| **a3_nom_code** | **String** | A3Nom employee code. | [optional] |
| **contracts_bank_holiday_treatment** | **String** | Defines whether a bank holiday should be considered as a workable or non-workable day. | [optional] |
| **contracts_annual_working_time_distribution** | **String** | the annual working time distribution of the employee. | [optional] |
| **contracts_working_time_percentage_in_cents** | **Integer** | Working time percentage in cents (e.g., when an employee is working part-time, the percentage of full-time hours they are working). | [optional] |
| **contracts_max_legal_yearly_hours** | **Integer** | the maximum amount of hours the employee can work in a year. | [optional] |
| **contracts_maximum_weekly_hours** | **Integer** | the maximum amount of hours the employee can work in a week. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::EmployeesEmployeesCreateWithContractPostRequest.new(
  company_id: 1,
  first_name: Ana,
  last_name: Blanco Perez,
  email: ana@factorial.com,
  contract_effective_on: 2024-10-06,
  contract_starts_on: 2024-10-06,
  ends_on: 2024-10-06,
  gender: female,
  identifier: QKG587532Y,
  identifier_type: passport,
  identifier_expiration_date: 2023-12-31,
  birthday_on: 1990-06-06,
  nationality: ES,
  address_line1: Calle Adaro 10 1 A,
  address_line_2: Calle Adaro 10 1 A,
  postal_code: 27004,
  city: Santander,
  state: Cantabria,
  country: es,
  bank_number: ES6220809324751871912999,
  swift_bic: CAGLES2M510,
  manager_id: 1,
  timeoff_manager_id: 1,
  legal_entity_id: 1,
  company_identifier: bb9d281e,
  seniority_calculation_date: 2024-10-07,
  job_catalog_tree_node_uuid: jobcatalog_treelevel-14,
  team_id: 1,
  location_id: 1,
  social_security_number: 150126298420,
  has_trial_period: true,
  trial_period_ends_on: 2024-10-06,
  contact_name: Laura Delgado,
  contact_number: 647384950,
  phone_number: 657483987,
  a3_innuva_code: 35600,
  a3_nom_code: 45600,
  contracts_bank_holiday_treatment: workable,
  contracts_annual_working_time_distribution: limit_daily_hours,
  contracts_working_time_percentage_in_cents: 8000,
  contracts_max_legal_yearly_hours: 18000,
  contracts_maximum_weekly_hours: 400
)
```

