# F::ContractsContractVersionRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **company_id** | **String** |  | [optional] |
| **employee_id** | **String** |  |  |
| **effective_on** | **String** |  |  |
| **country** | **String** |  | [optional] |
| **job_title** | **String** |  | [optional] |
| **job_catalog_level_id** | **String** |  | [optional] |
| **job_catalog_level_name** | **String** |  | [optional] |
| **job_catalog_level** | **String** |  | [optional] |
| **job_catalog_role** | **String** |  | [optional] |
| **job_catalog_role_id** | **String** |  | [optional] |
| **job_catalog_tree_node_uuid** | **String** |  | [optional] |
| **starts_on** | **String** |  | [optional] |
| **ends_on** | **String** |  | [optional] |
| **has_payroll** | **Boolean** |  |  |
| **has_payroll_policies** | **Boolean** |  | [optional] |
| **has_trial_period** | **Boolean** |  | [optional] |
| **trial_period_ends_on** | **String** |  | [optional] |
| **salary_amount** | **Integer** |  | [optional] |
| **salary_frequency** | **String** |  | [optional] |
| **working_week_days** | **String** |  | [optional] |
| **working_hours** | **Integer** |  | [optional] |
| **working_hours_frequency** | **String** |  | [optional] |
| **max_legal_yearly_hours** | **Integer** |  | [optional] |
| **maximum_weekly_hours** | **Integer** |  | [optional] |
| **adjusted_daily_minutes** | **Integer** |  | [optional] |
| **created_at** | **String** |  |  |
| **updated_at** | **String** |  |  |
| **created_by_name** | **String** |  | [optional] |
| **created_by_avatar** | **String** |  | [optional] |
| **action_type** | **String** |  | [optional] |
| **request_details** | **String** |  | [optional] |
| **approvers_ids** | **Array&lt;String&gt;** |  | [optional] |
| **status** | **String** |  |  |
| **approval_author_id** | **String** |  | [optional] |
| **approval_request_created_at** | **String** |  | [optional] |
| **approval_action_type** | **String** |  | [optional] |
| **es_has_teleworking_contract** | **Boolean** |  | [optional] |
| **es_cotization_group** | **Integer** |  | [optional] |
| **es_contract_observations** | **String** |  | [optional] |
| **es_job_description** | **String** |  | [optional] |
| **es_contract_type_id** | **String** |  | [optional] |
| **es_contract_type_name** | **String** |  | [optional] |
| **es_working_day_type_id** | **String** |  | [optional] |
| **es_working_day_type_name** | **String** |  | [optional] |
| **es_education_level_id** | **String** |  | [optional] |
| **es_education_level_name** | **String** |  | [optional] |
| **es_professional_category_id** | **String** |  | [optional] |
| **es_professional_category_name** | **String** |  | [optional] |
| **es_contribution_type_id** | **String** |  | [optional] |
| **es_contribution_type_name** | **String** |  | [optional] |
| **es_agreement_code_id** | **String** |  | [optional] |
| **es_agreement_code_name** | **String** |  | [optional] |
| **es_cno_occupation_id** | **String** |  | [optional] |
| **es_cno_occupation_name** | **String** |  | [optional] |
| **es_regime_id** | **String** |  | [optional] |
| **es_regime_name** | **String** |  | [optional] |
| **es_tariff_group_id** | **String** |  | [optional] |
| **es_tariff_group_name** | **String** |  | [optional] |
| **es_occupation_code_id** | **String** |  | [optional] |
| **es_occupation_code_name** | **String** |  | [optional] |
| **es_classification_id** | **String** |  | [optional] |
| **es_classification_name** | **String** |  | [optional] |
| **es_a3innuva_job_position_id** | **String** |  | [optional] |
| **es_a3innuva_job_position_name** | **String** |  | [optional] |
| **fr_employee_type** | **String** |  | [optional] |
| **fr_forfait_jours** | **Boolean** |  |  |
| **fr_jours_par_an** | **Integer** |  | [optional] |
| **fr_jours_par_an_cents** | **Integer** |  | [optional] |
| **fr_coefficient** | **String** |  | [optional] |
| **fr_contract_type_id** | **String** |  | [optional] |
| **fr_level_id** | **String** |  | [optional] |
| **fr_step_id** | **String** |  | [optional] |
| **fr_mutual_id** | **String** |  | [optional] |
| **fr_professional_category_id** | **String** |  | [optional] |
| **fr_work_type_id** | **String** |  | [optional] |
| **fr_contract_type_name** | **String** |  | [optional] |
| **fr_mutual_name** | **String** |  | [optional] |
| **fr_professional_category_name** | **String** |  | [optional] |
| **fr_work_type_name** | **String** |  | [optional] |
| **fr_level_name** | **String** |  | [optional] |
| **fr_step_name** | **String** |  | [optional] |
| **de_contract_type_id** | **String** |  | [optional] |
| **de_contract_type_name** | **String** |  | [optional] |
| **de_employment_type** | **Integer** |  | [optional] |
| **de_flat_rate_tax** | **Integer** |  | [optional] |
| **de_activity_type** | **Integer** |  | [optional] |
| **de_personal_key_group_id** | **String** |  | [optional] |
| **de_personal_key_group_name** | **String** |  | [optional] |
| **de_base_salary_type_id** | **String** |  | [optional] |
| **de_base_salary_type_name** | **String** |  | [optional] |
| **pt_contract_type_id** | **String** |  | [optional] |
| **pt_contract_type_name** | **String** |  | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsContractVersionRequest.new(
  id: null,
  company_id: null,
  employee_id: null,
  effective_on: null,
  country: null,
  job_title: null,
  job_catalog_level_id: null,
  job_catalog_level_name: null,
  job_catalog_level: null,
  job_catalog_role: null,
  job_catalog_role_id: null,
  job_catalog_tree_node_uuid: null,
  starts_on: null,
  ends_on: null,
  has_payroll: null,
  has_payroll_policies: null,
  has_trial_period: null,
  trial_period_ends_on: null,
  salary_amount: null,
  salary_frequency: null,
  working_week_days: null,
  working_hours: null,
  working_hours_frequency: null,
  max_legal_yearly_hours: null,
  maximum_weekly_hours: null,
  adjusted_daily_minutes: null,
  created_at: null,
  updated_at: null,
  created_by_name: null,
  created_by_avatar: null,
  action_type: null,
  request_details: null,
  approvers_ids: null,
  status: null,
  approval_author_id: null,
  approval_request_created_at: null,
  approval_action_type: null,
  es_has_teleworking_contract: null,
  es_cotization_group: null,
  es_contract_observations: null,
  es_job_description: null,
  es_contract_type_id: null,
  es_contract_type_name: null,
  es_working_day_type_id: null,
  es_working_day_type_name: null,
  es_education_level_id: null,
  es_education_level_name: null,
  es_professional_category_id: null,
  es_professional_category_name: null,
  es_contribution_type_id: null,
  es_contribution_type_name: null,
  es_agreement_code_id: null,
  es_agreement_code_name: null,
  es_cno_occupation_id: null,
  es_cno_occupation_name: null,
  es_regime_id: null,
  es_regime_name: null,
  es_tariff_group_id: null,
  es_tariff_group_name: null,
  es_occupation_code_id: null,
  es_occupation_code_name: null,
  es_classification_id: null,
  es_classification_name: null,
  es_a3innuva_job_position_id: null,
  es_a3innuva_job_position_name: null,
  fr_employee_type: null,
  fr_forfait_jours: null,
  fr_jours_par_an: null,
  fr_jours_par_an_cents: null,
  fr_coefficient: null,
  fr_contract_type_id: null,
  fr_level_id: null,
  fr_step_id: null,
  fr_mutual_id: null,
  fr_professional_category_id: null,
  fr_work_type_id: null,
  fr_contract_type_name: null,
  fr_mutual_name: null,
  fr_professional_category_name: null,
  fr_work_type_name: null,
  fr_level_name: null,
  fr_step_name: null,
  de_contract_type_id: null,
  de_contract_type_name: null,
  de_employment_type: null,
  de_flat_rate_tax: null,
  de_activity_type: null,
  de_personal_key_group_id: null,
  de_personal_key_group_name: null,
  de_base_salary_type_id: null,
  de_base_salary_type_name: null,
  pt_contract_type_id: null,
  pt_contract_type_name: null
)
```

