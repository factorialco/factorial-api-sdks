# F::JobCatalogLevelApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**job_catalog_levels_get**](JobCatalogLevelApi.md#job_catalog_levels_get) | **GET** /api/2026-07-01/resources/job_catalog/levels | Reads all Levels |
| [**job_catalog_levels_id_get**](JobCatalogLevelApi.md#job_catalog_levels_id_get) | **GET** /api/2026-07-01/resources/job_catalog/levels/{id} | Reads a single Level |


## job_catalog_levels_get

> <JobCatalogLevelsGet200Response> job_catalog_levels_get(opts)

Reads all Levels

This returns the job catalog levels

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

api_instance = F::JobCatalogLevelApi.new
opts = {
  ids: ['inner_example'], # Array<String> | filter by level ids.
  role_ids: ['inner_example'] # Array<String> | filter by role ids.
}

begin
  # Reads all Levels
  result = api_instance.job_catalog_levels_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling JobCatalogLevelApi->job_catalog_levels_get: #{e}"
end
```

#### Using the job_catalog_levels_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<JobCatalogLevelsGet200Response>, Integer, Hash)> job_catalog_levels_get_with_http_info(opts)

```ruby
begin
  # Reads all Levels
  data, status_code, headers = api_instance.job_catalog_levels_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <JobCatalogLevelsGet200Response>
rescue F::ApiError => e
  puts "Error when calling JobCatalogLevelApi->job_catalog_levels_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | filter by level ids. | [optional] |
| **role_ids** | [**Array&lt;String&gt;**](String.md) | filter by role ids. | [optional] |

### Return type

[**JobCatalogLevelsGet200Response**](JobCatalogLevelsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## job_catalog_levels_id_get

> <JobCatalogLevel> job_catalog_levels_id_get(id)

Reads a single Level

This returns the job catalog levels

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

api_instance = F::JobCatalogLevelApi.new
id = '1' # String | filter by level ids.

begin
  # Reads a single Level
  result = api_instance.job_catalog_levels_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling JobCatalogLevelApi->job_catalog_levels_id_get: #{e}"
end
```

#### Using the job_catalog_levels_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<JobCatalogLevel>, Integer, Hash)> job_catalog_levels_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Level
  data, status_code, headers = api_instance.job_catalog_levels_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <JobCatalogLevel>
rescue F::ApiError => e
  puts "Error when calling JobCatalogLevelApi->job_catalog_levels_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | filter by level ids. |  |

### Return type

[**JobCatalogLevel**](JobCatalogLevel.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

