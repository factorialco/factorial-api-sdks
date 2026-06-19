<!-- Vendored from https://apidoc.factorialhr.com/docs/oauth-scopes.md -->

# OAuth Scopes

Scopes specify the exact level of access needed, ensuring OAuth tokens are restricted to only the required resources. They do not grant any permissions beyond what the user already has.

Each scope represents a set of resources within our API. The list of resources accessible by the generated OAuth token is strictly limited to the scopes configured in the OAuth application.

> ⚠️ If you are a Factorial Partner
>
> If you have an OAuth application in production and wish to modify your scopes list, please [fill up this form](https://factorial.typeform.com/to/B2GJV4lT).

## How do scopes work

When you create a new OAuth application you will be able to select the scopes you want your app to have access to.

![](https://files.readme.io/af86dd0dfc32764bc8783572743f01e79521fdd972b20ca667504af3220996c4-image.png)

These scopes will be sent through the URL when requesting the authorization code:

`https://api.factorialhr.com/oauth/authorize?client_id=<YOUR_CLIENT_ID>&redirect_uri=<YOUR_REDIRECT_URI>&response_type=code&scope=project_management%20time_tracking`

Then the client will review the scopes sent though the URL and authorize/deny the app access to these.

![](https://files.readme.io/78b117156a5489903ab178dcfbdee535a81458d0231be300fc9c02474ab0f7b7-image.png)

<br />

Once the user authorizes the app to access the requested scopes, you can continue to [request the access token](https://apidoc.factorialhr.com/docs/request-an-access-token). The access token generated will be restricted to the authorized scopes.

**NOTE**: If you change the scopes in an already existing OAuth app, the already-generated tokens will become invalid so the client will need to re-authorize the app to be able to re-generate the OAuth tokens with the updated scopes list.

## Scopes list

Currently, our scopes allow both read and write actions within the resources.

<Table>
  <thead>
    <tr>
      <th>
        Scope
      </th>

      <th>
        Endpoints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        banking
      </td>

      <td>
        [`Banking > BankAccount`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-banking-bank-accounts)\
        [`Banking > BankAccountNumber > Upserts`](https://apidoc.factorialhr.com/v2025-04-01/reference/post_webhooks-banking-bankaccountnumber-upserts)\
        [`Banking > Transaction` ](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-banking-transactions)
      </td>
    </tr>

    <tr>
      <td>
        company\_legal\_entities
      </td>

      <td>
        [`Companies > Legal Entities`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-companies-legal-entities)
      </td>
    </tr>

    <tr>
      <td>
        company\_holidays
      </td>

      <td>
        [`Holidays > CompanyHoliday`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-holidays-company-holidays)
      </td>
    </tr>

    <tr>
      <td>
        company\_locations
      </td>

      <td>
        [`Locations > Location`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-locations-locations)\
        [`Locations > WorkArea`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-locations-work-areas)
      </td>
    </tr>

    <tr>
      <td>
        contracts
      </td>

      <td>
        [`Contracts > Compensation`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-contracts-compensations)\
        [`Contracts > ContractTemplate`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-contracts-contract-templates)\
        [`Contracts > ContractVersion`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-contracts-contract-versions)\
        [`Contracts > FrenchContractType`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-contracts-french-contract-types)\
        [`Contracts > GermanContractType`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-contracts-german-contract-types)\
        [`Contracts > PortugueseContractType`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-contracts-portuguese-contract-types)\
        [`Contracts > ReferenceContract`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-contracts-reference-contracts)\
        [`Contracts > SpanishContractType`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-contracts-spanish-contract-types)\
        [`Contracts > SpanishEducationLevel`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-contracts-spanish-education-levels)\
        [`Contracts > SpanishProfessionalCategory`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-contracts-spanish-professional-categories)\
        [`Contracts > Taxonomy`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-contracts-taxonomies)
      </td>
    </tr>

    <tr>
      <td>
        custom\_fields
      </td>

      <td>
        [`CustomFields > Field`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-custom-fields-fields)\
        [`CustomFields > Option`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-custom-fields-options)\
        [`CustomFields > ResourceField`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-custom-fields-resource-fields)\
        [`CustomFields > Value`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-custom-fields-values)\
        [`CustomResources > Schema`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-custom-resources-schemas)\
        [`CustomResources > Value`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-custom-resources-values)
      </td>
    </tr>

    <tr>
      <td>
        documents
      </td>

      <td>
        [`Documents > Document`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-documents-documents)\
        [`Documents > DownloadUrl`](https://apidoc.factorialhr.com/v2025-04-01/reference/post_api-2025-04-01-resources-documents-download-urls-bulk-create)
      </td>
    </tr>

    <tr>
      <td>
        employees
      </td>

      <td>
        [`Employees > Employee`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-employees-employees)\
        [`Teams > Membership`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-teams-memberships)\
        [`Teams > Team`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-teams-teams)
      </td>
    </tr>

    <tr>
      <td>
        employee\_updates
      </td>

      <td>
        [`BookkeepersManagement > Incidence`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-bookkeepers-management-incidences)\
        [`EmployeeUpdates > Absence`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-employee-updates-absences)\
        [`EmployeeUpdates > ContractChange`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-employee-updates-contract-changes)\
        [`EmployeeUpdates > NewHire`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-employee-updates-new-hires)\
        [`EmployeeUpdates > PersonalChange`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-employee-updates-personal-changes)\
        [`EmployeeUpdates > Summary`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-employee-updates-summaries)\
        [`EmployeeUpdates > Termination`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-employee-updates-terminations)
      </td>
    </tr>

    <tr>
      <td>
        expenses
      </td>

      <td>
        [`Expenses > Expensable`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-expenses-expensables)\
        [`Expenses > Expense`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-expenses-expenses)\
        [`Expenses > Milage`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-expenses-mileages)\
        [`Expenses > PerDiem`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-expenses-per-diems)
      </td>
    </tr>

    <tr>
      <td>
        finance
      </td>

      <td>
        [`Finance > Account`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-finance-accounts)\
        [`Finance > AccountSetting`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-finance-accounting-settings)\
        [`Finance > Contact`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-finance-contacts)\
        [`Finance > CostCenter`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-finance-cost-centers)\
        [`Finance > CostCenterMembership`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-finance-cost-center-memberships)\
        [`Finance > FinancialDocument`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-finance-financial-documents)\
        [`Finance > JournalEntry`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-finance-journal-entries)\
        [`Finance > JournalLine`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-finance-journal-lines)\
        [`Finance > TaxRate`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-finance-tax-rates)\
        [`Finance > TaxType`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-finance-tax-types)
      </td>
    </tr>

    <tr>
      <td>
        integrations
      </td>

      <td>
        [`PayrollIntegrationsBase > Code`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-payroll-integrations-base-codes)
      </td>
    </tr>

    <tr>
      <td>
        job\_catalog
      </td>

      <td>
        [`JobCatalog > Level`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-job-catalog-levels)\
        [`JobCatalog > Role`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-job-catalog-roles)
      </td>
    </tr>

    <tr>
      <td>
        marketplace
      </td>

      <td>
        [`Marketplace > InstallationSettings`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-marketplace-installation-settings)
      </td>
    </tr>

    <tr>
      <td>
        payroll
      </td>

      <td>
        [`Payroll > FamilySituations`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-payroll-family-situations)\
        [`Payroll > PolicyPeriod`](https://apidoc.factorialhr.com/v2025-04-01/reference/post_api-2025-04-01-resources-payroll-policy-periods-change-status)\
        [`PayrollEmployees > Identifier`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-payroll-employees-identifiers)
      </td>
    </tr>

    <tr>
      <td>
        payroll\_supplements
      </td>

      <td>
        [`Payroll > Supplement`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-payroll-supplements)
      </td>
    </tr>

    <tr>
      <td>
        performance
      </td>

      <td>
        [`Performance > Agreement`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-performance-agreements)\
        [`Performance > CompanyEmployeeScoreScale`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-performance-company-employee-score-scales)\
        [`Performance > EmployeeScoreScale`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-performance-employee-score-scales)\
        [`Performance > ReviewEmployeeScore`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-performance-review-employee-scores)\
        [`Performance > ReviewEvaluation`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-performance-review-evaluations)\
        [`Performance > ReviewEvaluationAnswer`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-performance-review-evaluation-answers)\
        [`Performance > ReviewOwner`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-performance-review-owners)\
        [`Performance > ReviewProcess`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-performance-review-processes)\
        [`Performance > ReviewEstimatedTarget`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-performance-review-process-estimated-targets)\
        [`Performance > ReviewProcessTarget`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-performance-review-process-targets)\
        [`Performance > ReviewQuestionnarieByStrategy`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-performance-review-questionnaire-by-strategies)\
        [`Performance > ReviewVisibilitySetting`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-performance-review-visibility-settings)\
        [`Performance > TargetManager`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-performance-target-managers)
      </td>
    </tr>

    <tr>
      <td>
        posts
      </td>

      <td>
        [`Posts > Comment`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-posts-comments)\
        [`Posts > Group`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-posts-groups)\
        [`Posts > Post`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-posts-posts)
      </td>
    </tr>

    <tr>
      <td>
        project\_management\_expenses
      </td>

      <td>
        [`ProjectManagement > ExpenseRecord`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-project-management-expense-records)\
        [`ProjectManagement > ExportableExpense`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-project-management-exportable-expenses)\
        [`ProjectManagement > ExportableProject`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-project-management-exportable-projects)
      </td>
    </tr>

    <tr>
      <td>
        project\_management\_projects
      </td>

      <td>
        [`ProjectManagement > Project`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-project-management-projects)\
        [`ProjectManagement > ProjectTask`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-project-management-project-tasks)\
        [`ProjectManagement > ProjectWorker`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-project-management-project-workers)\
        [`ProjectManagement > Subproject`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-project-management-subprojects)
      </td>
    </tr>

    <tr>
      <td>
        project\_management\_time
      </td>

      <td>
        [`ProjectManagement > FlexibleTimeRecord`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-project-management-flexible-time-records)\
        [`ProjectManagement > FlexibleTimeRecordComment`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-project-management-flexible-time-record-comments)\
        [`ProjectManagement > TimeRecord`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-project-management-time-records)
      </td>
    </tr>

    <tr>
      <td>
        shift\_management
      </td>

      <td>
        [`ShiftManagement > Shift`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-shift-management-shifts)
      </td>
    </tr>

    <tr>
      <td>
        tasks
      </td>

      <td>
        [`Tasks > Task`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-tasks-tasks)\
        [`Tasks > TaskFile`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-tasks-task-files)
      </td>
    </tr>

    <tr>
      <td>
        time\_off
      </td>

      <td>
        [`Timeoff > Allowance`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-timeoff-allowances)\
        [`Timeoff > AllowanceIncidence`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-timeoff-allowance-incidences)\
        [`Timeoff > AllowanceStat`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-timeoff-allowance-stats)\
        [`Timeoff > BlockedPeriod`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-timeoff-blocked-periods)\
        [`Timeoff > Leave`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-timeoff-leaves)\
        [`Timeoff > LeaveType`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-timeoff-leave-types)\
        [`Timeoff > Policy`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-timeoff-policies)\
        [`Timeoff > PolicyAssignment`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-timeoff-policy-assignments)\
        [`Timeoff > PolicyTimeline`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-timeoff-policy-timelines)
      </td>
    </tr>

    <tr>
      <td>
        time\_tracking
      </td>

      <td>
        [`Attendance > BreakConfiguration`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-attendance-break-configurations)\
        [`Attendance > EditTimesheetRequest`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-attendance-edit-timesheet-requests)\
        [`Attendance > EstimatedTime`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-attendance-estimated-times)\
        [`Attendance > OpenShift`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-attendance-open-shifts)\
        [`Attendance > OvertimeRequest`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-attendance-overtime-requests)\
        [`Attendance > Shift`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-attendance-shifts)\
        [`Attendance > WorkedTime`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-attendance-worked-times)\
        [`TimePlanning > PlanningVersion`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-time-planning-planning-versions)\
        [`TimeSettings > BreakConfiguration`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-time-settings-break-configurations)\
        [`WorkSchedule > DayConfiguration`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-work-schedule-day-configurations)\
        [`WorkSchedule > OverlapPeriod`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-work-schedule-overlap-periods)\
        [`WorkSchedule > Schedule`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-work-schedule-schedules)
      </td>
    </tr>

    <tr>
      <td>
        trainings
      </td>

      <td>
        [`Trainings > Category`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-trainings-categories)\
        [`Trainings > Session`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-trainings-sessions)\
        [`Trainings > SessionAccessMembership`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-trainings-session-access-memberships)\
        [`Trainings > SessionAttendance`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-trainings-session-attendances)\
        [`Trainings > Training`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-trainings-trainings)\
        [`Trainings > TrainingMembership`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-trainings-training-memberships)
      </td>
    </tr>

    <tr>
      <td>
        recruitment
      </td>

      <td>
        [`Ats > Answer`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-ats-answers)\
        [`Ats > Application`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-ats-applications)\
        [`Ats > ApplicationPhase`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-ats-application-phases)\
        [`Ats > Candidate`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-ats-candidates)\
        [`Ats > CandidateSource`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-ats-candidate-sources)\
        [`Ats > EvaluationForm`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-ats-evaluation-forms)\
        [`Ats > Feedback`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-ats-feedbacks)\
        [`Ats > HiringStage`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-ats-hiring-stages)\
        [`Ats > JobPosting`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-ats-job-postings)\
        [`Ats > Message`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-ats-messages)\
        [`Ats > Question`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-ats-questions)\
        [`Ats > RejectionReason`](https://apidoc.factorialhr.com/v2025-04-01/reference/get_api-2025-04-01-resources-ats-rejection-reasons)
      </td>
    </tr>
  </tbody>
</Table>
