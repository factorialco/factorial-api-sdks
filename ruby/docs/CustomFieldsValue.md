# F::CustomFieldsValue

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier for the custom field value |  |
| **value** | [**Unknown**](Unknown.md) | Custom Fields value | [optional] |
| **long_text_value** | **String** | Custom field text value | [optional] |
| **custom_field_identifier** | **String** | The unique identifier of the custom field |  |
| **date_value** | **String** | Custom field date value | [optional] |
| **single_choice_value** | **String** | Custom field single choice value | [optional] |
| **cents_value** | **Integer** | Custom field number value | [optional] |
| **valuable_id** | **String** | The identifier of the object that owns this custom field value |  |
| **field_id** | **String** | The identifier of the custom field |  |
| **valuable_type** | **String** | The type of the object that owns this custom field value |  |
| **label** | **String** | The label of the custom field | [optional] |
| **required** | **Boolean** | Whether the custom field is required | [optional] |
| **usage_group_id** | **String** | The identifier of the usage group | [optional] |
| **usage_group_slug** | **String** | The slug of the usage group | [optional] |
| **updated_at** | **String** | The date and time the custom field value was last updated. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::CustomFieldsValue.new(
  id: 73,
  value: 1235436,
  long_text_value: 1235436,
  custom_field_identifier: 01f931507aa27e1168025e27cd46b8588435b741,
  date_value: 2024-10-06,
  single_choice_value: Option 1,
  cents_value: 100,
  valuable_id: 18,
  field_id: 75,
  valuable_type: Employee,
  label: Matricule,
  required: true,
  usage_group_id: 37,
  usage_group_slug: employees-questions,
  updated_at: 2024-10-06T00:00:00.000Z
)
```

