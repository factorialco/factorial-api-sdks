# F::TrainingsTrainingClass

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the training to which the class belongs to |  |
| **training_id** | **String** | Identifier of the course |  |
| **name** | **String** | Class name |  |
| **description** | **String** | Class description | [optional] |
| **start_date** | **String** | Traning class start date | [optional] |
| **end_date** | **String** | Traning class end date | [optional] |
| **cost** | **String** | Training-related expenses, such as instructor fees, materials, venue, and logistics. |  |
| **indirect_cost** | **String** | General business expenses related to training, such as utilities and administrative fees. |  |
| **salary_cost** | **String** | Cost of all employees&#39; time spent on the course. |  |
| **subsidized_cost** | **String** | Amount of training expenses covered by financial aid or grants for this group. |  |
| **gross_cost** | **String** | Total cost before subsidies, calculated as the sum of cost, indirect_cost, and salary_cost. |  |
| **net_cost** | **String** | Final cost after subsidies, calculated as gross_cost minus subsidized_cost. |  |
| **completed_attendances_count** | **Integer** | Number of completed session attendances in this group. |  |
| **total_attendances_count** | **Integer** | Total number of session attendances expected in this group. |  |
| **payment_status** | **String** | Payment status of the cost of training class. | [optional] |
| **currency** | **String** | Currency of the training class |  |
| **created_at** | **String** | Date and time when the training class was created |  |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsTrainingClass.new(
  id: 1,
  training_id: 1,
  name: Edition 25,
  description: This is the group for the year 2025 edition,
  start_date: 2025-03-24,
  end_date: 2025-03-28,
  cost: 100.0,
  indirect_cost: 30.0,
  salary_cost: 60.0,
  subsidized_cost: 50.0,
  gross_cost: 190.0,
  net_cost: 140.0,
  completed_attendances_count: 10,
  total_attendances_count: 15,
  payment_status: pending,
  currency: EUR,
  created_at: 2025-03-24T10:00:00.000Z
)
```

