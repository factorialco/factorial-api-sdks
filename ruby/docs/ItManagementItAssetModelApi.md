# F::ItManagementItAssetModelApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**it_management_it_asset_models_get**](ItManagementItAssetModelApi.md#it_management_it_asset_models_get) | **GET** /api/2026-07-01/resources/it_management/it_asset_models | Reads all It asset models |
| [**it_management_it_asset_models_id_get**](ItManagementItAssetModelApi.md#it_management_it_asset_models_id_get) | **GET** /api/2026-07-01/resources/it_management/it_asset_models/{id} | Reads a single It asset model |
| [**it_management_it_asset_models_id_put**](ItManagementItAssetModelApi.md#it_management_it_asset_models_id_put) | **PUT** /api/2026-07-01/resources/it_management/it_asset_models/{id} | Updates an It asset model |
| [**it_management_it_asset_models_post**](ItManagementItAssetModelApi.md#it_management_it_asset_models_post) | **POST** /api/2026-07-01/resources/it_management/it_asset_models | Creates an It asset model |


## it_management_it_asset_models_get

> <ItManagementItAssetModelsGet200Response> it_management_it_asset_models_get(opts)

Reads all It asset models

Reads all It asset models

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

api_instance = F::ItManagementItAssetModelApi.new
opts = {
  ids: ['inner_example'] # Array<String> | IT Asset Model identifiers to retrieve
}

begin
  # Reads all It asset models
  result = api_instance.it_management_it_asset_models_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetModelApi->it_management_it_asset_models_get: #{e}"
end
```

#### Using the it_management_it_asset_models_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ItManagementItAssetModelsGet200Response>, Integer, Hash)> it_management_it_asset_models_get_with_http_info(opts)

```ruby
begin
  # Reads all It asset models
  data, status_code, headers = api_instance.it_management_it_asset_models_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ItManagementItAssetModelsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetModelApi->it_management_it_asset_models_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | IT Asset Model identifiers to retrieve | [optional] |

### Return type

[**ItManagementItAssetModelsGet200Response**](ItManagementItAssetModelsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## it_management_it_asset_models_id_get

> <ItManagementItAssetModel> it_management_it_asset_models_id_get(id)

Reads a single It asset model

Reads a single It asset model

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

api_instance = F::ItManagementItAssetModelApi.new
id = '0199e6ea-20c0-73d3-9782-8267dc96773a' # String | IT Asset Model identifiers to retrieve

begin
  # Reads a single It asset model
  result = api_instance.it_management_it_asset_models_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetModelApi->it_management_it_asset_models_id_get: #{e}"
end
```

#### Using the it_management_it_asset_models_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ItManagementItAssetModel>, Integer, Hash)> it_management_it_asset_models_id_get_with_http_info(id)

```ruby
begin
  # Reads a single It asset model
  data, status_code, headers = api_instance.it_management_it_asset_models_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ItManagementItAssetModel>
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetModelApi->it_management_it_asset_models_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | IT Asset Model identifiers to retrieve |  |

### Return type

[**ItManagementItAssetModel**](ItManagementItAssetModel.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## it_management_it_asset_models_id_put

> <ItManagementItAssetModel> it_management_it_asset_models_id_put(id, opts)

Updates an It asset model

Updates an It asset model

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

api_instance = F::ItManagementItAssetModelApi.new
id = '0199e6ea-20c0-73d3-9782-8267dc96773a' # String | IT Asset Model identifier
opts = {
  it_management_it_asset_models_id_put_request: F::ItManagementItAssetModelsIdPutRequest.new({id: '0199e6ea-20c0-73d3-9782-8267dc96773a', type_name: 'laptop', brand: 'Apple', name: 'MacBook Pro'}) # ItManagementItAssetModelsIdPutRequest | 
}

begin
  # Updates an It asset model
  result = api_instance.it_management_it_asset_models_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetModelApi->it_management_it_asset_models_id_put: #{e}"
end
```

#### Using the it_management_it_asset_models_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ItManagementItAssetModel>, Integer, Hash)> it_management_it_asset_models_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates an It asset model
  data, status_code, headers = api_instance.it_management_it_asset_models_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ItManagementItAssetModel>
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetModelApi->it_management_it_asset_models_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | IT Asset Model identifier |  |
| **it_management_it_asset_models_id_put_request** | [**ItManagementItAssetModelsIdPutRequest**](ItManagementItAssetModelsIdPutRequest.md) |  | [optional] |

### Return type

[**ItManagementItAssetModel**](ItManagementItAssetModel.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## it_management_it_asset_models_post

> <ItManagementItAssetModel> it_management_it_asset_models_post(opts)

Creates an It asset model

Creates an It asset model

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

api_instance = F::ItManagementItAssetModelApi.new
opts = {
  it_management_it_asset_models_post_request: F::ItManagementItAssetModelsPostRequest.new({type_name: 'laptop', brand: 'Apple', name: 'MacBook Pro'}) # ItManagementItAssetModelsPostRequest | 
}

begin
  # Creates an It asset model
  result = api_instance.it_management_it_asset_models_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetModelApi->it_management_it_asset_models_post: #{e}"
end
```

#### Using the it_management_it_asset_models_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ItManagementItAssetModel>, Integer, Hash)> it_management_it_asset_models_post_with_http_info(opts)

```ruby
begin
  # Creates an It asset model
  data, status_code, headers = api_instance.it_management_it_asset_models_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ItManagementItAssetModel>
rescue F::ApiError => e
  puts "Error when calling ItManagementItAssetModelApi->it_management_it_asset_models_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **it_management_it_asset_models_post_request** | [**ItManagementItAssetModelsPostRequest**](ItManagementItAssetModelsPostRequest.md) |  | [optional] |

### Return type

[**ItManagementItAssetModel**](ItManagementItAssetModel.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

