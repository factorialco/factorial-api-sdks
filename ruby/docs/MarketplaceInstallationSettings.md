# F::MarketplaceInstallationSettings

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **leave_types** | **Array&lt;Object&gt;** | Leave types codes |  |
| **file_numbers** | **Array&lt;Object&gt;** | Legal Entity file numbers |  |
| **establishment_codes** | **Array&lt;Object&gt;** | Workplace establishment codes |  |
| **timeoff_allowance_code** | **Array&lt;Object&gt;** | Timeoff allowance codes |  |

## Example

```ruby
require 'factorial_api'

instance = F::MarketplaceInstallationSettings.new(
  leave_types: [{id&#x3D;holidays, value&#x3D;123456}],
  file_numbers: [{legal_entity_id&#x3D;1, value&#x3D;123456}],
  establishment_codes: [{location_id&#x3D;1, value&#x3D;123456}],
  timeoff_allowance_code: [{id&#x3D;1, value&#x3D;123456}]
)
```

