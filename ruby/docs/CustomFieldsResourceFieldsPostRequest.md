# F::CustomFieldsResourceFieldsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **schema_id** | **String** | Schema identifier |  |
| **company_id** | **String** | Company identifier |  |
| **label** | **String** | Resource field label | [optional] |
| **field_type** | **String** | Type of the value for the resource field |  |
| **required** | **Boolean** | Requirement to fill this resource field |  |
| **max_value** | **Integer** | Maximum value for range field type | [optional] |
| **min_value** | **Integer** | Minimum value for range field type | [optional] |
| **position** | **Integer** | Field position within schema | [optional] |
| **editable** | **String** | Group for which this field is editable |  |
| **visible** | **String** | Group for which this field is visible |  |
| **options** | **Array&lt;String&gt;** | Array of options to choose from | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::CustomFieldsResourceFieldsPostRequest.new(
  schema_id: 1,
  company_id: 1,
  label: T-shirt size,
  field_type: text,
  required: true,
  max_value: 10,
  min_value: 0,
  position: 2,
  editable: team_leader,
  visible: everybody,
  options: [&quot;yes&quot;,&quot;no&quot;,&quot;maybe&quot;]
)
```

