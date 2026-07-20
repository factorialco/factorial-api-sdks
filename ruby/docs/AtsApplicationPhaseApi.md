# F::AtsApplicationPhaseApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**ats_application_phases_get**](AtsApplicationPhaseApi.md#ats_application_phases_get) | **GET** /api/2026-07-01/resources/ats/application_phases | Reads all Application phases |
| [**ats_application_phases_id_get**](AtsApplicationPhaseApi.md#ats_application_phases_id_get) | **GET** /api/2026-07-01/resources/ats/application_phases/{id} | Reads a single Application phase |


## ats_application_phases_get

> <AtsApplicationPhasesGet200Response> ats_application_phases_get(opts)

Reads all Application phases

Reads all Application phases

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

api_instance = F::AtsApplicationPhaseApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Application phases identifiers
  ats_job_posting_ids: ['inner_example'] # Array<String> | Job posting of application phases identifiers
}

begin
  # Reads all Application phases
  result = api_instance.ats_application_phases_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsApplicationPhaseApi->ats_application_phases_get: #{e}"
end
```

#### Using the ats_application_phases_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsApplicationPhasesGet200Response>, Integer, Hash)> ats_application_phases_get_with_http_info(opts)

```ruby
begin
  # Reads all Application phases
  data, status_code, headers = api_instance.ats_application_phases_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsApplicationPhasesGet200Response>
rescue F::ApiError => e
  puts "Error when calling AtsApplicationPhaseApi->ats_application_phases_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Application phases identifiers | [optional] |
| **ats_job_posting_ids** | [**Array&lt;String&gt;**](String.md) | Job posting of application phases identifiers | [optional] |

### Return type

[**AtsApplicationPhasesGet200Response**](AtsApplicationPhasesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_application_phases_id_get

> <AtsApplicationPhase> ats_application_phases_id_get(id)

Reads a single Application phase

Reads a single Application phase

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

api_instance = F::AtsApplicationPhaseApi.new
id = '1' # String | Application phases identifiers

begin
  # Reads a single Application phase
  result = api_instance.ats_application_phases_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsApplicationPhaseApi->ats_application_phases_id_get: #{e}"
end
```

#### Using the ats_application_phases_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsApplicationPhase>, Integer, Hash)> ats_application_phases_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Application phase
  data, status_code, headers = api_instance.ats_application_phases_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsApplicationPhase>
rescue F::ApiError => e
  puts "Error when calling AtsApplicationPhaseApi->ats_application_phases_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Application phases identifiers |  |

### Return type

[**AtsApplicationPhase**](AtsApplicationPhase.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

