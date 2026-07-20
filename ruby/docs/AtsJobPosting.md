# F::AtsJobPosting

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier for the job posting |  |
| **company_id** | **String** | Identifier of the company associated with the job posting |  |
| **ats_company_id** | **String** | Identifier of the ATS company associated with the job posting |  |
| **title** | **String** | Title of the job posting |  |
| **description** | **String** | Description of the job posting | [optional] |
| **contract_type** | **String** |  | [optional] |
| **category** | **String** |  | [optional] |
| **workplace_type** | **String** |  | [optional] |
| **remote** | **Boolean** | Indicates if the job posting is remote |  |
| **status** | **String** | The current status of the job posting (e.g., draft, published, archived) |  |
| **schedule_type** | **String** | The schedule type of the job posting (e.g., full_time, part_time) | [optional] |
| **team_id** | **String** | Identifier of the team associated with the job posting | [optional] |
| **location_id** | **String** | Identifier of the location associated with the job posting | [optional] |
| **legal_entity_id** | **String** | Identifier of the legal entity associated with the job posting | [optional] |
| **salary_format** | **String** | The format of the salary (e.g., range, fixed_amount) | [optional] |
| **salary_from_amount_in_cents** | **Integer** | The minimum salary amount in cents | [optional] |
| **salary_to_amount_in_cents** | **Integer** | The maximum salary amount in cents | [optional] |
| **hide_salary** | **Boolean** | Indicates whether the salary information for the job posting should be hidden from applicants. | [optional] |
| **cv_requirement** | **String** | Requirement for the CV (e.g, mandatory, optional, do_not_ask) |  |
| **cover_letter_requirement** | **String** | Requirement for the cover letter (e.g, mandatory, optional, do_not_ask) |  |
| **phone_requirement** | **String** | Requirement for the phone number (e.g, mandatory, optional, do_not_ask) |  |
| **photo_requirement** | **String** | Requirement for the phone number (e.g, mandatory, optional, do_not_ask) |  |
| **personal_url_requirement** | **String** | Requirement for the personal URL (e.g, mandatory, optional, do_not_ask) |  |
| **url** | **String** | If published, the public URL of the job posting. Otherwise will be null | [optional] |
| **salary_period** | **String** | The period of the salary (e.g., annual, monthly, daily) |  |
| **published_at** | **String** | Published date in ISO 8601 format of the job. If never been published the value will be null | [optional] |
| **created_at** | **String** | Date in ISO 8601 format when the job posting was created |  |

## Example

```ruby
require 'factorial_api'

instance = F::AtsJobPosting.new(
  id: 1,
  company_id: 1,
  ats_company_id: 1,
  title: My job title,
  description: My job description,
  contract_type: indefinite,
  category: engineering,
  workplace_type: onsite,
  remote: true,
  status: draft,
  schedule_type: full_time,
  team_id: 1,
  location_id: 1,
  legal_entity_id: 1,
  salary_format: range,
  salary_from_amount_in_cents: 3000000,
  salary_to_amount_in_cents: 5000000,
  hide_salary: false,
  cv_requirement: mandatory,
  cover_letter_requirement: optional,
  phone_requirement: do_not_ask,
  photo_requirement: do_not_ask,
  personal_url_requirement: do_not_ask,
  url: https://my-factorial-domain/job_posting/job-title-slug,
  salary_period: annual,
  published_at: 2024-07-02T08:28:00.000Z,
  created_at: 2024-07-10T13:30:02.000Z
)
```

