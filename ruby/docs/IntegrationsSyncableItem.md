# F::IntegrationsSyncableItem

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **syncable_sync_run_id** | **String** | identifier of a syncable item within the sync run. Refers to the integrations/syncable_sync_run resource |  |
| **sync_payload** | **Object** | data of the item to be synced |  |
| **syncable_type** | **String** | Type of the syncable item |  |

## Example

```ruby
require 'factorial_api'

instance = F::IntegrationsSyncableItem.new(
  syncable_sync_run_id: 1,
  sync_payload: {employee_id&#x3D;1, payroll_concept_id&#x3D;1, legal_entity_id&#x3D;1, amount&#x3D;7500, unit&#x3D;money, effective_on&#x3D;2028-03-31, employee_company_identifier&#x3D;123456},
  syncable_type: compensations/compensation
)
```

