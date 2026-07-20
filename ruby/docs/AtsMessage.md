# F::AtsMessage

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **content** | **String** |  |  |
| **ats_conversation_id** | **String** |  |  |
| **sent_by_id** | **String** |  |  |
| **sent_by_type** | **String** |  |  |
| **created_at** | **String** |  |  |
| **attachments** | **Array&lt;Object&gt;** |  |  |
| **topic** | **String** |  |  |
| **delayed_until** | **String** |  | [optional] |
| **sent_at** | **String** |  | [optional] |
| **delivered_at** | **String** |  | [optional] |
| **opened_at** | **String** |  | [optional] |
| **last_error_at** | **String** |  | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsMessage.new(
  id: null,
  content: null,
  ats_conversation_id: null,
  sent_by_id: null,
  sent_by_type: null,
  created_at: null,
  attachments: null,
  topic: null,
  delayed_until: null,
  sent_at: null,
  delivered_at: null,
  opened_at: null,
  last_error_at: null
)
```

