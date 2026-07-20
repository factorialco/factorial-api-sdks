# F::MarketplaceInstallationsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **company_id** | **String** | Identifier of the company |  |
| **integration_uuid** | **String** | UUID of the integration |  |

## Example

```ruby
require 'factorial_api'

instance = F::MarketplaceInstallationsPostRequest.new(
  company_id: 1,
  integration_uuid: 123e4567-e89b-12d3-a456-426614174000
)
```

