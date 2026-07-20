# F::CompensationsConceptApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**compensations_concepts_get**](CompensationsConceptApi.md#compensations_concepts_get) | **GET** /api/2026-07-01/resources/compensations/concepts | Reads all Concepts |
| [**compensations_concepts_id_get**](CompensationsConceptApi.md#compensations_concepts_id_get) | **GET** /api/2026-07-01/resources/compensations/concepts/{id} | Reads a single Concept |


## compensations_concepts_get

> <CompensationsConceptsGet200Response> compensations_concepts_get(opts)

Reads all Concepts

Reads all Concepts

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

api_instance = F::CompensationsConceptApi.new
opts = {
  ids: ['inner_example'], # Array<String> | The ids of the concepts
  categories: ['inner_example'], # Array<String> | The categories of the concept
  with_active_status: true # Boolean | Whether to return only active concepts
}

begin
  # Reads all Concepts
  result = api_instance.compensations_concepts_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling CompensationsConceptApi->compensations_concepts_get: #{e}"
end
```

#### Using the compensations_concepts_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CompensationsConceptsGet200Response>, Integer, Hash)> compensations_concepts_get_with_http_info(opts)

```ruby
begin
  # Reads all Concepts
  data, status_code, headers = api_instance.compensations_concepts_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CompensationsConceptsGet200Response>
rescue F::ApiError => e
  puts "Error when calling CompensationsConceptApi->compensations_concepts_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | The ids of the concepts | [optional] |
| **categories** | [**Array&lt;String&gt;**](String.md) | The categories of the concept | [optional] |
| **with_active_status** | **Boolean** | Whether to return only active concepts | [optional] |

### Return type

[**CompensationsConceptsGet200Response**](CompensationsConceptsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## compensations_concepts_id_get

> <CompensationsConcept> compensations_concepts_id_get(id)

Reads a single Concept

Reads a single Concept

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

api_instance = F::CompensationsConceptApi.new
id = '1' # String | The ids of the concepts

begin
  # Reads a single Concept
  result = api_instance.compensations_concepts_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling CompensationsConceptApi->compensations_concepts_id_get: #{e}"
end
```

#### Using the compensations_concepts_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CompensationsConcept>, Integer, Hash)> compensations_concepts_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Concept
  data, status_code, headers = api_instance.compensations_concepts_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CompensationsConcept>
rescue F::ApiError => e
  puts "Error when calling CompensationsConceptApi->compensations_concepts_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The ids of the concepts |  |

### Return type

[**CompensationsConcept**](CompensationsConcept.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

