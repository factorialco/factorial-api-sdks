# F::ProcurementPurchaseOrderApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**procurement_purchase_orders_get**](ProcurementPurchaseOrderApi.md#procurement_purchase_orders_get) | **GET** /api/2026-07-01/resources/procurement/purchase_orders | Reads all Purchase orders |
| [**procurement_purchase_orders_id_get**](ProcurementPurchaseOrderApi.md#procurement_purchase_orders_id_get) | **GET** /api/2026-07-01/resources/procurement/purchase_orders/{id} | Reads a single Purchase order |


## procurement_purchase_orders_get

> <ProcurementPurchaseOrdersGet200Response> procurement_purchase_orders_get(opts)

Reads all Purchase orders

Fetch one or all purchase orders for the company.

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

api_instance = F::ProcurementPurchaseOrderApi.new
opts = {
  ids: ['inner_example'], # Array<String> | An array of purchase order IDs to filter by.
  purchase_request_ids: ['inner_example'], # Array<String> | An array of purchase request IDs to filter by.
  status: 'processing', # String | Status to filter by.
  vendor_ids: ['inner_example'] # Array<String> | Vendor IDs to filter by.
}

begin
  # Reads all Purchase orders
  result = api_instance.procurement_purchase_orders_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProcurementPurchaseOrderApi->procurement_purchase_orders_get: #{e}"
end
```

#### Using the procurement_purchase_orders_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProcurementPurchaseOrdersGet200Response>, Integer, Hash)> procurement_purchase_orders_get_with_http_info(opts)

```ruby
begin
  # Reads all Purchase orders
  data, status_code, headers = api_instance.procurement_purchase_orders_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProcurementPurchaseOrdersGet200Response>
rescue F::ApiError => e
  puts "Error when calling ProcurementPurchaseOrderApi->procurement_purchase_orders_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | An array of purchase order IDs to filter by. | [optional] |
| **purchase_request_ids** | [**Array&lt;String&gt;**](String.md) | An array of purchase request IDs to filter by. | [optional] |
| **status** | **String** | Status to filter by. | [optional] |
| **vendor_ids** | [**Array&lt;String&gt;**](String.md) | Vendor IDs to filter by. | [optional] |

### Return type

[**ProcurementPurchaseOrdersGet200Response**](ProcurementPurchaseOrdersGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## procurement_purchase_orders_id_get

> <ProcurementPurchaseOrder> procurement_purchase_orders_id_get(id)

Reads a single Purchase order

Fetch one or all purchase orders for the company.

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

api_instance = F::ProcurementPurchaseOrderApi.new
id = '678432' # String | An array of purchase order IDs to filter by.

begin
  # Reads a single Purchase order
  result = api_instance.procurement_purchase_orders_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProcurementPurchaseOrderApi->procurement_purchase_orders_id_get: #{e}"
end
```

#### Using the procurement_purchase_orders_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProcurementPurchaseOrder>, Integer, Hash)> procurement_purchase_orders_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Purchase order
  data, status_code, headers = api_instance.procurement_purchase_orders_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProcurementPurchaseOrder>
rescue F::ApiError => e
  puts "Error when calling ProcurementPurchaseOrderApi->procurement_purchase_orders_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | An array of purchase order IDs to filter by. |  |

### Return type

[**ProcurementPurchaseOrder**](ProcurementPurchaseOrder.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

