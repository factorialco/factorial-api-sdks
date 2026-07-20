# F::TrainingsTrainingMembership

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier for the training membership. |  |
| **access_id** | **String** | Access_id associated to the employee, refers to employees/employees endpoint. |  |
| **employee_id** | **String** | Employee_id associated to the employee, refers to employees/employees endpoint. |  |
| **training_id** | **String** | This field is used to filter those trainings memberships that belongs to this training. |  |
| **status** | **String** | This field is used to filter those trainings memberships whose attendance status is the given. |  |
| **training_due_date** | **String** | This field is used for those trainings with an expiry date. | [optional] |
| **training_completed_at** | **String** | This field is used to record the date a training was completed for trainings that have an expiry date. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsTrainingMembership.new(
  id: 1,
  access_id: 20,
  employee_id: 20,
  training_id: 1,
  status: notstarted,
  training_due_date: 2022-01-01,
  training_completed_at: 2022-01-01
)
```

