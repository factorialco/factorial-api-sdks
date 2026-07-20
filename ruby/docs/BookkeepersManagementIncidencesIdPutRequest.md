# F::BookkeepersManagementIncidencesIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | incidence (aka employee update) identifier to update. |  |
| **status** | **String** | status of the incidence (aka employee update). It can be any of &#39;in-preparation&#39;, &#39;to-do&#39;, &#39;doing&#39;, &#39;done&#39;, &#39;discarded&#39; | [optional] |
| **has_message** | **Boolean** | Boolean that indicates is the incidence (aka employee update) has message | [optional] |
| **message_from** | **String** |  | [optional] |
| **read_at** | **String** | Date in which the  incidence (aka employee update) was read | [optional] |
| **mark_as_read** | **Boolean** | Boolean that indicate if the incidence is read | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::BookkeepersManagementIncidencesIdPutRequest.new(
  id: 1,
  status: to-do,
  has_message: true,
  message_from: null,
  read_at: 2020-01-01,
  mark_as_read: true
)
```

