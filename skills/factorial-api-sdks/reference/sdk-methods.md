# Factorial API endpoints → SDK calls

Auto-generated from the OpenAPI spec. 550 endpoints across 37 namespaces.

The SDK call column shows the **TypeScript** accessor and request shape (`client.<namespace>.<resource>.<method>({ path, query, body })`). The Python SDK uses the same namespaces/resources in `snake_case` (and `collect_all()` instead of `all()`), but takes the path id positionally: `get(id)`, `update(id, body=...)`. `body` contents are endpoint-specific; see the [online reference](https://apidoc.factorialhr.com/reference) for exact fields.

## api_public

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.apiPublic.credentials.list()` | GET | `/api/2026-07-01/resources/api_public/credentials` | Reads all Credentials |
| `client.apiPublic.webhookSubscriptions.list()` | GET | `/api/2026-07-01/resources/api_public/webhook_subscriptions` | Reads all Webhook subscriptions |
| `client.apiPublic.webhookSubscriptions.create({ body })` | POST | `/api/2026-07-01/resources/api_public/webhook_subscriptions` | Creates a Webhook subscription |
| `client.apiPublic.webhookSubscriptions.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/api_public/webhook_subscriptions/{id}` | Deletes a Webhook subscription |
| `client.apiPublic.webhookSubscriptions.get({ path: { id } })` | GET | `/api/2026-07-01/resources/api_public/webhook_subscriptions/{id}` | Reads a single Webhook subscription |
| `client.apiPublic.webhookSubscriptions.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/api_public/webhook_subscriptions/{id}` | Updates a Webhook subscription |

## approvals

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.approvals.materializedApprovalsFlows.approveResource` | POST | `/api/2026-07-01/resources/approvals/materialized_approvals_flows/approve_resource` | Approves an approval flow by resource |
| `client.approvals.materializedApprovalsFlows.rejectResource` | POST | `/api/2026-07-01/resources/approvals/materialized_approvals_flows/reject_resource` | Rejects an approval flow by resource |

## ats

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.ats.answers.list()` | GET | `/api/2026-07-01/resources/ats/answers` | Reads all Answers |
| `client.ats.answers.create({ body })` | POST | `/api/2026-07-01/resources/ats/answers` | Creates an Answer |
| `client.ats.answers.get({ path: { id } })` | GET | `/api/2026-07-01/resources/ats/answers/{id}` | Reads a single Answer |
| `client.ats.applicationPhases.list()` | GET | `/api/2026-07-01/resources/ats/application_phases` | Reads all Application phases |
| `client.ats.applicationPhases.get({ path: { id } })` | GET | `/api/2026-07-01/resources/ats/application_phases/{id}` | Reads a single Application phase |
| `client.ats.applications.list()` | GET | `/api/2026-07-01/resources/ats/applications` | Reads all Applications |
| `client.ats.applications.create({ body })` | POST | `/api/2026-07-01/resources/ats/applications` | Creates an Application |
| `client.ats.applications.apply` | POST | `/api/2026-07-01/resources/ats/applications/apply` | Applies an Application |
| `client.ats.applications.moveToPhase` | POST | `/api/2026-07-01/resources/ats/applications/move_to_phase` | Move to phases an Application |
| `client.ats.applications.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/ats/applications/{id}` | Deletes an Application |
| `client.ats.applications.get({ path: { id } })` | GET | `/api/2026-07-01/resources/ats/applications/{id}` | Reads a single Application |
| `client.ats.applications.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/ats/applications/{id}` | Updates an Application |
| `client.ats.candidateSources.list()` | GET | `/api/2026-07-01/resources/ats/candidate_sources` | Reads all Candidate sources |
| `client.ats.candidateSources.get({ path: { id } })` | GET | `/api/2026-07-01/resources/ats/candidate_sources/{id}` | Reads a single Candidate source |
| `client.ats.candidates.list()` | GET | `/api/2026-07-01/resources/ats/candidates` | Reads all Candidates |
| `client.ats.candidates.create({ body })` | POST | `/api/2026-07-01/resources/ats/candidates` | Creates a Candidate |
| `client.ats.candidates.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/ats/candidates/{id}` | Deletes a Candidate |
| `client.ats.candidates.get({ path: { id } })` | GET | `/api/2026-07-01/resources/ats/candidates/{id}` | Reads a single Candidate |
| `client.ats.candidates.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/ats/candidates/{id}` | Updates a Candidate |
| `client.ats.evaluationForms.list()` | GET | `/api/2026-07-01/resources/ats/evaluation_forms` | Reads all Evaluation forms |
| `client.ats.evaluationForms.saveAsTemplate` | POST | `/api/2026-07-01/resources/ats/evaluation_forms/save_as_template` | Save as templates an Evaluation form |
| `client.ats.evaluationForms.get({ path: { id } })` | GET | `/api/2026-07-01/resources/ats/evaluation_forms/{id}` | Reads a single Evaluation form |
| `client.ats.feedbacks.list()` | GET | `/api/2026-07-01/resources/ats/feedbacks` | Reads all Feedbacks |
| `client.ats.feedbacks.create({ body })` | POST | `/api/2026-07-01/resources/ats/feedbacks` | Creates a Feedback |
| `client.ats.feedbacks.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/ats/feedbacks/{id}` | Deletes a Feedback |
| `client.ats.feedbacks.get({ path: { id } })` | GET | `/api/2026-07-01/resources/ats/feedbacks/{id}` | Reads a single Feedback |
| `client.ats.feedbacks.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/ats/feedbacks/{id}` | Updates a Feedback |
| `client.ats.hiringStages.list()` | GET | `/api/2026-07-01/resources/ats/hiring_stages` | Reads all Hiring stages |
| `client.ats.hiringStages.get({ path: { id } })` | GET | `/api/2026-07-01/resources/ats/hiring_stages/{id}` | Reads a single Hiring stage |
| `client.ats.jobPostings.list()` | GET | `/api/2026-07-01/resources/ats/job_postings` | Reads all Job postings |
| `client.ats.jobPostings.create({ body })` | POST | `/api/2026-07-01/resources/ats/job_postings` | Creates a Job posting |
| `client.ats.jobPostings.duplicate` | POST | `/api/2026-07-01/resources/ats/job_postings/duplicate` | Duplicates a Job posting |
| `client.ats.jobPostings.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/ats/job_postings/{id}` | Deletes a Job posting |
| `client.ats.jobPostings.get({ path: { id } })` | GET | `/api/2026-07-01/resources/ats/job_postings/{id}` | Reads a single Job posting |
| `client.ats.jobPostings.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/ats/job_postings/{id}` | Updates a Job posting |
| `client.ats.messages.list()` | GET | `/api/2026-07-01/resources/ats/messages` | Reads all Messages |
| `client.ats.messages.create({ body })` | POST | `/api/2026-07-01/resources/ats/messages` | Creates a Message |
| `client.ats.messages.get({ path: { id } })` | GET | `/api/2026-07-01/resources/ats/messages/{id}` | Reads a single Message |
| `client.ats.questions.list()` | GET | `/api/2026-07-01/resources/ats/questions` | Reads all Questions |
| `client.ats.questions.create({ body })` | POST | `/api/2026-07-01/resources/ats/questions` | Creates a Question |
| `client.ats.questions.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/ats/questions/{id}` | Deletes a Question |
| `client.ats.questions.get({ path: { id } })` | GET | `/api/2026-07-01/resources/ats/questions/{id}` | Reads a single Question |
| `client.ats.questions.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/ats/questions/{id}` | Updates a Question |
| `client.ats.rejectionReasons.list()` | GET | `/api/2026-07-01/resources/ats/rejection_reasons` | Reads all Rejection reasons |
| `client.ats.rejectionReasons.get({ path: { id } })` | GET | `/api/2026-07-01/resources/ats/rejection_reasons/{id}` | Reads a single Rejection reason |

## attendance

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.attendance.breakConfigurations.list()` | GET | `/api/2026-07-01/resources/attendance/break_configurations` | Reads all Break configurations |
| `client.attendance.breakConfigurations.create({ body })` | POST | `/api/2026-07-01/resources/attendance/break_configurations` | Creates a Break configuration |
| `client.attendance.breakConfigurations.get({ path: { id } })` | GET | `/api/2026-07-01/resources/attendance/break_configurations/{id}` | Reads a single Break configuration |
| `client.attendance.breakConfigurations.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/attendance/break_configurations/{id}` | Updates a Break configuration |
| `client.attendance.editTimesheetRequests.list()` | GET | `/api/2026-07-01/resources/attendance/edit_timesheet_requests` | Reads all Edit timesheet requests |
| `client.attendance.editTimesheetRequests.create({ body })` | POST | `/api/2026-07-01/resources/attendance/edit_timesheet_requests` | Creates an Edit timesheet request |
| `client.attendance.editTimesheetRequests.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/attendance/edit_timesheet_requests/{id}` | Deletes an Edit timesheet request |
| `client.attendance.editTimesheetRequests.get({ path: { id } })` | GET | `/api/2026-07-01/resources/attendance/edit_timesheet_requests/{id}` | Reads all Edit timesheet requests |
| `client.attendance.editTimesheetRequests.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/attendance/edit_timesheet_requests/{id}` | Updates an Edit timesheet request |
| `client.attendance.estimatedTimes.list()` | GET | `/api/2026-07-01/resources/attendance/estimated_times` | Reads all Estimated times |
| `client.attendance.openShifts.list()` | GET | `/api/2026-07-01/resources/attendance/open_shifts` | Reads all Open shifts |
| `client.attendance.overtimeRequests.list()` | GET | `/api/2026-07-01/resources/attendance/overtime_requests` | Reads all Overtime requests |
| `client.attendance.overtimeRequests.create({ body })` | POST | `/api/2026-07-01/resources/attendance/overtime_requests` | Creates an Overtime request |
| `client.attendance.overtimeRequests.approve` | POST | `/api/2026-07-01/resources/attendance/overtime_requests/approve` | Approves an Overtime request |
| `client.attendance.overtimeRequests.reject` | POST | `/api/2026-07-01/resources/attendance/overtime_requests/reject` | Rejects an Overtime request |
| `client.attendance.overtimeRequests.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/attendance/overtime_requests/{id}` | Deletes an Overtime request |
| `client.attendance.overtimeRequests.get({ path: { id } })` | GET | `/api/2026-07-01/resources/attendance/overtime_requests/{id}` | Reads a single Overtime request |
| `client.attendance.overtimeRequests.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/attendance/overtime_requests/{id}` | Updates an Overtime request |
| `client.attendance.reviews.list()` | GET | `/api/2026-07-01/resources/attendance/reviews` | Reads all Reviews |
| `client.attendance.reviews.bulkCreate` | POST | `/api/2026-07-01/resources/attendance/reviews/bulk_create` | Bulk creates a Review |
| `client.attendance.reviews.bulkDestroy` | POST | `/api/2026-07-01/resources/attendance/reviews/bulk_destroy` | Bulk destroys a Review |
| `client.attendance.shifts.list()` | GET | `/api/2026-07-01/resources/attendance/shifts` | Reads all Shifts |
| `client.attendance.shifts.create({ body })` | POST | `/api/2026-07-01/resources/attendance/shifts` | Creates a shift |
| `client.attendance.shifts.autofill` | POST | `/api/2026-07-01/resources/attendance/shifts/autofill` | Autofills a Shift |
| `client.attendance.shifts.breakEnd` | POST | `/api/2026-07-01/resources/attendance/shifts/break_end` | Break ends a Shift |
| `client.attendance.shifts.breakStart` | POST | `/api/2026-07-01/resources/attendance/shifts/break_start` | Break starts a Shift |
| `client.attendance.shifts.clockIn` | POST | `/api/2026-07-01/resources/attendance/shifts/clock_in` | Clocks in a shift |
| `client.attendance.shifts.clockOut` | POST | `/api/2026-07-01/resources/attendance/shifts/clock_out` | Clocks out a shift |
| `client.attendance.shifts.toggleClock` | POST | `/api/2026-07-01/resources/attendance/shifts/toggle_clock` | Clock in/out a shift |
| `client.attendance.shifts.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/attendance/shifts/{id}` | Deletes a Shift |
| `client.attendance.shifts.get({ path: { id } })` | GET | `/api/2026-07-01/resources/attendance/shifts/{id}` | Reads a single Shift |
| `client.attendance.shifts.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/attendance/shifts/{id}` | Updates a Shift |
| `client.attendance.workedTimes.list()` | GET | `/api/2026-07-01/resources/attendance/worked_times` | Reads all Worked times |

## banking

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.banking.bankAccounts.list()` | GET | `/api/2026-07-01/resources/banking/bank_accounts` | Reads all Bank accounts |
| `client.banking.bankAccounts.createManual` | POST | `/api/2026-07-01/resources/banking/bank_accounts/create_manual` | Create manuals a Bank account |
| `client.banking.bankAccounts.get({ path: { id } })` | GET | `/api/2026-07-01/resources/banking/bank_accounts/{id}` | Reads a single Bank account |
| `client.banking.cardPayments.list()` | GET | `/api/2026-07-01/resources/banking/card_payments` | Reads all Card payments |
| `client.banking.cardPayments.get({ path: { id } })` | GET | `/api/2026-07-01/resources/banking/card_payments/{id}` | Reads a single Card payment |
| `client.banking.transactions.list()` | GET | `/api/2026-07-01/resources/banking/transactions` | Reads all Transactions |
| `client.banking.transactions.get({ path: { id } })` | GET | `/api/2026-07-01/resources/banking/transactions/{id}` | Reads a single Transaction |

## bookkeepers_management

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.bookkeepersManagement.incidences.list()` | GET | `/api/2026-07-01/resources/bookkeepers_management/incidences` | Reads all Incidences |
| `client.bookkeepersManagement.incidences.get({ path: { id } })` | GET | `/api/2026-07-01/resources/bookkeepers_management/incidences/{id}` | Reads a single Incidence |
| `client.bookkeepersManagement.incidences.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/bookkeepers_management/incidences/{id}` | Updates an Incidence |

## companies

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.companies.legalEntities.list()` | GET | `/api/2026-07-01/resources/companies/legal_entities` | Reads all Legal entities |
| `client.companies.legalEntities.create({ body })` | POST | `/api/2026-07-01/resources/companies/legal_entities` | Creates a Legal entity |
| `client.companies.legalEntities.get({ path: { id } })` | GET | `/api/2026-07-01/resources/companies/legal_entities/{id}` | Reads a single Legal entity |

## compensations

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.compensations.concepts.list()` | GET | `/api/2026-07-01/resources/compensations/concepts` | Reads all Concepts |
| `client.compensations.concepts.get({ path: { id } })` | GET | `/api/2026-07-01/resources/compensations/concepts/{id}` | Reads a single Concept |

## contracts

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.contracts.compensations.list()` | GET | `/api/2026-07-01/resources/contracts/compensations` | Reads all Compensations |
| `client.contracts.compensations.create({ body })` | POST | `/api/2026-07-01/resources/contracts/compensations` | Creates a Compensation |
| `client.contracts.compensations.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/contracts/compensations/{id}` | Deletes a Compensation |
| `client.contracts.compensations.get({ path: { id } })` | GET | `/api/2026-07-01/resources/contracts/compensations/{id}` | Reads a single Compensation |
| `client.contracts.compensations.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/contracts/compensations/{id}` | Updates a Compensation |
| `client.contracts.contractTemplates.list()` | GET | `/api/2026-07-01/resources/contracts/contract_templates` | Reads all Contract templates |
| `client.contracts.contractTemplates.get({ path: { id } })` | GET | `/api/2026-07-01/resources/contracts/contract_templates/{id}` | Reads a single Contract template |
| `client.contracts.contractVersionHistories.list()` | GET | `/api/2026-07-01/resources/contracts/contract_version_histories` | Reads all Contract version histories |
| `client.contracts.contractVersionHistories.get({ path: { id } })` | GET | `/api/2026-07-01/resources/contracts/contract_version_histories/{id}` | Reads a single Contract version history |
| `client.contracts.contractVersionMetaData.list()` | GET | `/api/2026-07-01/resources/contracts/contract_version_meta_data` | Reads all Contract version meta data |
| `client.contracts.contractVersions.list()` | GET | `/api/2026-07-01/resources/contracts/contract_versions` | Reads all Contract versions |
| `client.contracts.contractVersions.create({ body })` | POST | `/api/2026-07-01/resources/contracts/contract_versions` | Creates a Contract version |
| `client.contracts.contractVersions.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/contracts/contract_versions/{id}` | Deletes a Contract version |
| `client.contracts.contractVersions.get({ path: { id } })` | GET | `/api/2026-07-01/resources/contracts/contract_versions/{id}` | Reads a single Contract version |
| `client.contracts.contractVersions.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/contracts/contract_versions/{id}` | Updates a Contract version |
| `client.contracts.frenchContractTypes.list()` | GET | `/api/2026-07-01/resources/contracts/french_contract_types` | Reads all French contract types |
| `client.contracts.frenchContractTypes.get({ path: { id } })` | GET | `/api/2026-07-01/resources/contracts/french_contract_types/{id}` | Reads a single French contract type |
| `client.contracts.germanContractTypes.list()` | GET | `/api/2026-07-01/resources/contracts/german_contract_types` | Reads all German contract types |
| `client.contracts.germanContractTypes.get({ path: { id } })` | GET | `/api/2026-07-01/resources/contracts/german_contract_types/{id}` | Reads a single German contract type |
| `client.contracts.materializedTemplates.list()` | GET | `/api/2026-07-01/resources/contracts/materialized_templates` | Reads all Materialized templates |
| `client.contracts.portugueseContractTypes.list()` | GET | `/api/2026-07-01/resources/contracts/portuguese_contract_types` | Reads all Portuguese contract types |
| `client.contracts.portugueseContractTypes.get({ path: { id } })` | GET | `/api/2026-07-01/resources/contracts/portuguese_contract_types/{id}` | Reads a single Portuguese contract type |
| `client.contracts.referenceContracts.list()` | GET | `/api/2026-07-01/resources/contracts/reference_contracts` | Reads all Reference contracts |
| `client.contracts.spanishContractTypes.list()` | GET | `/api/2026-07-01/resources/contracts/spanish_contract_types` | Reads all Spanish contract types |
| `client.contracts.spanishContractTypes.create({ body })` | POST | `/api/2026-07-01/resources/contracts/spanish_contract_types` | Creates a Spanish contract type |
| `client.contracts.spanishContractTypes.get({ path: { id } })` | GET | `/api/2026-07-01/resources/contracts/spanish_contract_types/{id}` | Reads a single Spanish contract type |
| `client.contracts.spanishEducationLevels.list()` | GET | `/api/2026-07-01/resources/contracts/spanish_education_levels` | Reads all Spanish education levels |
| `client.contracts.spanishEducationLevels.create({ body })` | POST | `/api/2026-07-01/resources/contracts/spanish_education_levels` | Creates a Spanish education level |
| `client.contracts.spanishEducationLevels.get({ path: { id } })` | GET | `/api/2026-07-01/resources/contracts/spanish_education_levels/{id}` | Reads a single Spanish education level |
| `client.contracts.spanishProfessionalCategories.list()` | GET | `/api/2026-07-01/resources/contracts/spanish_professional_categories` | Reads all Spanish professional categories |
| `client.contracts.spanishProfessionalCategories.create({ body })` | POST | `/api/2026-07-01/resources/contracts/spanish_professional_categories` | Creates a Spanish professional category |
| `client.contracts.spanishProfessionalCategories.get({ path: { id } })` | GET | `/api/2026-07-01/resources/contracts/spanish_professional_categories/{id}` | Reads a single Spanish professional category |
| `client.contracts.spanishWorkingDayTypes.list()` | GET | `/api/2026-07-01/resources/contracts/spanish_working_day_types` | Reads all Spanish working day types |
| `client.contracts.spanishWorkingDayTypes.create({ body })` | POST | `/api/2026-07-01/resources/contracts/spanish_working_day_types` | Creates a Spanish working day type |
| `client.contracts.spanishWorkingDayTypes.get({ path: { id } })` | GET | `/api/2026-07-01/resources/contracts/spanish_working_day_types/{id}` | Reads a single Spanish working day type |
| `client.contracts.taxonomies.list()` | GET | `/api/2026-07-01/resources/contracts/taxonomies` | Reads all Taxonomies |
| `client.contracts.taxonomies.get({ path: { id } })` | GET | `/api/2026-07-01/resources/contracts/taxonomies/{id}` | Reads a single Taxonomy |

## custom_fields

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.customFields.fields.list()` | GET | `/api/2026-07-01/resources/custom_fields/fields` | Reads all Fields |
| `client.customFields.fields.create({ body })` | POST | `/api/2026-07-01/resources/custom_fields/fields` | Creates a Field |
| `client.customFields.fields.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/custom_fields/fields/{id}` | Deletes a Field |
| `client.customFields.fields.get({ path: { id } })` | GET | `/api/2026-07-01/resources/custom_fields/fields/{id}` | Reads a single Field |
| `client.customFields.options.list()` | GET | `/api/2026-07-01/resources/custom_fields/options` | Reads all Options |
| `client.customFields.options.create({ body })` | POST | `/api/2026-07-01/resources/custom_fields/options` | Creates an Option |
| `client.customFields.options.get({ path: { id } })` | GET | `/api/2026-07-01/resources/custom_fields/options/{id}` | Reads a single Option |
| `client.customFields.resourceFields.list()` | GET | `/api/2026-07-01/resources/custom_fields/resource_fields` | Reads all Resource fields |
| `client.customFields.resourceFields.create({ body })` | POST | `/api/2026-07-01/resources/custom_fields/resource_fields` | Creates a Resource field |
| `client.customFields.resourceFields.get({ path: { id } })` | GET | `/api/2026-07-01/resources/custom_fields/resource_fields/{id}` | Reads a single Resource field |
| `client.customFields.values.list()` | GET | `/api/2026-07-01/resources/custom_fields/values` | Reads all Values |
| `client.customFields.values.create({ body })` | POST | `/api/2026-07-01/resources/custom_fields/values` | Creates a Value |
| `client.customFields.values.get({ path: { id } })` | GET | `/api/2026-07-01/resources/custom_fields/values/{id}` | Reads a single Value |
| `client.customFields.values.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/custom_fields/values/{id}` | Updates a Value |

## custom_resources

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.customResources.resources.list()` | GET | `/api/2026-07-01/resources/custom_resources/resources` | Reads all Resources |
| `client.customResources.resources.get({ path: { id } })` | GET | `/api/2026-07-01/resources/custom_resources/resources/{id}` | Reads a single Resource |
| `client.customResources.schemas.list()` | GET | `/api/2026-07-01/resources/custom_resources/schemas` | Reads all Schemas |
| `client.customResources.schemas.create({ body })` | POST | `/api/2026-07-01/resources/custom_resources/schemas` | Creates a Schema |
| `client.customResources.schemas.get({ path: { id } })` | GET | `/api/2026-07-01/resources/custom_resources/schemas/{id}` | Reads a single Schema |
| `client.customResources.values.list()` | GET | `/api/2026-07-01/resources/custom_resources/values` | Reads all Values |
| `client.customResources.values.create({ body })` | POST | `/api/2026-07-01/resources/custom_resources/values` | Creates a Value |
| `client.customResources.values.get({ path: { id } })` | GET | `/api/2026-07-01/resources/custom_resources/values/{id}` | Reads a single Value |

## documents

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.documents.documents.list()` | GET | `/api/2026-07-01/resources/documents/documents` | Reads all Documents |
| `client.documents.documents.create({ body })` | POST | `/api/2026-07-01/resources/documents/documents` | Creates a Document |
| `client.documents.documents.moveToTrashBin` | POST | `/api/2026-07-01/resources/documents/documents/move_to_trash_bin` | Move to trash bins a Document |
| `client.documents.documents.restoreFromTrashBin` | POST | `/api/2026-07-01/resources/documents/documents/restore_from_trash_bin` | Restore from trash bins a Document |
| `client.documents.documents.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/documents/documents/{id}` | Deletes a Document |
| `client.documents.documents.get({ path: { id } })` | GET | `/api/2026-07-01/resources/documents/documents/{id}` | Reads a single Document |
| `client.documents.documents.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/documents/documents/{id}` | Updates a Document |
| `client.documents.downloadUrls.bulkCreate` | POST | `/api/2026-07-01/resources/documents/download_urls/bulk_create` | Bulk creates a Download url |
| `client.documents.folders.list()` | GET | `/api/2026-07-01/resources/documents/folders` | Reads all Folders |
| `client.documents.folders.create({ body })` | POST | `/api/2026-07-01/resources/documents/folders` | Creates a Folder |
| `client.documents.folders.get({ path: { id } })` | GET | `/api/2026-07-01/resources/documents/folders/{id}` | Reads a single Folder |
| `client.documents.folders.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/documents/folders/{id}` | Updates a Folder |

## employee_updates

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.employeeUpdates.absences.list()` | GET | `/api/2026-07-01/resources/employee_updates/absences` | Reads all Absences |
| `client.employeeUpdates.absences.get({ path: { id } })` | GET | `/api/2026-07-01/resources/employee_updates/absences/{id}` | Reads a single Absence |
| `client.employeeUpdates.contractChanges.list()` | GET | `/api/2026-07-01/resources/employee_updates/contract_changes` | Reads all Contract changes |
| `client.employeeUpdates.contractChanges.get({ path: { id } })` | GET | `/api/2026-07-01/resources/employee_updates/contract_changes/{id}` | Reads a single Contract change |
| `client.employeeUpdates.newHires.list()` | GET | `/api/2026-07-01/resources/employee_updates/new_hires` | Reads all New hires |
| `client.employeeUpdates.newHires.get({ path: { id } })` | GET | `/api/2026-07-01/resources/employee_updates/new_hires/{id}` | Reads a single New hire |
| `client.employeeUpdates.personalChanges.list()` | GET | `/api/2026-07-01/resources/employee_updates/personal_changes` | Reads all Personal changes |
| `client.employeeUpdates.personalChanges.get({ path: { id } })` | GET | `/api/2026-07-01/resources/employee_updates/personal_changes/{id}` | Reads a single Personal change |
| `client.employeeUpdates.summaries.list()` | GET | `/api/2026-07-01/resources/employee_updates/summaries` | Reads all Summaries |
| `client.employeeUpdates.summaries.get({ path: { id } })` | GET | `/api/2026-07-01/resources/employee_updates/summaries/{id}` | Reads a single Summary |
| `client.employeeUpdates.terminations.list()` | GET | `/api/2026-07-01/resources/employee_updates/terminations` | Reads all Terminations |
| `client.employeeUpdates.terminations.get({ path: { id } })` | GET | `/api/2026-07-01/resources/employee_updates/terminations/{id}` | Reads a single Termination |

## employees

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.employees.employees.list()` | GET | `/api/2026-07-01/resources/employees/employees` | Reads all Employees |
| `client.employees.employees.createWithContract` | POST | `/api/2026-07-01/resources/employees/employees/create_with_contract` | Create with contracts an Employee |
| `client.employees.employees.invite` | POST | `/api/2026-07-01/resources/employees/employees/invite` | Invites an Employee |
| `client.employees.employees.setRegularAccessStartDate` | POST | `/api/2026-07-01/resources/employees/employees/set_regular_access_start_date` | Set regular access start dates an Employee |
| `client.employees.employees.terminate` | POST | `/api/2026-07-01/resources/employees/employees/terminate` | Terminates an Employee |
| `client.employees.employees.unterminate` | POST | `/api/2026-07-01/resources/employees/employees/unterminate` | Unterminates an Employee |
| `client.employees.employees.get({ path: { id } })` | GET | `/api/2026-07-01/resources/employees/employees/{id}` | Reads a single Employee |
| `client.employees.employees.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/employees/employees/{id}` | Updates an Employee |

## expenses

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.expenses.expensables.list()` | GET | `/api/2026-07-01/resources/expenses/expensables` | Reads all Expensables |
| `client.expenses.expensables.bulkSetToPaid` | POST | `/api/2026-07-01/resources/expenses/expensables/bulk_set_to_paid` | Bulk set to paids an Expensable |
| `client.expenses.expensables.updateReimbursableAmount` | POST | `/api/2026-07-01/resources/expenses/expensables/update_reimbursable_amount` | Update reimbursable amount on an expensable |
| `client.expenses.expensables.get({ path: { id } })` | GET | `/api/2026-07-01/resources/expenses/expensables/{id}` | Reads a single Expensable |
| `client.expenses.expenses.list()` | GET | `/api/2026-07-01/resources/expenses/expenses` | Reads all Expenses |
| `client.expenses.expenses.get({ path: { id } })` | GET | `/api/2026-07-01/resources/expenses/expenses/{id}` | Reads a single Expense |
| `client.expenses.mileages.list()` | GET | `/api/2026-07-01/resources/expenses/mileages` | Reads all Mileages |
| `client.expenses.mileages.get({ path: { id } })` | GET | `/api/2026-07-01/resources/expenses/mileages/{id}` | Reads a single Mileage |
| `client.expenses.perDiems.list()` | GET | `/api/2026-07-01/resources/expenses/per_diems` | Reads all Per diems |
| `client.expenses.perDiems.get({ path: { id } })` | GET | `/api/2026-07-01/resources/expenses/per_diems/{id}` | Reads a single Per diem |

## finance

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.finance.accountingSettings.list()` | GET | `/api/2026-07-01/resources/finance/accounting_settings` | Reads all Accounting settings |
| `client.finance.accountingSettings.upsert` | POST | `/api/2026-07-01/resources/finance/accounting_settings/upsert` | Upserts an Accounting setting |
| `client.finance.accountingSettings.get({ path: { id } })` | GET | `/api/2026-07-01/resources/finance/accounting_settings/{id}` | Reads a single Accounting setting |
| `client.finance.accounts.list()` | GET | `/api/2026-07-01/resources/finance/accounts` | Reads all Accounts |
| `client.finance.accounts.create({ body })` | POST | `/api/2026-07-01/resources/finance/accounts` | Creates an Account |
| `client.finance.accounts.get({ path: { id } })` | GET | `/api/2026-07-01/resources/finance/accounts/{id}` | Reads a single Account |
| `client.finance.accounts.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/finance/accounts/{id}` | Updates an Account |
| `client.finance.budgetOptions.list()` | GET | `/api/2026-07-01/resources/finance/budget_options` | Reads all Budget options |
| `client.finance.budgetOptions.get({ path: { id } })` | GET | `/api/2026-07-01/resources/finance/budget_options/{id}` | Reads a single Budget option |
| `client.finance.categories.list()` | GET | `/api/2026-07-01/resources/finance/categories` | Reads all Categories |
| `client.finance.categories.get({ path: { id } })` | GET | `/api/2026-07-01/resources/finance/categories/{id}` | Reads a single Category |
| `client.finance.contacts.list()` | GET | `/api/2026-07-01/resources/finance/contacts` | Reads all Contacts |
| `client.finance.contacts.create({ body })` | POST | `/api/2026-07-01/resources/finance/contacts` | Creates a Contact |
| `client.finance.contacts.get({ path: { id } })` | GET | `/api/2026-07-01/resources/finance/contacts/{id}` | Reads a single Contact |
| `client.finance.contacts.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/finance/contacts/{id}` | Updates a Contact |
| `client.finance.costCenterMemberships.list()` | GET | `/api/2026-07-01/resources/finance/cost_center_memberships` | Reads all Cost center memberships |
| `client.finance.costCenterMemberships.bulkCreateUpdate` | POST | `/api/2026-07-01/resources/finance/cost_center_memberships/bulk_create_update` | Bulk create updates a Cost center membership |
| `client.finance.costCenters.list()` | GET | `/api/2026-07-01/resources/finance/cost_centers` | Reads all Cost centers |
| `client.finance.costCenters.create({ body })` | POST | `/api/2026-07-01/resources/finance/cost_centers` | Creates a Cost center |
| `client.finance.costCenters.edit` | POST | `/api/2026-07-01/resources/finance/cost_centers/edit` | Edits a Cost center |
| `client.finance.costCenters.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/finance/cost_centers/{id}` | Deletes a Cost center |
| `client.finance.costCenters.get({ path: { id } })` | GET | `/api/2026-07-01/resources/finance/cost_centers/{id}` | Reads a single Cost center |
| `client.finance.financialDocuments.list()` | GET | `/api/2026-07-01/resources/finance/financial_documents` | Reads all Financial documents |
| `client.finance.financialDocuments.get({ path: { id } })` | GET | `/api/2026-07-01/resources/finance/financial_documents/{id}` | Reads a single Financial document |
| `client.finance.journalEntries.list()` | GET | `/api/2026-07-01/resources/finance/journal_entries` | Reads all Journal entries |
| `client.finance.journalEntries.create({ body })` | POST | `/api/2026-07-01/resources/finance/journal_entries` | Creates a Journal entry |
| `client.finance.journalEntries.get({ path: { id } })` | GET | `/api/2026-07-01/resources/finance/journal_entries/{id}` | Reads a single Journal entry |
| `client.finance.journalLines.list()` | GET | `/api/2026-07-01/resources/finance/journal_lines` | Reads all Journal lines |
| `client.finance.journalLines.get({ path: { id } })` | GET | `/api/2026-07-01/resources/finance/journal_lines/{id}` | Reads a single Journal line |
| `client.finance.ledgerAccountResources.list()` | GET | `/api/2026-07-01/resources/finance/ledger_account_resources` | Reads all Ledger account resources |
| `client.finance.ledgerAccountResources.upsert` | POST | `/api/2026-07-01/resources/finance/ledger_account_resources/upsert` | Upserts a Ledger account resource |
| `client.finance.ledgerAccountResources.get({ path: { id } })` | GET | `/api/2026-07-01/resources/finance/ledger_account_resources/{id}` | Reads a single Ledger account resource |
| `client.finance.taxRates.list()` | GET | `/api/2026-07-01/resources/finance/tax_rates` | Reads all Tax rates |
| `client.finance.taxRates.create({ body })` | POST | `/api/2026-07-01/resources/finance/tax_rates` | Creates a Tax rate |
| `client.finance.taxRates.get({ path: { id } })` | GET | `/api/2026-07-01/resources/finance/tax_rates/{id}` | Reads a single Tax rate |
| `client.finance.taxRates.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/finance/tax_rates/{id}` | Updates a Tax rate |
| `client.finance.taxTypes.list()` | GET | `/api/2026-07-01/resources/finance/tax_types` | Reads all Tax types |
| `client.finance.taxTypes.create({ body })` | POST | `/api/2026-07-01/resources/finance/tax_types` | Creates a Tax type |
| `client.finance.taxTypes.get({ path: { id } })` | GET | `/api/2026-07-01/resources/finance/tax_types/{id}` | Reads a single Tax type |
| `client.finance.taxTypes.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/finance/tax_types/{id}` | Updates a Tax type |

## holidays

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.holidays.companyHolidays.list()` | GET | `/api/2026-07-01/resources/holidays/company_holidays` | Reads all Company holidays |
| `client.holidays.companyHolidays.get({ path: { id } })` | GET | `/api/2026-07-01/resources/holidays/company_holidays/{id}` | Reads a single Company holiday |

## integrations

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.integrations.syncRunOutputs.create({ body })` | POST | `/api/2026-07-01/resources/integrations/sync_run_outputs` | Creates a Sync run output |
| `client.integrations.syncableItems.list()` | GET | `/api/2026-07-01/resources/integrations/syncable_items` | Reads all Syncable items |
| `client.integrations.syncableSyncRuns.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/integrations/syncable_sync_runs/{id}` | Updates a Syncable sync run |

## it_management

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.itManagement.itAssetModels.list()` | GET | `/api/2026-07-01/resources/it_management/it_asset_models` | Reads all It asset models |
| `client.itManagement.itAssetModels.create({ body })` | POST | `/api/2026-07-01/resources/it_management/it_asset_models` | Creates an It asset model |
| `client.itManagement.itAssetModels.get({ path: { id } })` | GET | `/api/2026-07-01/resources/it_management/it_asset_models/{id}` | Reads a single It asset model |
| `client.itManagement.itAssetModels.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/it_management/it_asset_models/{id}` | Updates an It asset model |
| `client.itManagement.itAssets.list()` | GET | `/api/2026-07-01/resources/it_management/it_assets` | Reads all It assets |
| `client.itManagement.itAssets.create({ body })` | POST | `/api/2026-07-01/resources/it_management/it_assets` | Creates an It asset |
| `client.itManagement.itAssets.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/it_management/it_assets/{id}` | Deletes an It asset |
| `client.itManagement.itAssets.get({ path: { id } })` | GET | `/api/2026-07-01/resources/it_management/it_assets/{id}` | Reads a single It asset |
| `client.itManagement.itAssets.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/it_management/it_assets/{id}` | Updates an It asset |

## job_catalog

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.jobCatalog.levels.list()` | GET | `/api/2026-07-01/resources/job_catalog/levels` | Reads all Levels |
| `client.jobCatalog.levels.get({ path: { id } })` | GET | `/api/2026-07-01/resources/job_catalog/levels/{id}` | Reads a single Level |
| `client.jobCatalog.nodeAttributes.list()` | GET | `/api/2026-07-01/resources/job_catalog/node_attributes` | Reads all Node attributes |
| `client.jobCatalog.roles.list()` | GET | `/api/2026-07-01/resources/job_catalog/roles` | Reads all Roles |
| `client.jobCatalog.roles.get({ path: { id } })` | GET | `/api/2026-07-01/resources/job_catalog/roles/{id}` | Reads a single Role |
| `client.jobCatalog.treeNodes.list()` | GET | `/api/2026-07-01/resources/job_catalog/tree_nodes` | Reads all Tree nodes |

## locations

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.locations.locations.list()` | GET | `/api/2026-07-01/resources/locations/locations` | Reads all Locations |
| `client.locations.locations.create({ body })` | POST | `/api/2026-07-01/resources/locations/locations` | Creates a Location |
| `client.locations.locations.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/locations/locations/{id}` | Deletes a Location |
| `client.locations.locations.get({ path: { id } })` | GET | `/api/2026-07-01/resources/locations/locations/{id}` | Reads a single Location |
| `client.locations.locations.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/locations/locations/{id}` | Updates a Location |
| `client.locations.workAreas.list()` | GET | `/api/2026-07-01/resources/locations/work_areas` | Reads all Work areas |
| `client.locations.workAreas.create({ body })` | POST | `/api/2026-07-01/resources/locations/work_areas` | Creates a Work area |
| `client.locations.workAreas.archive` | POST | `/api/2026-07-01/resources/locations/work_areas/archive` | Archives a Work area |
| `client.locations.workAreas.unarchive` | POST | `/api/2026-07-01/resources/locations/work_areas/unarchive` | Unarchives a Work area |
| `client.locations.workAreas.get({ path: { id } })` | GET | `/api/2026-07-01/resources/locations/work_areas/{id}` | Reads a single Work area |
| `client.locations.workAreas.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/locations/work_areas/{id}` | Updates a Work area |

## marketplace

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.marketplace.installationSettings.list()` | GET | `/api/2026-07-01/resources/marketplace/installation_settings` | Reads all Installation settings |
| `client.marketplace.installations.create({ body })` | POST | `/api/2026-07-01/resources/marketplace/installations` | Creates an Installation |

## payroll

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.payroll.familySituations.list()` | GET | `/api/2026-07-01/resources/payroll/family_situations` | Reads all Family situations |
| `client.payroll.familySituations.create({ body })` | POST | `/api/2026-07-01/resources/payroll/family_situations` | Creates a Family situation |
| `client.payroll.familySituations.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/payroll/family_situations/{id}` | Updates a Family situation |
| `client.payroll.policyPeriods.changeStatus` | POST | `/api/2026-07-01/resources/payroll/policy_periods/change_status` | Change statuses a Policy period |
| `client.payroll.supplements.list()` | GET | `/api/2026-07-01/resources/payroll/supplements` | Reads all Supplements |
| `client.payroll.supplements.create({ body })` | POST | `/api/2026-07-01/resources/payroll/supplements` | Creates a Supplement |
| `client.payroll.supplements.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/payroll/supplements/{id}` | Deletes a Supplement |
| `client.payroll.supplements.get({ path: { id } })` | GET | `/api/2026-07-01/resources/payroll/supplements/{id}` | Reads a single Supplement |
| `client.payroll.supplements.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/payroll/supplements/{id}` | Updates a Supplement |

## payroll_employees

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.payrollEmployees.identifiers.list()` | GET | `/api/2026-07-01/resources/payroll_employees/identifiers` | Reads all Identifiers |
| `client.payrollEmployees.identifiers.create({ body })` | POST | `/api/2026-07-01/resources/payroll_employees/identifiers` | Creates an Identifier |
| `client.payrollEmployees.identifiers.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/payroll_employees/identifiers/{id}` | Deletes an Identifier |
| `client.payrollEmployees.identifiers.get({ path: { id } })` | GET | `/api/2026-07-01/resources/payroll_employees/identifiers/{id}` | Reads a single Identifier |
| `client.payrollEmployees.identifiers.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/payroll_employees/identifiers/{id}` | Updates an Identifier |

## payroll_integrations_base

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.payrollIntegrationsBase.codes.list()` | GET | `/api/2026-07-01/resources/payroll_integrations_base/codes` | Reads all Codes |
| `client.payrollIntegrationsBase.codes.create({ body })` | POST | `/api/2026-07-01/resources/payroll_integrations_base/codes` | Creates a Code |
| `client.payrollIntegrationsBase.codes.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/payroll_integrations_base/codes/{id}` | Deletes a Code |
| `client.payrollIntegrationsBase.codes.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/payroll_integrations_base/codes/{id}` | Updates a Code |

## performance

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.performance.agreements.list()` | GET | `/api/2026-07-01/resources/performance/agreements` | Reads all Agreements |
| `client.performance.agreements.bulkInitiate` | POST | `/api/2026-07-01/resources/performance/agreements/bulk_initiate` | Bulk initiates an Agreement |
| `client.performance.agreements.initiate` | POST | `/api/2026-07-01/resources/performance/agreements/initiate` | Initiates an Agreement |
| `client.performance.agreements.get({ path: { id } })` | GET | `/api/2026-07-01/resources/performance/agreements/{id}` | Reads a single Agreement |
| `client.performance.companyEmployeeScoreScales.list()` | GET | `/api/2026-07-01/resources/performance/company_employee_score_scales` | Reads all Company employee score scales |
| `client.performance.companyEmployeeScoreScales.set` | POST | `/api/2026-07-01/resources/performance/company_employee_score_scales/set` | Sets a Company employee score scale |
| `client.performance.companyEmployeeScoreScales.get({ path: { id } })` | GET | `/api/2026-07-01/resources/performance/company_employee_score_scales/{id}` | Reads a single Company employee score scale |
| `client.performance.employeeScoreScales.list()` | GET | `/api/2026-07-01/resources/performance/employee_score_scales` | Reads all Employee score scales |
| `client.performance.employeeScoreScales.get({ path: { id } })` | GET | `/api/2026-07-01/resources/performance/employee_score_scales/{id}` | Reads a single Employee score scale |
| `client.performance.reviewEvaluationAnswers.list()` | GET | `/api/2026-07-01/resources/performance/review_evaluation_answers` | Reads all Review evaluation answers |
| `client.performance.reviewEvaluationScores.list()` | GET | `/api/2026-07-01/resources/performance/review_evaluation_scores` | Reads all Review evaluation scores |
| `client.performance.reviewEvaluationScores.get({ path: { id } })` | GET | `/api/2026-07-01/resources/performance/review_evaluation_scores/{id}` | Reads a single Review evaluation score |
| `client.performance.reviewEvaluations.list()` | GET | `/api/2026-07-01/resources/performance/review_evaluations` | Reads all Review evaluations |
| `client.performance.reviewEvaluations.replaceReviewer` | POST | `/api/2026-07-01/resources/performance/review_evaluations/replace_reviewer` | Replace reviewers a Review evaluation |
| `client.performance.reviewEvaluations.get({ path: { id } })` | GET | `/api/2026-07-01/resources/performance/review_evaluations/{id}` | Reads a single Review evaluation |
| `client.performance.reviewOwners.list()` | GET | `/api/2026-07-01/resources/performance/review_owners` | Reads all Review owners |
| `client.performance.reviewOwners.bulkCreate` | POST | `/api/2026-07-01/resources/performance/review_owners/bulk_create` | Bulk creates a Review owner |
| `client.performance.reviewOwners.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/performance/review_owners/{id}` | Deletes a Review owner |
| `client.performance.reviewProcessCustomTemplates.list()` | GET | `/api/2026-07-01/resources/performance/review_process_custom_templates` | Reads all Review process custom templates |
| `client.performance.reviewProcessCustomTemplates.get({ path: { id } })` | GET | `/api/2026-07-01/resources/performance/review_process_custom_templates/{id}` | Reads a single Review process custom template |
| `client.performance.reviewProcessEstimatedTargets.list()` | GET | `/api/2026-07-01/resources/performance/review_process_estimated_targets` | Reads all Review process estimated targets |
| `client.performance.reviewProcessTargets.list()` | GET | `/api/2026-07-01/resources/performance/review_process_targets` | Reads all Review process targets |
| `client.performance.reviewProcessTargets.addPeers` | POST | `/api/2026-07-01/resources/performance/review_process_targets/add_peers` | Add peers a Review process target |
| `client.performance.reviewProcessTargets.bulkCreate` | POST | `/api/2026-07-01/resources/performance/review_process_targets/bulk_create` | Bulk creates a Review process target |
| `client.performance.reviewProcessTargets.removePeerEvaluations` | POST | `/api/2026-07-01/resources/performance/review_process_targets/remove_peer_evaluations` | Remove peer evaluations a Review process target |
| `client.performance.reviewProcessTargets.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/performance/review_process_targets/{id}` | Deletes a Review process target |
| `client.performance.reviewProcessTargets.get({ path: { id } })` | GET | `/api/2026-07-01/resources/performance/review_process_targets/{id}` | Reads a single Review process target |
| `client.performance.reviewProcesses.list()` | GET | `/api/2026-07-01/resources/performance/review_processes` | Reads all Review processes |
| `client.performance.reviewProcesses.create({ body })` | POST | `/api/2026-07-01/resources/performance/review_processes` | Creates a Review process |
| `client.performance.reviewProcesses.createFromTemplate` | POST | `/api/2026-07-01/resources/performance/review_processes/create_from_template` | Create from templates a Review process |
| `client.performance.reviewProcesses.duplicate` | POST | `/api/2026-07-01/resources/performance/review_processes/duplicate` | Duplicates a Review process |
| `client.performance.reviewProcesses.remindInBulk` | POST | `/api/2026-07-01/resources/performance/review_processes/remind_in_bulk` | Remind in bulks a Review process |
| `client.performance.reviewProcesses.removeSchedule` | POST | `/api/2026-07-01/resources/performance/review_processes/remove_schedule` | Remove schedules a Review process |
| `client.performance.reviewProcesses.reopen` | POST | `/api/2026-07-01/resources/performance/review_processes/reopen` | Reopens a Review process |
| `client.performance.reviewProcesses.schedule` | POST | `/api/2026-07-01/resources/performance/review_processes/schedule` | Schedules a Review process |
| `client.performance.reviewProcesses.start` | POST | `/api/2026-07-01/resources/performance/review_processes/start` | Starts a Review process |
| `client.performance.reviewProcesses.stop` | POST | `/api/2026-07-01/resources/performance/review_processes/stop` | Stops a Review process |
| `client.performance.reviewProcesses.toggleArchive` | POST | `/api/2026-07-01/resources/performance/review_processes/toggle_archive` | Toggle archives a Review process |
| `client.performance.reviewProcesses.updateAgreementsConfiguration` | POST | `/api/2026-07-01/resources/performance/review_processes/update_agreements_configuration` | Update agreements configurations a Review process |
| `client.performance.reviewProcesses.updateBasicInfo` | POST | `/api/2026-07-01/resources/performance/review_processes/update_basic_info` | Update basic infos a Review process |
| `client.performance.reviewProcesses.updateCompetenciesAssessmentsConfiguration` | POST | `/api/2026-07-01/resources/performance/review_processes/update_competencies_assessments_configuration` | Update competencies assessments configurations a Review process |
| `client.performance.reviewProcesses.updateDeadline` | POST | `/api/2026-07-01/resources/performance/review_processes/update_deadline` | Update deadlines a Review process |
| `client.performance.reviewProcesses.updateEmployeeScoreConfiguration` | POST | `/api/2026-07-01/resources/performance/review_processes/update_employee_score_configuration` | Update employee score configurations a Review process |
| `client.performance.reviewProcesses.updateReviewerStrategies` | POST | `/api/2026-07-01/resources/performance/review_processes/update_reviewer_strategies` | Update reviewer strategies a Review process |
| `client.performance.reviewProcesses.updateSchedule` | POST | `/api/2026-07-01/resources/performance/review_processes/update_schedule` | Update schedules a Review process |
| `client.performance.reviewProcesses.updateTargetStrategy` | POST | `/api/2026-07-01/resources/performance/review_processes/update_target_strategy` | Update target strategies a Review process |
| `client.performance.reviewProcesses.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/performance/review_processes/{id}` | Deletes a Review process |
| `client.performance.reviewProcesses.get({ path: { id } })` | GET | `/api/2026-07-01/resources/performance/review_processes/{id}` | Reads a single Review process |
| `client.performance.reviewQuestionnaireByStrategies.list()` | GET | `/api/2026-07-01/resources/performance/review_questionnaire_by_strategies` | Reads all Review questionnaire by strategies |
| `client.performance.reviewQuestionnaireByStrategies.updateDefaultRatingScale` | POST | `/api/2026-07-01/resources/performance/review_questionnaire_by_strategies/update_default_rating_scale` | Update default rating scales a Review questionnaire by strategy |
| `client.performance.reviewQuestionnaireByStrategies.updateQuestionnaireForStrategy` | POST | `/api/2026-07-01/resources/performance/review_questionnaire_by_strategies/update_questionnaire_for_strategy` | Update questionnaire for strategies a Review questionnaire by strategy |
| `client.performance.reviewQuestionnaireByStrategies.get({ path: { id } })` | GET | `/api/2026-07-01/resources/performance/review_questionnaire_by_strategies/{id}` | Reads a single Review questionnaire by strategy |
| `client.performance.reviewVisibilitySettings.list()` | GET | `/api/2026-07-01/resources/performance/review_visibility_settings` | Reads all Review visibility settings |
| `client.performance.reviewVisibilitySettings.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/performance/review_visibility_settings/{id}` | Updates a Review visibility setting |
| `client.performance.targetManagers.list()` | GET | `/api/2026-07-01/resources/performance/target_managers` | Reads all Target managers |
| `client.performance.targetManagers.get({ path: { id } })` | GET | `/api/2026-07-01/resources/performance/target_managers/{id}` | Reads a single Target manager |

## posts

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.posts.comments.list()` | GET | `/api/2026-07-01/resources/posts/comments` | Reads all Comments |
| `client.posts.comments.create({ body })` | POST | `/api/2026-07-01/resources/posts/comments` | Creates a Comment |
| `client.posts.comments.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/posts/comments/{id}` | Deletes a Comment |
| `client.posts.comments.get({ path: { id } })` | GET | `/api/2026-07-01/resources/posts/comments/{id}` | Reads a single Comment |
| `client.posts.comments.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/posts/comments/{id}` | Updates a Comment |
| `client.posts.groups.list()` | GET | `/api/2026-07-01/resources/posts/groups` | Reads all Groups |
| `client.posts.groups.create({ body })` | POST | `/api/2026-07-01/resources/posts/groups` | Creates a Group |
| `client.posts.groups.archive` | POST | `/api/2026-07-01/resources/posts/groups/archive` | Archives a Group |
| `client.posts.groups.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/posts/groups/{id}` | Deletes a Group |
| `client.posts.groups.get({ path: { id } })` | GET | `/api/2026-07-01/resources/posts/groups/{id}` | Reads a single Group |
| `client.posts.groups.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/posts/groups/{id}` | Updates a Group |
| `client.posts.posts.list()` | GET | `/api/2026-07-01/resources/posts/posts` | Reads all Posts |
| `client.posts.posts.create({ body })` | POST | `/api/2026-07-01/resources/posts/posts` | Creates a Post |
| `client.posts.posts.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/posts/posts/{id}` | Deletes a Post |
| `client.posts.posts.get({ path: { id } })` | GET | `/api/2026-07-01/resources/posts/posts/{id}` | Reads a single Post |
| `client.posts.posts.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/posts/posts/{id}` | Updates a Post |

## procurement

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.procurement.purchaseOrders.list()` | GET | `/api/2026-07-01/resources/procurement/purchase_orders` | Reads all Purchase orders |
| `client.procurement.purchaseOrders.get({ path: { id } })` | GET | `/api/2026-07-01/resources/procurement/purchase_orders/{id}` | Reads a single Purchase order |
| `client.procurement.purchaseRequests.list()` | GET | `/api/2026-07-01/resources/procurement/purchase_requests` | Reads all Purchase requests |
| `client.procurement.purchaseRequests.get({ path: { id } })` | GET | `/api/2026-07-01/resources/procurement/purchase_requests/{id}` | Reads a single Purchase request |
| `client.procurement.types.list()` | GET | `/api/2026-07-01/resources/procurement/types` | Reads all Types |
| `client.procurement.types.get({ path: { id } })` | GET | `/api/2026-07-01/resources/procurement/types/{id}` | Reads a single Type |

## project_management

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.projectManagement.budgetStrategies.list()` | GET | `/api/2026-07-01/resources/project_management/budget_strategies` | Reads all Budget strategies |
| `client.projectManagement.budgetStrategies.create({ body })` | POST | `/api/2026-07-01/resources/project_management/budget_strategies` | Creates a Budget strategy |
| `client.projectManagement.budgetStrategies.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/project_management/budget_strategies/{id}` | Deletes a Budget strategy |
| `client.projectManagement.budgetStrategies.get({ path: { id } })` | GET | `/api/2026-07-01/resources/project_management/budget_strategies/{id}` | Reads a single Budget strategy |
| `client.projectManagement.budgetStrategies.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/project_management/budget_strategies/{id}` | Updates a Budget strategy |
| `client.projectManagement.expenseRecords.list()` | GET | `/api/2026-07-01/resources/project_management/expense_records` | Reads all Expense records |
| `client.projectManagement.expenseRecords.get({ path: { id } })` | GET | `/api/2026-07-01/resources/project_management/expense_records/{id}` | Reads a single Expense record |
| `client.projectManagement.exportableExpenses.list()` | GET | `/api/2026-07-01/resources/project_management/exportable_expenses` | Reads all Exportable expenses |
| `client.projectManagement.imputableProjects.list()` | GET | `/api/2026-07-01/resources/project_management/imputable_projects` | Reads all Imputable projects |
| `client.projectManagement.imputableProjects.get({ path: { id } })` | GET | `/api/2026-07-01/resources/project_management/imputable_projects/{id}` | Reads a single Imputable project |
| `client.projectManagement.plannedRecords.list()` | GET | `/api/2026-07-01/resources/project_management/planned_records` | Reads all Planned records |
| `client.projectManagement.plannedRecords.bulkCreate` | POST | `/api/2026-07-01/resources/project_management/planned_records/bulk_create` | Bulk creates a Planned record |
| `client.projectManagement.plannedRecords.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/project_management/planned_records/{id}` | Deletes a Planned record |
| `client.projectManagement.plannedRecords.get({ path: { id } })` | GET | `/api/2026-07-01/resources/project_management/planned_records/{id}` | Reads a single Planned record |
| `client.projectManagement.plannedRecords.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/project_management/planned_records/{id}` | Updates a Planned record |
| `client.projectManagement.projectTasks.list()` | GET | `/api/2026-07-01/resources/project_management/project_tasks` | Reads all Project tasks |
| `client.projectManagement.projectTasks.create({ body })` | POST | `/api/2026-07-01/resources/project_management/project_tasks` | Creates a Project task |
| `client.projectManagement.projectTasks.bulkDestroy` | POST | `/api/2026-07-01/resources/project_management/project_tasks/bulk_destroy` | Bulk destroys a Project task |
| `client.projectManagement.projectTasks.bulkDuplicate` | POST | `/api/2026-07-01/resources/project_management/project_tasks/bulk_duplicate` | Bulk duplicates a Project task |
| `client.projectManagement.projectTasks.get({ path: { id } })` | GET | `/api/2026-07-01/resources/project_management/project_tasks/{id}` | Reads a single Project task |
| `client.projectManagement.projectTasks.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/project_management/project_tasks/{id}` | Updates a Project task |
| `client.projectManagement.projectWorkers.list()` | GET | `/api/2026-07-01/resources/project_management/project_workers` | Reads all Project workers |
| `client.projectManagement.projectWorkers.create({ body })` | POST | `/api/2026-07-01/resources/project_management/project_workers` | Creates a Project worker |
| `client.projectManagement.projectWorkers.bulkAssign` | POST | `/api/2026-07-01/resources/project_management/project_workers/bulk_assign` | Bulk assigns a Project worker |
| `client.projectManagement.projectWorkers.bulkCreate` | POST | `/api/2026-07-01/resources/project_management/project_workers/bulk_create` | Bulk creates a Project worker |
| `client.projectManagement.projectWorkers.unassign` | POST | `/api/2026-07-01/resources/project_management/project_workers/unassign` | Unassigns a Project worker |
| `client.projectManagement.projectWorkers.get({ path: { id } })` | GET | `/api/2026-07-01/resources/project_management/project_workers/{id}` | Reads a single Project worker |
| `client.projectManagement.projects.list()` | GET | `/api/2026-07-01/resources/project_management/projects` | Reads all Projects |
| `client.projectManagement.projects.create({ body })` | POST | `/api/2026-07-01/resources/project_management/projects` | Creates a Project |
| `client.projectManagement.projects.activate` | POST | `/api/2026-07-01/resources/project_management/projects/activate` | Activates a Project |
| `client.projectManagement.projects.changeAssignment` | POST | `/api/2026-07-01/resources/project_management/projects/change_assignment` | Change assignments a Project |
| `client.projectManagement.projects.changeStatus` | POST | `/api/2026-07-01/resources/project_management/projects/change_status` | Change statuses a Project |
| `client.projectManagement.projects.close` | POST | `/api/2026-07-01/resources/project_management/projects/close` | Closes a Project |
| `client.projectManagement.projects.softDelete` | POST | `/api/2026-07-01/resources/project_management/projects/soft_delete` | Soft deletes a Project |
| `client.projectManagement.projects.get({ path: { id } })` | GET | `/api/2026-07-01/resources/project_management/projects/{id}` | Reads a single Project |
| `client.projectManagement.projects.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/project_management/projects/{id}` | Updates a Project |
| `client.projectManagement.subprojects.list()` | GET | `/api/2026-07-01/resources/project_management/subprojects` | Reads all Subprojects |
| `client.projectManagement.subprojects.create({ body })` | POST | `/api/2026-07-01/resources/project_management/subprojects` | Creates a Subproject |
| `client.projectManagement.subprojects.rename` | POST | `/api/2026-07-01/resources/project_management/subprojects/rename` | Renames a Subproject |
| `client.projectManagement.subprojects.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/project_management/subprojects/{id}` | Deletes a Subproject |
| `client.projectManagement.subprojects.get({ path: { id } })` | GET | `/api/2026-07-01/resources/project_management/subprojects/{id}` | Reads a single Subproject |
| `client.projectManagement.subprojects.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/project_management/subprojects/{id}` | Updates a Subproject |
| `client.projectManagement.timeRecords.list()` | GET | `/api/2026-07-01/resources/project_management/time_records` | Reads all Time records |
| `client.projectManagement.timeRecords.create({ body })` | POST | `/api/2026-07-01/resources/project_management/time_records` | Creates a Time record |
| `client.projectManagement.timeRecords.bulkDelete` | POST | `/api/2026-07-01/resources/project_management/time_records/bulk_delete` | Bulk deletes a Time record |
| `client.projectManagement.timeRecords.bulkProcess` | POST | `/api/2026-07-01/resources/project_management/time_records/bulk_process` | Bulk processes a Time record |
| `client.projectManagement.timeRecords.updateProjectWorker` | POST | `/api/2026-07-01/resources/project_management/time_records/update_project_worker` | Update project workers a Time record |
| `client.projectManagement.timeRecords.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/project_management/time_records/{id}` | Deletes a Time record |
| `client.projectManagement.timeRecords.get({ path: { id } })` | GET | `/api/2026-07-01/resources/project_management/time_records/{id}` | Reads a single Time record |

## shift_management

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.shiftManagement.shifts.list()` | GET | `/api/2026-07-01/resources/shift_management/shifts` | Reads all Shifts |
| `client.shiftManagement.shifts.create({ body })` | POST | `/api/2026-07-01/resources/shift_management/shifts` | Creates a Shift |
| `client.shiftManagement.shifts.bulkCreate` | POST | `/api/2026-07-01/resources/shift_management/shifts/bulk_create` | Bulk creates a Shift |
| `client.shiftManagement.shifts.bulkDelete` | POST | `/api/2026-07-01/resources/shift_management/shifts/bulk_delete` | Bulk deletes a Shift |
| `client.shiftManagement.shifts.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/shift_management/shifts/{id}` | Deletes a Shift |
| `client.shiftManagement.shifts.get({ path: { id } })` | GET | `/api/2026-07-01/resources/shift_management/shifts/{id}` | Reads a single Shift |

## tasks

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.tasks.taskFiles.list()` | GET | `/api/2026-07-01/resources/tasks/task_files` | Reads all Task files |
| `client.tasks.taskFiles.create({ body })` | POST | `/api/2026-07-01/resources/tasks/task_files` | Creates a Task file |
| `client.tasks.taskFiles.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/tasks/task_files/{id}` | Deletes a Task file |
| `client.tasks.taskFiles.get({ path: { id } })` | GET | `/api/2026-07-01/resources/tasks/task_files/{id}` | Reads a single Task file |
| `client.tasks.tasks.list()` | GET | `/api/2026-07-01/resources/tasks/tasks` | Reads all Tasks |
| `client.tasks.tasks.create({ body })` | POST | `/api/2026-07-01/resources/tasks/tasks` | Creates a Task |
| `client.tasks.tasks.bulkCreate` | POST | `/api/2026-07-01/resources/tasks/tasks/bulk_create` | Bulk creates a Task |
| `client.tasks.tasks.bulkDelete` | POST | `/api/2026-07-01/resources/tasks/tasks/bulk_delete` | Bulk deletes a Task |
| `client.tasks.tasks.bulkUpdate` | POST | `/api/2026-07-01/resources/tasks/tasks/bulk_update` | Bulk updates a Task |
| `client.tasks.tasks.copy` | POST | `/api/2026-07-01/resources/tasks/tasks/copy` | Copies a Task |
| `client.tasks.tasks.createComment` | POST | `/api/2026-07-01/resources/tasks/tasks/create_comment` | Create comments a Task |
| `client.tasks.tasks.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/tasks/tasks/{id}` | Deletes a Task |
| `client.tasks.tasks.get({ path: { id } })` | GET | `/api/2026-07-01/resources/tasks/tasks/{id}` | Reads a single Task |
| `client.tasks.tasks.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/tasks/tasks/{id}` | Updates a Task |

## teams

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.teams.memberships.list()` | GET | `/api/2026-07-01/resources/teams/memberships` | Reads all Memberships |
| `client.teams.memberships.create({ body })` | POST | `/api/2026-07-01/resources/teams/memberships` | Creates a Membership |
| `client.teams.memberships.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/teams/memberships/{id}` | Deletes a Membership |
| `client.teams.memberships.get({ path: { id } })` | GET | `/api/2026-07-01/resources/teams/memberships/{id}` | Reads a single Membership |
| `client.teams.memberships.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/teams/memberships/{id}` | Updates a Membership |
| `client.teams.teams.list()` | GET | `/api/2026-07-01/resources/teams/teams` | Reads all Teams |
| `client.teams.teams.create({ body })` | POST | `/api/2026-07-01/resources/teams/teams` | Creates a Team |
| `client.teams.teams.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/teams/teams/{id}` | Deletes a Team |
| `client.teams.teams.get({ path: { id } })` | GET | `/api/2026-07-01/resources/teams/teams/{id}` | Reads a single Team |
| `client.teams.teams.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/teams/teams/{id}` | Updates a Team |

## time_planning

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.timePlanning.plannedBreaks.list()` | GET | `/api/2026-07-01/resources/time_planning/planned_breaks` | Reads all Planned breaks |
| `client.timePlanning.plannedBreaks.bulkCreate` | POST | `/api/2026-07-01/resources/time_planning/planned_breaks/bulk_create` | Bulk creates a Planned break |
| `client.timePlanning.plannedBreaks.get({ path: { id } })` | GET | `/api/2026-07-01/resources/time_planning/planned_breaks/{id}` | Reads a single Planned break |
| `client.timePlanning.planningVersions.list()` | GET | `/api/2026-07-01/resources/time_planning/planning_versions` | Reads all Planning versions |
| `client.timePlanning.planningVersions.create({ body })` | POST | `/api/2026-07-01/resources/time_planning/planning_versions` | Creates a Planning version |
| `client.timePlanning.planningVersions.bulkCreate` | POST | `/api/2026-07-01/resources/time_planning/planning_versions/bulk_create` | Bulk creates a Planning version |
| `client.timePlanning.planningVersions.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/time_planning/planning_versions/{id}` | Deletes a Planning version |
| `client.timePlanning.planningVersions.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/time_planning/planning_versions/{id}` | Updates a Planning version |

## time_settings

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.timeSettings.breakConfigurations.list()` | GET | `/api/2026-07-01/resources/time_settings/break_configurations` | Reads all Break configurations |
| `client.timeSettings.breakConfigurations.create({ body })` | POST | `/api/2026-07-01/resources/time_settings/break_configurations` | Creates a Break configuration |
| `client.timeSettings.breakConfigurations.get({ path: { id } })` | GET | `/api/2026-07-01/resources/time_settings/break_configurations/{id}` | Reads a single Break configuration |
| `client.timeSettings.breakConfigurations.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/time_settings/break_configurations/{id}` | Updates a Break configuration |

## timeoff

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.timeoff.allowanceIncidences.list()` | GET | `/api/2026-07-01/resources/timeoff/allowance_incidences` | Reads all Allowance incidences |
| `client.timeoff.allowanceIncidences.create({ body })` | POST | `/api/2026-07-01/resources/timeoff/allowance_incidences` | Creates an Allowance incidence |
| `client.timeoff.allowanceIncidences.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/timeoff/allowance_incidences/{id}` | Deletes an Allowance incidence |
| `client.timeoff.allowanceIncidences.get({ path: { id } })` | GET | `/api/2026-07-01/resources/timeoff/allowance_incidences/{id}` | Reads a single Allowance incidence |
| `client.timeoff.allowanceIncidences.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/timeoff/allowance_incidences/{id}` | Updates an Allowance incidence |
| `client.timeoff.allowanceStats.list()` | GET | `/api/2026-07-01/resources/timeoff/allowance_stats` | Reads all Allowance stats |
| `client.timeoff.allowanceStats.get({ path: { id } })` | GET | `/api/2026-07-01/resources/timeoff/allowance_stats/{id}` | Reads a single Allowance stat |
| `client.timeoff.allowances.list()` | GET | `/api/2026-07-01/resources/timeoff/allowances` | Reads all Allowances |
| `client.timeoff.allowances.create({ body })` | POST | `/api/2026-07-01/resources/timeoff/allowances` | Creates an Allowance |
| `client.timeoff.allowances.deleteWithAltAllowance` | POST | `/api/2026-07-01/resources/timeoff/allowances/delete_with_alt_allowance` | Delete with alt allowances an Allowance |
| `client.timeoff.allowances.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/timeoff/allowances/{id}` | Deletes an Allowance |
| `client.timeoff.allowances.get({ path: { id } })` | GET | `/api/2026-07-01/resources/timeoff/allowances/{id}` | Reads a single Allowance |
| `client.timeoff.allowances.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/timeoff/allowances/{id}` | Updates an Allowance |
| `client.timeoff.blockedPeriods.list()` | GET | `/api/2026-07-01/resources/timeoff/blocked_periods` | Reads all Blocked periods |
| `client.timeoff.blockedPeriods.create({ body })` | POST | `/api/2026-07-01/resources/timeoff/blocked_periods` | Creates a Blocked period |
| `client.timeoff.blockedPeriods.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/timeoff/blocked_periods/{id}` | Deletes a Blocked period |
| `client.timeoff.blockedPeriods.get({ path: { id } })` | GET | `/api/2026-07-01/resources/timeoff/blocked_periods/{id}` | Reads a single Blocked period |
| `client.timeoff.blockedPeriods.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/timeoff/blocked_periods/{id}` | Updates a Blocked period |
| `client.timeoff.leaveTypes.list()` | GET | `/api/2026-07-01/resources/timeoff/leave_types` | Reads all Leave types |
| `client.timeoff.leaveTypes.create({ body })` | POST | `/api/2026-07-01/resources/timeoff/leave_types` | Creates a Leave type |
| `client.timeoff.leaveTypes.get({ path: { id } })` | GET | `/api/2026-07-01/resources/timeoff/leave_types/{id}` | Reads a single Leave type |
| `client.timeoff.leaveTypes.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/timeoff/leave_types/{id}` | Updates a Leave type |
| `client.timeoff.leaves.list()` | GET | `/api/2026-07-01/resources/timeoff/leaves` | Reads all Leaves |
| `client.timeoff.leaves.create({ body })` | POST | `/api/2026-07-01/resources/timeoff/leaves` | Creates a Leave |
| `client.timeoff.leaves.approve` | POST | `/api/2026-07-01/resources/timeoff/leaves/approve` | Approves a Leave |
| `client.timeoff.leaves.approveAll` | POST | `/api/2026-07-01/resources/timeoff/leaves/approve_all` | Approve alls a Leave |
| `client.timeoff.leaves.reject` | POST | `/api/2026-07-01/resources/timeoff/leaves/reject` | Rejects a Leave |
| `client.timeoff.leaves.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/timeoff/leaves/{id}` | Deletes a Leave |
| `client.timeoff.leaves.get({ path: { id } })` | GET | `/api/2026-07-01/resources/timeoff/leaves/{id}` | Reads a single Leave |
| `client.timeoff.leaves.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/timeoff/leaves/{id}` | Updates a Leave |
| `client.timeoff.policies.list()` | GET | `/api/2026-07-01/resources/timeoff/policies` | Reads all Policies |
| `client.timeoff.policies.create({ body })` | POST | `/api/2026-07-01/resources/timeoff/policies` | Creates a Policy |
| `client.timeoff.policies.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/timeoff/policies/{id}` | Deletes a Policy |
| `client.timeoff.policies.get({ path: { id } })` | GET | `/api/2026-07-01/resources/timeoff/policies/{id}` | Reads a single Policy |
| `client.timeoff.policies.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/timeoff/policies/{id}` | Updates a Policy |
| `client.timeoff.policyAssignments.list()` | GET | `/api/2026-07-01/resources/timeoff/policy_assignments` | Reads all Policy assignments |
| `client.timeoff.policyAssignments.create({ body })` | POST | `/api/2026-07-01/resources/timeoff/policy_assignments` | Creates a Policy assignment |
| `client.timeoff.policyAssignments.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/timeoff/policy_assignments/{id}` | Deletes a Policy assignment |
| `client.timeoff.policyAssignments.get({ path: { id } })` | GET | `/api/2026-07-01/resources/timeoff/policy_assignments/{id}` | Reads a single Policy assignment |
| `client.timeoff.policyAssignments.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/timeoff/policy_assignments/{id}` | Updates a Policy assignment |
| `client.timeoff.policyTimelines.list()` | GET | `/api/2026-07-01/resources/timeoff/policy_timelines` | Reads all Policy timelines |

## trainings

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.trainings.categories.list()` | GET | `/api/2026-07-01/resources/trainings/categories` | Reads all Categories |
| `client.trainings.categories.create({ body })` | POST | `/api/2026-07-01/resources/trainings/categories` | Creates a Category |
| `client.trainings.categories.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/trainings/categories/{id}` | Deletes a Category |
| `client.trainings.categories.get({ path: { id } })` | GET | `/api/2026-07-01/resources/trainings/categories/{id}` | Reads a single Category |
| `client.trainings.sessionAccessMemberships.list()` | GET | `/api/2026-07-01/resources/trainings/session_access_memberships` | Reads all Session access memberships |
| `client.trainings.sessionAccessMemberships.bulkCreate` | POST | `/api/2026-07-01/resources/trainings/session_access_memberships/bulk_create` | Bulk creates a Session access membership |
| `client.trainings.sessionAccessMemberships.bulkDestroy` | POST | `/api/2026-07-01/resources/trainings/session_access_memberships/bulk_destroy` | Bulk destroys a Session access membership |
| `client.trainings.sessionAccessMemberships.get({ path: { id } })` | GET | `/api/2026-07-01/resources/trainings/session_access_memberships/{id}` | Reads a single Session access membership |
| `client.trainings.sessionAttendances.list()` | GET | `/api/2026-07-01/resources/trainings/session_attendances` | Reads all Session attendances |
| `client.trainings.sessionAttendances.bulkUpdate` | POST | `/api/2026-07-01/resources/trainings/session_attendances/bulk_update` | Bulk update session attendances |
| `client.trainings.sessionAttendances.get({ path: { id } })` | GET | `/api/2026-07-01/resources/trainings/session_attendances/{id}` | Reads a single Session attendance |
| `client.trainings.sessions.list()` | GET | `/api/2026-07-01/resources/trainings/sessions` | Reads all Sessions |
| `client.trainings.sessions.create({ body })` | POST | `/api/2026-07-01/resources/trainings/sessions` | Create a new training session |
| `client.trainings.sessions.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/trainings/sessions/{id}` | Deletes a Session |
| `client.trainings.sessions.get({ path: { id } })` | GET | `/api/2026-07-01/resources/trainings/sessions/{id}` | Reads a single Session |
| `client.trainings.sessions.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/trainings/sessions/{id}` | Update training session |
| `client.trainings.trainingClasses.list()` | GET | `/api/2026-07-01/resources/trainings/training_classes` | Reads all Training classes |
| `client.trainings.trainingClasses.create({ body })` | POST | `/api/2026-07-01/resources/trainings/training_classes` | Creates a Training class |
| `client.trainings.trainingClasses.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/trainings/training_classes/{id}` | Deletes a Training class |
| `client.trainings.trainingClasses.get({ path: { id } })` | GET | `/api/2026-07-01/resources/trainings/training_classes/{id}` | Reads a single Training class |
| `client.trainings.trainingClasses.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/trainings/training_classes/{id}` | Updates a Training class |
| `client.trainings.trainingMemberships.list()` | GET | `/api/2026-07-01/resources/trainings/training_memberships` | Reads all Training memberships |
| `client.trainings.trainingMemberships.bulkCreate` | POST | `/api/2026-07-01/resources/trainings/training_memberships/bulk_create` | Bulk creates a Training membership |
| `client.trainings.trainingMemberships.bulkDestroy` | POST | `/api/2026-07-01/resources/trainings/training_memberships/bulk_destroy` | Bulk destroys a Training membership |
| `client.trainings.trainingMemberships.get({ path: { id } })` | GET | `/api/2026-07-01/resources/trainings/training_memberships/{id}` | Reads a single Training membership |
| `client.trainings.trainingMemberships.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/trainings/training_memberships/{id}` | Updates a Training membership |
| `client.trainings.trainings.list()` | GET | `/api/2026-07-01/resources/trainings/trainings` | Reads all Trainings |
| `client.trainings.trainings.create({ body })` | POST | `/api/2026-07-01/resources/trainings/trainings` | Creates a Training |
| `client.trainings.trainings.bulkDelete` | POST | `/api/2026-07-01/resources/trainings/trainings/bulk_delete` | Bulk deletes a Training |
| `client.trainings.trainings.bulkUpdateCatalog` | POST | `/api/2026-07-01/resources/trainings/trainings/bulk_update_catalog` | Bulk update catalogs a Training |
| `client.trainings.trainings.updateStatus` | POST | `/api/2026-07-01/resources/trainings/trainings/update_status` | Update statuses a Training |
| `client.trainings.trainings.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/trainings/trainings/{id}` | Deletes a Training |
| `client.trainings.trainings.get({ path: { id } })` | GET | `/api/2026-07-01/resources/trainings/trainings/{id}` | Reads a single Training |
| `client.trainings.trainings.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/trainings/trainings/{id}` | Updates a Training |

## work_schedule

| SDK call | HTTP | path | summary |
| --- | --- | --- | --- |
| `client.workSchedule.dayConfigurations.list()` | GET | `/api/2026-07-01/resources/work_schedule/day_configurations` | Reads all Day configurations |
| `client.workSchedule.dayConfigurations.bulkCud` | POST | `/api/2026-07-01/resources/work_schedule/day_configurations/bulk_cud` | Bulk cuds a Day configuration |
| `client.workSchedule.dayConfigurations.get({ path: { id } })` | GET | `/api/2026-07-01/resources/work_schedule/day_configurations/{id}` | Reads a single Day configuration |
| `client.workSchedule.overlapPeriods.list()` | GET | `/api/2026-07-01/resources/work_schedule/overlap_periods` | Reads all Overlap periods |
| `client.workSchedule.overlapPeriods.create({ body })` | POST | `/api/2026-07-01/resources/work_schedule/overlap_periods` | Creates an Overlap period |
| `client.workSchedule.overlapPeriods.delete({ path: { id } })` | DELETE | `/api/2026-07-01/resources/work_schedule/overlap_periods/{id}` | Deletes an Overlap period |
| `client.workSchedule.overlapPeriods.get({ path: { id } })` | GET | `/api/2026-07-01/resources/work_schedule/overlap_periods/{id}` | Reads a single Overlap period |
| `client.workSchedule.overlapPeriods.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/work_schedule/overlap_periods/{id}` | Updates an Overlap period |
| `client.workSchedule.schedules.list()` | GET | `/api/2026-07-01/resources/work_schedule/schedules` | Reads all Schedules |
| `client.workSchedule.schedules.create({ body })` | POST | `/api/2026-07-01/resources/work_schedule/schedules` | Creates a Schedule |
| `client.workSchedule.schedules.toggleArchive` | POST | `/api/2026-07-01/resources/work_schedule/schedules/toggle_archive` | Toggle archives a Schedule |
| `client.workSchedule.schedules.get({ path: { id } })` | GET | `/api/2026-07-01/resources/work_schedule/schedules/{id}` | Reads a single Schedule |
| `client.workSchedule.schedules.update({ path: { id }, body })` | PUT | `/api/2026-07-01/resources/work_schedule/schedules/{id}` | Updates a Schedule |
