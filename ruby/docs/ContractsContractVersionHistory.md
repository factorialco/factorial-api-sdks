# F::ContractsContractVersionHistory

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier for the contract version history. |  |
| **employee_id** | **String** | employee identifier, refers to /employees/employees endpoint. |  |
| **effective_on** | **String** | the day the specific contract starts, in case of hiring the same than starts_on. |  |
| **country** | **String** | nationality country code of the employee. | [optional] |
| **job_title** | **String** | job title of the employee. | [optional] |
| **job_catalog_level_id** | **String** | job catalog level identifier, refers to /job_catalog/levels endpoint. | [optional] |
| **job_catalog_tree_node_uuid** | **String** | the uuid node in the job catalog tree. For now it only supports level nodes. From this point in the job catalog tree you can get the full ancestor path to the root node including the role. Refer to job_catalog/tree_nodes endpoint. | [optional] |
| **starts_on** | **String** | the day the employee is hired. | [optional] |
| **ends_on** | **String** | the day the employee is terminated. | [optional] |
| **has_payroll** | **Boolean** | boolean that indicates if the employee asociated to this contract belongs to a payroll policy. |  |
| **salary_amount** | **Integer** | the amount of money the employee earns in cents. | [optional] |
| **salary_frequency** | **String** | the frequency of the salary payment. | [optional] |
| **working_week_days** | **String** | the days of the week the employee works. | [optional] |
| **working_hours** | **Integer** | the amount of hours the employee works. | [optional] |
| **working_hours_frequency** | **String** | the frequency of the working hours. | [optional] |
| **max_legal_yearly_hours** | **Integer** | the maximum amount of hours the employee can work in a year. | [optional] |
| **maximum_weekly_hours** | **Integer** | the maximum amount of hours the employee can work in a week. | [optional] |
| **original_contract_version_id** | **String** | identifier for the original contract version. |  |
| **contracts_contract_version_id** | **String** | identifier for the current contract version. | [optional] |
| **changed_at** | [**Unknown**](Unknown.md) | the date the contract version was changed. |  |
| **trial_period_ends_on** | **String** | when the trial period ends. | [optional] |
| **has_trial_period** | **Boolean** | a flag that indicates if the employee has a trial period. | [optional] |
| **author** | **String** | the author of the contract version change. | [optional] |
| **action_type** | **String** | the type of action that was performed on the contract version. | [optional] |
| **adjusted_daily_minutes** | **Integer** | adjusted daily minutes for the employee. | [optional] |
| **created_at** | [**Unknown**](Unknown.md) | the date the contract version was created. |  |
| **updated_at** | [**Unknown**](Unknown.md) | the date of the last contract version updated. |  |
| **es_has_teleworking_contract** | **Boolean** | spanish boolean that indicates if the employee has a teleworking contract. | [optional] |
| **es_cotization_group** | **Integer** | spanish cotization group identifier. | [optional] |
| **es_contract_observations** | **String** | spanish observations of the contract. | [optional] |
| **es_job_description** | **String** | spanish job description of the contract. | [optional] |
| **es_contract_type_id** | **String** | spanish contract type identifier. | [optional] |
| **es_working_day_type_id** | **String** | spanish working day type identifier. | [optional] |
| **es_education_level_id** | **String** | spanish education level identifier. | [optional] |
| **es_professional_category_id** | **String** | spanish professional category identifier. | [optional] |
| **es_contribution_type_id** | **String** | spanish contribution type identifier. | [optional] |
| **es_agreement_code_id** | **String** | spanish agreement code identifier. | [optional] |
| **es_cno_occupation_id** | **String** | spanish cno occupation identifier. | [optional] |
| **es_tariff_group_id** | **String** | spanish tariff group identifier. | [optional] |
| **es_occupation_code_id** | **String** | spanish occupation code identifier. | [optional] |
| **es_classification_id** | **String** | spanish classification identifier. | [optional] |
| **fr_employee_type** | **String** | french employee type. | [optional] |
| **fr_forfait_jours** | **Boolean** | french flag that indicates if the employee is allowed to work within the framework of a fixed number of days. |  |
| **fr_jours_par_an** | **Integer** | french number of days the employee is allowed to work. | [optional] |
| **fr_jours_par_an_cents** | **Integer** | french number of days the employee is allowed to work in cents. | [optional] |
| **fr_coefficient** | **String** | french coefficient for france contracts. | [optional] |
| **fr_contract_type_id** | **String** | french contract type identifier. | [optional] |
| **fr_level_id** | **String** | french level identifier. | [optional] |
| **fr_step_id** | **String** | french step identifier. | [optional] |
| **fr_mutual_id** | **String** | french mutual identifier. | [optional] |
| **fr_professional_category_id** | **String** | french professional category identifier. | [optional] |
| **fr_work_type_id** | **String** | french work type identifier. | [optional] |
| **de_contract_type_id** | **String** | german contract type identifier. | [optional] |
| **de_base_salary_type_id** | **String** | Identifier for the German base salary type. References a payroll concept available via the /payroll/concepts endpoint. | [optional] |
| **pt_contract_type_id** | **String** | portuguese contract type identifier. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsContractVersionHistory.new(
  id: 1,
  employee_id: 1,
  effective_on: 2024-10-06,
  country: es,
  job_title: Designer,
  job_catalog_level_id: 1,
  job_catalog_tree_node_uuid: jobcatalog_treelevel-14,
  starts_on: 2024-10-06,
  ends_on: 2024-10-06,
  has_payroll: false,
  salary_amount: 1000,
  salary_frequency: yearly,
  working_week_days: monday,tuesday,wednesday,thursday,friday,
  working_hours: 40,
  working_hours_frequency: week,
  max_legal_yearly_hours: 2000,
  maximum_weekly_hours: 40,
  original_contract_version_id: 1,
  contracts_contract_version_id: 1,
  changed_at: 2024-10-06T00:00:00.000Z,
  trial_period_ends_on: 2024-10-06,
  has_trial_period: false,
  author: John Doe,
  action_type: promotion,
  adjusted_daily_minutes: 480,
  created_at: 2024-10-06,
  updated_at: 2024-10-06,
  es_has_teleworking_contract: false,
  es_cotization_group: 1,
  es_contract_observations: Observations,
  es_job_description: Job description,
  es_contract_type_id: 1,
  es_working_day_type_id: 1,
  es_education_level_id: 1,
  es_professional_category_id: 1,
  es_contribution_type_id: 1,
  es_agreement_code_id: null,
  es_cno_occupation_id: null,
  es_tariff_group_id: 1,
  es_occupation_code_id: 1,
  es_classification_id: null,
  fr_employee_type: apprenti,
  fr_forfait_jours: false,
  fr_jours_par_an: 200,
  fr_jours_par_an_cents: 20000,
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

