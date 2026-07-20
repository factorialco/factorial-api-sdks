# F::TrainingsSessionsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | Session name |  |
| **training_id** | **String** | Training this session belongs to |  |
| **description** | **String** | Session specific description | [optional] |
| **training_class_id** | **String** | Training class it belongs to | [optional] |
| **starts_at** | **String** | Start date for the session, if scheduled, starts at and ends at needs to happen within the same day. | [optional] |
| **ends_at** | **String** | End date for the session, if scheduled, starts at and ends at needs to happen within the same day. | [optional] |
| **due_date** | **String** | Only necessary for self paced sessions. | [optional] |
| **duration** | **String** | Duration in hours of the session | [optional] |
| **modality** | **String** | Online, In person or mixed | [optional] |
| **schedule** | **String** | Scheduled or Self paced. Scheduled needs to have a start time and end time within the same day, self paced can start and end in different days and specific time won&#39;t be shown in the frontend app. | [optional] |
| **link** | **String** | Link to join the session if it&#39;s online, or to access or download related material for the session. | [optional] |
| **location** | **String** | Place where the session will happen if modality is mixed or in person. | [optional] |
| **subsidized** | **Boolean** | Mark the session as subsidized | [optional] |
| **recurrent** | **Boolean** | - | [optional] |
| **reminders** | **Array&lt;Object&gt;** | Session reminder notifications for those assigned to the session | [optional] |
| **send_calendar_invites** | **Boolean** | Send calendar invites to attendees assigned to the session | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsSessionsPostRequest.new(
  name: Session one,
  training_id: null,
  description: This is the first session of this training class,
  training_class_id: null,
  starts_at: null,
  ends_at: null,
  due_date: null,
  duration: 1.5 &#x3D;&gt; 1h 30m,
  modality: null,
  schedule: null,
  link: null,
  location: null,
  subsidized: null,
  recurrent: null,
  reminders: null,
  send_calendar_invites: false
)
```

