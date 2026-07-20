# F::CustomFieldsOption

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Option identifier |  |
| **label** | **String** | Title for option | [optional] |
| **value** | **String** | Option value | [optional] |
| **is_active** | **Boolean** | Flag to make the option available | [optional] |
| **field_id** | **String** | Custom Fields identifier | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::CustomFieldsOption.new(
  id: 1,
  label: T-shirt size,
  value: L,
  is_active: true,
  field_id: 2
)
```

