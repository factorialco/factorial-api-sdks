# F::CustomFieldsValuesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **field_id** | **String** | Custom Fields identifier |  |
| **valuable_type** | **String** | Type of the object that the custom field is attached to: &#39;Document&#39; | &#39;Employee&#39; | &#39;Contracts::ContractVersion&#39; | &#39;CustomResources::Value&#39;  |  |
| **valuable_id** | **String** | Identifier of the object that the custom field is attached to |  |
| **value** | **String** | Custom Fields value |  |

## Example

```ruby
require 'factorial_api'

instance = F::CustomFieldsValuesPostRequest.new(
  field_id: 1,
  valuable_type: Employee,
  valuable_id: 1,
  value: This is an example value for a custom field
)
```

