# F::CustomResourcesValuesPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **schema_id** | **String** | Identifier of the schema this value belongs to |  |
| **employee_id** | **String** | The identifier of the employee that owns the resource value |  |
| **custom_resource_id** | **String** | The identifier of the resource that owns the resource value | [optional] |
| **field_id** | **String** | Identifier of the field this value belongs to |  |
| **value** | **String** | Value for schema custom field |  |

## Example

```ruby
require 'factorial_api'

instance = F::CustomResourcesValuesPostRequest.new(
  schema_id: 1,
  employee_id: 1,
  custom_resource_id: 1,
  field_id: 2,
  value: This is an example value for a custom field
)
```

