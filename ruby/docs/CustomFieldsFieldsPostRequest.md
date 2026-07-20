# F::CustomFieldsFieldsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **company_id** | **String** | Company identifier where this field belongs |  |
| **editable** | **String** | Group of employees that can edit the field | [optional] |
| **visible** | **String** | Group of employees that can see the field | [optional] |
| **label** | **String** | Field label | [optional] |
| **field_type** | **String** |  |  |
| **min_value** | **Integer** | Minimum value in range field type | [optional] |
| **max_value** | **Integer** | Maximum value in range field type | [optional] |
| **required** | **Boolean** | Requirement to fill this field | [optional] |
| **options** | **Array&lt;String&gt;** | Array of options | [optional] |
| **position** | **Integer** |  | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::CustomFieldsFieldsPostRequest.new(
  company_id: 3,
  editable: owned,
  visible: everybody,
  label: T-Shirt Size,
  field_type: null,
  min_value: 10,
  max_value: 0,
  required: true,
  options: [true,false,&quot;maybe&quot;],
  position: null
)
```

