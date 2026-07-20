# F::EmployeeUpdatesContractChange

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the contract change incidence |  |
| **status** | **String** | The status of the contract change incidence |  |
| **effective_on** | **String** | The effective date of the contract |  |
| **starts_on** | **String** | The start date of the contract | [optional] |
| **ends_on** | **String** | The end date of the contract | [optional] |
| **employee_id** | **String** | The employee id |  |
| **job_title** | **String** | The job title on the contract change | [optional] |
| **job_role** | **String** | The job role on the contract change | [optional] |
| **job_level** | **String** | The job level on the contract change | [optional] |
| **has_payroll** | **Boolean** | The payrollable status of the employee on the contract change |  |
| **salary_amount** | **Integer** | The salary amount on the contract change in cents. | [optional] |
| **salary_frequency** | **String** | The salary payment frequency on the contract change | [optional] |
| **working_week_days** | **String** | The working week days on the contract change | [optional] |
| **working_hours** | **Integer** | The working hours on the contract change | [optional] |
| **working_hours_frequency** | **String** | The working hours frequency on the contract change | [optional] |
| **country** | **String** | The country on the contract change | [optional] |
| **es_has_teleworking_contract** | **Boolean** | The teleworking status on the contract change | [optional] |
| **es_cotization_group** | **Integer** | The cotization group on the contract change | [optional] |
| **es_contract_observations** | **String** | The contract observations on the contract change | [optional] |
| **es_job_description** | **String** | The job description on the contract change | [optional] |
| **es_contract_type_id** | **String** | The contract type id on the contract change | [optional] |
| **es_contract_type_name** | **String** | The contract type name on the contract change | [optional] |
| **es_trial_period_ends_on** | **String** | The trial period end date on the contract change | [optional] |
| **es_working_day_type_id** | **String** | The working day type id on the contract change | [optional] |
| **es_education_level_id** | **String** | The education level id on the contract change | [optional] |
| **es_professional_category_id** | **String** | The professional category id on the contract change | [optional] |
| **fr_employee_type** | **String** | The employee type on the contract change | [optional] |
| **fr_forfait_jours** | **Boolean** | The forfait jours status on the contract change |  |
| **fr_jours_par_an** | **Integer** | The jours par an on the contract change | [optional] |
| **fr_coefficient** | **String** | The coefficient on the contract change | [optional] |
| **fr_level_id** | **String** | The level id on the contract change | [optional] |
| **fr_level_name** | **String** | The level name on the contract change | [optional] |
| **fr_step_id** | **String** | The step id on the contract change | [optional] |
| **fr_step_name** | **String** | The step name on the contract change | [optional] |
| **fr_mutual_id** | **String** | The mutual id on the contract change | [optional] |
| **fr_mutual_name** | **String** | The mutual name on the contract change | [optional] |
| **fr_professional_category_id** | **String** | The professional category id on the contract change | [optional] |
| **fr_professional_category_name** | **String** | The professional category name on the contract change | [optional] |
| **fr_work_type_id** | **String** | The work type id on the contract change | [optional] |
| **fr_work_type_name** | **String** | The work type name on the contract change | [optional] |
| **compensation_ids** | **Array&lt;String&gt;** |  | [optional] |
| **fr_contract_type_id** | **String** | The contract type id on the contract change | [optional] |
| **fr_contract_type_name** | **String** | The contract type name on the contract change | [optional] |
| **de_contract_type_id** | **String** | The contract type id on the contract change | [optional] |
| **de_contract_type_name** | **String** | The contract type name on the contract change | [optional] |
| **pt_contract_type_id** | **String** | The contract type id on the contract change | [optional] |
| **pt_contract_type_name** | **String** | The contract type name on the contract change | [optional] |
| **created_at** | **String** |  |  |
| **updated_at** | **String** |  |  |

## Example

```ruby
require 'factorial_api'

instance = F::EmployeeUpdatesContractChange.new(
  id: 1,
  status: done,
  effective_on: 2024-10-06,
  starts_on: 2024-10-06,
  ends_on: 2024-10-06,
  employee_id: 1,
  job_title: The job title,
  job_role: The job role,
  job_level: The job level,
  has_payroll: true,
  salary_amount: 200000,
  salary_frequency: monthly,
  working_week_days: Monday,
  working_hours: 40,
  working_hours_frequency: weekly,
  country: es,
  es_has_teleworking_contract: true,
  es_cotization_group: 1,
  es_contract_observations: The contract observations,
  es_job_description: The job description,
  es_contract_type_id: 1,
  es_contract_type_name: The contract type name,
  es_trial_period_ends_on: 2024-10-06,
  es_working_day_type_id: 1,
  es_education_level_id: 1,
  es_professional_category_id: 1,
  fr_employee_type: The employee type,
  fr_forfait_jours: true,
  fr_jours_par_an: 1,
  fr_coefficient: The coefficient,
  fr_level_id: 1,
  fr_level_name: The level name,
  fr_step_id: 1,
  fr_step_name: The step name,
  fr_mutual_id: 1,
  fr_mutual_name: The mutual name,
  fr_professional_category_id: 1,
  fr_professional_category_name: The professional category name,
  fr_work_type_id: 1,
  fr_work_type_name: The work type name,
  compensation_ids: null,
  fr_contract_type_id: 1,
  fr_contract_type_name: The contract type name,
  de_contract_type_id: 1,
  de_contract_type_name: The contract type name,
  pt_contract_type_id: 1,
  pt_contract_type_name: The contract type name,
  created_at: null,
  updated_at: null
)
```

