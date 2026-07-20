# F::PayrollPolicyPeriodApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**payroll_policy_periods_change_status_post**](PayrollPolicyPeriodApi.md#payroll_policy_periods_change_status_post) | **POST** /api/2026-07-01/resources/payroll/policy_periods/change_status | Change statuses a Policy period |


## payroll_policy_periods_change_status_post

> <PayrollPolicyPeriod> payroll_policy_periods_change_status_post(opts)

Change statuses a Policy period

Change statuses a Policy period

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

api_instance = F::PayrollPolicyPeriodApi.new
opts = {
  payroll_policy_periods_change_status_post_request: F::PayrollPolicyPeriodsChangeStatusPostRequest.new({id: '1', status: 'preparation', notify_employee: true, employee_ids: ["1", "2", "3"]}) # PayrollPolicyPeriodsChangeStatusPostRequest | 
}

begin
  # Change statuses a Policy period
  result = api_instance.payroll_policy_periods_change_status_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling PayrollPolicyPeriodApi->payroll_policy_periods_change_status_post: #{e}"
end
```

#### Using the payroll_policy_periods_change_status_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PayrollPolicyPeriod>, Integer, Hash)> payroll_policy_periods_change_status_post_with_http_info(opts)

```ruby
begin
  # Change statuses a Policy period
  data, status_code, headers = api_instance.payroll_policy_periods_change_status_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PayrollPolicyPeriod>
rescue F::ApiError => e
  puts "Error when calling PayrollPolicyPeriodApi->payroll_policy_periods_change_status_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **payroll_policy_periods_change_status_post_request** | [**PayrollPolicyPeriodsChangeStatusPostRequest**](PayrollPolicyPeriodsChangeStatusPostRequest.md) |  | [optional] |

### Return type

[**PayrollPolicyPeriod**](PayrollPolicyPeriod.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

