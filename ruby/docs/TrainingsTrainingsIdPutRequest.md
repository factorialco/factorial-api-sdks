# F::TrainingsTrainingsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **name** | **String** |  |  |
| **code** | **String** |  | [optional] |
| **description** | **String** |  |  |
| **external_provider** | **String** |  | [optional] |
| **external** | **Boolean** |  |  |
| **category_ids** | **Array&lt;String&gt;** |  | [optional] |
| **competency_ids** | **Array&lt;String&gt;** |  | [optional] |
| **cost** | **Integer** |  | [optional] |
| **subsidized_cost** | **Integer** |  | [optional] |
| **cost_decimal** | **String** |  | [optional] |
| **subsidized_cost_decimal** | **String** |  | [optional] |
| **year** | **Integer** |  |  |
| **valid_for** | **Integer** |  | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TrainingsTrainingsIdPutRequest.new(
  id: null,
  name: null,
  code: null,
  description: null,
  external_provider: null,
  external: null,
  category_ids: null,
  competency_ids: null,
  cost: null,
  subsidized_cost: null,
  cost_decimal: null,
  subsidized_cost_decimal: null,
  year: null,
  valid_for: null
)
```

