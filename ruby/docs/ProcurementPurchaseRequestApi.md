# F::ProcurementPurchaseRequestApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**procurement_purchase_requests_get**](ProcurementPurchaseRequestApi.md#procurement_purchase_requests_get) | **GET** /api/2026-07-01/resources/procurement/purchase_requests | Reads all Purchase requests |
| [**procurement_purchase_requests_id_get**](ProcurementPurchaseRequestApi.md#procurement_purchase_requests_id_get) | **GET** /api/2026-07-01/resources/procurement/purchase_requests/{id} | Reads a single Purchase request |


## procurement_purchase_requests_get

> <ProcurementPurchaseRequestsGet200Response> procurement_purchase_requests_get(opts)

Reads all Purchase requests

Fetch one or all purchase requests for the company.

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

api_instance = F::ProcurementPurchaseRequestApi.new
opts = {
  ids: ['inner_example'], # Array<String> | An array of purchase request IDs to filter by.
  requester_employee_ids: ['inner_example'], # Array<String> | An array of employee IDs to filter by as the purchase requester requesters.
  type_ids: ['inner_example'], # Array<String> | An array of purchase type IDs to filter by.
  status: 'approved' # String | Status to filter by.
}

begin
  # Reads all Purchase requests
  result = api_instance.procurement_purchase_requests_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProcurementPurchaseRequestApi->procurement_purchase_requests_get: #{e}"
end
```

#### Using the procurement_purchase_requests_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProcurementPurchaseRequestsGet200Response>, Integer, Hash)> procurement_purchase_requests_get_with_http_info(opts)

```ruby
begin
  # Reads all Purchase requests
  data, status_code, headers = api_instance.procurement_purchase_requests_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProcurementPurchaseRequestsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ProcurementPurchaseRequestApi->procurement_purchase_requests_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | An array of purchase request IDs to filter by. | [optional] |
| **requester_employee_ids** | [**Array&lt;String&gt;**](String.md) | An array of employee IDs to filter by as the purchase requester requesters. | [optional] |
| **type_ids** | [**Array&lt;String&gt;**](String.md) | An array of purchase type IDs to filter by. | [optional] |
| **status** | **String** | Status to filter by. | [optional] |

### Return type

[**ProcurementPurchaseRequestsGet200Response**](ProcurementPurchaseRequestsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## procurement_purchase_requests_id_get

> <ProcurementPurchaseRequest> procurement_purchase_requests_id_get(id)

Reads a single Purchase request

Fetch one or all purchase requests for the company.

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

api_instance = F::ProcurementPurchaseRequestApi.new
id = '678432' # String | An array of purchase request IDs to filter by.

begin
  # Reads a single Purchase request
  result = api_instance.procurement_purchase_requests_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProcurementPurchaseRequestApi->procurement_purchase_requests_id_get: #{e}"
end
```

#### Using the procurement_purchase_requests_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProcurementPurchaseRequest>, Integer, Hash)> procurement_purchase_requests_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Purchase request
  data, status_code, headers = api_instance.procurement_purchase_requests_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProcurementPurchaseRequest>
rescue F::ApiError => e
  puts "Error when calling ProcurementPurchaseRequestApi->procurement_purchase_requests_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | An array of purchase request IDs to filter by. |  |

### Return type

[**ProcurementPurchaseRequest**](ProcurementPurchaseRequest.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

