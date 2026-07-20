# F::ItManagementItAssetsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **it_asset_model_id** | **String** | IT Asset Model identifier |  |
| **serial_number** | **String** | Serial number of the IT asset |  |
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

instance = F::ItManagementItAssetsPostRequest.new(
  it_asset_model_id: 0199e6ea-20c0-73d3-9782-8267dc96773a,
  serial_number: SN123456789,
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
  company_id: 1
)
```

