# F::ContractsContractVersionsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_id** | **String** | employee identifier, refers to /employees/employees endpoint. |  |
| **effective_on** | **String** | the day the specific contract starts, in case of hiring the same than starts_on. |  |
| **starts_on** | **String** | the day the employee is hired. |  |
| **ends_on** | **String** | the day the employee is terminated. | [optional] |
| **working_hours_frequency** | **String** | the frequency of the working hours. | [optional] |
| **working_week_days** | **String** | the days of the week the employee works. | [optional] |
| **working_hours** | **Integer** | the amount of hours the employee works. | [optional] |
| **max_legal_yearly_hours** | **Integer** | the maximum amount of hours the employee can work in a year. | [optional] |
| **maximum_weekly_hours** | **Integer** | the maximum amount of hours the employee can work in a week. | [optional] |
| **min_rest_minutes_between_days** | **Integer** | the minimum amount of minutes the employee must rest between working periods. | [optional] |
| **max_work_minutes_per_day** | **Integer** | the maximum amount of minutes the employee can work in a day. | [optional] |
| **max_work_days_in_row** | **Integer** | the maximum amount of days the employee can work in a row. | [optional] |
| **min_rest_hours_in_row** | **Integer** | the minimum amount of hours the employee must rest in a row. | [optional] |
| **salary_frequency** | **String** | the frequency of the salary payment. When adding a salary to a contract that previously had none, both salary_amount and salary_frequency must be provided together. | [optional] |
| **salary_amount** | **Integer** | the amount of money the employee earns in cents. | [optional] |
| **job_title** | **String** | job title of the employee. | [optional] |
| **has_trial_period** | **Boolean** | a flag that indicates if the employee has a trial period. | [optional] |
| **trial_period_ends_on** | **String** | when the trial period ends. | [optional] |
| **working_time_percentage_in_cents** | **Integer** | Working time percentage in cents (e.g., when an employee is working part-time, the percentage of full-time hours they are working). | [optional] |
| **annual_working_time_distribution** | **String** | Allows companies to define how annual working hours are spread across the year to ensure compliance with legal limits. | [optional] |
| **copy_current_contract_version** | **Boolean** | wether to copy the current contract version. | [optional] |
| **bank_holiday_treatment** | **String** | Defines whether a bank holiday should be considered as a workable or non-workable day. | [optional] |
| **job_catalog_tree_node_uuid** | **String** | the uuid node in the job catalog tree. For now it only supports level nodes. From this point in the job catalog tree you can get the full ancestor path to the root node including the role. Refer to job_catalog/tree_nodes endpoint. | [optional] |
| **de_base_salary_type_id** | **String** | Identifier for the German base salary type. References a payroll concept available via the /payroll/concepts endpoint. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ContractsContractVersionsPostRequest.new(
  employee_id: 1,
  effective_on: 2024-10-06,
  starts_on: 2024-10-06,
  ends_on: 2024-10-06,
  working_hours_frequency: week,
  working_week_days: monday,tuesday,wednesday,thursday,friday,
  working_hours: 40,
  max_legal_yearly_hours: 2000,
  maximum_weekly_hours: 40,
  min_rest_minutes_between_days: 2880,
  max_work_minutes_per_day: 480,
  max_work_days_in_row: 6,
  min_rest_hours_in_row: 36,
  salary_frequency: yearly,
  salary_amount: 1000,
  job_title: Designer,
  has_trial_period: false,
  trial_period_ends_on: 2024-10-06,
  working_time_percentage_in_cents: 8000,
  annual_working_time_distribution: limit_workdays,
  copy_current_contract_version: true,
  bank_holiday_treatment: workable,
  job_catalog_tree_node_uuid: jobcatalog_treelevel-14,
  de_base_salary_type_id: 1
)
```

