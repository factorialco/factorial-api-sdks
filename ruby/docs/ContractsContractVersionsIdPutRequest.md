# F::ContractsContractVersionsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | contract version identifier. |  |
| **employee_id** | **String** | employee identifier, refers to /employees/employees endpoint. | [optional] |
| **effective_on** | **String** | the day the specific contract starts, in case of hiring the same than starts_on. | [optional] |
| **starts_on** | **String** | the day the employee is hired. | [optional] |
| **ends_on** | **String** | the day the employee is terminated. | [optional] |
| **working_hours_frequency** | **String** | the frequency of the working hours. | [optional] |
| **working_week_days** | **String** | the days of the week the employee works. | [optional] |
| **working_hours** | **Integer** | the amount of hours the employee works. | [optional] |
| **salary_frequency** | **String** | the frequency of the salary payment. When adding a salary to a contract that previously had none, both salary_amount and salary_frequency must be provided together. | [optional] |
| **salary_amount** | **Integer** | the amount of money the employee earns. When adding a salary to a contract that previously had none, both salary_amount and salary_frequency must be provided together. | [optional] |
| **job_title** | **String** | job title of the employee. | [optional] |
| **job_catalog_tree_node_uuid** | **String** | the uuid node in the job catalog tree. For now it only supports level nodes. From this point in the job catalog tree you can get the full ancestor path to the root node including the role. Refer to job_catalog/tree_nodes endpoint. | [optional] |
| **es_cotization_group** | **Integer** | cotization group identifier. | [optional] |
| **es_professional_category_id** | **String** | professional category identifier. | [optional] |
| **es_education_level_id** | **String** | education level identifier. | [optional] |
| **es_contract_type_id** | **String** | contract type identifier. | [optional] |
| **es_working_day_type_id** | **String** | working day type identifier. | [optional] |
| **has_trial_period** | **Boolean** | a flag that indicates if the employee has a trial period. | [optional] |
| **trial_period_ends_on** | **String** | when the trial period ends. | [optional] |
| **bank_holiday_treatment** | **String** | Defines whether a bank holiday should be considered as a workable or non-workable day. | [optional] |
| **working_time_percentage_in_cents** | **Integer** | Working time percentage in cents (e.g., when an employee is working part-time, the percentage of full-time hours they are working). | [optional] |
| **annual_working_time_distribution** | **String** | Allows companies to define how annual working hours are spread across the year to ensure compliance with legal limits. | [optional] |
| **de_base_salary_type_id** | **String** | Identifier for the German base salary type. References a payroll concept available via the /payroll/concepts endpoint. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsContractVersionsIdPutRequest.new(
  id: 1,
  employee_id: 1,
  effective_on: 2024-10-06,
  starts_on: 2024-10-06,
  ends_on: 2024-10-06,
  working_hours_frequency: week,
  working_week_days: monday,tuesday,wednesday,thursday,friday,
  working_hours: 40,
  salary_frequency: yearly,
  salary_amount: 1000,
  job_title: Designer,
  job_catalog_tree_node_uuid: jobcatalog_treelevel-14,
  es_cotization_group: 1,
  es_professional_category_id: 1,
  es_education_level_id: 1,
  es_contract_type_id: 1,
  es_working_day_type_id: 1,
  has_trial_period: false,
  trial_period_ends_on: 2024-10-06,
  bank_holiday_treatment: workable,
  working_time_percentage_in_cents: 8000,
  annual_working_time_distribution: limit_workdays,
  de_base_salary_type_id: 1
)
```

