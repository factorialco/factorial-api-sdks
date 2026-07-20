# F::TimeoffPolicyTimelineApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**timeoff_policy_timelines_get**](TimeoffPolicyTimelineApi.md#timeoff_policy_timelines_get) | **GET** /api/2026-07-01/resources/timeoff/policy_timelines | Reads all Policy timelines |


## timeoff_policy_timelines_get

> <TimeoffPolicyTimelinesGet200Response> timeoff_policy_timelines_get(employee_id, reference_date)

Reads all Policy timelines

Reads all Policy timelines

### Examples

```ruby
require 'time'
require 'factorial_api'
# setup authorization
F.configure do |config|
  # Configure API key authorization: apikey
  config.api_key['x-api-key'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x-api-key'] = 'Bearer'

  # Configure OAuth2 access token for authorization: oauth2
  config.access_token = 'YOUR ACCESS TOKEN'
end

api_instance = F::TimeoffPolicyTimelineApi.new
employee_id = 'employee_id_example' # String | 
reference_date = 'reference_date_example' # String | 

begin
  # Reads all Policy timelines
  result = api_instance.timeoff_policy_timelines_get(employee_id, reference_date)
  p result
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyTimelineApi->timeoff_policy_timelines_get: #{e}"
end
```

#### Using the timeoff_policy_timelines_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TimeoffPolicyTimelinesGet200Response>, Integer, Hash)> timeoff_policy_timelines_get_with_http_info(employee_id, reference_date)

```ruby
begin
  # Reads all Policy timelines
  data, status_code, headers = api_instance.timeoff_policy_timelines_get_with_http_info(employee_id, reference_date)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TimeoffPolicyTimelinesGet200Response>
rescue F::ApiError => e
  puts "Error when calling TimeoffPolicyTimelineApi->timeoff_policy_timelines_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_id** | **String** |  |  |
| **reference_date** | **String** |  |  |

### Return type

[**TimeoffPolicyTimelinesGet200Response**](TimeoffPolicyTimelinesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

