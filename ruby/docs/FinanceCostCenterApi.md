# F::FinanceCostCenterApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**finance_cost_centers_edit_post**](FinanceCostCenterApi.md#finance_cost_centers_edit_post) | **POST** /api/2026-07-01/resources/finance/cost_centers/edit | Edits a Cost center |
| [**finance_cost_centers_get**](FinanceCostCenterApi.md#finance_cost_centers_get) | **GET** /api/2026-07-01/resources/finance/cost_centers | Reads all Cost centers |
| [**finance_cost_centers_id_delete**](FinanceCostCenterApi.md#finance_cost_centers_id_delete) | **DELETE** /api/2026-07-01/resources/finance/cost_centers/{id} | Deletes a Cost center |
| [**finance_cost_centers_id_get**](FinanceCostCenterApi.md#finance_cost_centers_id_get) | **GET** /api/2026-07-01/resources/finance/cost_centers/{id} | Reads a single Cost center |
| [**finance_cost_centers_post**](FinanceCostCenterApi.md#finance_cost_centers_post) | **POST** /api/2026-07-01/resources/finance/cost_centers | Creates a Cost center |


## finance_cost_centers_edit_post

> <FinanceCostCenter> finance_cost_centers_edit_post(opts)

Edits a Cost center

Edits a Cost center

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

api_instance = F::FinanceCostCenterApi.new
opts = {
  finance_cost_centers_edit_post_request: F::FinanceCostCentersEditPostRequest.new({id: 'id_example', company_id: 'company_id_example'}) # FinanceCostCentersEditPostRequest | 
}

begin
  # Edits a Cost center
  result = api_instance.finance_cost_centers_edit_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceCostCenterApi->finance_cost_centers_edit_post: #{e}"
end
```

#### Using the finance_cost_centers_edit_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceCostCenter>, Integer, Hash)> finance_cost_centers_edit_post_with_http_info(opts)

```ruby
begin
  # Edits a Cost center
  data, status_code, headers = api_instance.finance_cost_centers_edit_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceCostCenter>
rescue F::ApiError => e
  puts "Error when calling FinanceCostCenterApi->finance_cost_centers_edit_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **finance_cost_centers_edit_post_request** | [**FinanceCostCentersEditPostRequest**](FinanceCostCentersEditPostRequest.md) |  | [optional] |

### Return type

[**FinanceCostCenter**](FinanceCostCenter.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## finance_cost_centers_get

> <FinanceCostCentersGet200Response> finance_cost_centers_get(opts)

Reads all Cost centers

Reads all Cost centers

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

api_instance = F::FinanceCostCenterApi.new
opts = {
  ids: ['inner_example'], # Array<String> | 
  company_id: 'company_id_example', # String | 
  legal_entity_ids: ['inner_example'], # Array<String> | 
  include_actives_on_date: 'include_actives_on_date_example', # String | 
  search: 'search_example' # String | 
}

begin
  # Reads all Cost centers
  result = api_instance.finance_cost_centers_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceCostCenterApi->finance_cost_centers_get: #{e}"
end
```

#### Using the finance_cost_centers_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceCostCentersGet200Response>, Integer, Hash)> finance_cost_centers_get_with_http_info(opts)

```ruby
begin
  # Reads all Cost centers
  data, status_code, headers = api_instance.finance_cost_centers_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceCostCentersGet200Response>
rescue F::ApiError => e
  puts "Error when calling FinanceCostCenterApi->finance_cost_centers_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **company_id** | **String** |  | [optional] |
| **legal_entity_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **include_actives_on_date** | **String** |  | [optional] |
| **search** | **String** |  | [optional] |

### Return type

[**FinanceCostCentersGet200Response**](FinanceCostCentersGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_cost_centers_id_delete

> <FinanceCostCenter> finance_cost_centers_id_delete(id)

Deletes a Cost center

Deletes a Cost center

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

api_instance = F::FinanceCostCenterApi.new
id = '1' # String | 

begin
  # Deletes a Cost center
  result = api_instance.finance_cost_centers_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceCostCenterApi->finance_cost_centers_id_delete: #{e}"
end
```

#### Using the finance_cost_centers_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceCostCenter>, Integer, Hash)> finance_cost_centers_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Cost center
  data, status_code, headers = api_instance.finance_cost_centers_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceCostCenter>
rescue F::ApiError => e
  puts "Error when calling FinanceCostCenterApi->finance_cost_centers_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**FinanceCostCenter**](FinanceCostCenter.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_cost_centers_id_get

> <FinanceCostCenter> finance_cost_centers_id_get(id)

Reads a single Cost center

Reads a single Cost center

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

api_instance = F::FinanceCostCenterApi.new
id = '1' # String | 

begin
  # Reads a single Cost center
  result = api_instance.finance_cost_centers_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceCostCenterApi->finance_cost_centers_id_get: #{e}"
end
```

#### Using the finance_cost_centers_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceCostCenter>, Integer, Hash)> finance_cost_centers_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Cost center
  data, status_code, headers = api_instance.finance_cost_centers_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceCostCenter>
rescue F::ApiError => e
  puts "Error when calling FinanceCostCenterApi->finance_cost_centers_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**FinanceCostCenter**](FinanceCostCenter.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_cost_centers_post

> <FinanceCostCenter> finance_cost_centers_post(opts)

Creates a Cost center

Creates a Cost center

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

api_instance = F::FinanceCostCenterApi.new
opts = {
  finance_cost_centers_post_request: F::FinanceCostCentersPostRequest.new({name: 'name_example', company_id: 'company_id_example'}) # FinanceCostCentersPostRequest | 
}

begin
  # Creates a Cost center
  result = api_instance.finance_cost_centers_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceCostCenterApi->finance_cost_centers_post: #{e}"
end
```

#### Using the finance_cost_centers_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceCostCenter>, Integer, Hash)> finance_cost_centers_post_with_http_info(opts)

```ruby
begin
  # Creates a Cost center
  data, status_code, headers = api_instance.finance_cost_centers_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceCostCenter>
rescue F::ApiError => e
  puts "Error when calling FinanceCostCenterApi->finance_cost_centers_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **finance_cost_centers_post_request** | [**FinanceCostCentersPostRequest**](FinanceCostCentersPostRequest.md) |  | [optional] |

### Return type

[**FinanceCostCenter**](FinanceCostCenter.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

