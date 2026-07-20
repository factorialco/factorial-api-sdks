# F::TeamsMembershipsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Membership id. |  |
| **lead** | **Boolean** | Assign an employee as a lead for their respective team. | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TeamsMembershipsIdPutRequest.new(
  id: 1,
  lead: true
)
```

