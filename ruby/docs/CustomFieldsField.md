# F::CustomFieldsField

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Field identifier |  |
| **field_type** | **String** | The type of the field&#39;s value |  |
| **label_text** | **String** | Field label |  |
| **position** | **Integer** | Field position within employee profile | [optional] |
| **required** | **Boolean** | Requirement to fill this field | [optional] |
| **min_value** | **Integer** | Minimum value in range field type | [optional] |
| **max_value** | **Integer** | Maximum value in range field type | [optional] |
| **legal_entity_name** | **String** | Legal entity name where this field belongs | [optional] |
| **legal_entity_id** | **String** | Legal entity id where this field belongs | [optional] |
| **slug** | **String** | Custom field slug | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::CustomFieldsField.new(
  id: 2,
  field_type: text,
  label_text: T-Shirt Size,
  position: 3,
  required: true,
  min_value: 10,
  max_value: 0,
  legal_entity_name: Factorial Legal,
  legal_entity_id: 1,
  slug: tshirt_size
)
```

