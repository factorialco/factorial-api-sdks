# F::FinanceCostCenterMembershipApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**finance_cost_center_memberships_bulk_create_update_post**](FinanceCostCenterMembershipApi.md#finance_cost_center_memberships_bulk_create_update_post) | **POST** /api/2026-07-01/resources/finance/cost_center_memberships/bulk_create_update | Bulk create updates a Cost center membership |
| [**finance_cost_center_memberships_get**](FinanceCostCenterMembershipApi.md#finance_cost_center_memberships_get) | **GET** /api/2026-07-01/resources/finance/cost_center_memberships | Reads all Cost center memberships |


## finance_cost_center_memberships_bulk_create_update_post

> <Array<FinanceCostCenterMembership>> finance_cost_center_memberships_bulk_create_update_post(opts)

Bulk create updates a Cost center membership

###### **What does it do?** Performs an update of cost center memberships for an employee. The action creates new memberships starting from today, terminating any pre-existing memberships for the employee. This ensures a history of cost center memberships is preserved. ###### **What does the `memberships` array look like?** An array of objects with these properties: - `cost_center_id` - `percentage`: A float between 0 and 1 representing the percentage that the employee is assigned to the cost center. For multiple assignments, the sum of percentages must equal 1.0. For example, for an employee assigned to cost center 1 during 30% of their time and cost center 2 during 70% of their time, the request parameters would look like: `memberships: [{\"cost_center_id\": 1, \"percentage\": 0.3} ,{\"cost_center_id\": 2, \"percentage\": 0.7}]`

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

api_instance = F::FinanceCostCenterMembershipApi.new
opts = {
  finance_cost_center_memberships_bulk_create_update_post_request: F::FinanceCostCenterMembershipsBulkCreateUpdatePostRequest.new({employee_id: 'employee_id_example', memberships: [3.56], company_id: 'company_id_example'}) # FinanceCostCenterMembershipsBulkCreateUpdatePostRequest | 
}

begin
  # Bulk create updates a Cost center membership
  result = api_instance.finance_cost_center_memberships_bulk_create_update_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceCostCenterMembershipApi->finance_cost_center_memberships_bulk_create_update_post: #{e}"
end
```

#### Using the finance_cost_center_memberships_bulk_create_update_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<FinanceCostCenterMembership>>, Integer, Hash)> finance_cost_center_memberships_bulk_create_update_post_with_http_info(opts)

```ruby
begin
  # Bulk create updates a Cost center membership
  data, status_code, headers = api_instance.finance_cost_center_memberships_bulk_create_update_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<FinanceCostCenterMembership>>
rescue F::ApiError => e
  puts "Error when calling FinanceCostCenterMembershipApi->finance_cost_center_memberships_bulk_create_update_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **finance_cost_center_memberships_bulk_create_update_post_request** | [**FinanceCostCenterMembershipsBulkCreateUpdatePostRequest**](FinanceCostCenterMembershipsBulkCreateUpdatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;FinanceCostCenterMembership&gt;**](FinanceCostCenterMembership.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## finance_cost_center_memberships_get

> <FinanceCostCenterMembershipsGet200Response> finance_cost_center_memberships_get(opts)

Reads all Cost center memberships

Reads all Cost center memberships

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

api_instance = F::FinanceCostCenterMembershipApi.new
opts = {
  cost_center_id: '1', # String | To retreive active cost center memberships for a specific cost center
  employee_id: '1', # String | To retreive active cost center memberships for a specific employee
  active_on: '2020-01-01', # String | To retreive active cost center memberships for a specific date
  only_active: false, # Boolean | To retreive only active cost center memberships, this is the default behavior
  applying_on: '2020-01-01', # String | To retreive cost center memberships applying on a specific date
  company_id: '1', # String | retrieve the cost center memberships for a specific company
  cost_center_ids: ['inner_example'] # Array<String> | retrieve the cost center memberships for a list of cost centers
}

begin
  # Reads all Cost center memberships
  result = api_instance.finance_cost_center_memberships_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceCostCenterMembershipApi->finance_cost_center_memberships_get: #{e}"
end
```

#### Using the finance_cost_center_memberships_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceCostCenterMembershipsGet200Response>, Integer, Hash)> finance_cost_center_memberships_get_with_http_info(opts)

```ruby
begin
  # Reads all Cost center memberships
  data, status_code, headers = api_instance.finance_cost_center_memberships_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceCostCenterMembershipsGet200Response>
rescue F::ApiError => e
  puts "Error when calling FinanceCostCenterMembershipApi->finance_cost_center_memberships_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **cost_center_id** | **String** | To retreive active cost center memberships for a specific cost center | [optional] |
| **employee_id** | **String** | To retreive active cost center memberships for a specific employee | [optional] |
| **active_on** | **String** | To retreive active cost center memberships for a specific date | [optional] |
| **only_active** | **Boolean** | To retreive only active cost center memberships, this is the default behavior | [optional] |
| **applying_on** | **String** | To retreive cost center memberships applying on a specific date | [optional] |
| **company_id** | **String** | retrieve the cost center memberships for a specific company | [optional] |
| **cost_center_ids** | [**Array&lt;String&gt;**](String.md) | retrieve the cost center memberships for a list of cost centers | [optional] |

### Return type

[**FinanceCostCenterMembershipsGet200Response**](FinanceCostCenterMembershipsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

