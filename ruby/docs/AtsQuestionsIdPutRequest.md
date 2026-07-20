# F::AtsQuestionsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the question |  |
| **label** | **String** | text of the question | [optional] |
| **position** | **Integer** | position of the question in the list | [optional] |
| **mandatory** | **Boolean** | is the question mandatory or not | [optional] |
| **auto_disqualify** | **Boolean** | if the question autodisqualifies the candidate depending on it&#39;s response. | [optional] |
| **options** | **Array&lt;Object&gt;** | options for the question. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AtsQuestionsIdPutRequest.new(
  id: 1,
  label: Are you open to relocate?,
  position: 1,
  mandatory: true,
  auto_disqualify: false,
  options: [{text&#x3D;Yes, disqualifies&#x3D;false}, {text&#x3D;No, disqualifies&#x3D;false}]
)
```

