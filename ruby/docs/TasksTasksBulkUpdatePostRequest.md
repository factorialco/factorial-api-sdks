# F::TasksTasksBulkUpdatePostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **tasks** | **Array&lt;Object&gt;** | a list of tasks to update. |  |

## Example

```ruby
require 'factorial_api'

instance = F::TasksTasksBulkUpdatePostRequest.new(
  tasks: [{&quot;id&quot;:1,&quot;name&quot;:&quot;My task&quot;,&quot;content&quot;:&quot;Complete your performance review before Friday&quot;,&quot;due_on&quot;:&quot;2024-06-06&quot;,&quot;assignee_ids&quot;:[1],&quot;status&quot;:&quot;todo&quot;}]
)
```

