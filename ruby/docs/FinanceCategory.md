# F::FinanceCategory

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Unique identifier for the category |  |
| **label** | **String** | Custom label for the category |  |
| **default_label** | **String** | Default translated label for the category |  |
| **parent_category_id** | **String** | Parent category ID (null for main categories) | [optional] |
| **identifier** | **String** | System identifier for the category |  |
| **visible** | **Boolean** | Whether the category is visible |  |
| **enabled** | **Boolean** | Whether the category is enabled |  |
| **position** | **Integer** | Display position of the category | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::FinanceCategory.new(
  id: 1,
  label: Accommodation Expenses,
  default_label: Alojamiento,
  parent_category_id: 2,
  identifier: accommodation,
  visible: true,
  enabled: true,
  position: 1
)
```

