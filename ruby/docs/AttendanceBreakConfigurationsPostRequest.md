# F::AttendanceBreakConfigurationsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **time_settings_break_configuration_id** | **String** | Id of the time settings break configuration |  |
| **attendance_employees_setting_id** | **String** | Id of the attendance employee setting |  |
| **enabled** | **Boolean** | Status of the break configuration if enabled or not |  |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceBreakConfigurationsPostRequest.new(
  time_settings_break_configuration_id: 1,
  attendance_employees_setting_id: 1,
  enabled: null
)
```

