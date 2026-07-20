# F::CustomResourcesValue

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Value identifier |  |
| **resource_id** | **String** | The identifier of the resource that owns the resource value |  |
| **attachable_id** | **String** | The id of the attached resource like an employee | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::CustomResourcesValue.new(
  id: 1,
  resource_id: 1,
  attachable_id: 1
)
```

