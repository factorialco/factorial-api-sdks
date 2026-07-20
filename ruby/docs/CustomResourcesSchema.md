# F::CustomResourcesSchema

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Schema identifier |  |
| **name** | **String** | Schema name |  |
| **company_id** | **String** | Company identifier where this schema belongs |  |
| **hidden** | **Boolean** | Manages visibility of the schema |  |
| **position** | **Integer** | Schema position within employee profile | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::CustomResourcesSchema.new(
  id: 1,
  name: Company Offsite,
  company_id: 2,
  hidden: false,
  position: 1
)
```

