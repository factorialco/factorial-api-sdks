# F::JobCatalogRole

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier for the job catalog role. |  |
| **company_id** | **String** | Identifier for the company. |  |
| **name** | **String** | Role name. |  |
| **description** | **String** | Role description. | [optional] |
| **legal_entities_ids** | **Array&lt;String&gt;** | List of legal entities. |  |
| **supervisors_ids** | **Array&lt;String&gt;** | List of supervisors. | [optional] |
| **competencies_ids** | **Array&lt;String&gt;** | List of competencies. | [optional] |
| **archived** | **Boolean** | Shows if the role is archived. |  |

## Example

```ruby
require 'factorial_api'

instance = F::JobCatalogRole.new(
  id: 1,
  company_id: 1,
  name: CFO,
  description: Financial director of the company.,
  legal_entities_ids: [1, 2],
  supervisors_ids: [1, 2],
  competencies_ids: [1, 2],
  archived: true
)
```

