# F::PayrollPolicyPeriod

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Policy period id |  |
| **name** | **String** | Policy name with start and end date | [optional] |
| **starts_on** | **String** | The start date of the policy period |  |
| **policy_id** | **String** | The id of the policy associated with the policy period |  |
| **company_id** | **String** | The id of the company |  |
| **ends_on** | **String** | The start date of the policy period |  |
| **period** | **String** | Period for the policy |  |
| **status** | **String** | Policy period status | [optional] |
| **policy_name** | **String** | Policy name | [optional] |
| **calculation_started_at** | **String** | The date and time the calculation started | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::PayrollPolicyPeriod.new(
  id: 1,
  name: Policy name example 20 aug - 13 sep,
  starts_on: 2020-01-01,
  policy_id: 1,
  company_id: 1,
  ends_on: 2020-01-01,
  period: 20 aug - 13 sep 2021,
  status: preparation,
  policy_name: Policy name example,
  calculation_started_at: 2020-01-01
)
```

