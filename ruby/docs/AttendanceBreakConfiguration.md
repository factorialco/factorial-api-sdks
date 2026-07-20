# F::AttendanceBreakConfiguration

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **attendance_employees_setting_id** | **String** | Id of the attendance employee setting |  |
| **time_settings_break_configuration_id** | **String** | Id of the time settings break configuration |  |
| **enabled** | **Boolean** | Status of the break configuration if enabled or not |  |
| **name** | **String** | Name of the break configuration | [optional] |
| **paid** | **Boolean** | Check the break configuration is paid or not | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::AttendanceBreakConfiguration.new(
  id: null,
  attendance_employees_setting_id: null,
  time_settings_break_configuration_id: null,
  enabled: null,
  name: null,
  paid: null
)
```

