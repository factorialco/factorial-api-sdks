# Factorial webhook events

Auto-generated from the OpenAPI spec. 128 events across 22 namespaces, 33 distinct payload schemas.

Factorial POSTs the payload (the resource object) to your `target_url` at the **top level** — it is not wrapped in a `{ type, data }` envelope. Subscribe with the `subscription_type` value shown below. See `../SKILL.md` for delivery, verification, and retry details.

Each SDK ships a typed catalog with one alias per event: at the package root in TypeScript/Python, and under `F::Api::` in Ruby (e.g. `F::Api::AtsApplicationCreateWebhook`).

## Events by namespace

### ApiPublic

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `api_public/webhook_subscription/create` | Creates | [`api_public_webhook_subscription`](#api_public_webhook_subscription) | ApiPublic > WebhookSubscription > Creates |
| `api_public/webhook_subscription/delete` | Deletes | [`api_public_webhook_subscription`](#api_public_webhook_subscription) | ApiPublic > WebhookSubscription > Deletes |
| `api_public/webhook_subscription/update` | Updates | [`api_public_webhook_subscription`](#api_public_webhook_subscription) | ApiPublic > WebhookSubscription > Updates |

### Ats

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `ats/application/apply` | Applies | [`ats_application`](#ats_application) | Ats > Application > Applies |
| `ats/application/create` | Creates | [`ats_application`](#ats_application) | Ats > Application > Creates |
| `ats/application/create_from_employee` | Create from employees | [`ats_application`](#ats_application) | Ats > Application > Create from employees |
| `ats/application/delete` | Deletes | [`ats_application`](#ats_application) | Ats > Application > Deletes |
| `ats/application/update` | Updates | [`ats_application`](#ats_application) | Ats > Application > Updates |
| `ats/candidate/create` | Creates | [`ats_candidate`](#ats_candidate) | Ats > Candidate > Creates |
| `ats/candidate/delete` | Deletes | [`ats_candidate`](#ats_candidate) | Ats > Candidate > Deletes |
| `ats/candidate/update` | Updates | [`ats_candidate`](#ats_candidate) | Ats > Candidate > Updates |
| `ats/evaluation_form/save_as_template` | Save as templates | [`ats_evaluation_form`](#ats_evaluation_form) | Ats > EvaluationForm > Save as templates |
| `ats/job_posting/create` | Creates | [`ats_job_posting`](#ats_job_posting) | Ats > JobPosting > Creates |
| `ats/job_posting/delete` | Deletes | [`ats_job_posting`](#ats_job_posting) | Ats > JobPosting > Deletes |
| `ats/job_posting/duplicate` | Duplicates | [`ats_job_posting`](#ats_job_posting) | Ats > JobPosting > Duplicates |
| `ats/job_posting/update` | Updates | [`ats_job_posting`](#ats_job_posting) | Ats > JobPosting > Updates |

### Attendance

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `attendance/shift/autofill` | Autofills | [`attendance_shift`](#attendance_shift) | Attendance > Shift > Autofills |
| `attendance/shift/break_end` | Break ends | [`attendance_shift`](#attendance_shift) | Attendance > Shift > Break ends |
| `attendance/shift/break_start` | Break starts | [`attendance_shift`](#attendance_shift) | Attendance > Shift > Break starts |
| `attendance/shift/clock_in` | Clock ins | [`attendance_shift`](#attendance_shift) | Attendance > Shift > Clock ins |
| `attendance/shift/clock_out` | Clock outs | [`attendance_shift`](#attendance_shift) | Attendance > Shift > Clock outs |
| `attendance/shift/create` | Creates | [`attendance_shift`](#attendance_shift) | Attendance > Shift > Creates |
| `attendance/shift/delete` | Deletes | [`attendance_shift`](#attendance_shift) | Attendance > Shift > Deletes |
| `attendance/shift/toggle_clock` | Toggle clocks | [`attendance_shift`](#attendance_shift) | Attendance > Shift > Toggle clocks |
| `attendance/shift/update` | Updates | [`attendance_shift`](#attendance_shift) | Attendance > Shift > Updates |

### Banking

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `banking/bank_account_number/upsert` | Upserts | [`banking_bank_account_number`](#banking_bank_account_number) | Banking > BankAccountNumber > Upserts |

### BookkeepersManagement

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `bookkeepers_management/incidence/update` | Updates | [`bookkeepers_management_incidence`](#bookkeepers_management_incidence) | BookkeepersManagement > Incidence > Updates |

### Companies

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `companies/legal_entity/create` | Creates | [`companies_legal_entity`](#companies_legal_entity) | Companies > LegalEntity > Creates |

### Contracts

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `contracts/contract_version/create` | Creates | [`contracts_contract_version`](#contracts_contract_version) | Contracts > ContractVersion > Creates |
| `contracts/contract_version/delete` | Deletes | [`contracts_contract_version`](#contracts_contract_version) | Contracts > ContractVersion > Deletes |
| `contracts/contract_version/update` | Updates | [`contracts_contract_version`](#contracts_contract_version) | Contracts > ContractVersion > Updates |
| `contracts/contract_version_request/approve` | Approves | [`contracts_contract_version_request`](#contracts_contract_version_request) | Contracts > ContractVersionRequest > Approves |
| `contracts/contract_version_request/create_promote_request` | Create promote requests | [`contracts_contract_version_request`](#contracts_contract_version_request) | Contracts > ContractVersionRequest > Create promote requests |
| `contracts/contract_version_request/delete` | Deletes | [`contracts_contract_version_request`](#contracts_contract_version_request) | Contracts > ContractVersionRequest > Deletes |
| `contracts/contract_version_request/reject` | Rejects | [`contracts_contract_version_request`](#contracts_contract_version_request) | Contracts > ContractVersionRequest > Rejects |

### CustomResources

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `custom_resources/schema/create` | Creates | [`custom_resources_schema`](#custom_resources_schema) | CustomResources > Schema > Creates |

### Documents

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `documents/document/bulk_create` | Bulk creates | [`documents_document`](#documents_document) | Documents > Document > Bulk creates |
| `documents/document/create` | Creates | [`documents_document`](#documents_document) | Documents > Document > Creates |
| `documents/document/delete` | Deletes | [`documents_document`](#documents_document) | Documents > Document > Deletes |
| `documents/document/move_to_trash_bin` | Move to trash bins | [`documents_document`](#documents_document) | Documents > Document > Move to trash bins |
| `documents/document/restore_from_trash_bin` | Restore from trash bins | [`documents_document`](#documents_document) | Documents > Document > Restore from trash bins |
| `documents/document/update` | Updates | [`documents_document`](#documents_document) | Documents > Document > Updates |
| `documents/folder/create` | Creates | [`documents_folder`](#documents_folder) | Documents > Folder > Creates |
| `documents/folder/update` | Updates | [`documents_folder`](#documents_folder) | Documents > Folder > Updates |

### Employees

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `employees/employee/create_with_contract` | Create with contracts | [`employees_employee`](#employees_employee) | Employees > Employee > Create with contracts |
| `employees/employee/invite` | Invites | [`employees_employee`](#employees_employee) | Employees > Employee > Invites |
| `employees/employee/set_regular_access_start_date` | Set regular access start dates | [`employees_employee`](#employees_employee) | Employees > Employee > Set regular access start dates |
| `employees/employee/terminate` | Terminates | [`employees_employee`](#employees_employee) | Employees > Employee > Terminates |
| `employees/employee/unterminate` | Unterminates | [`employees_employee`](#employees_employee) | Employees > Employee > Unterminates |
| `employees/employee/update` | Updates | [`employees_employee`](#employees_employee) | Employees > Employee > Updates |

### Expenses

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `expenses/expensable/bulk_set_to_paid` | Bulk set to paids | [`expenses_expensable`](#expenses_expensable) | Expenses > Expensable > Bulk set to paids |
| `expenses/expensable/update_reimbursable_amount` | Update reimbursable amounts | [`expenses_expensable`](#expenses_expensable) | Expenses > Expensable > Update reimbursable amounts |

### Finance

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `finance/cost_center/create` | Creates | [`finance_cost_center`](#finance_cost_center) | Finance > CostCenter > Creates |
| `finance/cost_center/delete` | Deletes | [`finance_cost_center`](#finance_cost_center) | Finance > CostCenter > Deletes |
| `finance/cost_center/edit` | Edits | [`finance_cost_center`](#finance_cost_center) | Finance > CostCenter > Edits |

### Locations

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `locations/location/create` | Creates | [`locations_location`](#locations_location) | Locations > Location > Creates |
| `locations/location/delete` | Deletes | [`locations_location`](#locations_location) | Locations > Location > Deletes |
| `locations/location/update` | Updates | [`locations_location`](#locations_location) | Locations > Location > Updates |

### Payroll

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `payroll/policy_period/change_status` | Change statuses | [`payroll_policy_period`](#payroll_policy_period) | Payroll > PolicyPeriod > Change statuses |
| `payroll/supplement/create` | Creates | [`payroll_supplement`](#payroll_supplement) | Payroll > Supplement > Creates |
| `payroll/supplement/delete` | Deletes | [`payroll_supplement`](#payroll_supplement) | Payroll > Supplement > Deletes |
| `payroll/supplement/update` | Updates | [`payroll_supplement`](#payroll_supplement) | Payroll > Supplement > Updates |

### PayrollIntegrationsBase

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `payroll_integrations_base/code/create` | Creates | [`payroll_integrations_base_code`](#payroll_integrations_base_code) | PayrollIntegrationsBase > Code > Creates |
| `payroll_integrations_base/code/delete` | Deletes | [`payroll_integrations_base_code`](#payroll_integrations_base_code) | PayrollIntegrationsBase > Code > Deletes |
| `payroll_integrations_base/code/update` | Updates | [`payroll_integrations_base_code`](#payroll_integrations_base_code) | PayrollIntegrationsBase > Code > Updates |

### Performance

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `performance/review_process/create` | Creates | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Creates |
| `performance/review_process/create_from_template` | Create from templates | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Create from templates |
| `performance/review_process/delete` | Deletes | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Deletes |
| `performance/review_process/duplicate` | Duplicates | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Duplicates |
| `performance/review_process/remind_in_bulk` | Remind in bulks | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Remind in bulks |
| `performance/review_process/remove_schedule` | Remove schedules | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Remove schedules |
| `performance/review_process/reopen` | Reopens | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Reopens |
| `performance/review_process/schedule` | Schedules | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Schedules |
| `performance/review_process/start` | Starts | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Starts |
| `performance/review_process/stop` | Stops | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Stops |
| `performance/review_process/toggle_archive` | Toggle archives | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Toggle archives |
| `performance/review_process/update_agreements_configuration` | Update agreements configurations | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Update agreements configurations |
| `performance/review_process/update_basic_info` | Update basic infos | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Update basic infos |
| `performance/review_process/update_competencies_assessments_configuration` | Update competencies assessments configurations | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Update competencies assessments configurations |
| `performance/review_process/update_deadline` | Update deadlines | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Update deadlines |
| `performance/review_process/update_employee_score_configuration` | Update employee score configurations | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Update employee score configurations |
| `performance/review_process/update_reviewer_strategies` | Update reviewer strategies | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Update reviewer strategies |
| `performance/review_process/update_schedule` | Update schedules | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Update schedules |
| `performance/review_process/update_target_strategy` | Update target strategies | [`performance_review_process`](#performance_review_process) | Performance > ReviewProcess > Update target strategies |

### ShiftManagement

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `shift_management/shift/bulk_create` | Bulk creates | [`shift_management_shift`](#shift_management_shift) | ShiftManagement > Shift > Bulk creates |
| `shift_management/shift/bulk_delete` | Bulk deletes | [`shift_management_shift`](#shift_management_shift) | ShiftManagement > Shift > Bulk deletes |
| `shift_management/shift/create` | Creates | [`shift_management_shift`](#shift_management_shift) | ShiftManagement > Shift > Creates |
| `shift_management/shift/delete` | Deletes | [`shift_management_shift`](#shift_management_shift) | ShiftManagement > Shift > Deletes |

### Tasks

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `tasks/task/bulk_create` | Bulk creates | [`tasks_task`](#tasks_task) | Tasks > Task > Bulk creates |
| `tasks/task/bulk_delete` | Bulk deletes | [`tasks_task`](#tasks_task) | Tasks > Task > Bulk deletes |
| `tasks/task/bulk_update` | Bulk updates | [`tasks_task`](#tasks_task) | Tasks > Task > Bulk updates |
| `tasks/task/copy` | Copies | [`tasks_task`](#tasks_task) | Tasks > Task > Copies |
| `tasks/task/create` | Creates | [`tasks_task`](#tasks_task) | Tasks > Task > Creates |
| `tasks/task/create_comment` | Create comments | [`tasks_task`](#tasks_task) | Tasks > Task > Create comments |
| `tasks/task/delete` | Deletes | [`tasks_task`](#tasks_task) | Tasks > Task > Deletes |
| `tasks/task/update` | Updates | [`tasks_task`](#tasks_task) | Tasks > Task > Updates |

### Teams

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `teams/membership/bulk_upsert` | Bulk upserts | [`teams_membership`](#teams_membership) | Teams > Membership > Bulk upserts |
| `teams/membership/create` | Creates | [`teams_membership`](#teams_membership) | Teams > Membership > Creates |
| `teams/membership/delete` | Deletes | [`teams_membership`](#teams_membership) | Teams > Membership > Deletes |
| `teams/membership/update` | Updates | [`teams_membership`](#teams_membership) | Teams > Membership > Updates |
| `teams/team/create` | Creates | [`teams_team`](#teams_team) | Teams > Team > Creates |
| `teams/team/delete` | Deletes | [`teams_team`](#teams_team) | Teams > Team > Deletes |
| `teams/team/project` | Projects | [`teams_team`](#teams_team) | Teams > Team > Projects |
| `teams/team/update` | Updates | [`teams_team`](#teams_team) | Teams > Team > Updates |

### Timeoff

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `timeoff/blocked_period/create` | Creates | [`timeoff_blocked_periods_policy`](#timeoff_blocked_periods_policy) | Timeoff > BlockedPeriod > Creates |
| `timeoff/blocked_period/delete` | Deletes | [`timeoff_blocked_periods_policy`](#timeoff_blocked_periods_policy) | Timeoff > BlockedPeriod > Deletes |
| `timeoff/blocked_period/update` | Updates | [`timeoff_blocked_periods_policy`](#timeoff_blocked_periods_policy) | Timeoff > BlockedPeriod > Updates |
| `timeoff/leave/approve` | Approves | [`timeoff_leave`](#timeoff_leave) | Timeoff > Leave > Approves |
| `timeoff/leave/create` | Creates | [`timeoff_leave`](#timeoff_leave) | Timeoff > Leave > Creates |
| `timeoff/leave/delete` | Deletes | [`timeoff_leave`](#timeoff_leave) | Timeoff > Leave > Deletes |
| `timeoff/leave/reject` | Rejects | [`timeoff_leave`](#timeoff_leave) | Timeoff > Leave > Rejects |
| `timeoff/leave/update` | Updates | [`timeoff_leave`](#timeoff_leave) | Timeoff > Leave > Updates |
| `timeoff/leave_type/create` | Creates | [`timeoff_leave_type`](#timeoff_leave_type) | Timeoff > LeaveType > Creates |
| `timeoff/leave_type/update` | Updates | [`timeoff_leave_type`](#timeoff_leave_type) | Timeoff > LeaveType > Updates |
| `timeoff/policy/create` | Creates | [`timeoff_policy`](#timeoff_policy) | Timeoff > Policy > Creates |
| `timeoff/policy/delete` | Deletes | [`timeoff_policy`](#timeoff_policy) | Timeoff > Policy > Deletes |
| `timeoff/policy/update` | Updates | [`timeoff_policy`](#timeoff_policy) | Timeoff > Policy > Updates |

### Trainings

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `trainings/category/create` | Creates | [`trainings_category`](#trainings_category) | Trainings > Category > Creates |
| `trainings/category/delete` | Deletes | [`trainings_category`](#trainings_category) | Trainings > Category > Deletes |
| `trainings/training/bulk_delete` | Bulk deletes | [`trainings_training`](#trainings_training) | Trainings > Training > Bulk deletes |
| `trainings/training/bulk_update_catalog` | Bulk update catalogs | [`trainings_training`](#trainings_training) | Trainings > Training > Bulk update catalogs |
| `trainings/training/create` | Creates | [`trainings_training`](#trainings_training) | Trainings > Training > Creates |
| `trainings/training/delete` | Deletes | [`trainings_training`](#trainings_training) | Trainings > Training > Deletes |
| `trainings/training/update` | Updates | [`trainings_training`](#trainings_training) | Trainings > Training > Updates |
| `trainings/training/update_status` | Update statuses | [`trainings_training`](#trainings_training) | Trainings > Training > Update statuses |

### WorkSchedule

| subscription_type | event | payload schema | summary |
| --- | --- | --- | --- |
| `work_schedule/schedule/create` | Creates | [`work_schedule_schedule`](#work_schedule_schedule) | WorkSchedule > Schedule > Creates |
| `work_schedule/schedule/toggle_archive` | Toggle archives | [`work_schedule_schedule`](#work_schedule_schedule) | WorkSchedule > Schedule > Toggle archives |
| `work_schedule/schedule/update` | Updates | [`work_schedule_schedule`](#work_schedule_schedule) | WorkSchedule > Schedule > Updates |

## Payload schemas

Top-level fields of each payload. Nested object types reference other schemas by name; see the [full OpenAPI reference](https://apidoc.factorialhr.com/reference) for their fields.

### api_public_webhook_subscription

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Identifier of the webhook subscription |
| `target_url` | string | yes | URL where the webhook payload will be sent |
| `type` | string | yes | Type of the webhook subscription |
| `company_id` | string | yes | Company identifier of the webhook subscription |
| `name` | string | no | Name of the webhook subscription |
| `challenge` | string | no | String to verify the subscription |
| `enabled` | boolean | yes | Boolean to enable/disable the subscription |
| `api_version` | string | yes | API version of the webhook subscription that determines the schema of the payload |

### ats_application

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Id of the application |
| `company_id` | string | yes | Company id of the application |
| `ats_job_posting_id` | string | yes | Job posting id of the application |
| `ats_candidate_id` | string | yes | Candidate id of the application |
| `employee_id` | string | no | Employee id of the application |
| `phone` | string | no | Candidate phone of the application |
| `qualified` | boolean | no | Qualified of the application |
| `ats_application_phase_id` | string | no | Application phase id |
| `created_at` | string | yes | Application created at date |
| `cover_letter` | string | no | Application cover letter |
| `cv` | object | no | CV file attachment of the application (includes filename, url, byte_size, content_type, created_at) |
| `ats_conversation_id` | string | no | Application conversation id |
| `medium` | string | no | Application medium |
| `rating_average` | integer | no | Application average rating |
| `ats_rejection_reason_id` | string | no | Application rejection reason id |
| `source_id` | string | no | Application source id |

### ats_candidate

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | identifier of the candidate. |
| `company_id` | string | no | company identifier. |
| `first_name` | string | yes | name of the candidate. |
| `last_name` | string | yes | last name of the candidate. |
| `full_name` | string | yes | full name of the candidate. |
| `email` | string | no | email of the candidate. |
| `talent_pool` | boolean | yes | is the candidate part of talent pool? |
| `phone_number` | string | no | phone number of the candidate. |
| `created_at` | string | yes | creation date of the candidate. |
| `updated_at` | string | yes | last update of the candidate. |
| `consent_given_at` | string | no | date when the consent was given. |
| `inactive_since` | string | no | date when the candidate became inactive. |
| `ats_job_posting_ids` | array<string> | no | list of job posting identifiers. |
| `personal_url` | string | no | personal web resource from the candidate. |
| `consent_expiration_date` | string | no | date when the consent expires. |
| `consent_to_talent_pool` | boolean | no | consent to talent pool. |
| `medium` | string | no | specifies additional details related to the source of the candidate, such as the referrer name for example if the source is referred. |
| `source_id` | string | no | candidate source identifier, refers to ats/candidate_sources endpoint. |
| `gender` | string | no | gender of the candidate. |
| `score` | number | no | score of the candidate. |

### ats_evaluation_form

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Id of the evaluation form. |
| `company_id` | string | yes | Id of the company that the evaluation form belongs to. |
| `ats_job_posting_id` | string | no | Id of the job posting that the evaluation form is associated with. |
| `name` | string | yes | Name of the evaluation form. |
| `based_on_id` | string | no | Id of the evaluation form that this evaluation form is related. |
| `questions` | array<object> | yes | List of questions in the evaluation form. |
| `created_at` | string | yes | date and time when the evaluation form was created. |
| `updated_at` | string | yes | date and time when the evaluation form was last updated. |

### ats_job_posting

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Unique identifier for the job posting |
| `company_id` | string | yes | Identifier of the company associated with the job posting |
| `ats_company_id` | string | yes | Identifier of the ATS company associated with the job posting |
| `title` | string | yes | Title of the job posting |
| `description` | string | no | Description of the job posting |
| `contract_type` | string | no |  |
| `category` | string | no |  |
| `workplace_type` | string | no |  |
| `remote` | boolean | yes | Indicates if the job posting is remote |
| `status` | string | yes | The current status of the job posting (e.g., draft, published, archived) |
| `schedule_type` | string | no | The schedule type of the job posting (e.g., full_time, part_time) |
| `team_id` | string | no | Identifier of the team associated with the job posting |
| `location_id` | string | no | Identifier of the location associated with the job posting |
| `legal_entity_id` | string | no | Identifier of the legal entity associated with the job posting |
| `salary_format` | string | no | The format of the salary (e.g., range, fixed_amount) |
| `salary_from_amount_in_cents` | integer | no | The minimum salary amount in cents |
| `salary_to_amount_in_cents` | integer | no | The maximum salary amount in cents |
| `hide_salary` | boolean | no | Indicates whether the salary information for the job posting should be hidden from applicants. |
| `cv_requirement` | string | yes | Requirement for the CV (e.g, mandatory, optional, do_not_ask) |
| `cover_letter_requirement` | string | yes | Requirement for the cover letter (e.g, mandatory, optional, do_not_ask) |
| `phone_requirement` | string | yes | Requirement for the phone number (e.g, mandatory, optional, do_not_ask) |
| `photo_requirement` | string | yes | Requirement for the phone number (e.g, mandatory, optional, do_not_ask) |
| `personal_url_requirement` | string | yes | Requirement for the personal URL (e.g, mandatory, optional, do_not_ask) |
| `url` | string | no | If published, the public URL of the job posting. Otherwise will be null |
| `salary_period` | string | yes | The period of the salary (e.g., annual, monthly, daily) |
| `published_at` | string | no | Published date in ISO 8601 format of the job. If never been published the value will be null |
| `created_at` | string | yes | Date in ISO 8601 format when the job posting was created |

### attendance_shift

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Unique identifier for the shift |
| `employee_id` | string | yes | Identifier for the employee assigned to the shift |
| `date` | string | yes | Date of the shift |
| `reference_date` | string | yes | Reference date for the shift |
| `clock_in` | string | no | Time when the employee clocked in |
| `clock_out` | string | no | Time when the employee clocked out |
| `in_source` | string | no | Source of the clock-in time |
| `out_source` | string | no | Source of the clock-out time |
| `observations` | string | no | Additional observations about the shift |
| `location_type` | string | no | Type of location for the shift |
| `half_day` | string | no | Indicates which worked part of the day |
| `in_location_latitude` | number | no | Latitude of the clock-in location |
| `in_location_longitude` | number | no | Longitude of the clock-in location |
| `in_location_accuracy` | number | no | Accuracy of the clock-in location |
| `out_location_latitude` | number | no | Latitude of the clock-out location |
| `out_location_longitude` | number | no | Longitude of the clock-out location |
| `out_location_accuracy` | number | no | Accuracy of the clock-out location |
| `workable` | boolean | no | Indicates if the shift is workable |
| `created_at` | string | yes | Timestamp when the shift record was created |
| `workplace_id` | string | no | Identifier for the location |
| `time_settings_break_configuration_id` | string | no | Identifier for the break configuration |
| `company_id` | string | yes | Identifier for the company |
| `updated_at` | string | yes | Timestamp when the shift record was updated |
| `minutes` | integer | yes | Number in minutes of the shift |
| `clock_in_with_seconds` | string | no | Clock in time with seconds |

### banking_bank_account_number

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Employee id. |
| `company_id` | string | yes | Company identifier |
| `account_number` | string | yes | Account number |
| `complementary_data` | string | no | Additional banking information, depending on the selected format. |
| `format` | string | yes | The format of the account number. |

### bookkeepers_management_incidence

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | identifier of the incidence (aka employee update). |
| `employee_id` | string | no | identifier of employee related. |
| `legal_entity_id` | string | yes | identifier of legal entity related. |
| `name` | string | yes | name of the incidence (aka employee update). It also represent the incidence type. For example a new hire incidence will be |
| `custom_name` | string | no |  |
| `target_id` | string | yes | The incidence (aka employee update) is also related to a another resource, for example for a leave target, the target identifier will be the leave id. |
| `target_type` | string | yes | The incidence (aka employee update) is also related to a another resource, for example a leave. This is the target type. The other types are Employee, Contracts::ContractVersion, BookkeepersManagement::ManualIncidence, Finance::CostCenterMembership. |
| `starts_on` | string | no | The date the incidence (aka employee update) starts. |
| `ends_on` | string | no | The date the incidence (aka employee update) end. |
| `read_at` | string | no | The date the incidence (aka employee update) was read. |
| `status` | string | yes |  |
| `company_id` | string | yes | identifier of company related. |
| `message_from` | string | no | Indicate the message sender on the incidence (aka employee update). It can be any of 'bookkeeper', 'admin' |
| `has_message` | boolean | no | Boolean that indicates if the incidence (aka employee update) has unread messages. |
| `created_at` | string | yes | Date in which incidence (aka employee update) was created. |
| `is_reopened` | boolean | yes | Boolean that indicates if the incidence (aka employee update) has been reopened. |
| `legal_entity_name` | string | no |  |
| `employee_first_name` | string | no |  |
| `employee_last_name` | string | no |  |

### companies_legal_entity

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | identifier of the legal entity |
| `company_id` | string | yes | company identifier |
| `country` | string | yes | Country code of the jurisdiction the legal entity is registered in (lowercase two-letter code, e.g. "es"). |
| `legal_name` | string | yes | Legal name of the legal entity |
| `currency` | string | yes | The currency code in ISO 4217 format |
| `tin` | string | no | Tax identification number |
| `city` | string | no | City of the legal entity |
| `state` | string | no | State of the legal entity |
| `postal_code` | string | no | Postal code of the legal entity |
| `address_line_1` | string | no | Address line 1 of the legal entity |
| `address_line_2` | string | no | Address line 2 of the legal entity |

### contracts_contract_version

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | no | identifier for the contract version. |
| `company_id` | string | yes | identifier for company. |
| `employee_id` | string | yes | employee identifier, refers to /employees/employees endpoint. |
| `effective_on` | string | yes | the day the specific contract starts, in case of hiring the same than starts_on. |
| `country` | string | no | nationality country code of the employee (Spain ES, United Kingdom GB). |
| `job_title` | string | no | job title of the employee. |
| `job_catalog_level_id` | string | no | job catalog level identifier, refers to /job_catalog/levels endpoint. |
| `job_catalog_tree_node_uuid` | string | no | the uuid node in the job catalog tree. For now it only supports level nodes. From this point in the job catalog tree you can get the full ancestor path to the root node including the role. Refer to job_catalog/tree_nodes endpoint. |
| `starts_on` | string | no | the day the employee is hired. |
| `ends_on` | string | no | the day the employee is terminated. It has nothing to do with trial period, these are concepts totally unrelated. |
| `has_payroll` | boolean | yes | boolean that indicates if the employee asociated to this contract belongs to a payroll policy. |
| `has_trial_period` | boolean | no | a flag that indicates if the contract version has ever had a trial period. |
| `trial_period_ends_on` | string | no | when the trial period ends. If there is no date, it means that the employee has never been in trial. This date is not related with the end date of a contract. |
| `salary_amount` | integer | no | the amount of money the employee earns in cents. |
| `salary_frequency` | string | no | the frequency of the salary payment. |
| `working_week_days` | string | no | the days of the week the employee works. |
| `working_hours` | integer | no | the amount of hours the employee works. |
| `working_hours_frequency` | string | no | the frequency of the working hours. |
| `max_legal_yearly_hours` | integer | no | the maximum amount of hours the employee can work in a year. |
| `maximum_weekly_hours` | integer | no | the maximum amount of hours the employee can work in a week. |
| `bank_holiday_treatment` | string | yes | Defines whether a bank holiday should be considered as a workable or non-workable day. |
| `working_time_percentage_in_cents` | integer | no | Working time percentage in cents (e.g., when an employee is working part-time, the percentage of full-time hours they are working). |
| `annual_working_time_distribution` | string | no | Allows companies to define how annual working hours are spread across the year to ensure compliance with legal limits. |
| `version_data` | object | no | Country-specific contract data (template fragments and fields). |
| `min_rest_minutes_between_days` | integer | no | the minimum amount of minutes the employee must rest between working periods. |
| `max_work_minutes_per_day` | integer | no | the maximum amount of minutes the employee can work in a day. |
| `max_work_days_in_row` | integer | no | the maximum amount of days the employee can work in a row. |
| `min_rest_hours_in_row` | integer | no | the minimum amount of hours the employee must rest in a row. |
| `created_at` | string | yes | the date the contract version was created. |
| `updated_at` | string | yes | the date of the last contract version updated. |
| `es_has_teleworking_contract` | boolean | no | flag that indicates if the contract has teleworking. |
| `es_cotization_group` | integer | no | the group of cotization of the employee. |
| `contracts_es_tariff_group_id` | string | no | the group of cotization of the employee. |
| `es_contract_observations` | string | no | observations of the contract. |
| `es_job_description` | string | no | the job description of the employee. |
| `es_contract_type_id` | string | no | contract type identifier. |
| `es_working_day_type_id` | string | no | working day type identifier. |
| `es_education_level_id` | string | no | education level identifier. |
| `es_professional_category_id` | string | no | professional category identifier. |
| `fr_employee_type` | string | no | employee type. |
| `fr_forfait_jours` | boolean | yes | flag that indicates if the employee is allowed to work within the framework of a fixed number of days. |
| `fr_jours_par_an` | integer | no | the number of days the employee is allowed to work. |
| `fr_coefficient` | string | no | coefficient for france contracts. |
| `fr_contract_type_id` | string | no | contract type identifier. |
| `fr_level_id` | string | no | level identifier. |
| `fr_step_id` | string | no | step identifier. |
| `fr_mutual_id` | string | no | mutual identifier. |
| `fr_professional_category_id` | string | no | professional category identifier. |
| `fr_work_type_id` | string | no | work type identifier. |
| `de_contract_type_id` | string | no | contract type identifier. |
| `de_base_salary_type_id` | string | no | Identifier for the German base salary type. References a payroll concept available via the /payroll/concepts endpoint. |
| `pt_contract_type_id` | string | no | contract type identifier. |

### contracts_contract_version_request

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | no |  |
| `company_id` | string | no |  |
| `employee_id` | string | yes |  |
| `effective_on` | string | yes |  |
| `country` | string | no |  |
| `job_title` | string | no |  |
| `job_catalog_level_id` | string | no |  |
| `job_catalog_level_name` | string | no |  |
| `job_catalog_level` | string | no |  |
| `job_catalog_role` | string | no |  |
| `job_catalog_role_id` | string | no |  |
| `job_catalog_tree_node_uuid` | string | no |  |
| `starts_on` | string | no |  |
| `ends_on` | string | no |  |
| `has_payroll` | boolean | yes |  |
| `has_payroll_policies` | boolean | no |  |
| `has_trial_period` | boolean | no |  |
| `trial_period_ends_on` | string | no |  |
| `salary_amount` | integer | no |  |
| `salary_frequency` | string | no |  |
| `working_week_days` | string | no |  |
| `working_hours` | integer | no |  |
| `working_hours_frequency` | string | no |  |
| `max_legal_yearly_hours` | integer | no |  |
| `maximum_weekly_hours` | integer | no |  |
| `adjusted_daily_minutes` | integer | no |  |
| `created_at` | string | yes |  |
| `updated_at` | string | yes |  |
| `created_by_name` | string | no |  |
| `created_by_avatar` | string | no |  |
| `action_type` | string | no |  |
| `request_details` | string | no |  |
| `approvers_ids` | array<string> | no |  |
| `status` | string | yes |  |
| `approval_author_id` | string | no |  |
| `approval_request_created_at` | string | no |  |
| `approval_action_type` | string | no |  |
| `es_has_teleworking_contract` | boolean | no |  |
| `es_cotization_group` | integer | no |  |
| `es_contract_observations` | string | no |  |
| `es_job_description` | string | no |  |
| `es_contract_type_id` | string | no |  |
| `es_contract_type_name` | string | no |  |
| `es_working_day_type_id` | string | no |  |
| `es_working_day_type_name` | string | no |  |
| `es_education_level_id` | string | no |  |
| `es_education_level_name` | string | no |  |
| `es_professional_category_id` | string | no |  |
| `es_professional_category_name` | string | no |  |
| `es_contribution_type_id` | string | no |  |
| `es_contribution_type_name` | string | no |  |
| `es_agreement_code_id` | string | no |  |
| `es_agreement_code_name` | string | no |  |
| `es_cno_occupation_id` | string | no |  |
| `es_cno_occupation_name` | string | no |  |
| `es_regime_id` | string | no |  |
| `es_regime_name` | string | no |  |
| `es_tariff_group_id` | string | no |  |
| `es_tariff_group_name` | string | no |  |
| `es_occupation_code_id` | string | no |  |
| `es_occupation_code_name` | string | no |  |
| `es_classification_id` | string | no |  |
| `es_classification_name` | string | no |  |
| `es_a3innuva_job_position_id` | string | no |  |
| `es_a3innuva_job_position_name` | string | no |  |
| `fr_employee_type` | string | no |  |
| `fr_forfait_jours` | boolean | yes |  |
| `fr_jours_par_an` | integer | no |  |
| `fr_jours_par_an_cents` | integer | no |  |
| `fr_coefficient` | string | no |  |
| `fr_contract_type_id` | string | no |  |
| `fr_level_id` | string | no |  |
| `fr_step_id` | string | no |  |
| `fr_mutual_id` | string | no |  |
| `fr_professional_category_id` | string | no |  |
| `fr_work_type_id` | string | no |  |
| `fr_contract_type_name` | string | no |  |
| `fr_mutual_name` | string | no |  |
| `fr_professional_category_name` | string | no |  |
| `fr_work_type_name` | string | no |  |
| `fr_level_name` | string | no |  |
| `fr_step_name` | string | no |  |
| `de_contract_type_id` | string | no |  |
| `de_contract_type_name` | string | no |  |
| `de_employment_type` | integer | no |  |
| `de_flat_rate_tax` | integer | no |  |
| `de_activity_type` | integer | no |  |
| `de_personal_key_group_id` | string | no |  |
| `de_personal_key_group_name` | string | no |  |
| `de_base_salary_type_id` | string | no |  |
| `de_base_salary_type_name` | string | no |  |
| `pt_contract_type_id` | string | no |  |
| `pt_contract_type_name` | string | no |  |

### custom_resources_schema

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Schema identifier |
| `name` | string | yes | Schema name |
| `company_id` | string | yes | Company identifier where this schema belongs |
| `hidden` | boolean | yes | Manages visibility of the schema |
| `position` | integer | no | Schema position within employee profile |

### documents_document

| field | type | required | description |
| --- | --- | --- | --- |
| `author_id` | string | no | access identifier of the author, refers to /employees/employees endpoint. |
| `company_id` | string | no | company identifier, refers to /api/me endpoint. |
| `content_type` | string | no | document content type. |
| `created_at` | string | yes | creation date of the document. |
| `employee_id` | string | no | employee identifier associated to the document. |
| `extension` | string | no | document extension. |
| `file_size` | integer | no | document file size in bytes. |
| `filename` | string | yes | name of the document. |
| `folder_id` | string | no | folder identifier, references to documents/folders endpoint. |
| `id` | string | yes | document identifier. |
| `is_company_document` | boolean | no | flag that indicates if the document is a company document. |
| `is_management_document` | boolean | no | flag that indicates if the document is a management document. |
| `is_pending_assignment` | boolean | no | flag that indicates if the document is pending assignment. |
| `leave_id` | string | no | leave identifier associated to the document, refers to /timeoff/leaves endpoint. |
| `public` | boolean | yes | flag to indicate if the document is public. |
| `signature_status` | string | no | document signature status. |
| `signees` | array<string> | no | list of signee access identifiers associated to the document, refers to /employees/employees endpoint. |
| `space` | string | yes | document space. |
| `updated_at` | string | yes | last update date of the document. |
| `deleted_at` | string | no | deletion date of the document. |

### documents_folder

| field | type | required | description |
| --- | --- | --- | --- |
| `active` | boolean | yes | Whether the folder is active or not |
| `company_id` | string | no | Company ID of the folder |
| `id` | string | yes | Folder ID |
| `name` | string | yes | Folder name |
| `parent_folder_id` | string | no | Id of the parent folder |
| `space` | string | yes | The space of the folder is related to the place where the folder is displayed. |

### employees_employee

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | id of the employee. |
| `access_id` | string | yes | access_id associated to the employee. |
| `first_name` | string | yes | name of the employee. |
| `last_name` | string | yes | last name of the employee. |
| `full_name` | string | yes | full name of the employee. |
| `preferred_name` | string | no | nickname of the employee or a name that defines the employee better. |
| `birth_name` | string | no | Birthname of the employee. |
| `gender` | string | no | gender of the employee (male \| female). |
| `identifier` | string | no | national identifier number. |
| `identifier_type` | string | no | type of identifier (ex passport). |
| `email` | string | no | personal email of the employee. |
| `login_email` | string | no | email associated to the session. |
| `birthday_on` | string | no | birthday of the employee. |
| `nationality` | string | no | nationality country code of the employee (Spain ES, United Kingdom GB). |
| `address_line_1` | string | no | address of the employee. |
| `address_line_2` | string | no | secondary address of the employee. |
| `postal_code` | string | no | postal code of the employee. |
| `city` | string | no | city of the employee. |
| `state` | string | no | state/province/region of the employee. |
| `country` | string | no | country code of the employee (Spain ES, United Kingdom GB). |
| `bank_number` | string | no | bank account number of the employee. |
| `swift_bic` | string | no | code to identify banks and financial institutions globally. |
| `bank_number_format` | string | no | bank number format. |
| `company_id` | string | yes | id of the company to which the employee belongs (not editable). |
| `legal_entity_id` | string | no | legal entity of the employee, references to companies/legal_entities. |
| `location_id` | string | yes | location id of the employee, references to locations/locations. |
| `default_work_area_id` | string | no | Default work area ID for the employee at the default workplace. References locations/work_areas. |
| `created_at` | string | yes | creation date of the employee. |
| `updated_at` | string | yes | date of last modification of the employee |
| `social_security_number` | string | no | social security number of the employee. |
| `is_terminating` | boolean | yes | is the employee being terminated? |
| `terminated_on` | string | no | termination date of the employee. |
| `termination_reason_type` | string | no | termination reason type of the employee |
| `termination_reason` | string | no | A reason for the termination. |
| `termination_observations` | string | no | observations about the termination. |
| `manager_id` | string | no | manager id of the employee, you can get the manager id from employees endpoint. |
| `timeoff_manager_id` | string | no | Timeoff manager id of the employee. |
| `phone_number` | string | no | phone number of the employee. |
| `company_identifier` | string | no | identity number or string used inside a company to internally identify the employee. |
| `age_number` | integer | no | age of the employee. |
| `termination_type_description` | string | no | The description of the termination type. |
| `contact_name` | string | no | name of the employee contact. |
| `contact_number` | string | no | phone number of the employee contact . |
| `personal_email` | string | no | personal email of the employee. |
| `seniority_calculation_date` | string | no | date since when the employee is working in the company. |
| `communications_email` | string | no | Confirmed email address for company communications and notifications. Separate from login email, used for internal company announcements. |
| `unconfirmed_communications_email` | string | no | unconfirmed communications email address for the employee. |
| `pronouns` | string | no | pronouns that an employee uses to define themselves. |
| `active` | boolean | no | status of the employee, true when active, false when terminated. |
| `disability_percentage_cents` | integer | no | officially certified level of disability granted by public administration for individuals with physical or mental impairments, expressed in cents |
| `identifier_expiration_date` | string | no | identifier expiration date |
| `attendable` | boolean | yes | employee included in a time tracking policy. |
| `country_of_birth` | string | no | Country of birth of the employee. |
| `birthplace` | string | no | Birthplace of the employee. |

### expenses_expensable

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Unique identifier for the expensable |
| `type` | string | yes | Type of the expensable. Can be either "expense" or "mileage" or "perdiem" |
| `company_id` | string | yes | The ID of the company that owns the expensable |
| `employee_id` | string | yes | The ID of the employee that owns the expensable |
| `group_id` | string | no | The ID of the expense report (group of expensables submitted together) this expensable was submitted in, if any |
| `legal_entity_id` | string | no | The optional ID of the legal entity that the expensable belongs to |
| `created_at` | string | yes | The date and time when the expensable was created |
| `amount` | integer | no | The optional amount in cents |
| `currency` | string | yes | The currency code in ISO 4217 format |
| `status` | string | yes | The lifecycle status of the expensable in the review/payment flow |
| `description` | string | no | The optional description of the expensable |
| `reporter_id` | string | no | The optional ID of the employee that reported the expensable |
| `status_updated_at` | string | yes | The optional date and time when the status was last updated |
| `effective_on` | string | no | The optional date and time when the expensable was effective |
| `review_request_at` | string | no | The optional date and time when the expensable was requested for review |
| `paid_at` | string | no | The optional date and time when the expensable was set as paid |
| `updated_at` | string | yes | The date and time when the expensable was last updated |
| `reimbursable_amount` | integer | no | The optional reimbursable amount in cents |
| `reimbursable_currency` | string | no | The optional reimbursable currency code in ISO 4217 format |
| `reimbursement_method` | string | no | The optional reimbursement method |
| `internal_reference` | string | no | The optional internal reference of the expensable |
| `expense_id` | string | no | The ID of the receipt-backed expense detail record; set only when `type` is "expense" |
| `mileage_id` | string | no | The ID of the mileage claim detail record; set only when `type` is "mileage" |
| `per_diem_id` | string | no | The ID of the per-diem allowance detail record; set only when `type` is "perdiem" |
| `budget_id` | string | no | The ID of the budget this expensable draws from, when one is linked |
| `project_id` | string | no | The ID of the project this expensable is charged to, when one is linked |
| `cost_center_ids` | array<string> | yes | The IDs of the cost centers the expensable's cost is allocated to |

### finance_cost_center

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes |  |
| `name` | string | yes |  |
| `company_id` | string | yes |  |
| `legal_entity_id` | string | no |  |
| `code` | string | no |  |
| `description` | string | no |  |
| `active_employees_count` | integer | yes |  |
| `historical_employees_count` | integer | yes |  |
| `status` | string | yes |  |
| `deactivation_date` | string | no |  |

### locations_location

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | identifier of the location |
| `company_id` | string | yes | company identifier |
| `name` | string | yes | name of the location |
| `timezone` | string | no | timezone of the location |
| `country` | string | no | country code of the location |
| `state` | string | no | State of the location |
| `city` | string | no | City of the location |
| `address_line_1` | string | no | Address line 1 of the location |
| `address_line_2` | string | no | Address line 2 of the location |
| `postal_code` | string | no | Postal code of the location |
| `phone_number` | string | no | phone number of the location |
| `main` | boolean | yes | whether the location is the main one |
| `latitude` | number | no | latitude of the location |
| `longitude` | number | no | longitude of the location |
| `radius` | number | no | radius of the location |
| `siret` | string | no | siret of the location (only for France) |

### payroll_integrations_base_code

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Code identifier |
| `company_id` | string | yes | Company ID where the code belongs to |
| `code` | string | yes | Code value |
| `codeable_id` | string | yes | Related object ID. Used together with codeable_type |
| `codeable_type` | string | yes | Related object type. Used together with codeable_id |
| `integration` | string | yes | Integration name |

### payroll_policy_period

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Policy period id |
| `name` | string | no | Policy name with start and end date |
| `starts_on` | string | yes | The start date of the policy period |
| `policy_id` | string | yes | The id of the policy associated with the policy period |
| `company_id` | string | yes | The id of the company |
| `ends_on` | string | yes | The start date of the policy period |
| `period` | string | yes | Period for the policy |
| `status` | string | no | Policy period status |
| `policy_name` | string | no | Policy name |
| `calculation_started_at` | string | no | The date and time the calculation started |

### payroll_supplement

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | The identifier of the supplement |
| `employee_id` | string | yes | The identifier of the employee associated with the supplement |
| `company_id` | string | yes | The identifier of the company associated with the supplement |
| `contracts_compensation_id` | string | no | The contract compensation identifier associated with the supplement |
| `contracts_taxonomy_id` | string | no | The taxonomy identifier associated with the supplement |
| `amount_in_cents` | integer | no | The amount of the supplement in cents |
| `unit` | string | yes | The unit of the supplement |
| `effective_on` | string | no | The date on which the supplement becomes effective |
| `created_at` | string | no | The created at date when the supplement was created |
| `updated_at` | string | no | The last updated at date when the supplement was last updated |
| `description` | string | no | The description of the supplement |
| `payroll_policy_period_id` | string | no | The payroll policy period identifier associated with the supplement |
| `employee_observations` | array<string> | no | Observations on the employee made by the admin or manager |
| `raw_minutes_in_cents` | integer | no | The raw value of minutes in cents associated with the supplement |
| `minutes_in_cents` | integer | no | The value of minutes in cents after adjustments |
| `equivalent_minutes_in_cents` | integer | no | The equivalent value of minutes in cents for payroll processing |
| `currency` | string | no | The currency used for the supplement, typically in ISO 4217 format |
| `legal_entity_id` | string | no | The legal entity identifier associated with the supplement |

### performance_review_process

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Review process ID |
| `company_id` | string | yes | Company ID |
| `name` | string | no | Review process name |
| `description` | string | no | A brief description of the review process |
| `status` | string | yes | Review process status |
| `target_strategy` | object | no | Condition that defines the employees that will be evaluated (participants). Calculated when the review process starts |
| `reviewer_strategies` | array<string> | no | Review types that will be assigned to the review process. It'll be used to create the evaluations when the process starts |
| `starts_at` | string | no | Date when the review process should start |
| `ends_at` | string | no | Date when the review process should end |
| `start_validation_errors` | array<string> | yes | Missing or invalid information to be able to start the review process |
| `archived` | boolean | yes | Whether the review process is archived or not |
| `agreements_configuration` | object | yes | Action plans help track goal progress, and facilitate performance review discussions. |
| `competencies_assessments_configuration` | object | yes | Assess employees based on their assigned competencies through both manager and self-reviews. Ensure roles with designated competencies are properly set up. |
| `last_bulk_reminder` | string | no | Date when the last bulk reminder was sent |
| `cycle_id` | string | no | Performance cycle ID |

### shift_management_shift

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Unique identifier for the shift |
| `company_id` | string | yes | Identifier of the company that owns this shift |
| `name` | string | no | Display name of the shift. If not explicitly set, falls back to the default shift title or template week name |
| `state` | string | yes | Current state of the shift. 'draft' means the shift is not yet visible to employees, 'published' means it's visible and confirmed, 'backup' indicates a backup shift that can be replaced |
| `location_id` | string | no | Identifier of the location where the shift takes place. Can be null if the shift uses the employee's default location |
| `locations_work_area_id` | string | no | Identifier of the specific work area within the location where the shift occurs. Work areas allow further subdivision of locations |
| `employee_id` | string | yes | Identifier of the employee assigned to this shift |
| `start_at` | string | yes | Timestamp indicating when the shift starts |
| `end_at` | string | yes | Timestamp indicating when the shift ends |
| `notes` | string | no | Optional notes or comments about the shift, visible to managers and schedulers |
| `extra_hours` | boolean | yes | Indicates whether this shift counts as extra hours beyond the employee's regular schedule. Used for overtime calculations |
| `default_shift_title` | string | no | Title from the default shift template that was used to create this shift, if applicable |
| `timezone` | string | yes | IANA timezone identifier (e.g., 'Europe/Madrid', 'America/New_York') used to display the shift times in the local timezone |
| `local_start_at` | string | yes | Start time of the shift converted to the local timezone. This is what employees see in their schedule |
| `local_end_at` | string | yes | End time of the shift converted to the local timezone. This is what employees see in their schedule |

### tasks_task

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Identifier of the task |
| `name` | string | yes | Name of the task |
| `company_id` | string | yes | Company identifier of the author of the task |
| `content` | string | no | Content of the task |
| `due_on` | string | no | Due on date of the task |
| `assignee_ids` | array<string> | yes | Employees assigned to the task, assignee_id references to access_id |
| `author_employee_id` | string | no | Employee id of the author of the task |
| `completed_at` | string | no | Completed at date of the task |
| `completed_by_id` | string | no | Completed by identifier |
| `created_at` | string | yes |  |
| `updated_at` | string | yes | Updated at date of the task |
| `status` | string | no | Status of the task |

### teams_membership

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Membership ID |
| `company_id` | string | no | Company ID of the membership |
| `employee_id` | string | yes | Employee ID of the membership |
| `team_id` | string | yes | Team ID of the membership |
| `lead` | boolean | yes | Whether the employee is a lead of the team or not |

### teams_team

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes |  |
| `name` | string | yes |  |
| `description` | string | no |  |
| `avatar` | string | no |  |
| `employee_ids` | array<string> | no |  |
| `lead_ids` | array<string> | no |  |
| `company_id` | string | yes |  |

### timeoff_blocked_periods_policy

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Unique identifier of the blocked period |
| `company_id` | string | yes | Company id of the blocked period |
| `name` | string | yes | Name of the blocked period. |
| `leave_type_ids` | array<string> | yes | Leave types for which absence request has been blocked |
| `time_periods` | array<object> | yes | The tenure periods associated with the allowance. |
| `strategy` | string | yes | Type of access group |
| `members` | array<string> | yes | Employees whose timeoff will be affected |
| `location_ids` | array<string> | no | List of locations workplace identifiers where the employees are located |
| `team_ids` | array<string> | no | List of team identifiers which the selected employees belong to |
| `legal_entity_ids` | array<string> | no | List of legal entity identifiers which the selected employees belong to |

### timeoff_leave

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Identifier of the Leave |
| `company_id` | string | yes | Company identifier of the employee of the leave |
| `employee_id` | string | yes | Employee identifier of the leave |
| `start_on` | string | yes | The start date of the leave |
| `finish_on` | string | no | The end date of the leave |
| `half_day` | string | no | Indicates if the leave is taken as a half-day |
| `description` | string | no | A description of the leave |
| `reason` | string | no | The reason provided by the employee for taking the leave |
| `leave_type_id` | string | no | The identifier for the type of leave |
| `leave_type_name` | string | no | The name of the leave type |
| `approved` | boolean | no | Indicates whether the leave has been approved |
| `employee_full_name` | string | no | The full name of the employee taking the leave |
| `start_time` | string | no | The start time of the leave |
| `hours_amount_in_cents` | integer | no | The total number of hours taken for the leave, represented in cents |
| `updated_at` | string | yes | The updated at date of the leave |
| `created_at` | string | no | The created at date of the leave |
| `deleted_at` | string | no | The date when the leave was deleted |
| `duration_attributes` | string | no | The duration attributes of the leave |
| `days_taken` | number | yes | Number of days taken for paid leave |

### timeoff_leave_type

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Identifier of the leave type |
| `name` | string | yes | Name of the leave type |
| `translated_name` | string | no | Translated name of the leave type, if available |
| `identifier` | string | yes | Unique identifier of the leave type |
| `color` | string | yes | The color associated with this leave type |
| `active` | boolean | no | Whether the leave type is active |
| `editable` | boolean | no | Whether the leave type is editable |
| `approval_required` | boolean | no | Whether approval is required for this leave type |
| `accrues` | boolean | no | Whether the leave type accrues over time |
| `attachment` | boolean | yes | Whether an attachment is required for this leave type |
| `allow_endless` | boolean | no | Whether endless leave is allowed |
| `restricted` | boolean | no | Whether the leave type is restricted |
| `visibility` | boolean | yes | Whether the leave type is visible to employees |
| `workable` | boolean | yes | Whether the leave type is workable |
| `payable` | boolean | no | Whether the leave type is payable |
| `company_id` | string | yes | Identifier of the company associated with this leave type |
| `is_attachment_mandatory` | boolean | no | Whether the attachment is mandatory |
| `allowance_ids` | array<string> | yes | List of allowance identifiers associated with this leave type |
| `half_days_units_enabled` | boolean | no | Whether half-day units are enabled for this leave type |
| `max_days_in_cents` | integer | no | Maximum days in cents that can be taken |
| `min_days_in_cents` | integer | no | Minimum days in cents that must be taken |
| `description` | string | no | Description of the leave type |
| `details_required` | boolean | yes | Whether additional details are required for the leave type |

### timeoff_policy

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | The policy id. |
| `name` | string | yes | Policy name. |
| `main` | boolean | no | Is the main policy? It will return true if it's the main policy if not it will return false. |
| `company_id` | string | yes | The company id. |
| `description` | string | no | The policy description. |

### trainings_category

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes |  |
| `name` | string | yes |  |
| `company_id` | string | yes |  |
| `created_at` | string | no |  |
| `updated_at` | string | no |  |

### trainings_training

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes | Identifier of the course |
| `company_id` | string | yes | Company identifier |
| `author_id` | string | yes | The person that creates the training |
| `author_employee_id` | string | no | Employee identifier of the training author |
| `name` | string | yes | Name of the training |
| `code` | string | no | Code of the training |
| `description` | string | yes | Description of the training |
| `created_at` | string | no | Creation date of the course |
| `updated_at` | string | no | Last modification date of the course |
| `external_provider` | string | no | The name of the provider if any |
| `external` | boolean | yes | External training |
| `total_cost` | integer | no |  |
| `fundae_subsidized` | boolean | yes | Subsidized by Fundae |
| `subsidized` | boolean | yes | Marked as subsidized |
| `cost` | integer | yes |  |
| `subsidized_cost` | integer | yes |  |
| `total_cost_decimal` | string | no |  |
| `cost_decimal` | string | yes |  |
| `subsidized_cost_decimal` | string | yes |  |
| `category_ids` | array<string> | no | List of ids of training categories |
| `status` | string | no | Training status. Can be one of the following values |
| `year` | integer | yes | Year of the training |
| `catalog` | boolean | yes | Visible in catalog |
| `competency_ids` | array<string> | yes | List of ids of training competencies |
| `total_training_cost` | string | yes | The total direct cost of all course's groups |
| `total_training_indirect_cost` | string | yes | The total indirect cost of all course's groups |
| `total_training_salary_cost` | string | yes | The total salary cost of all course's groups |
| `total_training_subsidized_cost` | string | yes | The total subsidized cost of all course's groups |
| `total_participants` | integer | yes | Number of participants of all course's groups |
| `training_attendance_status` | string | yes |  |
| `valid_for` | integer | no | Number of years this course is valid for |
| `objectives` | string | no | Objectives of the course |
| `number_of_expired_participants` | integer | no | Number of participants that have the course expired or about to expire in the next 3 months. Only applicable to trainings with validity period. |
| `total_duration` | number | yes | The total duration in hours and minutes of the course |
| `is_mandatory` | boolean | yes | This field is used to define if the training is mandatory or not |

### work_schedule_schedule

| field | type | required | description |
| --- | --- | --- | --- |
| `id` | string | yes |  |
| `name` | string | yes |  |
| `archived_at` | string | no |  |
| `company_id` | string | yes |  |
| `created_at` | string | yes |  |
| `updated_at` | string | yes |  |
| `employee_ids` | array<string> | yes |  |
| `periods` | array<object> | yes |  |
