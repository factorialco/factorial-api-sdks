# F::ProcurementType

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **author_id** | **String** | Employee ID who created this type (null for system types) | [optional] |
| **company_id** | **String** | Identifier of the company that owns this type |  |
| **created_at** | **String** | Time the procurement type was created |  |
| **description** | **String** | Description of the procurement type | [optional] |
| **enabled** | **Boolean** | Defines if a type is enabled | [optional] |
| **id** | **String** | The id of the type |  |
| **identifier** | **String** | System identifier for default types | [optional] |
| **name** | **String** | Name of the procurement type |  |
| **updated_at** | **String** | Time the procurement type was last updated |  |

## Example

```ruby
require 'factorial_api'

instance = F::ProcurementType.new(
  author_id: 20,
  company_id: 1,
  created_at: 2025-01-01T00:00:00.000Z,
  description: For purchasing software licenses,
  enabled: true,
  id: 1,
  identifier: software_license,
  name: Software Purchase,
  updated_at: 2025-01-01T00:00:00.000Z
)
```

