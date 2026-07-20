# F::ExpensesMileage

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier for the mileage |  |
| **employee_id** | **String** | The ID of the employee that owns the mileage | [optional] |
| **company_id** | **String** | The ID of the company that owns the mileage |  |
| **expenses_expensable_id** | **String** | The ID of the expensable associated with this mileage | [optional] |
| **category** | **Object** | The category of the mileage | [optional] |
| **subcategory** | **String** | The subcategory of the mileage | [optional] |
| **category_id** | **String** | The ID of the category | [optional] |
| **amount** | **Integer** | The amount in cents | [optional] |
| **currency** | **String** | The currency code in ISO 4217 format |  |
| **reimbursable_amount** | **Integer** | The amount to be reimbursed for the mileage in cents. | [optional] |
| **reimbursable_currency** | **String** | The currency for the reimbursable amount. | [optional] |
| **status** | **String** | The status of the mileage |  |
| **mileage** | **Integer** | The distance travelled, expressed in &#x60;units&#x60; | [optional] |
| **units** | **String** | The distance unit &#x60;mileage&#x60; is expressed in (e.g. km) | [optional] |
| **rate** | **String** | The reimbursement rate per distance unit, in &#x60;currency&#x60; | [optional] |
| **from** | **String** | The origin location | [optional] |
| **to** | **String** | The destination location | [optional] |
| **description** | **String** | The description of the mileage | [optional] |
| **effective_on** | **String** | The date when the mileage was effective | [optional] |
| **review_request_at** | **String** | The date when the mileage was requested for review | [optional] |
| **files** | **Array&lt;Object&gt;** | The files associated with the mileage |  |
| **paid_at** | **String** | The date when the mileage was paid | [optional] |
| **payment** | **String** | The payment method |  |
| **ledger_account_id** | **String** | The ID of the ledger account | [optional] |
| **round_trip** | **Boolean** | Indicates if the mileage is a round trip | [optional] |
| **origin_longitude** | **String** | The longitude of the origin of the mileage | [optional] |
| **origin_latitude** | **String** | The latitude of the origin of the mileage | [optional] |
| **destination_longitude** | **String** | The longitude of the destination of the mileage | [optional] |
| **destination_latitude** | **String** | The latitude of the destination of the mileage | [optional] |
| **calculated_mileage** | **Integer** | The calculated mileage between origin and destination in decameters/10-milers | [optional] |
| **budget_id** | **String** | The id of the budget associated with this mileage | [optional] |
| **project_id** | **String** | The id of the project associated with this mileage | [optional] |
| **cost_center_ids** | **Array&lt;String&gt;** | Array of cost center IDs associated with this mileage |  |

## Example

```ruby
require 'factorial_api'

instance = F::ExpensesMileage.new(
  id: 1,
  employee_id: 1,
  company_id: 1,
  expenses_expensable_id: 1,
  category: business_travel,
  subcategory: client_visit,
  category_id: 1,
  amount: 1000,
  currency: EUR,
  reimbursable_amount: 250,
  reimbursable_currency: USD,
  status: approved,
  mileage: 100,
  units: km,
  rate: 0.5,
  from: Madrid,
  to: Barcelona,
  description: Client meeting,
  effective_on: 2024-06-06T12:00:00.000Z,
  review_request_at: 2024-06-06T12:00:00.000Z,
  files: null,
  paid_at: 2024-06-06T12:00:00.000Z,
  payment: reimbursable,
  ledger_account_id: 1,
  round_trip: true,
  origin_longitude: 2.1686,
  origin_latitude: 41.3874,
  destination_longitude: 3.7033,
  destination_latitude: 40.4167,
  calculated_mileage: 62700,
  budget_id: 2,
  project_id: 3,
  cost_center_ids: [4, 5]
)
```

