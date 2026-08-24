# Factorial API endpoints → SDK calls

Auto-generated from the OpenAPI spec. 550 endpoints across 37 namespaces.

The SDK call column shows the **TypeScript** accessor and request shape (`client.<namespace>.<resource>.<method>({ path, query, body })`). The Python SDK uses the same namespaces/resources in `snake_case` (and `collect_all()` instead of `all()`), but takes the path id positionally: `get(id)`, `update(id, body=...)`. The Ruby column shows the full call on an `F::Api.new` client, with its required params as named keywords; optional query params go in a trailing `query_params:` hash and bodies under their `*_request` keyword (every listable resource also has `paginate` and `all`). `body` contents are endpoint-specific; see the [online reference](https://apidoc.factorialhr.com/reference) for exact fields.

## api_public

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.apiPublic.credentials.list()` | `api.api_public.credential.list` | GET | `/api/2026-07-01/resources/api_public/credentials` | Reads all Credentials |
| `client.apiPublic.webhookSubscriptions.list()` | `api.api_public.webhook_subscription.list` | GET | `/api/2026-07-01/resources/api_public/webhook_subscriptions` | Reads all Webhook subscriptions |
| `client.apiPublic.webhookSubscriptions.create({ body })` | `api.api_public.webhook_subscription.create` | POST | `/api/2026-07-01/resources/api_public/webhook_subscriptions` | Creates a Webhook subscription |
| `client.apiPublic.webhookSubscriptions.delete({ path: { id } })` | `api.api_public.webhook_subscription.delete(id:)` | DELETE | `/api/2026-07-01/resources/api_public/webhook_subscriptions/{id}` | Deletes a Webhook subscription |
| `client.apiPublic.webhookSubscriptions.get({ path: { id } })` | `api.api_public.webhook_subscription.get(id:)` | GET | `/api/2026-07-01/resources/api_public/webhook_subscriptions/{id}` | Reads a single Webhook subscription |
| `client.apiPublic.webhookSubscriptions.update({ path: { id }, body })` | `api.api_public.webhook_subscription.update(id:)` | PUT | `/api/2026-07-01/resources/api_public/webhook_subscriptions/{id}` | Updates a Webhook subscription |

## approvals

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.approvals.materializedApprovalsFlows.approveResource` | `api.approvals.materialized_approvals_flow.approve_resource` | POST | `/api/2026-07-01/resources/approvals/materialized_approvals_flows/approve_resource` | Approves an approval flow by resource |
| `client.approvals.materializedApprovalsFlows.rejectResource` | `api.approvals.materialized_approvals_flow.reject_resource` | POST | `/api/2026-07-01/resources/approvals/materialized_approvals_flows/reject_resource` | Rejects an approval flow by resource |

## ats

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.ats.answers.list()` | `api.ats.answer.list` | GET | `/api/2026-07-01/resources/ats/answers` | Reads all Answers |
| `client.ats.answers.create({ body })` | `api.ats.answer.create` | POST | `/api/2026-07-01/resources/ats/answers` | Creates an Answer |
| `client.ats.answers.get({ path: { id } })` | `api.ats.answer.get(id:)` | GET | `/api/2026-07-01/resources/ats/answers/{id}` | Reads a single Answer |
| `client.ats.applicationPhases.list()` | `api.ats.application_phase.list` | GET | `/api/2026-07-01/resources/ats/application_phases` | Reads all Application phases |
| `client.ats.applicationPhases.get({ path: { id } })` | `api.ats.application_phase.get(id:)` | GET | `/api/2026-07-01/resources/ats/application_phases/{id}` | Reads a single Application phase |
| `client.ats.applications.list()` | `api.ats.application.list` | GET | `/api/2026-07-01/resources/ats/applications` | Reads all Applications |
| `client.ats.applications.create({ body })` | `api.ats.application.create` | POST | `/api/2026-07-01/resources/ats/applications` | Creates an Application |
| `client.ats.applications.apply` | `api.ats.application.apply` | POST | `/api/2026-07-01/resources/ats/applications/apply` | Applies an Application |
| `client.ats.applications.moveToPhase` | `api.ats.application.move_to_phase` | POST | `/api/2026-07-01/resources/ats/applications/move_to_phase` | Move to phases an Application |
| `client.ats.applications.delete({ path: { id } })` | `api.ats.application.delete(id:)` | DELETE | `/api/2026-07-01/resources/ats/applications/{id}` | Deletes an Application |
| `client.ats.applications.get({ path: { id } })` | `api.ats.application.get(id:)` | GET | `/api/2026-07-01/resources/ats/applications/{id}` | Reads a single Application |
| `client.ats.applications.update({ path: { id }, body })` | `api.ats.application.update(id:)` | PUT | `/api/2026-07-01/resources/ats/applications/{id}` | Updates an Application |
| `client.ats.candidateSources.list()` | `api.ats.candidate_source.list` | GET | `/api/2026-07-01/resources/ats/candidate_sources` | Reads all Candidate sources |
| `client.ats.candidateSources.get({ path: { id } })` | `api.ats.candidate_source.get(id:)` | GET | `/api/2026-07-01/resources/ats/candidate_sources/{id}` | Reads a single Candidate source |
| `client.ats.candidates.list()` | `api.ats.candidate.list` | GET | `/api/2026-07-01/resources/ats/candidates` | Reads all Candidates |
| `client.ats.candidates.create({ body })` | `api.ats.candidate.create` | POST | `/api/2026-07-01/resources/ats/candidates` | Creates a Candidate |
| `client.ats.candidates.delete({ path: { id } })` | `api.ats.candidate.delete(id:)` | DELETE | `/api/2026-07-01/resources/ats/candidates/{id}` | Deletes a Candidate |
| `client.ats.candidates.get({ path: { id } })` | `api.ats.candidate.get(id:)` | GET | `/api/2026-07-01/resources/ats/candidates/{id}` | Reads a single Candidate |
| `client.ats.candidates.update({ path: { id }, body })` | `api.ats.candidate.update(id:)` | PUT | `/api/2026-07-01/resources/ats/candidates/{id}` | Updates a Candidate |
| `client.ats.evaluationForms.list()` | `api.ats.evaluation_form.list` | GET | `/api/2026-07-01/resources/ats/evaluation_forms` | Reads all Evaluation forms |
| `client.ats.evaluationForms.saveAsTemplate` | `api.ats.evaluation_form.save_as_template` | POST | `/api/2026-07-01/resources/ats/evaluation_forms/save_as_template` | Save as templates an Evaluation form |
| `client.ats.evaluationForms.get({ path: { id } })` | `api.ats.evaluation_form.get(id:)` | GET | `/api/2026-07-01/resources/ats/evaluation_forms/{id}` | Reads a single Evaluation form |
| `client.ats.feedbacks.list()` | `api.ats.feedback.list` | GET | `/api/2026-07-01/resources/ats/feedbacks` | Reads all Feedbacks |
| `client.ats.feedbacks.create({ body })` | `api.ats.feedback.create` | POST | `/api/2026-07-01/resources/ats/feedbacks` | Creates a Feedback |
| `client.ats.feedbacks.delete({ path: { id } })` | `api.ats.feedback.delete(id:)` | DELETE | `/api/2026-07-01/resources/ats/feedbacks/{id}` | Deletes a Feedback |
| `client.ats.feedbacks.get({ path: { id } })` | `api.ats.feedback.get(id:)` | GET | `/api/2026-07-01/resources/ats/feedbacks/{id}` | Reads a single Feedback |
| `client.ats.feedbacks.update({ path: { id }, body })` | `api.ats.feedback.update(id:)` | PUT | `/api/2026-07-01/resources/ats/feedbacks/{id}` | Updates a Feedback |
| `client.ats.hiringStages.list()` | `api.ats.hiring_stage.list` | GET | `/api/2026-07-01/resources/ats/hiring_stages` | Reads all Hiring stages |
| `client.ats.hiringStages.get({ path: { id } })` | `api.ats.hiring_stage.get(id:)` | GET | `/api/2026-07-01/resources/ats/hiring_stages/{id}` | Reads a single Hiring stage |
| `client.ats.jobPostings.list()` | `api.ats.job_posting.list` | GET | `/api/2026-07-01/resources/ats/job_postings` | Reads all Job postings |
| `client.ats.jobPostings.create({ body })` | `api.ats.job_posting.create` | POST | `/api/2026-07-01/resources/ats/job_postings` | Creates a Job posting |
| `client.ats.jobPostings.duplicate` | `api.ats.job_posting.duplicate` | POST | `/api/2026-07-01/resources/ats/job_postings/duplicate` | Duplicates a Job posting |
| `client.ats.jobPostings.delete({ path: { id } })` | `api.ats.job_posting.delete(id:)` | DELETE | `/api/2026-07-01/resources/ats/job_postings/{id}` | Deletes a Job posting |
| `client.ats.jobPostings.get({ path: { id } })` | `api.ats.job_posting.get(id:)` | GET | `/api/2026-07-01/resources/ats/job_postings/{id}` | Reads a single Job posting |
| `client.ats.jobPostings.update({ path: { id }, body })` | `api.ats.job_posting.update(id:)` | PUT | `/api/2026-07-01/resources/ats/job_postings/{id}` | Updates a Job posting |
| `client.ats.messages.list()` | `api.ats.message.list(last_per_conversation:)` | GET | `/api/2026-07-01/resources/ats/messages` | Reads all Messages |
| `client.ats.messages.create({ body })` | `api.ats.message.create(content:, sent_by_id:, sent_by_type:, ats_application_id:, attachments:, topic:, send_as_corporate_email:)` | POST | `/api/2026-07-01/resources/ats/messages` | Creates a Message |
| `client.ats.messages.get({ path: { id } })` | `api.ats.message.get(id:)` | GET | `/api/2026-07-01/resources/ats/messages/{id}` | Reads a single Message |
| `client.ats.questions.list()` | `api.ats.question.list` | GET | `/api/2026-07-01/resources/ats/questions` | Reads all Questions |
| `client.ats.questions.create({ body })` | `api.ats.question.create` | POST | `/api/2026-07-01/resources/ats/questions` | Creates a Question |
| `client.ats.questions.delete({ path: { id } })` | `api.ats.question.delete(id:)` | DELETE | `/api/2026-07-01/resources/ats/questions/{id}` | Deletes a Question |
| `client.ats.questions.get({ path: { id } })` | `api.ats.question.get(id:)` | GET | `/api/2026-07-01/resources/ats/questions/{id}` | Reads a single Question |
| `client.ats.questions.update({ path: { id }, body })` | `api.ats.question.update(id:)` | PUT | `/api/2026-07-01/resources/ats/questions/{id}` | Updates a Question |
| `client.ats.rejectionReasons.list()` | `api.ats.rejection_reason.list` | GET | `/api/2026-07-01/resources/ats/rejection_reasons` | Reads all Rejection reasons |
| `client.ats.rejectionReasons.get({ path: { id } })` | `api.ats.rejection_reason.get(id:)` | GET | `/api/2026-07-01/resources/ats/rejection_reasons/{id}` | Reads a single Rejection reason |

## attendance

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.attendance.breakConfigurations.list()` | `api.attendance.break_configuration.list` | GET | `/api/2026-07-01/resources/attendance/break_configurations` | Reads all Break configurations |
| `client.attendance.breakConfigurations.create({ body })` | `api.attendance.break_configuration.create` | POST | `/api/2026-07-01/resources/attendance/break_configurations` | Creates a Break configuration |
| `client.attendance.breakConfigurations.get({ path: { id } })` | `api.attendance.break_configuration.get(id:)` | GET | `/api/2026-07-01/resources/attendance/break_configurations/{id}` | Reads a single Break configuration |
| `client.attendance.breakConfigurations.update({ path: { id }, body })` | `api.attendance.break_configuration.update(id:)` | PUT | `/api/2026-07-01/resources/attendance/break_configurations/{id}` | Updates a Break configuration |
| `client.attendance.editTimesheetRequests.list()` | `api.attendance.edit_timesheet_request.list` | GET | `/api/2026-07-01/resources/attendance/edit_timesheet_requests` | Reads all Edit timesheet requests |
| `client.attendance.editTimesheetRequests.create({ body })` | `api.attendance.edit_timesheet_request.create` | POST | `/api/2026-07-01/resources/attendance/edit_timesheet_requests` | Creates an Edit timesheet request |
| `client.attendance.editTimesheetRequests.delete({ path: { id } })` | `api.attendance.edit_timesheet_request.delete(id:)` | DELETE | `/api/2026-07-01/resources/attendance/edit_timesheet_requests/{id}` | Deletes an Edit timesheet request |
| `client.attendance.editTimesheetRequests.get({ path: { id } })` | `api.attendance.edit_timesheet_request.get(id:)` | GET | `/api/2026-07-01/resources/attendance/edit_timesheet_requests/{id}` | Reads all Edit timesheet requests |
| `client.attendance.editTimesheetRequests.update({ path: { id }, body })` | `api.attendance.edit_timesheet_request.update(id:)` | PUT | `/api/2026-07-01/resources/attendance/edit_timesheet_requests/{id}` | Updates an Edit timesheet request |
| `client.attendance.estimatedTimes.list()` | `api.attendance.estimated_time.list(start_on:, end_on:, employee_ids:)` | GET | `/api/2026-07-01/resources/attendance/estimated_times` | Reads all Estimated times |
| `client.attendance.openShifts.list()` | `api.attendance.open_shift.list` | GET | `/api/2026-07-01/resources/attendance/open_shifts` | Reads all Open shifts |
| `client.attendance.overtimeRequests.list()` | `api.attendance.overtime_request.list(include_approval_flow:)` | GET | `/api/2026-07-01/resources/attendance/overtime_requests` | Reads all Overtime requests |
| `client.attendance.overtimeRequests.create({ body })` | `api.attendance.overtime_request.create` | POST | `/api/2026-07-01/resources/attendance/overtime_requests` | Creates an Overtime request |
| `client.attendance.overtimeRequests.approve` | `api.attendance.overtime_request.approve` | POST | `/api/2026-07-01/resources/attendance/overtime_requests/approve` | Approves an Overtime request |
| `client.attendance.overtimeRequests.reject` | `api.attendance.overtime_request.reject` | POST | `/api/2026-07-01/resources/attendance/overtime_requests/reject` | Rejects an Overtime request |
| `client.attendance.overtimeRequests.delete({ path: { id } })` | `api.attendance.overtime_request.delete(id:)` | DELETE | `/api/2026-07-01/resources/attendance/overtime_requests/{id}` | Deletes an Overtime request |
| `client.attendance.overtimeRequests.get({ path: { id } })` | `api.attendance.overtime_request.get(id:)` | GET | `/api/2026-07-01/resources/attendance/overtime_requests/{id}` | Reads a single Overtime request |
| `client.attendance.overtimeRequests.update({ path: { id }, body })` | `api.attendance.overtime_request.update(id:)` | PUT | `/api/2026-07-01/resources/attendance/overtime_requests/{id}` | Updates an Overtime request |
| `client.attendance.reviews.list()` | `api.attendance.review.list(employee_ids:, start_on:, end_on:, reviewed_at:)` | GET | `/api/2026-07-01/resources/attendance/reviews` | Reads all Reviews |
| `client.attendance.reviews.bulkCreate` | `api.attendance.review.bulk_create` | POST | `/api/2026-07-01/resources/attendance/reviews/bulk_create` | Bulk creates a Review |
| `client.attendance.reviews.bulkDestroy` | `api.attendance.review.bulk_destroy` | POST | `/api/2026-07-01/resources/attendance/reviews/bulk_destroy` | Bulk destroys a Review |
| `client.attendance.shifts.list()` | `api.attendance.shift.list(half_day:, sort_created_at_asc:)` | GET | `/api/2026-07-01/resources/attendance/shifts` | Reads all Shifts |
| `client.attendance.shifts.create({ body })` | `api.attendance.shift.create` | POST | `/api/2026-07-01/resources/attendance/shifts` | Creates a shift |
| `client.attendance.shifts.autofill` | `api.attendance.shift.autofill` | POST | `/api/2026-07-01/resources/attendance/shifts/autofill` | Autofills a Shift |
| `client.attendance.shifts.breakEnd` | `api.attendance.shift.break_end` | POST | `/api/2026-07-01/resources/attendance/shifts/break_end` | Break ends a Shift |
| `client.attendance.shifts.breakStart` | `api.attendance.shift.break_start` | POST | `/api/2026-07-01/resources/attendance/shifts/break_start` | Break starts a Shift |
| `client.attendance.shifts.clockIn` | `api.attendance.shift.clock_in` | POST | `/api/2026-07-01/resources/attendance/shifts/clock_in` | Clocks in a shift |
| `client.attendance.shifts.clockOut` | `api.attendance.shift.clock_out` | POST | `/api/2026-07-01/resources/attendance/shifts/clock_out` | Clocks out a shift |
| `client.attendance.shifts.toggleClock` | `api.attendance.shift.toggle_clock` | POST | `/api/2026-07-01/resources/attendance/shifts/toggle_clock` | Clock in/out a shift |
| `client.attendance.shifts.delete({ path: { id } })` | `api.attendance.shift.delete(id:)` | DELETE | `/api/2026-07-01/resources/attendance/shifts/{id}` | Deletes a Shift |
| `client.attendance.shifts.get({ path: { id } })` | `api.attendance.shift.get(id:)` | GET | `/api/2026-07-01/resources/attendance/shifts/{id}` | Reads a single Shift |
| `client.attendance.shifts.update({ path: { id }, body })` | `api.attendance.shift.update(id:)` | PUT | `/api/2026-07-01/resources/attendance/shifts/{id}` | Updates a Shift |
| `client.attendance.workedTimes.list()` | `api.attendance.worked_time.list(include_time_range_category:, include_non_attendable_employees:)` | GET | `/api/2026-07-01/resources/attendance/worked_times` | Reads all Worked times |

## banking

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.banking.bankAccounts.list()` | `api.banking.bank_account.list` | GET | `/api/2026-07-01/resources/banking/bank_accounts` | Reads all Bank accounts |
| `client.banking.bankAccounts.createManual` | `api.banking.bank_account.create_manual` | POST | `/api/2026-07-01/resources/banking/bank_accounts/create_manual` | Create manuals a Bank account |
| `client.banking.bankAccounts.get({ path: { id } })` | `api.banking.bank_account.get(id:)` | GET | `/api/2026-07-01/resources/banking/bank_accounts/{id}` | Reads a single Bank account |
| `client.banking.cardPayments.list()` | `api.banking.card_payment.list` | GET | `/api/2026-07-01/resources/banking/card_payments` | Reads all Card payments |
| `client.banking.cardPayments.get({ path: { id } })` | `api.banking.card_payment.get(id:)` | GET | `/api/2026-07-01/resources/banking/card_payments/{id}` | Reads a single Card payment |
| `client.banking.transactions.list()` | `api.banking.transaction.list` | GET | `/api/2026-07-01/resources/banking/transactions` | Reads all Transactions |
| `client.banking.transactions.get({ path: { id } })` | `api.banking.transaction.get(id:)` | GET | `/api/2026-07-01/resources/banking/transactions/{id}` | Reads a single Transaction |

## bookkeepers_management

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.bookkeepersManagement.incidences.list()` | `api.bookkeepers_management.incidence.list` | GET | `/api/2026-07-01/resources/bookkeepers_management/incidences` | Reads all Incidences |
| `client.bookkeepersManagement.incidences.get({ path: { id } })` | `api.bookkeepers_management.incidence.get(id:)` | GET | `/api/2026-07-01/resources/bookkeepers_management/incidences/{id}` | Reads a single Incidence |
| `client.bookkeepersManagement.incidences.update({ path: { id }, body })` | `api.bookkeepers_management.incidence.update(id:)` | PUT | `/api/2026-07-01/resources/bookkeepers_management/incidences/{id}` | Updates an Incidence |

## companies

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.companies.legalEntities.list()` | `api.companies.legal_entity.list` | GET | `/api/2026-07-01/resources/companies/legal_entities` | Reads all Legal entities |
| `client.companies.legalEntities.create({ body })` | `api.companies.legal_entity.create` | POST | `/api/2026-07-01/resources/companies/legal_entities` | Creates a Legal entity |
| `client.companies.legalEntities.get({ path: { id } })` | `api.companies.legal_entity.get(id:)` | GET | `/api/2026-07-01/resources/companies/legal_entities/{id}` | Reads a single Legal entity |

## compensations

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.compensations.concepts.list()` | `api.compensations.concept.list` | GET | `/api/2026-07-01/resources/compensations/concepts` | Reads all Concepts |
| `client.compensations.concepts.get({ path: { id } })` | `api.compensations.concept.get(id:)` | GET | `/api/2026-07-01/resources/compensations/concepts/{id}` | Reads a single Concept |

## contracts

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.contracts.compensations.list()` | `api.contracts.compensation.list` | GET | `/api/2026-07-01/resources/contracts/compensations` | Reads all Compensations |
| `client.contracts.compensations.create({ body })` | `api.contracts.compensation.create` | POST | `/api/2026-07-01/resources/contracts/compensations` | Creates a Compensation |
| `client.contracts.compensations.delete({ path: { id } })` | `api.contracts.compensation.delete(id:)` | DELETE | `/api/2026-07-01/resources/contracts/compensations/{id}` | Deletes a Compensation |
| `client.contracts.compensations.get({ path: { id } })` | `api.contracts.compensation.get(id:)` | GET | `/api/2026-07-01/resources/contracts/compensations/{id}` | Reads a single Compensation |
| `client.contracts.compensations.update({ path: { id }, body })` | `api.contracts.compensation.update(id:)` | PUT | `/api/2026-07-01/resources/contracts/compensations/{id}` | Updates a Compensation |
| `client.contracts.contractTemplates.list()` | `api.contracts.contract_template.list` | GET | `/api/2026-07-01/resources/contracts/contract_templates` | Reads all Contract templates |
| `client.contracts.contractTemplates.get({ path: { id } })` | `api.contracts.contract_template.get(id:)` | GET | `/api/2026-07-01/resources/contracts/contract_templates/{id}` | Reads a single Contract template |
| `client.contracts.contractVersionHistories.list()` | `api.contracts.contract_version_history.list` | GET | `/api/2026-07-01/resources/contracts/contract_version_histories` | Reads all Contract version histories |
| `client.contracts.contractVersionHistories.get({ path: { id } })` | `api.contracts.contract_version_history.get(id:)` | GET | `/api/2026-07-01/resources/contracts/contract_version_histories/{id}` | Reads a single Contract version history |
| `client.contracts.contractVersionMetaData.list()` | `api.contracts.contract_version_meta_datum.list(contract_version_ids:)` | GET | `/api/2026-07-01/resources/contracts/contract_version_meta_data` | Reads all Contract version meta data |
| `client.contracts.contractVersions.list()` | `api.contracts.contract_version.list(job_catalog_tree_node_uuids:)` | GET | `/api/2026-07-01/resources/contracts/contract_versions` | Reads all Contract versions |
| `client.contracts.contractVersions.create({ body })` | `api.contracts.contract_version.create` | POST | `/api/2026-07-01/resources/contracts/contract_versions` | Creates a Contract version |
| `client.contracts.contractVersions.delete({ path: { id } })` | `api.contracts.contract_version.delete(id:)` | DELETE | `/api/2026-07-01/resources/contracts/contract_versions/{id}` | Deletes a Contract version |
| `client.contracts.contractVersions.get({ path: { id } })` | `api.contracts.contract_version.get(id:)` | GET | `/api/2026-07-01/resources/contracts/contract_versions/{id}` | Reads a single Contract version |
| `client.contracts.contractVersions.update({ path: { id }, body })` | `api.contracts.contract_version.update(id:)` | PUT | `/api/2026-07-01/resources/contracts/contract_versions/{id}` | Updates a Contract version |
| `client.contracts.frenchContractTypes.list()` | `api.contracts.french_contract_type.list` | GET | `/api/2026-07-01/resources/contracts/french_contract_types` | Reads all French contract types |
| `client.contracts.frenchContractTypes.get({ path: { id } })` | `api.contracts.french_contract_type.get(id:)` | GET | `/api/2026-07-01/resources/contracts/french_contract_types/{id}` | Reads a single French contract type |
| `client.contracts.germanContractTypes.list()` | `api.contracts.german_contract_type.list` | GET | `/api/2026-07-01/resources/contracts/german_contract_types` | Reads all German contract types |
| `client.contracts.germanContractTypes.get({ path: { id } })` | `api.contracts.german_contract_type.get(id:)` | GET | `/api/2026-07-01/resources/contracts/german_contract_types/{id}` | Reads a single German contract type |
| `client.contracts.materializedTemplates.list()` | `api.contracts.materialized_template.list(company_id:, template_type:, include_archived:)` | GET | `/api/2026-07-01/resources/contracts/materialized_templates` | Reads all Materialized templates |
| `client.contracts.portugueseContractTypes.list()` | `api.contracts.portuguese_contract_type.list` | GET | `/api/2026-07-01/resources/contracts/portuguese_contract_types` | Reads all Portuguese contract types |
| `client.contracts.portugueseContractTypes.get({ path: { id } })` | `api.contracts.portuguese_contract_type.get(id:)` | GET | `/api/2026-07-01/resources/contracts/portuguese_contract_types/{id}` | Reads a single Portuguese contract type |
| `client.contracts.referenceContracts.list()` | `api.contracts.reference_contract.list(job_catalog_tree_node_uuids:)` | GET | `/api/2026-07-01/resources/contracts/reference_contracts` | Reads all Reference contracts |
| `client.contracts.spanishContractTypes.list()` | `api.contracts.spanish_contract_type.list` | GET | `/api/2026-07-01/resources/contracts/spanish_contract_types` | Reads all Spanish contract types |
| `client.contracts.spanishContractTypes.create({ body })` | `api.contracts.spanish_contract_type.create` | POST | `/api/2026-07-01/resources/contracts/spanish_contract_types` | Creates a Spanish contract type |
| `client.contracts.spanishContractTypes.get({ path: { id } })` | `api.contracts.spanish_contract_type.get(id:)` | GET | `/api/2026-07-01/resources/contracts/spanish_contract_types/{id}` | Reads a single Spanish contract type |
| `client.contracts.spanishEducationLevels.list()` | `api.contracts.spanish_education_level.list` | GET | `/api/2026-07-01/resources/contracts/spanish_education_levels` | Reads all Spanish education levels |
| `client.contracts.spanishEducationLevels.create({ body })` | `api.contracts.spanish_education_level.create` | POST | `/api/2026-07-01/resources/contracts/spanish_education_levels` | Creates a Spanish education level |
| `client.contracts.spanishEducationLevels.get({ path: { id } })` | `api.contracts.spanish_education_level.get(id:)` | GET | `/api/2026-07-01/resources/contracts/spanish_education_levels/{id}` | Reads a single Spanish education level |
| `client.contracts.spanishProfessionalCategories.list()` | `api.contracts.spanish_professional_category.list` | GET | `/api/2026-07-01/resources/contracts/spanish_professional_categories` | Reads all Spanish professional categories |
| `client.contracts.spanishProfessionalCategories.create({ body })` | `api.contracts.spanish_professional_category.create` | POST | `/api/2026-07-01/resources/contracts/spanish_professional_categories` | Creates a Spanish professional category |
| `client.contracts.spanishProfessionalCategories.get({ path: { id } })` | `api.contracts.spanish_professional_category.get(id:)` | GET | `/api/2026-07-01/resources/contracts/spanish_professional_categories/{id}` | Reads a single Spanish professional category |
| `client.contracts.spanishWorkingDayTypes.list()` | `api.contracts.spanish_working_day_type.list` | GET | `/api/2026-07-01/resources/contracts/spanish_working_day_types` | Reads all Spanish working day types |
| `client.contracts.spanishWorkingDayTypes.create({ body })` | `api.contracts.spanish_working_day_type.create` | POST | `/api/2026-07-01/resources/contracts/spanish_working_day_types` | Creates a Spanish working day type |
| `client.contracts.spanishWorkingDayTypes.get({ path: { id } })` | `api.contracts.spanish_working_day_type.get(id:)` | GET | `/api/2026-07-01/resources/contracts/spanish_working_day_types/{id}` | Reads a single Spanish working day type |
| `client.contracts.taxonomies.list()` | `api.contracts.taxonomy.list` | GET | `/api/2026-07-01/resources/contracts/taxonomies` | Reads all Taxonomies |
| `client.contracts.taxonomies.get({ path: { id } })` | `api.contracts.taxonomy.get(id:)` | GET | `/api/2026-07-01/resources/contracts/taxonomies/{id}` | Reads a single Taxonomy |

## custom_fields

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.customFields.fields.list()` | `api.custom_fields.field.list` | GET | `/api/2026-07-01/resources/custom_fields/fields` | Reads all Fields |
| `client.customFields.fields.create({ body })` | `api.custom_fields.field.create` | POST | `/api/2026-07-01/resources/custom_fields/fields` | Creates a Field |
| `client.customFields.fields.delete({ path: { id } })` | `api.custom_fields.field.delete(id:)` | DELETE | `/api/2026-07-01/resources/custom_fields/fields/{id}` | Deletes a Field |
| `client.customFields.fields.get({ path: { id } })` | `api.custom_fields.field.get(id:)` | GET | `/api/2026-07-01/resources/custom_fields/fields/{id}` | Reads a single Field |
| `client.customFields.options.list()` | `api.custom_fields.option.list` | GET | `/api/2026-07-01/resources/custom_fields/options` | Reads all Options |
| `client.customFields.options.create({ body })` | `api.custom_fields.option.create` | POST | `/api/2026-07-01/resources/custom_fields/options` | Creates an Option |
| `client.customFields.options.get({ path: { id } })` | `api.custom_fields.option.get(id:)` | GET | `/api/2026-07-01/resources/custom_fields/options/{id}` | Reads a single Option |
| `client.customFields.resourceFields.list()` | `api.custom_fields.resource_field.list` | GET | `/api/2026-07-01/resources/custom_fields/resource_fields` | Reads all Resource fields |
| `client.customFields.resourceFields.create({ body })` | `api.custom_fields.resource_field.create` | POST | `/api/2026-07-01/resources/custom_fields/resource_fields` | Creates a Resource field |
| `client.customFields.resourceFields.get({ path: { id } })` | `api.custom_fields.resource_field.get(id:)` | GET | `/api/2026-07-01/resources/custom_fields/resource_fields/{id}` | Reads a single Resource field |
| `client.customFields.values.list()` | `api.custom_fields.value.list` | GET | `/api/2026-07-01/resources/custom_fields/values` | Reads all Values |
| `client.customFields.values.create({ body })` | `api.custom_fields.value.create` | POST | `/api/2026-07-01/resources/custom_fields/values` | Creates a Value |
| `client.customFields.values.get({ path: { id } })` | `api.custom_fields.value.get(id:)` | GET | `/api/2026-07-01/resources/custom_fields/values/{id}` | Reads a single Value |
| `client.customFields.values.update({ path: { id }, body })` | `api.custom_fields.value.update(id:)` | PUT | `/api/2026-07-01/resources/custom_fields/values/{id}` | Updates a Value |

## custom_resources

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.customResources.resources.list()` | `api.custom_resources.resource.list` | GET | `/api/2026-07-01/resources/custom_resources/resources` | Reads all Resources |
| `client.customResources.resources.get({ path: { id } })` | `api.custom_resources.resource.get(id:)` | GET | `/api/2026-07-01/resources/custom_resources/resources/{id}` | Reads a single Resource |
| `client.customResources.schemas.list()` | `api.custom_resources.schema.list` | GET | `/api/2026-07-01/resources/custom_resources/schemas` | Reads all Schemas |
| `client.customResources.schemas.create({ body })` | `api.custom_resources.schema.create` | POST | `/api/2026-07-01/resources/custom_resources/schemas` | Creates a Schema |
| `client.customResources.schemas.get({ path: { id } })` | `api.custom_resources.schema.get(id:)` | GET | `/api/2026-07-01/resources/custom_resources/schemas/{id}` | Reads a single Schema |
| `client.customResources.values.list()` | `api.custom_resources.value.list` | GET | `/api/2026-07-01/resources/custom_resources/values` | Reads all Values |
| `client.customResources.values.create({ body })` | `api.custom_resources.value.create` | POST | `/api/2026-07-01/resources/custom_resources/values` | Creates a Value |
| `client.customResources.values.get({ path: { id } })` | `api.custom_resources.value.get(id:)` | GET | `/api/2026-07-01/resources/custom_resources/values/{id}` | Reads a single Value |

## documents

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.documents.documents.list()` | `api.documents.document.list(by_pending_assignment:, by_trash_bin:)` | GET | `/api/2026-07-01/resources/documents/documents` | Reads all Documents |
| `client.documents.documents.create({ body })` | `api.documents.document.create(public:, space:, is_pending_assignment:, file:, author_id:, company_id:, signee_ids:, request_esignature:)` | POST | `/api/2026-07-01/resources/documents/documents` | Creates a Document |
| `client.documents.documents.moveToTrashBin` | `api.documents.document.move_to_trash_bin` | POST | `/api/2026-07-01/resources/documents/documents/move_to_trash_bin` | Move to trash bins a Document |
| `client.documents.documents.restoreFromTrashBin` | `api.documents.document.restore_from_trash_bin` | POST | `/api/2026-07-01/resources/documents/documents/restore_from_trash_bin` | Restore from trash bins a Document |
| `client.documents.documents.delete({ path: { id } })` | `api.documents.document.delete(id:)` | DELETE | `/api/2026-07-01/resources/documents/documents/{id}` | Deletes a Document |
| `client.documents.documents.get({ path: { id } })` | `api.documents.document.get(id:)` | GET | `/api/2026-07-01/resources/documents/documents/{id}` | Reads a single Document |
| `client.documents.documents.update({ path: { id }, body })` | `api.documents.document.update(id:)` | PUT | `/api/2026-07-01/resources/documents/documents/{id}` | Updates a Document |
| `client.documents.downloadUrls.bulkCreate` | `api.documents.download_url.bulk_create` | POST | `/api/2026-07-01/resources/documents/download_urls/bulk_create` | Bulk creates a Download url |
| `client.documents.folders.list()` | `api.documents.folder.list` | GET | `/api/2026-07-01/resources/documents/folders` | Reads all Folders |
| `client.documents.folders.create({ body })` | `api.documents.folder.create` | POST | `/api/2026-07-01/resources/documents/folders` | Creates a Folder |
| `client.documents.folders.get({ path: { id } })` | `api.documents.folder.get(id:)` | GET | `/api/2026-07-01/resources/documents/folders/{id}` | Reads a single Folder |
| `client.documents.folders.update({ path: { id }, body })` | `api.documents.folder.update(id:)` | PUT | `/api/2026-07-01/resources/documents/folders/{id}` | Updates a Folder |

## employee_updates

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.employeeUpdates.absences.list()` | `api.employee_updates.absence.list` | GET | `/api/2026-07-01/resources/employee_updates/absences` | Reads all Absences |
| `client.employeeUpdates.absences.get({ path: { id } })` | `api.employee_updates.absence.get(id:)` | GET | `/api/2026-07-01/resources/employee_updates/absences/{id}` | Reads a single Absence |
| `client.employeeUpdates.contractChanges.list()` | `api.employee_updates.contract_change.list` | GET | `/api/2026-07-01/resources/employee_updates/contract_changes` | Reads all Contract changes |
| `client.employeeUpdates.contractChanges.get({ path: { id } })` | `api.employee_updates.contract_change.get(id:)` | GET | `/api/2026-07-01/resources/employee_updates/contract_changes/{id}` | Reads a single Contract change |
| `client.employeeUpdates.newHires.list()` | `api.employee_updates.new_hire.list` | GET | `/api/2026-07-01/resources/employee_updates/new_hires` | Reads all New hires |
| `client.employeeUpdates.newHires.get({ path: { id } })` | `api.employee_updates.new_hire.get(id:)` | GET | `/api/2026-07-01/resources/employee_updates/new_hires/{id}` | Reads a single New hire |
| `client.employeeUpdates.personalChanges.list()` | `api.employee_updates.personal_change.list` | GET | `/api/2026-07-01/resources/employee_updates/personal_changes` | Reads all Personal changes |
| `client.employeeUpdates.personalChanges.get({ path: { id } })` | `api.employee_updates.personal_change.get(id:)` | GET | `/api/2026-07-01/resources/employee_updates/personal_changes/{id}` | Reads a single Personal change |
| `client.employeeUpdates.summaries.list()` | `api.employee_updates.summary.list` | GET | `/api/2026-07-01/resources/employee_updates/summaries` | Reads all Summaries |
| `client.employeeUpdates.summaries.get({ path: { id } })` | `api.employee_updates.summary.get(id:)` | GET | `/api/2026-07-01/resources/employee_updates/summaries/{id}` | Reads a single Summary |
| `client.employeeUpdates.terminations.list()` | `api.employee_updates.termination.list` | GET | `/api/2026-07-01/resources/employee_updates/terminations` | Reads all Terminations |
| `client.employeeUpdates.terminations.get({ path: { id } })` | `api.employee_updates.termination.get(id:)` | GET | `/api/2026-07-01/resources/employee_updates/terminations/{id}` | Reads a single Termination |

## employees

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.employees.employees.list()` | `api.employees.employee.list(only_active:, only_managers:)` | GET | `/api/2026-07-01/resources/employees/employees` | Reads all Employees |
| `client.employees.employees.createWithContract` | `api.employees.employee.create_with_contract` | POST | `/api/2026-07-01/resources/employees/employees/create_with_contract` | Create with contracts an Employee |
| `client.employees.employees.invite` | `api.employees.employee.invite` | POST | `/api/2026-07-01/resources/employees/employees/invite` | Invites an Employee |
| `client.employees.employees.setRegularAccessStartDate` | `api.employees.employee.set_regular_access_start_date` | POST | `/api/2026-07-01/resources/employees/employees/set_regular_access_start_date` | Set regular access start dates an Employee |
| `client.employees.employees.terminate` | `api.employees.employee.terminate` | POST | `/api/2026-07-01/resources/employees/employees/terminate` | Terminates an Employee |
| `client.employees.employees.unterminate` | `api.employees.employee.unterminate` | POST | `/api/2026-07-01/resources/employees/employees/unterminate` | Unterminates an Employee |
| `client.employees.employees.get({ path: { id } })` | `api.employees.employee.get(id:)` | GET | `/api/2026-07-01/resources/employees/employees/{id}` | Reads a single Employee |
| `client.employees.employees.update({ path: { id }, body })` | `api.employees.employee.update(id:)` | PUT | `/api/2026-07-01/resources/employees/employees/{id}` | Updates an Employee |

## expenses

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.expenses.expensables.list()` | `api.expenses.expensable.list(include_grouped:, include_attachments:, include_manual_drafts:)` | GET | `/api/2026-07-01/resources/expenses/expensables` | Reads all Expensables |
| `client.expenses.expensables.bulkSetToPaid` | `api.expenses.expensable.bulk_set_to_paid` | POST | `/api/2026-07-01/resources/expenses/expensables/bulk_set_to_paid` | Bulk set to paids an Expensable |
| `client.expenses.expensables.updateReimbursableAmount` | `api.expenses.expensable.update_reimbursable_amount` | POST | `/api/2026-07-01/resources/expenses/expensables/update_reimbursable_amount` | Update reimbursable amount on an expensable |
| `client.expenses.expensables.get({ path: { id } })` | `api.expenses.expensable.get(id:)` | GET | `/api/2026-07-01/resources/expenses/expensables/{id}` | Reads a single Expensable |
| `client.expenses.expenses.list()` | `api.expenses.expense.list(include_manual_drafts:, include_attachments:)` | GET | `/api/2026-07-01/resources/expenses/expenses` | Reads all Expenses |
| `client.expenses.expenses.get({ path: { id } })` | `api.expenses.expense.get(id:)` | GET | `/api/2026-07-01/resources/expenses/expenses/{id}` | Reads a single Expense |
| `client.expenses.mileages.list()` | `api.expenses.mileage.list(include_manual_drafts:, include_attachments:)` | GET | `/api/2026-07-01/resources/expenses/mileages` | Reads all Mileages |
| `client.expenses.mileages.get({ path: { id } })` | `api.expenses.mileage.get(id:)` | GET | `/api/2026-07-01/resources/expenses/mileages/{id}` | Reads a single Mileage |
| `client.expenses.perDiems.list()` | `api.expenses.per_diem.list` | GET | `/api/2026-07-01/resources/expenses/per_diems` | Reads all Per diems |
| `client.expenses.perDiems.get({ path: { id } })` | `api.expenses.per_diem.get(id:)` | GET | `/api/2026-07-01/resources/expenses/per_diems/{id}` | Reads a single Per diem |

## finance

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.finance.accountingSettings.list()` | `api.finance.accounting_setting.list` | GET | `/api/2026-07-01/resources/finance/accounting_settings` | Reads all Accounting settings |
| `client.finance.accountingSettings.upsert` | `api.finance.accounting_setting.upsert` | POST | `/api/2026-07-01/resources/finance/accounting_settings/upsert` | Upserts an Accounting setting |
| `client.finance.accountingSettings.get({ path: { id } })` | `api.finance.accounting_setting.get(id:)` | GET | `/api/2026-07-01/resources/finance/accounting_settings/{id}` | Reads a single Accounting setting |
| `client.finance.accounts.list()` | `api.finance.account.list` | GET | `/api/2026-07-01/resources/finance/accounts` | Reads all Accounts |
| `client.finance.accounts.create({ body })` | `api.finance.account.create` | POST | `/api/2026-07-01/resources/finance/accounts` | Creates an Account |
| `client.finance.accounts.get({ path: { id } })` | `api.finance.account.get(id:)` | GET | `/api/2026-07-01/resources/finance/accounts/{id}` | Reads a single Account |
| `client.finance.accounts.update({ path: { id }, body })` | `api.finance.account.update(id:)` | PUT | `/api/2026-07-01/resources/finance/accounts/{id}` | Updates an Account |
| `client.finance.budgetOptions.list()` | `api.finance.budget_option.list(include_inactive:, include_archived:)` | GET | `/api/2026-07-01/resources/finance/budget_options` | Reads all Budget options |
| `client.finance.budgetOptions.get({ path: { id } })` | `api.finance.budget_option.get(id:)` | GET | `/api/2026-07-01/resources/finance/budget_options/{id}` | Reads a single Budget option |
| `client.finance.categories.list()` | `api.finance.category.list(category_level:, type:, statuses:)` | GET | `/api/2026-07-01/resources/finance/categories` | Reads all Categories |
| `client.finance.categories.get({ path: { id } })` | `api.finance.category.get(id:)` | GET | `/api/2026-07-01/resources/finance/categories/{id}` | Reads a single Category |
| `client.finance.contacts.list()` | `api.finance.contact.list` | GET | `/api/2026-07-01/resources/finance/contacts` | Reads all Contacts |
| `client.finance.contacts.create({ body })` | `api.finance.contact.create` | POST | `/api/2026-07-01/resources/finance/contacts` | Creates a Contact |
| `client.finance.contacts.get({ path: { id } })` | `api.finance.contact.get(id:)` | GET | `/api/2026-07-01/resources/finance/contacts/{id}` | Reads a single Contact |
| `client.finance.contacts.update({ path: { id }, body })` | `api.finance.contact.update(id:)` | PUT | `/api/2026-07-01/resources/finance/contacts/{id}` | Updates a Contact |
| `client.finance.costCenterMemberships.list()` | `api.finance.cost_center_membership.list` | GET | `/api/2026-07-01/resources/finance/cost_center_memberships` | Reads all Cost center memberships |
| `client.finance.costCenterMemberships.bulkCreateUpdate` | `api.finance.cost_center_membership.bulk_create_update` | POST | `/api/2026-07-01/resources/finance/cost_center_memberships/bulk_create_update` | Bulk create updates a Cost center membership |
| `client.finance.costCenters.list()` | `api.finance.cost_center.list` | GET | `/api/2026-07-01/resources/finance/cost_centers` | Reads all Cost centers |
| `client.finance.costCenters.create({ body })` | `api.finance.cost_center.create` | POST | `/api/2026-07-01/resources/finance/cost_centers` | Creates a Cost center |
| `client.finance.costCenters.edit` | `api.finance.cost_center.edit` | POST | `/api/2026-07-01/resources/finance/cost_centers/edit` | Edits a Cost center |
| `client.finance.costCenters.delete({ path: { id } })` | `api.finance.cost_center.delete(id:)` | DELETE | `/api/2026-07-01/resources/finance/cost_centers/{id}` | Deletes a Cost center |
| `client.finance.costCenters.get({ path: { id } })` | `api.finance.cost_center.get(id:)` | GET | `/api/2026-07-01/resources/finance/cost_centers/{id}` | Reads a single Cost center |
| `client.finance.financialDocuments.list()` | `api.finance.financial_document.list` | GET | `/api/2026-07-01/resources/finance/financial_documents` | Reads all Financial documents |
| `client.finance.financialDocuments.get({ path: { id } })` | `api.finance.financial_document.get(id:)` | GET | `/api/2026-07-01/resources/finance/financial_documents/{id}` | Reads a single Financial document |
| `client.finance.journalEntries.list()` | `api.finance.journal_entry.list` | GET | `/api/2026-07-01/resources/finance/journal_entries` | Reads all Journal entries |
| `client.finance.journalEntries.create({ body })` | `api.finance.journal_entry.create` | POST | `/api/2026-07-01/resources/finance/journal_entries` | Creates a Journal entry |
| `client.finance.journalEntries.get({ path: { id } })` | `api.finance.journal_entry.get(id:)` | GET | `/api/2026-07-01/resources/finance/journal_entries/{id}` | Reads a single Journal entry |
| `client.finance.journalLines.list()` | `api.finance.journal_line.list` | GET | `/api/2026-07-01/resources/finance/journal_lines` | Reads all Journal lines |
| `client.finance.journalLines.get({ path: { id } })` | `api.finance.journal_line.get(id:)` | GET | `/api/2026-07-01/resources/finance/journal_lines/{id}` | Reads a single Journal line |
| `client.finance.ledgerAccountResources.list()` | `api.finance.ledger_account_resource.list` | GET | `/api/2026-07-01/resources/finance/ledger_account_resources` | Reads all Ledger account resources |
| `client.finance.ledgerAccountResources.upsert` | `api.finance.ledger_account_resource.upsert` | POST | `/api/2026-07-01/resources/finance/ledger_account_resources/upsert` | Upserts a Ledger account resource |
| `client.finance.ledgerAccountResources.get({ path: { id } })` | `api.finance.ledger_account_resource.get(id:)` | GET | `/api/2026-07-01/resources/finance/ledger_account_resources/{id}` | Reads a single Ledger account resource |
| `client.finance.taxRates.list()` | `api.finance.tax_rate.list` | GET | `/api/2026-07-01/resources/finance/tax_rates` | Reads all Tax rates |
| `client.finance.taxRates.create({ body })` | `api.finance.tax_rate.create` | POST | `/api/2026-07-01/resources/finance/tax_rates` | Creates a Tax rate |
| `client.finance.taxRates.get({ path: { id } })` | `api.finance.tax_rate.get(id:)` | GET | `/api/2026-07-01/resources/finance/tax_rates/{id}` | Reads a single Tax rate |
| `client.finance.taxRates.update({ path: { id }, body })` | `api.finance.tax_rate.update(id:)` | PUT | `/api/2026-07-01/resources/finance/tax_rates/{id}` | Updates a Tax rate |
| `client.finance.taxTypes.list()` | `api.finance.tax_type.list` | GET | `/api/2026-07-01/resources/finance/tax_types` | Reads all Tax types |
| `client.finance.taxTypes.create({ body })` | `api.finance.tax_type.create` | POST | `/api/2026-07-01/resources/finance/tax_types` | Creates a Tax type |
| `client.finance.taxTypes.get({ path: { id } })` | `api.finance.tax_type.get(id:)` | GET | `/api/2026-07-01/resources/finance/tax_types/{id}` | Reads a single Tax type |
| `client.finance.taxTypes.update({ path: { id }, body })` | `api.finance.tax_type.update(id:)` | PUT | `/api/2026-07-01/resources/finance/tax_types/{id}` | Updates a Tax type |

## holidays

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.holidays.companyHolidays.list()` | `api.holidays.company_holiday.list` | GET | `/api/2026-07-01/resources/holidays/company_holidays` | Reads all Company holidays |
| `client.holidays.companyHolidays.get({ path: { id } })` | `api.holidays.company_holiday.get(id:)` | GET | `/api/2026-07-01/resources/holidays/company_holidays/{id}` | Reads a single Company holiday |

## integrations

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.integrations.syncRunOutputs.create({ body })` | `api.integrations.sync_run_output.create(sync_run_id:, file:)` | POST | `/api/2026-07-01/resources/integrations/sync_run_outputs` | Creates a Sync run output |
| `client.integrations.syncableItems.list()` | `api.integrations.syncable_item.list(sync_run_id:)` | GET | `/api/2026-07-01/resources/integrations/syncable_items` | Reads all Syncable items |
| `client.integrations.syncableSyncRuns.update({ path: { id }, body })` | `api.integrations.syncable_sync_run.update(id:)` | PUT | `/api/2026-07-01/resources/integrations/syncable_sync_runs/{id}` | Updates a Syncable sync run |

## it_management

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.itManagement.itAssetModels.list()` | `api.it_management.it_asset_model.list` | GET | `/api/2026-07-01/resources/it_management/it_asset_models` | Reads all It asset models |
| `client.itManagement.itAssetModels.create({ body })` | `api.it_management.it_asset_model.create` | POST | `/api/2026-07-01/resources/it_management/it_asset_models` | Creates an It asset model |
| `client.itManagement.itAssetModels.get({ path: { id } })` | `api.it_management.it_asset_model.get(id:)` | GET | `/api/2026-07-01/resources/it_management/it_asset_models/{id}` | Reads a single It asset model |
| `client.itManagement.itAssetModels.update({ path: { id }, body })` | `api.it_management.it_asset_model.update(id:)` | PUT | `/api/2026-07-01/resources/it_management/it_asset_models/{id}` | Updates an It asset model |
| `client.itManagement.itAssets.list()` | `api.it_management.it_asset.list` | GET | `/api/2026-07-01/resources/it_management/it_assets` | Reads all It assets |
| `client.itManagement.itAssets.create({ body })` | `api.it_management.it_asset.create` | POST | `/api/2026-07-01/resources/it_management/it_assets` | Creates an It asset |
| `client.itManagement.itAssets.delete({ path: { id } })` | `api.it_management.it_asset.delete(id:)` | DELETE | `/api/2026-07-01/resources/it_management/it_assets/{id}` | Deletes an It asset |
| `client.itManagement.itAssets.get({ path: { id } })` | `api.it_management.it_asset.get(id:)` | GET | `/api/2026-07-01/resources/it_management/it_assets/{id}` | Reads a single It asset |
| `client.itManagement.itAssets.update({ path: { id }, body })` | `api.it_management.it_asset.update(id:)` | PUT | `/api/2026-07-01/resources/it_management/it_assets/{id}` | Updates an It asset |

## job_catalog

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.jobCatalog.levels.list()` | `api.job_catalog.level.list` | GET | `/api/2026-07-01/resources/job_catalog/levels` | Reads all Levels |
| `client.jobCatalog.levels.get({ path: { id } })` | `api.job_catalog.level.get(id:)` | GET | `/api/2026-07-01/resources/job_catalog/levels/{id}` | Reads a single Level |
| `client.jobCatalog.nodeAttributes.list()` | `api.job_catalog.node_attribute.list(node_uuid:, attribute_types:)` | GET | `/api/2026-07-01/resources/job_catalog/node_attributes` | Reads all Node attributes |
| `client.jobCatalog.roles.list()` | `api.job_catalog.role.list` | GET | `/api/2026-07-01/resources/job_catalog/roles` | Reads all Roles |
| `client.jobCatalog.roles.get({ path: { id } })` | `api.job_catalog.role.get(id:)` | GET | `/api/2026-07-01/resources/job_catalog/roles/{id}` | Reads a single Role |
| `client.jobCatalog.treeNodes.list()` | `api.job_catalog.tree_node.list(node_type:)` | GET | `/api/2026-07-01/resources/job_catalog/tree_nodes` | Reads all Tree nodes |

## locations

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.locations.locations.list()` | `api.locations.location.list` | GET | `/api/2026-07-01/resources/locations/locations` | Reads all Locations |
| `client.locations.locations.create({ body })` | `api.locations.location.create` | POST | `/api/2026-07-01/resources/locations/locations` | Creates a Location |
| `client.locations.locations.delete({ path: { id } })` | `api.locations.location.delete(id:)` | DELETE | `/api/2026-07-01/resources/locations/locations/{id}` | Deletes a Location |
| `client.locations.locations.get({ path: { id } })` | `api.locations.location.get(id:)` | GET | `/api/2026-07-01/resources/locations/locations/{id}` | Reads a single Location |
| `client.locations.locations.update({ path: { id }, body })` | `api.locations.location.update(id:)` | PUT | `/api/2026-07-01/resources/locations/locations/{id}` | Updates a Location |
| `client.locations.workAreas.list()` | `api.locations.work_area.list(only_non_archived:)` | GET | `/api/2026-07-01/resources/locations/work_areas` | Reads all Work areas |
| `client.locations.workAreas.create({ body })` | `api.locations.work_area.create` | POST | `/api/2026-07-01/resources/locations/work_areas` | Creates a Work area |
| `client.locations.workAreas.archive` | `api.locations.work_area.archive` | POST | `/api/2026-07-01/resources/locations/work_areas/archive` | Archives a Work area |
| `client.locations.workAreas.unarchive` | `api.locations.work_area.unarchive` | POST | `/api/2026-07-01/resources/locations/work_areas/unarchive` | Unarchives a Work area |
| `client.locations.workAreas.get({ path: { id } })` | `api.locations.work_area.get(id:)` | GET | `/api/2026-07-01/resources/locations/work_areas/{id}` | Reads a single Work area |
| `client.locations.workAreas.update({ path: { id }, body })` | `api.locations.work_area.update(id:)` | PUT | `/api/2026-07-01/resources/locations/work_areas/{id}` | Updates a Work area |

## marketplace

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.marketplace.installationSettings.list()` | `api.marketplace.installation_setting.list(company_id:, integration_id:)` | GET | `/api/2026-07-01/resources/marketplace/installation_settings` | Reads all Installation settings |
| `client.marketplace.installations.create({ body })` | `api.marketplace.installation.create` | POST | `/api/2026-07-01/resources/marketplace/installations` | Creates an Installation |

## payroll

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.payroll.familySituations.list()` | `api.payroll.family_situation.list` | GET | `/api/2026-07-01/resources/payroll/family_situations` | Reads all Family situations |
| `client.payroll.familySituations.create({ body })` | `api.payroll.family_situation.create` | POST | `/api/2026-07-01/resources/payroll/family_situations` | Creates a Family situation |
| `client.payroll.familySituations.update({ path: { id }, body })` | `api.payroll.family_situation.update(id:)` | PUT | `/api/2026-07-01/resources/payroll/family_situations/{id}` | Updates a Family situation |
| `client.payroll.policyPeriods.changeStatus` | `api.payroll.policy_period.change_status` | POST | `/api/2026-07-01/resources/payroll/policy_periods/change_status` | Change statuses a Policy period |
| `client.payroll.supplements.list()` | `api.payroll.supplement.list(policy_period_ids:)` | GET | `/api/2026-07-01/resources/payroll/supplements` | Reads all Supplements |
| `client.payroll.supplements.create({ body })` | `api.payroll.supplement.create` | POST | `/api/2026-07-01/resources/payroll/supplements` | Creates a Supplement |
| `client.payroll.supplements.delete({ path: { id } })` | `api.payroll.supplement.delete(id:)` | DELETE | `/api/2026-07-01/resources/payroll/supplements/{id}` | Deletes a Supplement |
| `client.payroll.supplements.get({ path: { id } })` | `api.payroll.supplement.get(id:)` | GET | `/api/2026-07-01/resources/payroll/supplements/{id}` | Reads a single Supplement |
| `client.payroll.supplements.update({ path: { id }, body })` | `api.payroll.supplement.update(id:)` | PUT | `/api/2026-07-01/resources/payroll/supplements/{id}` | Updates a Supplement |

## payroll_employees

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.payrollEmployees.identifiers.list()` | `api.payroll_employees.identifier.list(country:)` | GET | `/api/2026-07-01/resources/payroll_employees/identifiers` | Reads all Identifiers |
| `client.payrollEmployees.identifiers.create({ body })` | `api.payroll_employees.identifier.create` | POST | `/api/2026-07-01/resources/payroll_employees/identifiers` | Creates an Identifier |
| `client.payrollEmployees.identifiers.delete({ path: { id } })` | `api.payroll_employees.identifier.delete(id:)` | DELETE | `/api/2026-07-01/resources/payroll_employees/identifiers/{id}` | Deletes an Identifier |
| `client.payrollEmployees.identifiers.get({ path: { id } })` | `api.payroll_employees.identifier.get(id:)` | GET | `/api/2026-07-01/resources/payroll_employees/identifiers/{id}` | Reads a single Identifier |
| `client.payrollEmployees.identifiers.update({ path: { id }, body })` | `api.payroll_employees.identifier.update(id:)` | PUT | `/api/2026-07-01/resources/payroll_employees/identifiers/{id}` | Updates an Identifier |

## payroll_integrations_base

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.payrollIntegrationsBase.codes.list()` | `api.payroll_integrations_base.code.list(integrations:)` | GET | `/api/2026-07-01/resources/payroll_integrations_base/codes` | Reads all Codes |
| `client.payrollIntegrationsBase.codes.create({ body })` | `api.payroll_integrations_base.code.create` | POST | `/api/2026-07-01/resources/payroll_integrations_base/codes` | Creates a Code |
| `client.payrollIntegrationsBase.codes.delete({ path: { id } })` | `api.payroll_integrations_base.code.delete(id:)` | DELETE | `/api/2026-07-01/resources/payroll_integrations_base/codes/{id}` | Deletes a Code |
| `client.payrollIntegrationsBase.codes.update({ path: { id }, body })` | `api.payroll_integrations_base.code.update(id:)` | PUT | `/api/2026-07-01/resources/payroll_integrations_base/codes/{id}` | Updates a Code |

## performance

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.performance.agreements.list()` | `api.performance.agreement.list` | GET | `/api/2026-07-01/resources/performance/agreements` | Reads all Agreements |
| `client.performance.agreements.bulkInitiate` | `api.performance.agreement.bulk_initiate` | POST | `/api/2026-07-01/resources/performance/agreements/bulk_initiate` | Bulk initiates an Agreement |
| `client.performance.agreements.initiate` | `api.performance.agreement.initiate` | POST | `/api/2026-07-01/resources/performance/agreements/initiate` | Initiates an Agreement |
| `client.performance.agreements.get({ path: { id } })` | `api.performance.agreement.get(id:)` | GET | `/api/2026-07-01/resources/performance/agreements/{id}` | Reads a single Agreement |
| `client.performance.companyEmployeeScoreScales.list()` | `api.performance.company_employee_score_scale.list` | GET | `/api/2026-07-01/resources/performance/company_employee_score_scales` | Reads all Company employee score scales |
| `client.performance.companyEmployeeScoreScales.set` | `api.performance.company_employee_score_scale.set` | POST | `/api/2026-07-01/resources/performance/company_employee_score_scales/set` | Sets a Company employee score scale |
| `client.performance.companyEmployeeScoreScales.get({ path: { id } })` | `api.performance.company_employee_score_scale.get(id:)` | GET | `/api/2026-07-01/resources/performance/company_employee_score_scales/{id}` | Reads a single Company employee score scale |
| `client.performance.employeeScoreScales.list()` | `api.performance.employee_score_scale.list` | GET | `/api/2026-07-01/resources/performance/employee_score_scales` | Reads all Employee score scales |
| `client.performance.employeeScoreScales.get({ path: { id } })` | `api.performance.employee_score_scale.get(id:)` | GET | `/api/2026-07-01/resources/performance/employee_score_scales/{id}` | Reads a single Employee score scale |
| `client.performance.reviewEvaluationAnswers.list()` | `api.performance.review_evaluation_answer.list` | GET | `/api/2026-07-01/resources/performance/review_evaluation_answers` | Reads all Review evaluation answers |
| `client.performance.reviewEvaluationScores.list()` | `api.performance.review_evaluation_score.list` | GET | `/api/2026-07-01/resources/performance/review_evaluation_scores` | Reads all Review evaluation scores |
| `client.performance.reviewEvaluationScores.get({ path: { id } })` | `api.performance.review_evaluation_score.get(id:)` | GET | `/api/2026-07-01/resources/performance/review_evaluation_scores/{id}` | Reads a single Review evaluation score |
| `client.performance.reviewEvaluations.list()` | `api.performance.review_evaluation.list` | GET | `/api/2026-07-01/resources/performance/review_evaluations` | Reads all Review evaluations |
| `client.performance.reviewEvaluations.replaceReviewer` | `api.performance.review_evaluation.replace_reviewer` | POST | `/api/2026-07-01/resources/performance/review_evaluations/replace_reviewer` | Replace reviewers a Review evaluation |
| `client.performance.reviewEvaluations.get({ path: { id } })` | `api.performance.review_evaluation.get(id:)` | GET | `/api/2026-07-01/resources/performance/review_evaluations/{id}` | Reads a single Review evaluation |
| `client.performance.reviewOwners.list()` | `api.performance.review_owner.list` | GET | `/api/2026-07-01/resources/performance/review_owners` | Reads all Review owners |
| `client.performance.reviewOwners.bulkCreate` | `api.performance.review_owner.bulk_create` | POST | `/api/2026-07-01/resources/performance/review_owners/bulk_create` | Bulk creates a Review owner |
| `client.performance.reviewOwners.delete({ path: { id } })` | `api.performance.review_owner.delete(id:)` | DELETE | `/api/2026-07-01/resources/performance/review_owners/{id}` | Deletes a Review owner |
| `client.performance.reviewProcessCustomTemplates.list()` | `api.performance.review_process_custom_template.list` | GET | `/api/2026-07-01/resources/performance/review_process_custom_templates` | Reads all Review process custom templates |
| `client.performance.reviewProcessCustomTemplates.get({ path: { id } })` | `api.performance.review_process_custom_template.get(id:)` | GET | `/api/2026-07-01/resources/performance/review_process_custom_templates/{id}` | Reads a single Review process custom template |
| `client.performance.reviewProcessEstimatedTargets.list()` | `api.performance.review_process_estimated_target.list` | GET | `/api/2026-07-01/resources/performance/review_process_estimated_targets` | Reads all Review process estimated targets |
| `client.performance.reviewProcessTargets.list()` | `api.performance.review_process_target.list` | GET | `/api/2026-07-01/resources/performance/review_process_targets` | Reads all Review process targets |
| `client.performance.reviewProcessTargets.addPeers` | `api.performance.review_process_target.add_peers` | POST | `/api/2026-07-01/resources/performance/review_process_targets/add_peers` | Add peers a Review process target |
| `client.performance.reviewProcessTargets.bulkCreate` | `api.performance.review_process_target.bulk_create` | POST | `/api/2026-07-01/resources/performance/review_process_targets/bulk_create` | Bulk creates a Review process target |
| `client.performance.reviewProcessTargets.removePeerEvaluations` | `api.performance.review_process_target.remove_peer_evaluations` | POST | `/api/2026-07-01/resources/performance/review_process_targets/remove_peer_evaluations` | Remove peer evaluations a Review process target |
| `client.performance.reviewProcessTargets.delete({ path: { id } })` | `api.performance.review_process_target.delete(id:)` | DELETE | `/api/2026-07-01/resources/performance/review_process_targets/{id}` | Deletes a Review process target |
| `client.performance.reviewProcessTargets.get({ path: { id } })` | `api.performance.review_process_target.get(id:)` | GET | `/api/2026-07-01/resources/performance/review_process_targets/{id}` | Reads a single Review process target |
| `client.performance.reviewProcesses.list()` | `api.performance.review_process.list` | GET | `/api/2026-07-01/resources/performance/review_processes` | Reads all Review processes |
| `client.performance.reviewProcesses.create({ body })` | `api.performance.review_process.create` | POST | `/api/2026-07-01/resources/performance/review_processes` | Creates a Review process |
| `client.performance.reviewProcesses.createFromTemplate` | `api.performance.review_process.create_from_template` | POST | `/api/2026-07-01/resources/performance/review_processes/create_from_template` | Create from templates a Review process |
| `client.performance.reviewProcesses.duplicate` | `api.performance.review_process.duplicate` | POST | `/api/2026-07-01/resources/performance/review_processes/duplicate` | Duplicates a Review process |
| `client.performance.reviewProcesses.remindInBulk` | `api.performance.review_process.remind_in_bulk` | POST | `/api/2026-07-01/resources/performance/review_processes/remind_in_bulk` | Remind in bulks a Review process |
| `client.performance.reviewProcesses.removeSchedule` | `api.performance.review_process.remove_schedule` | POST | `/api/2026-07-01/resources/performance/review_processes/remove_schedule` | Remove schedules a Review process |
| `client.performance.reviewProcesses.reopen` | `api.performance.review_process.reopen` | POST | `/api/2026-07-01/resources/performance/review_processes/reopen` | Reopens a Review process |
| `client.performance.reviewProcesses.schedule` | `api.performance.review_process.schedule` | POST | `/api/2026-07-01/resources/performance/review_processes/schedule` | Schedules a Review process |
| `client.performance.reviewProcesses.start` | `api.performance.review_process.start` | POST | `/api/2026-07-01/resources/performance/review_processes/start` | Starts a Review process |
| `client.performance.reviewProcesses.stop` | `api.performance.review_process.stop` | POST | `/api/2026-07-01/resources/performance/review_processes/stop` | Stops a Review process |
| `client.performance.reviewProcesses.toggleArchive` | `api.performance.review_process.toggle_archive` | POST | `/api/2026-07-01/resources/performance/review_processes/toggle_archive` | Toggle archives a Review process |
| `client.performance.reviewProcesses.updateAgreementsConfiguration` | `api.performance.review_process.update_agreements_configuration` | POST | `/api/2026-07-01/resources/performance/review_processes/update_agreements_configuration` | Update agreements configurations a Review process |
| `client.performance.reviewProcesses.updateBasicInfo` | `api.performance.review_process.update_basic_info` | POST | `/api/2026-07-01/resources/performance/review_processes/update_basic_info` | Update basic infos a Review process |
| `client.performance.reviewProcesses.updateCompetenciesAssessmentsConfiguration` | `api.performance.review_process.update_competencies_assessments_configuration` | POST | `/api/2026-07-01/resources/performance/review_processes/update_competencies_assessments_configuration` | Update competencies assessments configurations a Review process |
| `client.performance.reviewProcesses.updateDeadline` | `api.performance.review_process.update_deadline` | POST | `/api/2026-07-01/resources/performance/review_processes/update_deadline` | Update deadlines a Review process |
| `client.performance.reviewProcesses.updateEmployeeScoreConfiguration` | `api.performance.review_process.update_employee_score_configuration` | POST | `/api/2026-07-01/resources/performance/review_processes/update_employee_score_configuration` | Update employee score configurations a Review process |
| `client.performance.reviewProcesses.updateReviewerStrategies` | `api.performance.review_process.update_reviewer_strategies` | POST | `/api/2026-07-01/resources/performance/review_processes/update_reviewer_strategies` | Update reviewer strategies a Review process |
| `client.performance.reviewProcesses.updateSchedule` | `api.performance.review_process.update_schedule` | POST | `/api/2026-07-01/resources/performance/review_processes/update_schedule` | Update schedules a Review process |
| `client.performance.reviewProcesses.updateTargetStrategy` | `api.performance.review_process.update_target_strategy` | POST | `/api/2026-07-01/resources/performance/review_processes/update_target_strategy` | Update target strategies a Review process |
| `client.performance.reviewProcesses.delete({ path: { id } })` | `api.performance.review_process.delete(id:)` | DELETE | `/api/2026-07-01/resources/performance/review_processes/{id}` | Deletes a Review process |
| `client.performance.reviewProcesses.get({ path: { id } })` | `api.performance.review_process.get(id:)` | GET | `/api/2026-07-01/resources/performance/review_processes/{id}` | Reads a single Review process |
| `client.performance.reviewQuestionnaireByStrategies.list()` | `api.performance.review_questionnaire_by_strategy.list` | GET | `/api/2026-07-01/resources/performance/review_questionnaire_by_strategies` | Reads all Review questionnaire by strategies |
| `client.performance.reviewQuestionnaireByStrategies.updateDefaultRatingScale` | `api.performance.review_questionnaire_by_strategy.update_default_rating_scale` | POST | `/api/2026-07-01/resources/performance/review_questionnaire_by_strategies/update_default_rating_scale` | Update default rating scales a Review questionnaire by strategy |
| `client.performance.reviewQuestionnaireByStrategies.updateQuestionnaireForStrategy` | `api.performance.review_questionnaire_by_strategy.update_questionnaire_for_strategy` | POST | `/api/2026-07-01/resources/performance/review_questionnaire_by_strategies/update_questionnaire_for_strategy` | Update questionnaire for strategies a Review questionnaire by strategy |
| `client.performance.reviewQuestionnaireByStrategies.get({ path: { id } })` | `api.performance.review_questionnaire_by_strategy.get(id:)` | GET | `/api/2026-07-01/resources/performance/review_questionnaire_by_strategies/{id}` | Reads a single Review questionnaire by strategy |
| `client.performance.reviewVisibilitySettings.list()` | `api.performance.review_visibility_setting.list` | GET | `/api/2026-07-01/resources/performance/review_visibility_settings` | Reads all Review visibility settings |
| `client.performance.reviewVisibilitySettings.update({ path: { id }, body })` | `api.performance.review_visibility_setting.update(id:)` | PUT | `/api/2026-07-01/resources/performance/review_visibility_settings/{id}` | Updates a Review visibility setting |
| `client.performance.targetManagers.list()` | `api.performance.target_manager.list(performance_review_process_ids:)` | GET | `/api/2026-07-01/resources/performance/target_managers` | Reads all Target managers |
| `client.performance.targetManagers.get({ path: { id } })` | `api.performance.target_manager.get(id:)` | GET | `/api/2026-07-01/resources/performance/target_managers/{id}` | Reads a single Target manager |

## posts

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.posts.comments.list()` | `api.posts.comment.list(post_ids:)` | GET | `/api/2026-07-01/resources/posts/comments` | Reads all Comments |
| `client.posts.comments.create({ body })` | `api.posts.comment.create` | POST | `/api/2026-07-01/resources/posts/comments` | Creates a Comment |
| `client.posts.comments.delete({ path: { id } })` | `api.posts.comment.delete(id:)` | DELETE | `/api/2026-07-01/resources/posts/comments/{id}` | Deletes a Comment |
| `client.posts.comments.get({ path: { id } })` | `api.posts.comment.get(id:)` | GET | `/api/2026-07-01/resources/posts/comments/{id}` | Reads a single Comment |
| `client.posts.comments.update({ path: { id }, body })` | `api.posts.comment.update(id:)` | PUT | `/api/2026-07-01/resources/posts/comments/{id}` | Updates a Comment |
| `client.posts.groups.list()` | `api.posts.group.list` | GET | `/api/2026-07-01/resources/posts/groups` | Reads all Groups |
| `client.posts.groups.create({ body })` | `api.posts.group.create` | POST | `/api/2026-07-01/resources/posts/groups` | Creates a Group |
| `client.posts.groups.archive` | `api.posts.group.archive` | POST | `/api/2026-07-01/resources/posts/groups/archive` | Archives a Group |
| `client.posts.groups.delete({ path: { id } })` | `api.posts.group.delete(id:)` | DELETE | `/api/2026-07-01/resources/posts/groups/{id}` | Deletes a Group |
| `client.posts.groups.get({ path: { id } })` | `api.posts.group.get(id:)` | GET | `/api/2026-07-01/resources/posts/groups/{id}` | Reads a single Group |
| `client.posts.groups.update({ path: { id }, body })` | `api.posts.group.update(id:)` | PUT | `/api/2026-07-01/resources/posts/groups/{id}` | Updates a Group |
| `client.posts.posts.list()` | `api.posts.post.list` | GET | `/api/2026-07-01/resources/posts/posts` | Reads all Posts |
| `client.posts.posts.create({ body })` | `api.posts.post.create` | POST | `/api/2026-07-01/resources/posts/posts` | Creates a Post |
| `client.posts.posts.delete({ path: { id } })` | `api.posts.post.delete(id:)` | DELETE | `/api/2026-07-01/resources/posts/posts/{id}` | Deletes a Post |
| `client.posts.posts.get({ path: { id } })` | `api.posts.post.get(id:)` | GET | `/api/2026-07-01/resources/posts/posts/{id}` | Reads a single Post |
| `client.posts.posts.update({ path: { id }, body })` | `api.posts.post.update(id:)` | PUT | `/api/2026-07-01/resources/posts/posts/{id}` | Updates a Post |

## procurement

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.procurement.purchaseOrders.list()` | `api.procurement.purchase_order.list` | GET | `/api/2026-07-01/resources/procurement/purchase_orders` | Reads all Purchase orders |
| `client.procurement.purchaseOrders.get({ path: { id } })` | `api.procurement.purchase_order.get(id:)` | GET | `/api/2026-07-01/resources/procurement/purchase_orders/{id}` | Reads a single Purchase order |
| `client.procurement.purchaseRequests.list()` | `api.procurement.purchase_request.list` | GET | `/api/2026-07-01/resources/procurement/purchase_requests` | Reads all Purchase requests |
| `client.procurement.purchaseRequests.get({ path: { id } })` | `api.procurement.purchase_request.get(id:)` | GET | `/api/2026-07-01/resources/procurement/purchase_requests/{id}` | Reads a single Purchase request |
| `client.procurement.types.list()` | `api.procurement.type.list` | GET | `/api/2026-07-01/resources/procurement/types` | Reads all Types |
| `client.procurement.types.get({ path: { id } })` | `api.procurement.type.get(id:)` | GET | `/api/2026-07-01/resources/procurement/types/{id}` | Reads a single Type |

## project_management

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.projectManagement.budgetStrategies.list()` | `api.project_management.budget_strategy.list` | GET | `/api/2026-07-01/resources/project_management/budget_strategies` | Reads all Budget strategies |
| `client.projectManagement.budgetStrategies.create({ body })` | `api.project_management.budget_strategy.create` | POST | `/api/2026-07-01/resources/project_management/budget_strategies` | Creates a Budget strategy |
| `client.projectManagement.budgetStrategies.delete({ path: { id } })` | `api.project_management.budget_strategy.delete(id:)` | DELETE | `/api/2026-07-01/resources/project_management/budget_strategies/{id}` | Deletes a Budget strategy |
| `client.projectManagement.budgetStrategies.get({ path: { id } })` | `api.project_management.budget_strategy.get(id:)` | GET | `/api/2026-07-01/resources/project_management/budget_strategies/{id}` | Reads a single Budget strategy |
| `client.projectManagement.budgetStrategies.update({ path: { id }, body })` | `api.project_management.budget_strategy.update(id:)` | PUT | `/api/2026-07-01/resources/project_management/budget_strategies/{id}` | Updates a Budget strategy |
| `client.projectManagement.expenseRecords.list()` | `api.project_management.expense_record.list` | GET | `/api/2026-07-01/resources/project_management/expense_records` | Reads all Expense records |
| `client.projectManagement.expenseRecords.get({ path: { id } })` | `api.project_management.expense_record.get(id:)` | GET | `/api/2026-07-01/resources/project_management/expense_records/{id}` | Reads a single Expense record |
| `client.projectManagement.exportableExpenses.list()` | `api.project_management.exportable_expense.list(start_date:, end_date:, project_ids:)` | GET | `/api/2026-07-01/resources/project_management/exportable_expenses` | Reads all Exportable expenses |
| `client.projectManagement.imputableProjects.list()` | `api.project_management.imputable_project.list` | GET | `/api/2026-07-01/resources/project_management/imputable_projects` | Reads all Imputable projects |
| `client.projectManagement.imputableProjects.get({ path: { id } })` | `api.project_management.imputable_project.get(id:)` | GET | `/api/2026-07-01/resources/project_management/imputable_projects/{id}` | Reads a single Imputable project |
| `client.projectManagement.plannedRecords.list()` | `api.project_management.planned_record.list` | GET | `/api/2026-07-01/resources/project_management/planned_records` | Reads all Planned records |
| `client.projectManagement.plannedRecords.bulkCreate` | `api.project_management.planned_record.bulk_create` | POST | `/api/2026-07-01/resources/project_management/planned_records/bulk_create` | Bulk creates a Planned record |
| `client.projectManagement.plannedRecords.delete({ path: { id } })` | `api.project_management.planned_record.delete(id:)` | DELETE | `/api/2026-07-01/resources/project_management/planned_records/{id}` | Deletes a Planned record |
| `client.projectManagement.plannedRecords.get({ path: { id } })` | `api.project_management.planned_record.get(id:)` | GET | `/api/2026-07-01/resources/project_management/planned_records/{id}` | Reads a single Planned record |
| `client.projectManagement.plannedRecords.update({ path: { id }, body })` | `api.project_management.planned_record.update(id:)` | PUT | `/api/2026-07-01/resources/project_management/planned_records/{id}` | Updates a Planned record |
| `client.projectManagement.projectTasks.list()` | `api.project_management.project_task.list(ids:, project_ids:, subproject_ids:, completed:, overdue:, search:, due_status:, client_ids:)` | GET | `/api/2026-07-01/resources/project_management/project_tasks` | Reads all Project tasks |
| `client.projectManagement.projectTasks.create({ body })` | `api.project_management.project_task.create(name:, project_id:, status:)` | POST | `/api/2026-07-01/resources/project_management/project_tasks` | Creates a Project task |
| `client.projectManagement.projectTasks.bulkDestroy` | `api.project_management.project_task.bulk_destroy` | POST | `/api/2026-07-01/resources/project_management/project_tasks/bulk_destroy` | Bulk destroys a Project task |
| `client.projectManagement.projectTasks.bulkDuplicate` | `api.project_management.project_task.bulk_duplicate` | POST | `/api/2026-07-01/resources/project_management/project_tasks/bulk_duplicate` | Bulk duplicates a Project task |
| `client.projectManagement.projectTasks.get({ path: { id } })` | `api.project_management.project_task.get(id:)` | GET | `/api/2026-07-01/resources/project_management/project_tasks/{id}` | Reads a single Project task |
| `client.projectManagement.projectTasks.update({ path: { id }, body })` | `api.project_management.project_task.update(id:, id2:, name:, project_id:)` | PUT | `/api/2026-07-01/resources/project_management/project_tasks/{id}` | Updates a Project task |
| `client.projectManagement.projectWorkers.list()` | `api.project_management.project_worker.list` | GET | `/api/2026-07-01/resources/project_management/project_workers` | Reads all Project workers |
| `client.projectManagement.projectWorkers.create({ body })` | `api.project_management.project_worker.create` | POST | `/api/2026-07-01/resources/project_management/project_workers` | Creates a Project worker |
| `client.projectManagement.projectWorkers.bulkAssign` | `api.project_management.project_worker.bulk_assign` | POST | `/api/2026-07-01/resources/project_management/project_workers/bulk_assign` | Bulk assigns a Project worker |
| `client.projectManagement.projectWorkers.bulkCreate` | `api.project_management.project_worker.bulk_create` | POST | `/api/2026-07-01/resources/project_management/project_workers/bulk_create` | Bulk creates a Project worker |
| `client.projectManagement.projectWorkers.unassign` | `api.project_management.project_worker.unassign` | POST | `/api/2026-07-01/resources/project_management/project_workers/unassign` | Unassigns a Project worker |
| `client.projectManagement.projectWorkers.get({ path: { id } })` | `api.project_management.project_worker.get(id:)` | GET | `/api/2026-07-01/resources/project_management/project_workers/{id}` | Reads a single Project worker |
| `client.projectManagement.projects.list()` | `api.project_management.project.list(include_inputed_minutes:)` | GET | `/api/2026-07-01/resources/project_management/projects` | Reads all Projects |
| `client.projectManagement.projects.create({ body })` | `api.project_management.project.create` | POST | `/api/2026-07-01/resources/project_management/projects` | Creates a Project |
| `client.projectManagement.projects.activate` | `api.project_management.project.activate` | POST | `/api/2026-07-01/resources/project_management/projects/activate` | Activates a Project |
| `client.projectManagement.projects.changeAssignment` | `api.project_management.project.change_assignment` | POST | `/api/2026-07-01/resources/project_management/projects/change_assignment` | Change assignments a Project |
| `client.projectManagement.projects.changeStatus` | `api.project_management.project.change_status` | POST | `/api/2026-07-01/resources/project_management/projects/change_status` | Change statuses a Project |
| `client.projectManagement.projects.close` | `api.project_management.project.close` | POST | `/api/2026-07-01/resources/project_management/projects/close` | Closes a Project |
| `client.projectManagement.projects.softDelete` | `api.project_management.project.soft_delete` | POST | `/api/2026-07-01/resources/project_management/projects/soft_delete` | Soft deletes a Project |
| `client.projectManagement.projects.get({ path: { id } })` | `api.project_management.project.get(id:)` | GET | `/api/2026-07-01/resources/project_management/projects/{id}` | Reads a single Project |
| `client.projectManagement.projects.update({ path: { id }, body })` | `api.project_management.project.update(id:)` | PUT | `/api/2026-07-01/resources/project_management/projects/{id}` | Updates a Project |
| `client.projectManagement.subprojects.list()` | `api.project_management.subproject.list` | GET | `/api/2026-07-01/resources/project_management/subprojects` | Reads all Subprojects |
| `client.projectManagement.subprojects.create({ body })` | `api.project_management.subproject.create` | POST | `/api/2026-07-01/resources/project_management/subprojects` | Creates a Subproject |
| `client.projectManagement.subprojects.rename` | `api.project_management.subproject.rename` | POST | `/api/2026-07-01/resources/project_management/subprojects/rename` | Renames a Subproject |
| `client.projectManagement.subprojects.delete({ path: { id } })` | `api.project_management.subproject.delete(id:)` | DELETE | `/api/2026-07-01/resources/project_management/subprojects/{id}` | Deletes a Subproject |
| `client.projectManagement.subprojects.get({ path: { id } })` | `api.project_management.subproject.get(id:)` | GET | `/api/2026-07-01/resources/project_management/subprojects/{id}` | Reads a single Subproject |
| `client.projectManagement.subprojects.update({ path: { id }, body })` | `api.project_management.subproject.update(id:)` | PUT | `/api/2026-07-01/resources/project_management/subprojects/{id}` | Updates a Subproject |
| `client.projectManagement.timeRecords.list()` | `api.project_management.time_record.list` | GET | `/api/2026-07-01/resources/project_management/time_records` | Reads all Time records |
| `client.projectManagement.timeRecords.create({ body })` | `api.project_management.time_record.create` | POST | `/api/2026-07-01/resources/project_management/time_records` | Creates a Time record |
| `client.projectManagement.timeRecords.bulkDelete` | `api.project_management.time_record.bulk_delete` | POST | `/api/2026-07-01/resources/project_management/time_records/bulk_delete` | Bulk deletes a Time record |
| `client.projectManagement.timeRecords.bulkProcess` | `api.project_management.time_record.bulk_process` | POST | `/api/2026-07-01/resources/project_management/time_records/bulk_process` | Bulk processes a Time record |
| `client.projectManagement.timeRecords.updateProjectWorker` | `api.project_management.time_record.update_project_worker` | POST | `/api/2026-07-01/resources/project_management/time_records/update_project_worker` | Update project workers a Time record |
| `client.projectManagement.timeRecords.delete({ path: { id } })` | `api.project_management.time_record.delete(id:)` | DELETE | `/api/2026-07-01/resources/project_management/time_records/{id}` | Deletes a Time record |
| `client.projectManagement.timeRecords.get({ path: { id } })` | `api.project_management.time_record.get(id:)` | GET | `/api/2026-07-01/resources/project_management/time_records/{id}` | Reads a single Time record |

## shift_management

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.shiftManagement.shifts.list()` | `api.shift_management.shift.list` | GET | `/api/2026-07-01/resources/shift_management/shifts` | Reads all Shifts |
| `client.shiftManagement.shifts.create({ body })` | `api.shift_management.shift.create` | POST | `/api/2026-07-01/resources/shift_management/shifts` | Creates a Shift |
| `client.shiftManagement.shifts.bulkCreate` | `api.shift_management.shift.bulk_create` | POST | `/api/2026-07-01/resources/shift_management/shifts/bulk_create` | Bulk creates a Shift |
| `client.shiftManagement.shifts.bulkDelete` | `api.shift_management.shift.bulk_delete` | POST | `/api/2026-07-01/resources/shift_management/shifts/bulk_delete` | Bulk deletes a Shift |
| `client.shiftManagement.shifts.delete({ path: { id } })` | `api.shift_management.shift.delete(id:)` | DELETE | `/api/2026-07-01/resources/shift_management/shifts/{id}` | Deletes a Shift |
| `client.shiftManagement.shifts.get({ path: { id } })` | `api.shift_management.shift.get(id:)` | GET | `/api/2026-07-01/resources/shift_management/shifts/{id}` | Reads a single Shift |

## tasks

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.tasks.taskFiles.list()` | `api.tasks.task_file.list(task_id:)` | GET | `/api/2026-07-01/resources/tasks/task_files` | Reads all Task files |
| `client.tasks.taskFiles.create({ body })` | `api.tasks.task_file.create(task_id:, file:)` | POST | `/api/2026-07-01/resources/tasks/task_files` | Creates a Task file |
| `client.tasks.taskFiles.delete({ path: { id } })` | `api.tasks.task_file.delete(id:)` | DELETE | `/api/2026-07-01/resources/tasks/task_files/{id}` | Deletes a Task file |
| `client.tasks.taskFiles.get({ path: { id } })` | `api.tasks.task_file.get(id:)` | GET | `/api/2026-07-01/resources/tasks/task_files/{id}` | Reads a single Task file |
| `client.tasks.tasks.list()` | `api.tasks.task.list` | GET | `/api/2026-07-01/resources/tasks/tasks` | Reads all Tasks |
| `client.tasks.tasks.create({ body })` | `api.tasks.task.create` | POST | `/api/2026-07-01/resources/tasks/tasks` | Creates a Task |
| `client.tasks.tasks.bulkCreate` | `api.tasks.task.bulk_create` | POST | `/api/2026-07-01/resources/tasks/tasks/bulk_create` | Bulk creates a Task |
| `client.tasks.tasks.bulkDelete` | `api.tasks.task.bulk_delete` | POST | `/api/2026-07-01/resources/tasks/tasks/bulk_delete` | Bulk deletes a Task |
| `client.tasks.tasks.bulkUpdate` | `api.tasks.task.bulk_update` | POST | `/api/2026-07-01/resources/tasks/tasks/bulk_update` | Bulk updates a Task |
| `client.tasks.tasks.copy` | `api.tasks.task.copy` | POST | `/api/2026-07-01/resources/tasks/tasks/copy` | Copies a Task |
| `client.tasks.tasks.createComment` | `api.tasks.task.create_comment` | POST | `/api/2026-07-01/resources/tasks/tasks/create_comment` | Create comments a Task |
| `client.tasks.tasks.delete({ path: { id } })` | `api.tasks.task.delete(id:)` | DELETE | `/api/2026-07-01/resources/tasks/tasks/{id}` | Deletes a Task |
| `client.tasks.tasks.get({ path: { id } })` | `api.tasks.task.get(id:)` | GET | `/api/2026-07-01/resources/tasks/tasks/{id}` | Reads a single Task |
| `client.tasks.tasks.update({ path: { id }, body })` | `api.tasks.task.update(id:)` | PUT | `/api/2026-07-01/resources/tasks/tasks/{id}` | Updates a Task |

## teams

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.teams.memberships.list()` | `api.teams.membership.list` | GET | `/api/2026-07-01/resources/teams/memberships` | Reads all Memberships |
| `client.teams.memberships.create({ body })` | `api.teams.membership.create` | POST | `/api/2026-07-01/resources/teams/memberships` | Creates a Membership |
| `client.teams.memberships.delete({ path: { id } })` | `api.teams.membership.delete(id:)` | DELETE | `/api/2026-07-01/resources/teams/memberships/{id}` | Deletes a Membership |
| `client.teams.memberships.get({ path: { id } })` | `api.teams.membership.get(id:)` | GET | `/api/2026-07-01/resources/teams/memberships/{id}` | Reads a single Membership |
| `client.teams.memberships.update({ path: { id }, body })` | `api.teams.membership.update(id:)` | PUT | `/api/2026-07-01/resources/teams/memberships/{id}` | Updates a Membership |
| `client.teams.teams.list()` | `api.teams.team.list` | GET | `/api/2026-07-01/resources/teams/teams` | Reads all Teams |
| `client.teams.teams.create({ body })` | `api.teams.team.create` | POST | `/api/2026-07-01/resources/teams/teams` | Creates a Team |
| `client.teams.teams.delete({ path: { id } })` | `api.teams.team.delete(id:)` | DELETE | `/api/2026-07-01/resources/teams/teams/{id}` | Deletes a Team |
| `client.teams.teams.get({ path: { id } })` | `api.teams.team.get(id:)` | GET | `/api/2026-07-01/resources/teams/teams/{id}` | Reads a single Team |
| `client.teams.teams.update({ path: { id }, body })` | `api.teams.team.update(id:)` | PUT | `/api/2026-07-01/resources/teams/teams/{id}` | Updates a Team |

## time_planning

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.timePlanning.plannedBreaks.list()` | `api.time_planning.planned_break.list(ids:, paid:, default_shift_ids:, shift_ids:, day_configuration_ids:, shift_configuration_ids:, active_break_configuration:)` | GET | `/api/2026-07-01/resources/time_planning/planned_breaks` | Reads all Planned breaks |
| `client.timePlanning.plannedBreaks.bulkCreate` | `api.time_planning.planned_break.bulk_create` | POST | `/api/2026-07-01/resources/time_planning/planned_breaks/bulk_create` | Bulk creates a Planned break |
| `client.timePlanning.plannedBreaks.get({ path: { id } })` | `api.time_planning.planned_break.get(id:)` | GET | `/api/2026-07-01/resources/time_planning/planned_breaks/{id}` | Reads a single Planned break |
| `client.timePlanning.planningVersions.list()` | `api.time_planning.planning_version.list(only_active:)` | GET | `/api/2026-07-01/resources/time_planning/planning_versions` | Reads all Planning versions |
| `client.timePlanning.planningVersions.create({ body })` | `api.time_planning.planning_version.create` | POST | `/api/2026-07-01/resources/time_planning/planning_versions` | Creates a Planning version |
| `client.timePlanning.planningVersions.bulkCreate` | `api.time_planning.planning_version.bulk_create` | POST | `/api/2026-07-01/resources/time_planning/planning_versions/bulk_create` | Bulk creates a Planning version |
| `client.timePlanning.planningVersions.delete({ path: { id } })` | `api.time_planning.planning_version.delete(id:)` | DELETE | `/api/2026-07-01/resources/time_planning/planning_versions/{id}` | Deletes a Planning version |
| `client.timePlanning.planningVersions.update({ path: { id }, body })` | `api.time_planning.planning_version.update(id:)` | PUT | `/api/2026-07-01/resources/time_planning/planning_versions/{id}` | Updates a Planning version |

## time_settings

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.timeSettings.breakConfigurations.list()` | `api.time_settings.break_configuration.list(active:)` | GET | `/api/2026-07-01/resources/time_settings/break_configurations` | Reads all Break configurations |
| `client.timeSettings.breakConfigurations.create({ body })` | `api.time_settings.break_configuration.create` | POST | `/api/2026-07-01/resources/time_settings/break_configurations` | Creates a Break configuration |
| `client.timeSettings.breakConfigurations.get({ path: { id } })` | `api.time_settings.break_configuration.get(id:)` | GET | `/api/2026-07-01/resources/time_settings/break_configurations/{id}` | Reads a single Break configuration |
| `client.timeSettings.breakConfigurations.update({ path: { id }, body })` | `api.time_settings.break_configuration.update(id:)` | PUT | `/api/2026-07-01/resources/time_settings/break_configurations/{id}` | Updates a Break configuration |

## timeoff

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.timeoff.allowanceIncidences.list()` | `api.timeoff.allowance_incidence.list` | GET | `/api/2026-07-01/resources/timeoff/allowance_incidences` | Reads all Allowance incidences |
| `client.timeoff.allowanceIncidences.create({ body })` | `api.timeoff.allowance_incidence.create` | POST | `/api/2026-07-01/resources/timeoff/allowance_incidences` | Creates an Allowance incidence |
| `client.timeoff.allowanceIncidences.delete({ path: { id } })` | `api.timeoff.allowance_incidence.delete(id:)` | DELETE | `/api/2026-07-01/resources/timeoff/allowance_incidences/{id}` | Deletes an Allowance incidence |
| `client.timeoff.allowanceIncidences.get({ path: { id } })` | `api.timeoff.allowance_incidence.get(id:)` | GET | `/api/2026-07-01/resources/timeoff/allowance_incidences/{id}` | Reads a single Allowance incidence |
| `client.timeoff.allowanceIncidences.update({ path: { id }, body })` | `api.timeoff.allowance_incidence.update(id:)` | PUT | `/api/2026-07-01/resources/timeoff/allowance_incidences/{id}` | Updates an Allowance incidence |
| `client.timeoff.allowanceStats.list()` | `api.timeoff.allowance_stat.list` | GET | `/api/2026-07-01/resources/timeoff/allowance_stats` | Reads all Allowance stats |
| `client.timeoff.allowanceStats.get({ path: { id } })` | `api.timeoff.allowance_stat.get(id:)` | GET | `/api/2026-07-01/resources/timeoff/allowance_stats/{id}` | Reads a single Allowance stat |
| `client.timeoff.allowances.list()` | `api.timeoff.allowance.list` | GET | `/api/2026-07-01/resources/timeoff/allowances` | Reads all Allowances |
| `client.timeoff.allowances.create({ body })` | `api.timeoff.allowance.create` | POST | `/api/2026-07-01/resources/timeoff/allowances` | Creates an Allowance |
| `client.timeoff.allowances.deleteWithAltAllowance` | `api.timeoff.allowance.delete_with_alt_allowance` | POST | `/api/2026-07-01/resources/timeoff/allowances/delete_with_alt_allowance` | Delete with alt allowances an Allowance |
| `client.timeoff.allowances.delete({ path: { id } })` | `api.timeoff.allowance.delete(id:)` | DELETE | `/api/2026-07-01/resources/timeoff/allowances/{id}` | Deletes an Allowance |
| `client.timeoff.allowances.get({ path: { id } })` | `api.timeoff.allowance.get(id:)` | GET | `/api/2026-07-01/resources/timeoff/allowances/{id}` | Reads a single Allowance |
| `client.timeoff.allowances.update({ path: { id }, body })` | `api.timeoff.allowance.update(id:)` | PUT | `/api/2026-07-01/resources/timeoff/allowances/{id}` | Updates an Allowance |
| `client.timeoff.blockedPeriods.list()` | `api.timeoff.blocked_period.list` | GET | `/api/2026-07-01/resources/timeoff/blocked_periods` | Reads all Blocked periods |
| `client.timeoff.blockedPeriods.create({ body })` | `api.timeoff.blocked_period.create` | POST | `/api/2026-07-01/resources/timeoff/blocked_periods` | Creates a Blocked period |
| `client.timeoff.blockedPeriods.delete({ path: { id } })` | `api.timeoff.blocked_period.delete(id:)` | DELETE | `/api/2026-07-01/resources/timeoff/blocked_periods/{id}` | Deletes a Blocked period |
| `client.timeoff.blockedPeriods.get({ path: { id } })` | `api.timeoff.blocked_period.get(id:)` | GET | `/api/2026-07-01/resources/timeoff/blocked_periods/{id}` | Reads a single Blocked period |
| `client.timeoff.blockedPeriods.update({ path: { id }, body })` | `api.timeoff.blocked_period.update(id:)` | PUT | `/api/2026-07-01/resources/timeoff/blocked_periods/{id}` | Updates a Blocked period |
| `client.timeoff.leaveTypes.list()` | `api.timeoff.leave_type.list` | GET | `/api/2026-07-01/resources/timeoff/leave_types` | Reads all Leave types |
| `client.timeoff.leaveTypes.create({ body })` | `api.timeoff.leave_type.create` | POST | `/api/2026-07-01/resources/timeoff/leave_types` | Creates a Leave type |
| `client.timeoff.leaveTypes.get({ path: { id } })` | `api.timeoff.leave_type.get(id:)` | GET | `/api/2026-07-01/resources/timeoff/leave_types/{id}` | Reads a single Leave type |
| `client.timeoff.leaveTypes.update({ path: { id }, body })` | `api.timeoff.leave_type.update(id:)` | PUT | `/api/2026-07-01/resources/timeoff/leave_types/{id}` | Updates a Leave type |
| `client.timeoff.leaves.list()` | `api.timeoff.leave.list(include_deleted_leaves:)` | GET | `/api/2026-07-01/resources/timeoff/leaves` | Reads all Leaves |
| `client.timeoff.leaves.create({ body })` | `api.timeoff.leave.create` | POST | `/api/2026-07-01/resources/timeoff/leaves` | Creates a Leave |
| `client.timeoff.leaves.approve` | `api.timeoff.leave.approve` | POST | `/api/2026-07-01/resources/timeoff/leaves/approve` | Approves a Leave |
| `client.timeoff.leaves.approveAll` | `api.timeoff.leave.approve_all` | POST | `/api/2026-07-01/resources/timeoff/leaves/approve_all` | Approve alls a Leave |
| `client.timeoff.leaves.reject` | `api.timeoff.leave.reject` | POST | `/api/2026-07-01/resources/timeoff/leaves/reject` | Rejects a Leave |
| `client.timeoff.leaves.delete({ path: { id } })` | `api.timeoff.leave.delete(id:)` | DELETE | `/api/2026-07-01/resources/timeoff/leaves/{id}` | Deletes a Leave |
| `client.timeoff.leaves.get({ path: { id } })` | `api.timeoff.leave.get(id:)` | GET | `/api/2026-07-01/resources/timeoff/leaves/{id}` | Reads a single Leave |
| `client.timeoff.leaves.update({ path: { id }, body })` | `api.timeoff.leave.update(id:)` | PUT | `/api/2026-07-01/resources/timeoff/leaves/{id}` | Updates a Leave |
| `client.timeoff.policies.list()` | `api.timeoff.policy.list` | GET | `/api/2026-07-01/resources/timeoff/policies` | Reads all Policies |
| `client.timeoff.policies.create({ body })` | `api.timeoff.policy.create` | POST | `/api/2026-07-01/resources/timeoff/policies` | Creates a Policy |
| `client.timeoff.policies.delete({ path: { id } })` | `api.timeoff.policy.delete(id:)` | DELETE | `/api/2026-07-01/resources/timeoff/policies/{id}` | Deletes a Policy |
| `client.timeoff.policies.get({ path: { id } })` | `api.timeoff.policy.get(id:)` | GET | `/api/2026-07-01/resources/timeoff/policies/{id}` | Reads a single Policy |
| `client.timeoff.policies.update({ path: { id }, body })` | `api.timeoff.policy.update(id:)` | PUT | `/api/2026-07-01/resources/timeoff/policies/{id}` | Updates a Policy |
| `client.timeoff.policyAssignments.list()` | `api.timeoff.policy_assignment.list` | GET | `/api/2026-07-01/resources/timeoff/policy_assignments` | Reads all Policy assignments |
| `client.timeoff.policyAssignments.create({ body })` | `api.timeoff.policy_assignment.create` | POST | `/api/2026-07-01/resources/timeoff/policy_assignments` | Creates a Policy assignment |
| `client.timeoff.policyAssignments.delete({ path: { id } })` | `api.timeoff.policy_assignment.delete(id:)` | DELETE | `/api/2026-07-01/resources/timeoff/policy_assignments/{id}` | Deletes a Policy assignment |
| `client.timeoff.policyAssignments.get({ path: { id } })` | `api.timeoff.policy_assignment.get(id:)` | GET | `/api/2026-07-01/resources/timeoff/policy_assignments/{id}` | Reads a single Policy assignment |
| `client.timeoff.policyAssignments.update({ path: { id }, body })` | `api.timeoff.policy_assignment.update(id:)` | PUT | `/api/2026-07-01/resources/timeoff/policy_assignments/{id}` | Updates a Policy assignment |
| `client.timeoff.policyTimelines.list()` | `api.timeoff.policy_timeline.list(employee_id:, reference_date:)` | GET | `/api/2026-07-01/resources/timeoff/policy_timelines` | Reads all Policy timelines |

## trainings

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.trainings.categories.list()` | `api.trainings.category.list` | GET | `/api/2026-07-01/resources/trainings/categories` | Reads all Categories |
| `client.trainings.categories.create({ body })` | `api.trainings.category.create` | POST | `/api/2026-07-01/resources/trainings/categories` | Creates a Category |
| `client.trainings.categories.delete({ path: { id } })` | `api.trainings.category.delete(id:)` | DELETE | `/api/2026-07-01/resources/trainings/categories/{id}` | Deletes a Category |
| `client.trainings.categories.get({ path: { id } })` | `api.trainings.category.get(id:)` | GET | `/api/2026-07-01/resources/trainings/categories/{id}` | Reads a single Category |
| `client.trainings.sessionAccessMemberships.list()` | `api.trainings.session_access_membership.list(session_id:)` | GET | `/api/2026-07-01/resources/trainings/session_access_memberships` | Reads all Session access memberships |
| `client.trainings.sessionAccessMemberships.bulkCreate` | `api.trainings.session_access_membership.bulk_create` | POST | `/api/2026-07-01/resources/trainings/session_access_memberships/bulk_create` | Bulk creates a Session access membership |
| `client.trainings.sessionAccessMemberships.bulkDestroy` | `api.trainings.session_access_membership.bulk_destroy` | POST | `/api/2026-07-01/resources/trainings/session_access_memberships/bulk_destroy` | Bulk destroys a Session access membership |
| `client.trainings.sessionAccessMemberships.get({ path: { id } })` | `api.trainings.session_access_membership.get(id:)` | GET | `/api/2026-07-01/resources/trainings/session_access_memberships/{id}` | Reads a single Session access membership |
| `client.trainings.sessionAttendances.list()` | `api.trainings.session_attendance.list` | GET | `/api/2026-07-01/resources/trainings/session_attendances` | Reads all Session attendances |
| `client.trainings.sessionAttendances.bulkUpdate` | `api.trainings.session_attendance.bulk_update` | POST | `/api/2026-07-01/resources/trainings/session_attendances/bulk_update` | Bulk update session attendances |
| `client.trainings.sessionAttendances.get({ path: { id } })` | `api.trainings.session_attendance.get(id:)` | GET | `/api/2026-07-01/resources/trainings/session_attendances/{id}` | Reads a single Session attendance |
| `client.trainings.sessions.list()` | `api.trainings.session.list` | GET | `/api/2026-07-01/resources/trainings/sessions` | Reads all Sessions |
| `client.trainings.sessions.create({ body })` | `api.trainings.session.create` | POST | `/api/2026-07-01/resources/trainings/sessions` | Create a new training session |
| `client.trainings.sessions.delete({ path: { id } })` | `api.trainings.session.delete(id:)` | DELETE | `/api/2026-07-01/resources/trainings/sessions/{id}` | Deletes a Session |
| `client.trainings.sessions.get({ path: { id } })` | `api.trainings.session.get(id:)` | GET | `/api/2026-07-01/resources/trainings/sessions/{id}` | Reads a single Session |
| `client.trainings.sessions.update({ path: { id }, body })` | `api.trainings.session.update(id:)` | PUT | `/api/2026-07-01/resources/trainings/sessions/{id}` | Update training session |
| `client.trainings.trainingClasses.list()` | `api.trainings.training_class.list` | GET | `/api/2026-07-01/resources/trainings/training_classes` | Reads all Training classes |
| `client.trainings.trainingClasses.create({ body })` | `api.trainings.training_class.create` | POST | `/api/2026-07-01/resources/trainings/training_classes` | Creates a Training class |
| `client.trainings.trainingClasses.delete({ path: { id } })` | `api.trainings.training_class.delete(id:)` | DELETE | `/api/2026-07-01/resources/trainings/training_classes/{id}` | Deletes a Training class |
| `client.trainings.trainingClasses.get({ path: { id } })` | `api.trainings.training_class.get(id:)` | GET | `/api/2026-07-01/resources/trainings/training_classes/{id}` | Reads a single Training class |
| `client.trainings.trainingClasses.update({ path: { id }, body })` | `api.trainings.training_class.update(id:)` | PUT | `/api/2026-07-01/resources/trainings/training_classes/{id}` | Updates a Training class |
| `client.trainings.trainingMemberships.list()` | `api.trainings.training_membership.list(due_date:)` | GET | `/api/2026-07-01/resources/trainings/training_memberships` | Reads all Training memberships |
| `client.trainings.trainingMemberships.bulkCreate` | `api.trainings.training_membership.bulk_create` | POST | `/api/2026-07-01/resources/trainings/training_memberships/bulk_create` | Bulk creates a Training membership |
| `client.trainings.trainingMemberships.bulkDestroy` | `api.trainings.training_membership.bulk_destroy` | POST | `/api/2026-07-01/resources/trainings/training_memberships/bulk_destroy` | Bulk destroys a Training membership |
| `client.trainings.trainingMemberships.get({ path: { id } })` | `api.trainings.training_membership.get(id:)` | GET | `/api/2026-07-01/resources/trainings/training_memberships/{id}` | Reads a single Training membership |
| `client.trainings.trainingMemberships.update({ path: { id }, body })` | `api.trainings.training_membership.update(id:)` | PUT | `/api/2026-07-01/resources/trainings/training_memberships/{id}` | Updates a Training membership |
| `client.trainings.trainings.list()` | `api.trainings.training.list` | GET | `/api/2026-07-01/resources/trainings/trainings` | Reads all Trainings |
| `client.trainings.trainings.create({ body })` | `api.trainings.training.create` | POST | `/api/2026-07-01/resources/trainings/trainings` | Creates a Training |
| `client.trainings.trainings.bulkDelete` | `api.trainings.training.bulk_delete` | POST | `/api/2026-07-01/resources/trainings/trainings/bulk_delete` | Bulk deletes a Training |
| `client.trainings.trainings.bulkUpdateCatalog` | `api.trainings.training.bulk_update_catalog` | POST | `/api/2026-07-01/resources/trainings/trainings/bulk_update_catalog` | Bulk update catalogs a Training |
| `client.trainings.trainings.updateStatus` | `api.trainings.training.update_status` | POST | `/api/2026-07-01/resources/trainings/trainings/update_status` | Update statuses a Training |
| `client.trainings.trainings.delete({ path: { id } })` | `api.trainings.training.delete(id:)` | DELETE | `/api/2026-07-01/resources/trainings/trainings/{id}` | Deletes a Training |
| `client.trainings.trainings.get({ path: { id } })` | `api.trainings.training.get(id:)` | GET | `/api/2026-07-01/resources/trainings/trainings/{id}` | Reads a single Training |
| `client.trainings.trainings.update({ path: { id }, body })` | `api.trainings.training.update(id:)` | PUT | `/api/2026-07-01/resources/trainings/trainings/{id}` | Updates a Training |

## work_schedule

| SDK call (TS) | Ruby | HTTP | path | summary |
| --- | --- | --- | --- | --- |
| `client.workSchedule.dayConfigurations.list()` | `api.work_schedule.day_configuration.list` | GET | `/api/2026-07-01/resources/work_schedule/day_configurations` | Reads all Day configurations |
| `client.workSchedule.dayConfigurations.bulkCud` | `api.work_schedule.day_configuration.bulk_cud` | POST | `/api/2026-07-01/resources/work_schedule/day_configurations/bulk_cud` | Bulk cuds a Day configuration |
| `client.workSchedule.dayConfigurations.get({ path: { id } })` | `api.work_schedule.day_configuration.get(id:)` | GET | `/api/2026-07-01/resources/work_schedule/day_configurations/{id}` | Reads a single Day configuration |
| `client.workSchedule.overlapPeriods.list()` | `api.work_schedule.overlap_period.list` | GET | `/api/2026-07-01/resources/work_schedule/overlap_periods` | Reads all Overlap periods |
| `client.workSchedule.overlapPeriods.create({ body })` | `api.work_schedule.overlap_period.create` | POST | `/api/2026-07-01/resources/work_schedule/overlap_periods` | Creates an Overlap period |
| `client.workSchedule.overlapPeriods.delete({ path: { id } })` | `api.work_schedule.overlap_period.delete(id:)` | DELETE | `/api/2026-07-01/resources/work_schedule/overlap_periods/{id}` | Deletes an Overlap period |
| `client.workSchedule.overlapPeriods.get({ path: { id } })` | `api.work_schedule.overlap_period.get(id:)` | GET | `/api/2026-07-01/resources/work_schedule/overlap_periods/{id}` | Reads a single Overlap period |
| `client.workSchedule.overlapPeriods.update({ path: { id }, body })` | `api.work_schedule.overlap_period.update(id:)` | PUT | `/api/2026-07-01/resources/work_schedule/overlap_periods/{id}` | Updates an Overlap period |
| `client.workSchedule.schedules.list()` | `api.work_schedule.schedule.list(with_employee_ids:, with_periods:)` | GET | `/api/2026-07-01/resources/work_schedule/schedules` | Reads all Schedules |
| `client.workSchedule.schedules.create({ body })` | `api.work_schedule.schedule.create` | POST | `/api/2026-07-01/resources/work_schedule/schedules` | Creates a Schedule |
| `client.workSchedule.schedules.toggleArchive` | `api.work_schedule.schedule.toggle_archive` | POST | `/api/2026-07-01/resources/work_schedule/schedules/toggle_archive` | Toggle archives a Schedule |
| `client.workSchedule.schedules.get({ path: { id } })` | `api.work_schedule.schedule.get(id:)` | GET | `/api/2026-07-01/resources/work_schedule/schedules/{id}` | Reads a single Schedule |
| `client.workSchedule.schedules.update({ path: { id }, body })` | `api.work_schedule.schedule.update(id:)` | PUT | `/api/2026-07-01/resources/work_schedule/schedules/{id}` | Updates a Schedule |
