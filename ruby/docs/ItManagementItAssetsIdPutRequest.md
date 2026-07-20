# F::ItManagementItAssetsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | IT Asset identifier |  |
| **it_asset_model_id** | **String** | IT Asset Model identifier (Endpoints related to ItManagement/it_asset_models). | [optional] |
| **serial_number** | **String** | Serial number of the IT asset | [optional] |
| **status** | **String** | Status of the IT asset. Possible values: - &#x60;assigned&#x60;: Asset is assigned to an employee - &#x60;in_stock&#x60;: Asset is available in inventory - &#x60;maintenance&#x60;: Asset is under maintenance or repair - &#x60;retired&#x60;: Asset has been retired or decommissioned  Note: Not all status transitions are allowed. For example, an asset cannot be directly changed from &#x60;assigned&#x60; or &#x60;in_stock&#x60; to certain other statuses without proper workflow validation.  | [optional] |
| **owner_id** | **String** | Owner (employee) identifier | [optional] |
| **location_id** | **String** | Space identifier | [optional] |
| **workplace_id** | **String** | Workplace identifier | [optional] |
| **team_id** | **String** | Team identifier | [optional] |
| **purchase_date** | **String** | Purchase date of the IT asset (YYYY-MM-DD) | [optional] |
| **purchase_price_cents** | **Integer** | Purchase price in cents | [optional] |
| **currency** | **String** | Currency of the purchase price | [optional] |
| **warranty_end_date** | **String** | Warranty end date of the IT asset (YYYY-MM-DD) | [optional] |
| **label** | **String** | Label of the IT asset | [optional] |
| **notes** | **String** | Notes about the IT asset | [optional] |
| **company_id** | **String** | Company identifier | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ItManagementItAssetsIdPutRequest.new(
  id: 0199e6ea-20c0-73d3-9782-8267dc96773a,
  it_asset_model_id: 0199e6ea-20c0-73d3-9782-8267dc96773a,
  serial_number: SN123456789,
  status: maintenance,
  owner_id: null,
  location_id: null,
  workplace_id: null,
  team_id: null,
  purchase_date: 2024-01-01,
  purchase_price_cents: 100000,
  currency: EUR,
  warranty_end_date: 2027-01-01,
  label: null,
  notes: null,
  company_id: 1
)
```

