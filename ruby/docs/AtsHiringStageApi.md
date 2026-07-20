# F::AtsHiringStageApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**ats_hiring_stages_get**](AtsHiringStageApi.md#ats_hiring_stages_get) | **GET** /api/2026-07-01/resources/ats/hiring_stages | Reads all Hiring stages |
| [**ats_hiring_stages_id_get**](AtsHiringStageApi.md#ats_hiring_stages_id_get) | **GET** /api/2026-07-01/resources/ats/hiring_stages/{id} | Reads a single Hiring stage |


## ats_hiring_stages_get

> <AtsHiringStagesGet200Response> ats_hiring_stages_get(opts)

Reads all Hiring stages

Reads all Hiring stages

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

api_instance = F::AtsHiringStageApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Identifiers of the hiring stages
  ats_application_phase_id: '1' # String | Identifier of the application phase that belongs to a hiring stage
}

begin
  # Reads all Hiring stages
  result = api_instance.ats_hiring_stages_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsHiringStageApi->ats_hiring_stages_get: #{e}"
end
```

#### Using the ats_hiring_stages_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsHiringStagesGet200Response>, Integer, Hash)> ats_hiring_stages_get_with_http_info(opts)

```ruby
begin
  # Reads all Hiring stages
  data, status_code, headers = api_instance.ats_hiring_stages_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsHiringStagesGet200Response>
rescue F::ApiError => e
  puts "Error when calling AtsHiringStageApi->ats_hiring_stages_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Identifiers of the hiring stages | [optional] |
| **ats_application_phase_id** | **String** | Identifier of the application phase that belongs to a hiring stage | [optional] |

### Return type

[**AtsHiringStagesGet200Response**](AtsHiringStagesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_hiring_stages_id_get

> <AtsHiringStage> ats_hiring_stages_id_get(id)

Reads a single Hiring stage

Reads a single Hiring stage

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

api_instance = F::AtsHiringStageApi.new
id = '1' # String | Identifiers of the hiring stages

begin
  # Reads a single Hiring stage
  result = api_instance.ats_hiring_stages_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsHiringStageApi->ats_hiring_stages_id_get: #{e}"
end
```

#### Using the ats_hiring_stages_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsHiringStage>, Integer, Hash)> ats_hiring_stages_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Hiring stage
  data, status_code, headers = api_instance.ats_hiring_stages_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsHiringStage>
rescue F::ApiError => e
  puts "Error when calling AtsHiringStageApi->ats_hiring_stages_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifiers of the hiring stages |  |

### Return type

[**AtsHiringStage**](AtsHiringStage.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

