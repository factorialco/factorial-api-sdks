# F::TrainingsTrainingsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | Name of the training |  |
| **code** | **String** | Code of the training | [optional] |
| **description** | **String** | Description of the training |  |
| **external_provider** | **String** | External provider of the training | [optional] |
| **external** | **Boolean** | External training |  |
| **category_ids** | **Array&lt;String&gt;** | List of ids of training categories | [optional] |
| **competency_ids** | **Array&lt;String&gt;** | Competency ids of the training | [optional] |
| **author_id** | **String** | The person that creates the training | [optional] |
| **employee_id** | **String** | Employee identifier associated with the training | [optional] |
| **cost** | **Integer** |  | [optional] |
| **subsidized_cost** | **Integer** |  | [optional] |
| **cost_decimal** | **String** |  | [optional] |
| **subsidized_cost_decimal** | **String** |  | [optional] |
| **year** | **Integer** | Year of the training |  |
| **company_id** | **String** | Company identifier of the training | [optional] |
| **attachments** | **Array&lt;Object&gt;** | Attachments of the training |  |
| **valid_for** | **Integer** | The training validity period in years | [optional] |
| **objectives** | **String** | Objectives of the course | [optional] |
| **total_duration** | **Float** | The total duration in hours and minutes of the course | [optional] |
| **is_mandatory** | **Boolean** | This field is used to define if the training is mandatory or not | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsTrainingsPostRequest.new(
  name: Communication Course,
  code: COM-101,
  description: Intermediate-level communication course that focuses on building and enhancing language skills.,
  external_provider: Coursera,
  external: false,
  category_ids: [1, 20],
  competency_ids: [&quot;1&quot;,&quot;2&quot;],
  author_id: 20,
  employee_id: 15,
  cost: 0,
  subsidized_cost: 0,
  cost_decimal: 0.0,
  subsidized_cost_decimal: 0.0,
  year: 2022,
  company_id: 1,
  attachments: null,
  valid_for: 1,
  objectives: Intermediate-level communication course that focuses on building and enhancing language skills.,
  total_duration: 2.5,
  is_mandatory: false
)
```

