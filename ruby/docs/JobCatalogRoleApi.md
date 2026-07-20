# F::JobCatalogRoleApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**job_catalog_roles_get**](JobCatalogRoleApi.md#job_catalog_roles_get) | **GET** /api/2026-07-01/resources/job_catalog/roles | Reads all Roles |
| [**job_catalog_roles_id_get**](JobCatalogRoleApi.md#job_catalog_roles_id_get) | **GET** /api/2026-07-01/resources/job_catalog/roles/{id} | Reads a single Role |


## job_catalog_roles_get

> <JobCatalogRolesGet200Response> job_catalog_roles_get(opts)

Reads all Roles

Reads all Roles

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

api_instance = F::JobCatalogRoleApi.new
opts = {
  ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Roles
  result = api_instance.job_catalog_roles_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling JobCatalogRoleApi->job_catalog_roles_get: #{e}"
end
```

#### Using the job_catalog_roles_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<JobCatalogRolesGet200Response>, Integer, Hash)> job_catalog_roles_get_with_http_info(opts)

```ruby
begin
  # Reads all Roles
  data, status_code, headers = api_instance.job_catalog_roles_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <JobCatalogRolesGet200Response>
rescue F::ApiError => e
  puts "Error when calling JobCatalogRoleApi->job_catalog_roles_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**JobCatalogRolesGet200Response**](JobCatalogRolesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## job_catalog_roles_id_get

> <JobCatalogRole> job_catalog_roles_id_get(id)

Reads a single Role

Reads a single Role

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

api_instance = F::JobCatalogRoleApi.new
id = '1' # String | 

begin
  # Reads a single Role
  result = api_instance.job_catalog_roles_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling JobCatalogRoleApi->job_catalog_roles_id_get: #{e}"
end
```

#### Using the job_catalog_roles_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<JobCatalogRole>, Integer, Hash)> job_catalog_roles_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Role
  data, status_code, headers = api_instance.job_catalog_roles_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <JobCatalogRole>
rescue F::ApiError => e
  puts "Error when calling JobCatalogRoleApi->job_catalog_roles_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**JobCatalogRole**](JobCatalogRole.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

