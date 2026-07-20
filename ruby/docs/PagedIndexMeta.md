# F::PagedIndexMeta

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **start_cursor** | **String** |  | [optional] |
| **end_cursor** | **String** |  | [optional] |
| **has_previous_page** | **Boolean** |  |  |
| **has_next_page** | **Boolean** |  |  |
| **limit** | **Integer** |  |  |
| **total** | **Integer** |  |  |

## Example

```ruby
require 'factorial_api'

instance = F::PagedIndexMeta.new(
  start_cursor: null,
  end_cursor: null,
  has_previous_page: null,
  has_next_page: null,
  limit: null,
  total: null
)
```

