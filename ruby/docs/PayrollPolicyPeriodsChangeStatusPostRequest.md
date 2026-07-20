# F::PayrollPolicyPeriodsChangeStatusPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Policy period id |  |
| **status** | **String** | Status of the policy period |  |
| **notify_employee** | **Boolean** | Flag to notify employees |  |
| **employee_ids** | **Array&lt;String&gt;** | Ids of the employees |  |

## Example

```ruby
require 'factorial_api'

instance = F::PayrollPolicyPeriodsChangeStatusPostRequest.new(
  id: 1,
  status: preparation,
  notify_employee: true,
  employee_ids: [&quot;1&quot;,&quot;2&quot;,&quot;3&quot;]
)
```

