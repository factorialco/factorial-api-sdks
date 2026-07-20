# F::JobCatalogNodeAttribute

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier of the node attribute |  |
| **type** | **String** | Type of the attribute (e.g., competency, salary_range, working_conditions, it_management_asset) |  |
| **attribute_id** | **String** | Identifier of the attribute being assigned to the node it it makes sense like in competecies, but not for working_conditions | [optional] |
| **value_competency** | **Object** | Competency payload including name, short description and optional level metadata | [optional] |
| **value_it_management_asset** | **Object** | IT asset payload describing the device assigned to the node | [optional] |
| **value_salary_range** | **Object** | Salary payload (cents) with currency, periodicity, range (min and max) or gross values in cents (35.000 EUR is stored as 3500000) and optional workplaces | [optional] |
| **value_working_conditions** | **Object** | Working-conditions payload with agreement info and simple key/value constraints. Numeric values are stored in cents (40 hours is stored as 4000). | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::JobCatalogNodeAttribute.new(
  id: 1,
  type: competency,
  attribute_id: 1,
  value_competency: {&quot;name&quot;:&quot;Design Fundamentals&quot;,&quot;description&quot;:&quot;Core visual principles&quot;,&quot;level&quot;:{&quot;id&quot;:1,&quot;name&quot;:&quot;Level 1&quot;,&quot;description&quot;:&quot;Understands basics&quot;}},
  value_it_management_asset: {&quot;type_name&quot;:&quot;headset&quot;,&quot;brand&quot;:&quot;Apple&quot;,&quot;name&quot;:&quot;AirPods Pro&quot;},
  value_salary_range: [{&quot;currency&quot;:&quot;EUR&quot;,&quot;periodicity&quot;:&quot;yearly&quot;,&quot;min&quot;:18000,&quot;max&quot;:25000,&quot;workplaces&quot;:[{&quot;id&quot;:1,&quot;name&quot;:&quot;Barcelona HQ&quot;}]}, {&quot;currency&quot;:&quot;EUR&quot;,&quot;periodicity&quot;:&quot;yearly&quot;,&quot;gross&quot;:2000000,&quot;workplaces&quot;:[{&quot;id&quot;:1,&quot;name&quot;:&quot;Barcelona HQ&quot;}]}],
  value_working_conditions: {&quot;name&quot;:&quot;Retail Agreement&quot;,&quot;description&quot;:&quot;Standard UK contract&quot;,&quot;conditions&quot;:[{&quot;key&quot;:&quot;max_weekly_hours&quot;,&quot;value&quot;:&quot;4000&quot;},{&quot;key&quot;:&quot;bank_holidays_treatment&quot;,&quot;value&quot;:&quot;non_workable&quot;}]}
)
```

