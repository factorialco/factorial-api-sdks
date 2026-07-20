# F::TrainingsTrainingClassesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | Class name | [optional] |
| **description** | **String** | Class description | [optional] |
| **start_date** | **String** | Traning class start date |  |
| **end_date** | **String** | Traning class end date |  |
| **training_id** | **String** | Training the class belongs to |  |
| **company_id** | **String** | Company identifier the class belongs to |  |
| **author_id** | **String** | access_id associated to the employee that creates the training class, refers to employees/employees endpoint. |  |
| **cost** | **String** | Training-related expenses, such as instructor fees, materials, venue, and logistics. |  |
| **subsidized_cost** | **String** | Amount of training expenses covered by financial aid or grants for this group. |  |
| **indirect_cost** | **String** | General business expenses related to training, such as utilities and administrative fees. |  |
| **salary_cost** | **String** | Cost of all employees&#39; time spent on the course. |  |
| **payment_status** | **String** | Payment status of the training class. |  |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsTrainingClassesPostRequest.new(
  name: Edition 25,
  description: This is the group for the year 2025 edition,
  start_date: 2025-03-24,
  end_date: 2025-03-28,
  training_id: 1,
  company_id: 1,
  author_id: 20,
  cost: 100.0,
  subsidized_cost: 50.0,
  indirect_cost: 30.0,
  salary_cost: 60.0,
  payment_status: pending
)
```

