# F::ItManagementItAsset

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | IT Asset identifier |  |
| **company_id** | **String** | Company identifier |  |
| **it_asset_model_id** | **String** | IT Asset Model identifier |  |
| **serial_number** | **String** | Serial number of the IT asset |  |
| **status** | **String** | Status of the IT asset. Possible values: - &#x60;assigned&#x60;: Asset is assigned to an employee - &#x60;in_stock&#x60;: Asset is available in inventory - &#x60;maintenance&#x60;: Asset is under maintenance or repair - &#x60;retired&#x60;: Asset has been retired or decommissioned  Note: Not all status transitions are allowed. For example, an asset cannot be directly changed from &#x60;assigned&#x60; or &#x60;in_stock&#x60; to certain other statuses without proper workflow validation.  |  |
| **owner_id** | **String** | Owner (employee) identifier | [optional] |
| **location_id** | **String** | Location identifier | [optional] |
| **workplace_id** | **String** | Workplace identifier | [optional] |
| **team_id** | **String** | Team identifier | [optional] |
| **purchase_date** | **String** | Purchase date of the IT asset | [optional] |
| **purchase_price_cents** | **Integer** | Purchase price in cents | [optional] |
| **currency** | **String** | Currency of the purchase price | [optional] |
| **warranty_end_date** | **String** | Warranty end date of the IT asset | [optional] |
| **label** | **String** | Label of the IT asset | [optional] |
| **notes** | **String** | Notes about the IT asset | [optional] |
| **created_at** | **String** | Creation date of the IT asset |  |
| **updated_at** | **String** | Last update date of the IT asset |  |
| **discarded_at** | **String** | Timestamp when the IT asset was soft deleted | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ItManagementItAsset.new(
  id: 0199e6ea-20c0-73d3-9782-8267dc96773a,
  company_id: 1,
  it_asset_model_id: 0199e6ea-20c0-73d3-9782-8267dc96773a,
  serial_number: SN123456789,
  status: in_stock,
  owner_id: 1,
  location_id: null,
  workplace_id: null,
  team_id: null,
  purchase_date: 2024-01-01,
  purchase_price_cents: 100000,
  currency: EUR,
  warranty_end_date: 2027-01-01,
  label: Internal asset label,
  notes: This field is for custom data related to the asset,
  created_at: 2024-01-20T18:05:45.000Z,
  updated_at: 2024-01-20T18:05:45.000Z,
  discarded_at: 2024-01-20T18:05:45.000Z
)
```

