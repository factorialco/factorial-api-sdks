# F::ItManagementItAssetModelsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | IT Asset Model identifier |  |
| **type_name** | **String** | Type name of the IT asset model. Possible values are &#39;laptop&#39;, &#39;desktop&#39;, &#39;tablet&#39;, &#39;phone&#39;, &#39;screen&#39;, &#39;mouse&#39;, &#39;keyboard&#39;, &#39;headset&#39;, &#39;other&#39; |  |
| **brand** | **String** | Brand of the IT asset model |  |
| **name** | **String** | Name/model of the IT asset model |  |
| **company_id** | **String** | Company identifier | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ItManagementItAssetModelsIdPutRequest.new(
  id: 0199e6ea-20c0-73d3-9782-8267dc96773a,
  type_name: laptop,
  brand: Apple,
  name: MacBook Pro,
  company_id: 1
)
```

