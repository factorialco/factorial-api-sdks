# F::CustomResourcesSchemasPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** | Schema name |  |
| **company_id** | **String** | Company identifier where this schema belongs |  |
| **effective_at_id** | **String** | Custom field identifier | [optional] |
| **hidden** | **Boolean** | Manages visibility of the schema |  |
| **position** | **Integer** | Schema position within employee profile | [optional] |
| **usage_group_slug** | **String** | Schema slug | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::CustomResourcesSchemasPostRequest.new(
  name: Company Offsite,
  company_id: 2,
  effective_at_id: 1,
  hidden: false,
  position: 1,
  usage_group_slug: company_offsite
)
```

