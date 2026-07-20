# F::AtsRejectionReasonApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**ats_rejection_reasons_get**](AtsRejectionReasonApi.md#ats_rejection_reasons_get) | **GET** /api/2026-07-01/resources/ats/rejection_reasons | Reads all Rejection reasons |
| [**ats_rejection_reasons_id_get**](AtsRejectionReasonApi.md#ats_rejection_reasons_id_get) | **GET** /api/2026-07-01/resources/ats/rejection_reasons/{id} | Reads a single Rejection reason |


## ats_rejection_reasons_get

> <AtsRejectionReasonsGet200Response> ats_rejection_reasons_get(opts)

Reads all Rejection reasons

Reads all Rejection reasons

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

api_instance = F::AtsRejectionReasonApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Rejection reasons identifiers
  ats_application_ids: ['inner_example'] # Array<String> | Rejected application identifiers
}

begin
  # Reads all Rejection reasons
  result = api_instance.ats_rejection_reasons_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsRejectionReasonApi->ats_rejection_reasons_get: #{e}"
end
```

#### Using the ats_rejection_reasons_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsRejectionReasonsGet200Response>, Integer, Hash)> ats_rejection_reasons_get_with_http_info(opts)

```ruby
begin
  # Reads all Rejection reasons
  data, status_code, headers = api_instance.ats_rejection_reasons_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsRejectionReasonsGet200Response>
rescue F::ApiError => e
  puts "Error when calling AtsRejectionReasonApi->ats_rejection_reasons_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Rejection reasons identifiers | [optional] |
| **ats_application_ids** | [**Array&lt;String&gt;**](String.md) | Rejected application identifiers | [optional] |

### Return type

[**AtsRejectionReasonsGet200Response**](AtsRejectionReasonsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_rejection_reasons_id_get

> <AtsRejectionReason> ats_rejection_reasons_id_get(id)

Reads a single Rejection reason

Reads a single Rejection reason

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

api_instance = F::AtsRejectionReasonApi.new
id = '1' # String | Rejection reasons identifiers

begin
  # Reads a single Rejection reason
  result = api_instance.ats_rejection_reasons_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsRejectionReasonApi->ats_rejection_reasons_id_get: #{e}"
end
```

#### Using the ats_rejection_reasons_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsRejectionReason>, Integer, Hash)> ats_rejection_reasons_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Rejection reason
  data, status_code, headers = api_instance.ats_rejection_reasons_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsRejectionReason>
rescue F::ApiError => e
  puts "Error when calling AtsRejectionReasonApi->ats_rejection_reasons_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Rejection reasons identifiers |  |

### Return type

[**AtsRejectionReason**](AtsRejectionReason.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

