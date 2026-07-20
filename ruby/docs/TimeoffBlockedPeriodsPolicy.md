# F::TimeoffBlockedPeriodsPolicy

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier of the blocked period |  |
| **company_id** | **String** | Company id of the blocked period |  |
| **name** | **String** | Name of the blocked period. |  |
| **leave_type_ids** | **Array&lt;String&gt;** | Leave types for which absence request has been blocked |  |
| **time_periods** | **Array&lt;Object&gt;** | The tenure periods associated with the allowance. |  |
| **strategy** | **String** | Type of access group |  |
| **members** | **Array&lt;String&gt;** | Employees whose timeoff will be affected |  |
| **location_ids** | **Array&lt;String&gt;** | List of locations workplace identifiers where the employees are located | [optional] |
| **team_ids** | **Array&lt;String&gt;** | List of team identifiers which the selected employees belong to | [optional] |
| **legal_entity_ids** | **Array&lt;String&gt;** | List of legal entity identifiers which the selected employees belong to | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffBlockedPeriodsPolicy.new(
  id: 1,
  company_id: 1,
  name: Onboarding period,
  leave_type_ids: [1, 2],
  time_periods: [{name&#x3D;Product offsite, period_type&#x3D;by_contract_start_date, duration&#x3D;2, duration_unit&#x3D;months, start_on&#x3D;2024-01-01, finish_on&#x3D;2024-02-28}],
  strategy: everyone,
  members: [1, 2],
  location_ids: [1, 2],
  team_ids: [1, 2],
  legal_entity_ids: [1, 2]
)
```

