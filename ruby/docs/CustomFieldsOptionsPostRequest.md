# F::CustomFieldsOptionsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **label** | **String** | Title for option |  |
| **is_active** | **Boolean** | Flag to make the option available | [optional] |
| **field_id** | **String** | Custom Fields identifier |  |

## Example

```ruby
require 'factorial_api'

instance = F::CustomFieldsOptionsPostRequest.new(
  label: T-shirt size,
  is_active: true,
  field_id: 2
)
```

