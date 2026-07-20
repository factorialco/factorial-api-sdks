# F::TrainingsTraining

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the course |  |
| **company_id** | **String** | Company identifier |  |
| **author_id** | **String** | The person that creates the training |  |
| **author_employee_id** | **String** | Employee identifier of the training author | [optional] |
| **name** | **String** | Name of the training |  |
| **code** | **String** | Code of the training | [optional] |
| **description** | **String** | Description of the training |  |
| **created_at** | **String** | Creation date of the course | [optional] |
| **updated_at** | **String** | Last modification date of the course | [optional] |
| **external_provider** | **String** | The name of the provider if any | [optional] |
| **external** | **Boolean** | External training |  |
| **total_cost** | **Integer** |  | [optional] |
| **fundae_subsidized** | **Boolean** | Subsidized by Fundae |  |
| **subsidized** | **Boolean** | Marked as subsidized |  |
| **cost** | **Integer** |  |  |
| **subsidized_cost** | **Integer** |  |  |
| **total_cost_decimal** | **String** |  | [optional] |
| **cost_decimal** | **String** |  |  |
| **subsidized_cost_decimal** | **String** |  |  |
| **category_ids** | **Array&lt;String&gt;** | List of ids of training categories | [optional] |
| **status** | **String** | Training status. Can be one of the following values | [optional] |
| **year** | **Integer** | Year of the training |  |
| **catalog** | **Boolean** | Visible in catalog |  |
| **competency_ids** | **Array&lt;String&gt;** | List of ids of training competencies |  |
| **total_training_cost** | **String** | The total direct cost of all course&#39;s groups |  |
| **total_training_indirect_cost** | **String** | The total indirect cost of all course&#39;s groups |  |
| **total_training_salary_cost** | **String** | The total salary cost of all course&#39;s groups |  |
| **total_training_subsidized_cost** | **String** | The total subsidized cost of all course&#39;s groups |  |
| **total_participants** | **Integer** | Number of participants of all course&#39;s groups |  |
| **training_attendance_status** | **String** |  |  |
| **valid_for** | **Integer** | Number of years this course is valid for | [optional] |
| **objectives** | **String** | Objectives of the course | [optional] |
| **number_of_expired_participants** | **Integer** | Number of participants that have the course expired or about to expire in the next 3 months. Only applicable to trainings with validity period. | [optional] |
| **total_duration** | **Float** | The total duration in hours and minutes of the course |  |
| **is_mandatory** | **Boolean** | This field is used to define if the training is mandatory or not |  |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsTraining.new(
  id: 1,
  company_id: 1,
  author_id: 20,
  author_employee_id: 15,
  name: Communication Course,
  code: COM-101,
  description: Intermediate-level communication course that focuses on building and enhancing language skills.,
  created_at: 2025-02-04T10:31:48.000Z,
  updated_at: 2025-02-04T10:31:48.000Z,
  external_provider: null,
  external: false,
  total_cost: 0,
  fundae_subsidized: false,
  subsidized: false,
  cost: 0,
  subsidized_cost: 0,
  total_cost_decimal: 0.0,
  cost_decimal: 0.0,
  subsidized_cost_decimal: 0.0,
  category_ids: [1, 20],
  status: active,
  year: 2025,
  catalog: true,
  competency_ids: [1, 3],
  total_training_cost: 0.0,
  total_training_indirect_cost: 0.0,
  total_training_salary_cost: 0.0,
  total_training_subsidized_cost: 0.0,
  total_participants: 0,
  training_attendance_status: completed,
  valid_for: null,
  objectives: Build and enhance language skills.,
  number_of_expired_participants: 2,
  total_duration: 2.5,
  is_mandatory: false
)
```

