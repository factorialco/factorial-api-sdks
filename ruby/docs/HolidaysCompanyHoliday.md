# F::HolidaysCompanyHoliday

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Company holiday id |  |
| **location_id** | **String** | Related location id |  |
| **summary** | **String** | Company holiday summary | [optional] |
| **description** | **String** | Company holiday description | [optional] |
| **date** | **String** | Company holiday date |  |
| **half_day** | **String** | If the company holiday is half-day and which part of the day | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::HolidaysCompanyHoliday.new(
  id: 56,
  location_id: 1,
  summary: Christmas Day,
  description: Christmas Day,
  date: 2024-12-25,
  half_day: null
)
```

