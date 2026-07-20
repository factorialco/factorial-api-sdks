# F::JobCatalogLevel

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier for the job catalog level. |  |
| **role_id** | **String** | identifier for the job catalog role. |  |
| **name** | **String** | Level name. |  |
| **role_name** | **String** | Role name. |  |
| **order** | **Integer** | Order of the level. |  |
| **archived** | **Boolean** | Shows if the role is archived. |  |
| **is_default** | **Boolean** | Shows if the level is the default one. |  |

## Example

```ruby
require 'factorial_api'

instance = F::JobCatalogLevel.new(
  id: 1,
  role_id: 1,
  name: Senior,
  role_name: Sofware Engineer,
  order: 1,
  archived: false,
  is_default: false
)
```

