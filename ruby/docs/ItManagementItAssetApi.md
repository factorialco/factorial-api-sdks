# F::ItManagementItAssetApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**it_management_it_assets_get**](ItManagementItAssetApi.md#it_management_it_assets_get) | **GET** /api/2026-07-01/resources/it_management/it_assets | Reads all It assets |
| [**it_management_it_assets_id_delete**](ItManagementItAssetApi.md#it_management_it_assets_id_delete) | **DELETE** /api/2026-07-01/resources/it_management/it_assets/{id} | Deletes an It asset |
| [**it_management_it_assets_id_get**](ItManagementItAssetApi.md#it_management_it_assets_id_get) | **GET** /api/2026-07-01/resources/it_management/it_assets/{id} | Reads a single It asset |
| [**it_management_it_assets_id_put**](ItManagementItAssetApi.md#it_management_it_assets_id_put) | **PUT** /api/2026-07-01/resources/it_management/it_assets/{id} | Updates an It asset |
| [**it_management_it_assets_post**](ItManagementItAssetApi.md#it_management_it_assets_post) | **POST** /api/2026-07-01/resources/it_management/it_assets | Creates an It asset |


## it_management_it_assets_get

> <ItManagementItAssetsGet200Response> it_management_it_assets_get(opts)

Reads all It assets

Reads all It assets

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

api_instance = F::ItManagementItAssetApi.new
opts = {
  ids: ['inner_example'], # Array<String> | IT Asset identifiers to retrieve
  serial_numbers: ['inner_example'], # Array<String> | Serial numbers of IT assets to retrieve
  type_names: ['inner_example'], # Array<String> | Type names of IT assets to filter
  owner_ids: ['inner_example'], # Array<String> | Owner (employee) identifiers to filter assets
  location_ids: ['inner_example'], # Array<String> | Location identifiers to filter assets
  workplace_ids: ['inner_example'], # Array<String> | Workplace identifiers to filter assets
  team_ids: ['inner_example'] # Array<String> | Team identifiers to filter assets
}

begin
  # Reads all It assets
  result = api_instance.it_management_it_assets_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetApi->it_management_it_assets_get: #{e}"
end
```

#### Using the it_management_it_assets_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ItManagementItAssetsGet200Response>, Integer, Hash)> it_management_it_assets_get_with_http_info(opts)

```ruby
begin
  # Reads all It assets
  data, status_code, headers = api_instance.it_management_it_assets_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ItManagementItAssetsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetApi->it_management_it_assets_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | IT Asset identifiers to retrieve | [optional] |
| **serial_numbers** | [**Array&lt;String&gt;**](String.md) | Serial numbers of IT assets to retrieve | [optional] |
| **type_names** | [**Array&lt;String&gt;**](String.md) | Type names of IT assets to filter | [optional] |
| **owner_ids** | [**Array&lt;String&gt;**](String.md) | Owner (employee) identifiers to filter assets | [optional] |
| **location_ids** | [**Array&lt;String&gt;**](String.md) | Location identifiers to filter assets | [optional] |
| **workplace_ids** | [**Array&lt;String&gt;**](String.md) | Workplace identifiers to filter assets | [optional] |
| **team_ids** | [**Array&lt;String&gt;**](String.md) | Team identifiers to filter assets | [optional] |

### Return type

[**ItManagementItAssetsGet200Response**](ItManagementItAssetsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## it_management_it_assets_id_delete

> <ItManagementItAsset> it_management_it_assets_id_delete(id)

Deletes an It asset

Deletes an It asset

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

api_instance = F::ItManagementItAssetApi.new
id = '0199e6ea-20c0-73d3-9782-8267dc96773a' # String | IT Asset identifier to delete

begin
  # Deletes an It asset
  result = api_instance.it_management_it_assets_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetApi->it_management_it_assets_id_delete: #{e}"
end
```

#### Using the it_management_it_assets_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ItManagementItAsset>, Integer, Hash)> it_management_it_assets_id_delete_with_http_info(id)

```ruby
begin
  # Deletes an It asset
  data, status_code, headers = api_instance.it_management_it_assets_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ItManagementItAsset>
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetApi->it_management_it_assets_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | IT Asset identifier to delete |  |

### Return type

[**ItManagementItAsset**](ItManagementItAsset.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## it_management_it_assets_id_get

> <ItManagementItAsset> it_management_it_assets_id_get(id)

Reads a single It asset

Reads a single It asset

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

api_instance = F::ItManagementItAssetApi.new
id = '0199e6ea-20c0-73d3-9782-8267dc96773a' # String | IT Asset identifiers to retrieve

begin
  # Reads a single It asset
  result = api_instance.it_management_it_assets_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetApi->it_management_it_assets_id_get: #{e}"
end
```

#### Using the it_management_it_assets_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ItManagementItAsset>, Integer, Hash)> it_management_it_assets_id_get_with_http_info(id)

```ruby
begin
  # Reads a single It asset
  data, status_code, headers = api_instance.it_management_it_assets_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ItManagementItAsset>
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetApi->it_management_it_assets_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | IT Asset identifiers to retrieve |  |

### Return type

[**ItManagementItAsset**](ItManagementItAsset.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## it_management_it_assets_id_put

> <ItManagementItAsset> it_management_it_assets_id_put(id, opts)

Updates an It asset

Updates an It asset

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

api_instance = F::ItManagementItAssetApi.new
id = '0199e6ea-20c0-73d3-9782-8267dc96773a' # String | IT Asset identifier
opts = {
  it_management_it_assets_id_put_request: F::ItManagementItAssetsIdPutRequest.new({id: '0199e6ea-20c0-73d3-9782-8267dc96773a'}) # ItManagementItAssetsIdPutRequest | 
}

begin
  # Updates an It asset
  result = api_instance.it_management_it_assets_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetApi->it_management_it_assets_id_put: #{e}"
end
```

#### Using the it_management_it_assets_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ItManagementItAsset>, Integer, Hash)> it_management_it_assets_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates an It asset
  data, status_code, headers = api_instance.it_management_it_assets_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ItManagementItAsset>
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetApi->it_management_it_assets_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | IT Asset identifier |  |
| **it_management_it_assets_id_put_request** | [**ItManagementItAssetsIdPutRequest**](ItManagementItAssetsIdPutRequest.md) |  | [optional] |

### Return type

[**ItManagementItAsset**](ItManagementItAsset.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## it_management_it_assets_post

> <ItManagementItAsset> it_management_it_assets_post(opts)

Creates an It asset

Creates an It asset

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

api_instance = F::ItManagementItAssetApi.new
opts = {
  it_management_it_assets_post_request: F::ItManagementItAssetsPostRequest.new({it_asset_model_id: '0199e6ea-20c0-73d3-9782-8267dc96773a', serial_number: 'SN123456789'}) # ItManagementItAssetsPostRequest | 
}

begin
  # Creates an It asset
  result = api_instance.it_management_it_assets_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetApi->it_management_it_assets_post: #{e}"
end
```

#### Using the it_management_it_assets_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ItManagementItAsset>, Integer, Hash)> it_management_it_assets_post_with_http_info(opts)

```ruby
begin
  # Creates an It asset
  data, status_code, headers = api_instance.it_management_it_assets_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ItManagementItAsset>
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetApi->it_management_it_assets_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **it_management_it_assets_post_request** | [**ItManagementItAssetsPostRequest**](ItManagementItAssetsPostRequest.md) |  | [optional] |

### Return type

[**ItManagementItAsset**](ItManagementItAsset.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

