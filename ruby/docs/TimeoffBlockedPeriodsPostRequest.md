# F::TimeoffBlockedPeriodsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **company_id** | **String** | The company id |  |
| **name** | **String** | Name of the blocked period. |  |
| **leave_type_ids** | **Array&lt;String&gt;** | An array of leave type identifiers for which employees can not request timeoff |  |

## Example

```ruby
require 'factorial_api'

instance = F::TimeoffBlockedPeriodsPostRequest.new(
  company_id: 1,
  name: Onboarding period,
  leave_type_ids: [&quot;1&quot;,&quot;2&quot;,&quot;4&quot;]
)
```

