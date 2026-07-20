# F::ContractsContractVersion

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier for the contract version. | [optional] |
| **company_id** | **String** | identifier for company. |  |
| **employee_id** | **String** | employee identifier, refers to /employees/employees endpoint. |  |
| **effective_on** | **String** | the day the specific contract starts, in case of hiring the same than starts_on. |  |
| **country** | **String** | nationality country code of the employee (Spain ES, United Kingdom GB). | [optional] |
| **job_title** | **String** | job title of the employee. | [optional] |
| **job_catalog_level_id** | **String** | job catalog level identifier, refers to /job_catalog/levels endpoint. | [optional] |
| **job_catalog_tree_node_uuid** | **String** | the uuid node in the job catalog tree. For now it only supports level nodes. From this point in the job catalog tree you can get the full ancestor path to the root node including the role. Refer to job_catalog/tree_nodes endpoint. | [optional] |
| **starts_on** | **String** | the day the employee is hired. | [optional] |
| **ends_on** | **String** | the day the employee is terminated. It has nothing to do with trial period, these are concepts totally unrelated. | [optional] |
| **has_payroll** | **Boolean** | boolean that indicates if the employee asociated to this contract belongs to a payroll policy. |  |
| **has_trial_period** | **Boolean** | a flag that indicates if the contract version has ever had a trial period. | [optional] |
| **trial_period_ends_on** | **String** | when the trial period ends. If there is no date, it means that the employee has never been in trial. This date is not related with the end date of a contract. | [optional] |
| **salary_amount** | **Integer** | the amount of money the employee earns in cents. | [optional] |
| **salary_frequency** | **String** | the frequency of the salary payment. | [optional] |
| **working_week_days** | **String** | the days of the week the employee works. | [optional] |
| **working_hours** | **Integer** | the amount of hours the employee works. | [optional] |
| **working_hours_frequency** | **String** | the frequency of the working hours. | [optional] |
| **max_legal_yearly_hours** | **Integer** | the maximum amount of hours the employee can work in a year. | [optional] |
| **maximum_weekly_hours** | **Integer** | the maximum amount of hours the employee can work in a week. | [optional] |
| **bank_holiday_treatment** | **String** | Defines whether a bank holiday should be considered as a workable or non-workable day. |  |
| **working_time_percentage_in_cents** | **Integer** | Working time percentage in cents (e.g., when an employee is working part-time, the percentage of full-time hours they are working). | [optional] |
| **annual_working_time_distribution** | **String** | Allows companies to define how annual working hours are spread across the year to ensure compliance with legal limits. | [optional] |
| **version_data** | **Object** | Country-specific contract data (template fragments and fields). | [optional] |
| **min_rest_minutes_between_days** | **Integer** | the minimum amount of minutes the employee must rest between working periods. | [optional] |
| **max_work_minutes_per_day** | **Integer** | the maximum amount of minutes the employee can work in a day. | [optional] |
| **max_work_days_in_row** | **Integer** | the maximum amount of days the employee can work in a row. | [optional] |
| **min_rest_hours_in_row** | **Integer** | the minimum amount of hours the employee must rest in a row. | [optional] |
| **created_at** | **String** | the date the contract version was created. |  |
| **updated_at** | **String** | the date of the last contract version updated. |  |
| **es_has_teleworking_contract** | **Boolean** | flag that indicates if the contract has teleworking. | [optional] |
| **es_cotization_group** | **Integer** | the group of cotization of the employee. | [optional] |
| **contracts_es_tariff_group_id** | **String** | the group of cotization of the employee. | [optional] |
| **es_contract_observations** | **String** | observations of the contract. | [optional] |
| **es_job_description** | **String** | the job description of the employee. | [optional] |
| **es_contract_type_id** | **String** | contract type identifier. | [optional] |
| **es_working_day_type_id** | **String** | working day type identifier. | [optional] |
| **es_education_level_id** | **String** | education level identifier. | [optional] |
| **es_professional_category_id** | **String** | professional category identifier. | [optional] |
| **fr_employee_type** | **String** | employee type. | [optional] |
| **fr_forfait_jours** | **Boolean** | flag that indicates if the employee is allowed to work within the framework of a fixed number of days. |  |
| **fr_jours_par_an** | **Integer** | the number of days the employee is allowed to work. | [optional] |
| **fr_coefficient** | **String** | coefficient for france contracts. | [optional] |
| **fr_contract_type_id** | **String** | contract type identifier. | [optional] |
| **fr_level_id** | **String** | level identifier. | [optional] |
| **fr_step_id** | **String** | step identifier. | [optional] |
| **fr_mutual_id** | **String** | mutual identifier. | [optional] |
| **fr_professional_category_id** | **String** | professional category identifier. | [optional] |
| **fr_work_type_id** | **String** | work type identifier. | [optional] |
| **de_contract_type_id** | **String** | contract type identifier. | [optional] |
| **de_base_salary_type_id** | **String** | Identifier for the German base salary type. References a payroll concept available via the /payroll/concepts endpoint. | [optional] |
| **pt_contract_type_id** | **String** | contract type identifier. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsContractVersion.new(
  id: 1,
  company_id: 1,
  employee_id: 1,
  effective_on: 2024-10-06,
  country: es,
  job_title: Designer,
  job_catalog_level_id: 1,
  job_catalog_tree_node_uuid: jobcatalog_treelevel-14,
  starts_on: 2024-10-06,
  ends_on: 2024-10-06,
  has_payroll: false,
  has_trial_period: false,
  trial_period_ends_on: 2024-10-06,
  salary_amount: 1000,
  salary_frequency: yearly,
  working_week_days: monday,tuesday,wednesday,thursday,friday,
  working_hours: 40,
  working_hours_frequency: week,
  max_legal_yearly_hours: 2000,
  maximum_weekly_hours: 40,
  bank_holiday_treatment: workable,
  working_time_percentage_in_cents: 8000,
  annual_working_time_distribution: limit_workdays,
  version_data: {country_data&#x3D;{country&#x3D;es, fields&#x3D;[{name&#x3D;contract_type, field_name&#x3D;Tipo de contrato, value_label&#x3D;Indefinido, value_id&#x3D;1}, {name&#x3D;working_hours, field_name&#x3D;working_hours, value_label&#x3D;40, value_id&#x3D;40}]}},
  min_rest_minutes_between_days: 2880,
  max_work_minutes_per_day: 480,
  max_work_days_in_row: 6,
  min_rest_hours_in_row: 36,
  created_at: 2024-10-06T00:00:00.000Z,
  updated_at: 2024-10-06T00:00:00.000Z,
  es_has_teleworking_contract: false,
  es_cotization_group: 1,
  contracts_es_tariff_group_id: 1,
  es_contract_observations: review contract for job promotion,
  es_job_description: Designer,
  es_contract_type_id: 1,
  es_working_day_type_id: 1,
  es_education_level_id: 1,
  es_professional_category_id: 1,
  fr_employee_type: apprenti,
  fr_forfait_jours: false,
  fr_jours_par_an: 200,
  fr_coefficient: 1,
  fr_contract_type_id: 1,
  fr_level_id: 1,
  fr_step_id: 1,
  fr_mutual_id: 1,
  fr_professional_category_id: 1,
  fr_work_type_id: 1,
  de_contract_type_id: 1,
  de_base_salary_type_id: 1,
  pt_contract_type_id: 1
)
```

