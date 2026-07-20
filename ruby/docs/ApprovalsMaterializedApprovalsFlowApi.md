# F::ApprovalsMaterializedApprovalsFlowApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**approvals_materialized_approvals_flows_approve_resource_post**](ApprovalsMaterializedApprovalsFlowApi.md#approvals_materialized_approvals_flows_approve_resource_post) | **POST** /api/2026-07-01/resources/approvals/materialized_approvals_flows/approve_resource | Approves an approval flow by resource |
| [**approvals_materialized_approvals_flows_reject_resource_post**](ApprovalsMaterializedApprovalsFlowApi.md#approvals_materialized_approvals_flows_reject_resource_post) | **POST** /api/2026-07-01/resources/approvals/materialized_approvals_flows/reject_resource | Rejects an approval flow by resource |


## approvals_materialized_approvals_flows_approve_resource_post

> <ApprovalsMaterializedApprovalsFlow> approvals_materialized_approvals_flows_approve_resource_post(opts)

Approves an approval flow by resource

Approves the current pending step of an approval flow identified by resource_id and resource_type, without needing to know the materialized_approval_flow_id.

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

api_instance = F::ApprovalsMaterializedApprovalsFlowApi.new
opts = {
  approvals_materialized_approvals_flows_approve_resource_post_request: F::ApprovalsMaterializedApprovalsFlowsApproveResourcePostRequest.new({resource_id: '1', resource_type: 'Timeoff::Leave'}) # ApprovalsMaterializedApprovalsFlowsApproveResourcePostRequest | 
}

begin
  # Approves an approval flow by resource
  result = api_instance.approvals_materialized_approvals_flows_approve_resource_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ApprovalsMaterializedApprovalsFlowApi->approvals_materialized_approvals_flows_approve_resource_post: #{e}"
end
```

#### Using the approvals_materialized_approvals_flows_approve_resource_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ApprovalsMaterializedApprovalsFlow>, Integer, Hash)> approvals_materialized_approvals_flows_approve_resource_post_with_http_info(opts)

```ruby
begin
  # Approves an approval flow by resource
  data, status_code, headers = api_instance.approvals_materialized_approvals_flows_approve_resource_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ApprovalsMaterializedApprovalsFlow>
rescue F::ApiError => e
  puts "Error when calling ApprovalsMaterializedApprovalsFlowApi->approvals_materialized_approvals_flows_approve_resource_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **approvals_materialized_approvals_flows_approve_resource_post_request** | [**ApprovalsMaterializedApprovalsFlowsApproveResourcePostRequest**](ApprovalsMaterializedApprovalsFlowsApproveResourcePostRequest.md) |  | [optional] |

### Return type

[**ApprovalsMaterializedApprovalsFlow**](ApprovalsMaterializedApprovalsFlow.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## approvals_materialized_approvals_flows_reject_resource_post

> <ApprovalsMaterializedApprovalsFlow> approvals_materialized_approvals_flows_reject_resource_post(opts)

Rejects an approval flow by resource

Rejects the current pending step of an approval flow identified by resource_id and resource_type, without needing to know the materialized_approval_flow_id.

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

api_instance = F::ApprovalsMaterializedApprovalsFlowApi.new
opts = {
  approvals_materialized_approvals_flows_reject_resource_post_request: F::ApprovalsMaterializedApprovalsFlowsRejectResourcePostRequest.new({resource_id: '1', resource_type: 'Timeoff::Leave'}) # ApprovalsMaterializedApprovalsFlowsRejectResourcePostRequest | 
}

begin
  # Rejects an approval flow by resource
  result = api_instance.approvals_materialized_approvals_flows_reject_resource_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ApprovalsMaterializedApprovalsFlowApi->approvals_materialized_approvals_flows_reject_resource_post: #{e}"
end
```

#### Using the approvals_materialized_approvals_flows_reject_resource_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ApprovalsMaterializedApprovalsFlow>, Integer, Hash)> approvals_materialized_approvals_flows_reject_resource_post_with_http_info(opts)

```ruby
begin
  # Rejects an approval flow by resource
  data, status_code, headers = api_instance.approvals_materialized_approvals_flows_reject_resource_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ApprovalsMaterializedApprovalsFlow>
rescue F::ApiError => e
  puts "Error when calling ApprovalsMaterializedApprovalsFlowApi->approvals_materialized_approvals_flows_reject_resource_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **approvals_materialized_approvals_flows_reject_resource_post_request** | [**ApprovalsMaterializedApprovalsFlowsRejectResourcePostRequest**](ApprovalsMaterializedApprovalsFlowsRejectResourcePostRequest.md) |  | [optional] |

### Return type

[**ApprovalsMaterializedApprovalsFlow**](ApprovalsMaterializedApprovalsFlow.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

