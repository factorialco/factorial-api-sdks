# F::TrainingsTrainingClassesIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | Class name | [optional] |
| **description** | **String** | Class description | [optional] |
| **start_date** | **String** | Traning class start date | [optional] |
| **end_date** | **String** | Traning class end date | [optional] |
| **id** | **String** | Identifier of the training class to update |  |
| **cost** | **String** | Training-related expenses, such as instructor fees, materials, venue, and logistics. |  |
| **subsidized_cost** | **String** | Amount of training expenses covered by financial aid or grants for this group. |  |
| **salary_cost** | **String** | Cost of all employees&#39; time spent on the course. |  |
| **indirect_cost** | **String** | General business expenses related to training, such as utilities and administrative fees. |  |
| **payment_status** | **String** | Payment status of the training class. |  |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsTrainingClassesIdPutRequest.new(
  name: Edition 25,
  description: This is the group for the year 2025 edition,
  start_date: 2025-03-24,
  end_date: 2025-03-28,
  id: 1,
  cost: 100.0,
  subsidized_cost: 50.0,
  salary_cost: 60.0,
  indirect_cost: 30.0,
  payment_status: pending
)
```

