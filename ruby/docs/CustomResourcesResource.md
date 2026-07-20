# F::CustomResourcesResource

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The id of the Resource |  |
| **schema_id** | **String** | The id of the Schema this resource belongs to |  |
| **attachable_type** | **String** | Attachable type (the type of the attachable) |  |
| **attachable_id** | **String** | The id of the Attachable |  |

## Example

```ruby
require 'factorial_api'

instance = F::CustomResourcesResource.new(
  id: 1,
  schema_id: 2,
  attachable_type: Employee,
  attachable_id: 1
)
```

