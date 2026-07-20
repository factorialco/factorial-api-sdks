# F::TimePlanningPlannedBreaksBulkCreatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **planned_breaks** | **Array&lt;Object&gt;** | List of planned breaks to create |  |

## Example

```ruby
require 'factorial_api'

instance = F::TimePlanningPlannedBreaksBulkCreatePostRequest.new(
  planned_breaks: [{&quot;id&quot;:1,&quot;start_at&quot;:&quot;2020-09-07T06:00:00.000+00:00&quot;,&quot;end_at&quot;:&quot;2020-09-07T15:00:00.000+00:00&quot;,&quot;duration&quot;:30,&quot;break_type&quot;:&quot;semi_flexible&quot;,&quot;break_configuration_id&quot;:1,&quot;shift_id&quot;:1}]
)
```

