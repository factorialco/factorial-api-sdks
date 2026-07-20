# F::BookkeepersManagementIncidence

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the incidence (aka employee update). |  |
| **employee_id** | **String** | identifier of employee related. | [optional] |
| **legal_entity_id** | **String** | identifier of legal entity related. |  |
| **name** | **String** | name of the incidence (aka employee update). It also represent the incidence type. For example a new hire incidence will be |  |
| **custom_name** | **String** |  | [optional] |
| **target_id** | **String** | The incidence (aka employee update) is also related to a another resource, for example for a leave target, the target identifier will be the leave id. |  |
| **target_type** | **String** | The incidence (aka employee update) is also related to a another resource, for example a leave. This is the target type. The other types are Employee, Contracts::ContractVersion, BookkeepersManagement::ManualIncidence, Finance::CostCenterMembership. |  |
| **starts_on** | **String** | The date the incidence (aka employee update) starts. | [optional] |
| **ends_on** | **String** | The date the incidence (aka employee update) end. | [optional] |
| **read_at** | **String** | The date the incidence (aka employee update) was read. | [optional] |
| **status** | **String** |  |  |
| **company_id** | **String** | identifier of company related. |  |
| **message_from** | **String** | Indicate the message sender on the incidence (aka employee update). It can be any of &#39;bookkeeper&#39;, &#39;admin&#39; | [optional] |
| **has_message** | **Boolean** | Boolean that indicates if the incidence (aka employee update) has unread messages. | [optional] |
| **created_at** | **String** | Date in which incidence (aka employee update) was created. |  |
| **is_reopened** | **Boolean** | Boolean that indicates if the incidence (aka employee update) has been reopened. |  |
| **legal_entity_name** | **String** |  | [optional] |
| **employee_first_name** | **String** |  | [optional] |
| **employee_last_name** | **String** |  | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::BookkeepersManagementIncidence.new(
  id: 1,
  employee_id: 1,
  legal_entity_id: 1,
  name: hiring,
  custom_name: null,
  target_id: 1,
  target_type: Timeoff::Leave,
  starts_on: 2020-01-01,
  ends_on: 2020-01-01,
  read_at: 2020-01-01,
  status: null,
  company_id: 1,
  message_from: admin,
  has_message: true,
  created_at: true,
  is_reopened: true,
  legal_entity_name: null,
  employee_first_name: null,
  employee_last_name: null
)
```

