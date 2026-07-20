# F::TimeoffBlockedPeriodsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **name** | **String** | Name of the blocked period. |  |
| **leave_type_ids** | **Array&lt;String&gt;** | List of leave type identifiers for which employees can not request timeoff edited |  |
| **time_periods_attributes** | **Array&lt;Object&gt;** | The tenure periods associated with the allowance edited. |  |
| **strategy** | **String** | Type of access group |  |
| **members** | **Array&lt;String&gt;** | List of employees manually selected | [optional] |
| **query** | **String** |  | [optional] |
| **team_ids** | **Array&lt;String&gt;** | List of team identifiers which the selected employees belong to | [optional] |
| **location_ids** | **Array&lt;String&gt;** | List of locations workplace identifiers where the employees are located | [optional] |
| **legal_entity_ids** | **Array&lt;String&gt;** | List of legal entity identifiers which the selected employees belong to | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffBlockedPeriodsIdPutRequest.new(
  id: null,
  name: Onboarding period edited,
  leave_type_ids: [&quot;1&quot;,&quot;2&quot;],
  time_periods_attributes: [{&quot;name&quot;:&quot;Product offsite updated&quot;,&quot;period_type&quot;:&quot;by_contract_start_date&quot;,&quot;duration&quot;:2,&quot;duration_unit&quot;:&quot;months&quot;,&quot;start_on&quot;:&quot;2024-01-02&quot;,&quot;finish_on&quot;:&quot;2024-02-28&quot;}],
  strategy: fqlmultiselect,
  members: [&quot;25&quot;,&quot;22&quot;,&quot;23&quot;],
  query: null,
  team_ids: [1, 2],
  location_ids: [1, 2],
  legal_entity_ids: [1, 2]
)
```

