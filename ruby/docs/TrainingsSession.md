# F::TrainingsSession

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | id of the session |  |
| **name** | **String** |  |  |
| **training_id** | **String** | Identifier of the course |  |
| **description** | **String** | Session description | [optional] |
| **training_class_id** | **String** | Identifier of the group | [optional] |
| **starts_at** | **String** | Date when the session should start | [optional] |
| **ends_at** | **String** | Date when the session should end | [optional] |
| **due_date** | **String** | Date when the session should end | [optional] |
| **duration** | **String** | The duration in hours and minutes of the session | [optional] |
| **modality** | **String** | The mode the session will be handled, online, in person or hybrid. | [optional] |
| **schedule** | **String** | Session schedule information (scheduled, self-paced) | [optional] |
| **link** | **String** | The link to see material from the session | [optional] |
| **location** | **String** | The place where the session takes place | [optional] |
| **session_attendance_ids** | **Array&lt;String&gt;** |  | [optional] |
| **session_feedback_id** | **String** |  | [optional] |
| **subsidized** | **Boolean** | if the session is subsidized |  |
| **status** | **String** | Status of the session | [optional] |
| **parent_id** | **String** | Id of the recurrent session that is parent of the current one | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsSession.new(
  id: 1,
  name: Session 1,
  training_id: 1,
  description: First session of group January 2025,
  training_class_id: 1,
  starts_at: 2025-02-04T10:31:48.000Z,
  ends_at: 2025-02-04T10:31:48.000Z,
  due_date: 2025-02-04,
  duration: 2.5,
  modality: inperson,
  schedule: schedule,
  link: https://www.google.com,
  location: Address Street 1223,
  session_attendance_ids: [1],
  session_feedback_id: 1,
  subsidized: false,
  status: pending,
  parent_id: 1
)
```

