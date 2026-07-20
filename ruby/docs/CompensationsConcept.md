# F::CompensationsConcept

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The identifier of the concept |  |
| **category** | **String** | The category of the concept | [optional] |
| **company_id** | **String** | The company identifier of the concept |  |
| **default** | **Boolean** | Whether the concept is a default or a custom concept |  |
| **description** | **String** | The description of the concept |  |
| **label** | **String** | The label of the concept |  |
| **name** | **String** | The name of the concept |  |
| **translated_name** | **String** | The translated name of the concept if it is a default concept. |  |
| **unit_name** | **String** | The name of the unit of the concept | [optional] |
| **unit_type** | **String** | The type of the unit of the concept | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::CompensationsConcept.new(
  id: 1,
  category: earnings_fixed_salary,
  company_id: 1,
  default: false,
  description: Fixed Comission,
  label: Fixed comission,
  name: fixed_comission,
  translated_name: Fixed comission,
  unit_name: EUR,
  unit_type: money
)
```

