# F::ProjectManagementBudgetStrategyApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**project_management_budget_strategies_get**](ProjectManagementBudgetStrategyApi.md#project_management_budget_strategies_get) | **GET** /api/2026-07-01/resources/project_management/budget_strategies | Reads all Budget strategies |
| [**project_management_budget_strategies_id_delete**](ProjectManagementBudgetStrategyApi.md#project_management_budget_strategies_id_delete) | **DELETE** /api/2026-07-01/resources/project_management/budget_strategies/{id} | Deletes a Budget strategy |
| [**project_management_budget_strategies_id_get**](ProjectManagementBudgetStrategyApi.md#project_management_budget_strategies_id_get) | **GET** /api/2026-07-01/resources/project_management/budget_strategies/{id} | Reads a single Budget strategy |
| [**project_management_budget_strategies_id_put**](ProjectManagementBudgetStrategyApi.md#project_management_budget_strategies_id_put) | **PUT** /api/2026-07-01/resources/project_management/budget_strategies/{id} | Updates a Budget strategy |
| [**project_management_budget_strategies_post**](ProjectManagementBudgetStrategyApi.md#project_management_budget_strategies_post) | **POST** /api/2026-07-01/resources/project_management/budget_strategies | Creates a Budget strategy |


## project_management_budget_strategies_get

> <ProjectManagementBudgetStrategiesGet200Response> project_management_budget_strategies_get(opts)

Reads all Budget strategies

Reads all Budget strategies

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

api_instance = F::ProjectManagementBudgetStrategyApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Filter budget strategies by these ids
  project_ids: ['inner_example'], # Array<String> | Filter budget strategies by these project ids
  subproject_ids: ['inner_example'], # Array<String> | Filter budget strategies by these subproject ids
  without_subproject: false # Boolean | When true, return only budget strategies without a subproject
}

begin
  # Reads all Budget strategies
  result = api_instance.project_management_budget_strategies_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementBudgetStrategyApi->project_management_budget_strategies_get: #{e}"
end
```

#### Using the project_management_budget_strategies_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementBudgetStrategiesGet200Response>, Integer, Hash)> project_management_budget_strategies_get_with_http_info(opts)

```ruby
begin
  # Reads all Budget strategies
  data, status_code, headers = api_instance.project_management_budget_strategies_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementBudgetStrategiesGet200Response>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementBudgetStrategyApi->project_management_budget_strategies_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter budget strategies by these ids | [optional] |
| **project_ids** | [**Array&lt;String&gt;**](String.md) | Filter budget strategies by these project ids | [optional] |
| **subproject_ids** | [**Array&lt;String&gt;**](String.md) | Filter budget strategies by these subproject ids | [optional] |
| **without_subproject** | **Boolean** | When true, return only budget strategies without a subproject | [optional] |

### Return type

[**ProjectManagementBudgetStrategiesGet200Response**](ProjectManagementBudgetStrategiesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_budget_strategies_id_delete

> <ProjectManagementBudgetStrategy> project_management_budget_strategies_id_delete(id)

Deletes a Budget strategy

Deletes a Budget strategy

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

api_instance = F::ProjectManagementBudgetStrategyApi.new
id = '1234' # String | Id of the budget strategy to delete

begin
  # Deletes a Budget strategy
  result = api_instance.project_management_budget_strategies_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementBudgetStrategyApi->project_management_budget_strategies_id_delete: #{e}"
end
```

#### Using the project_management_budget_strategies_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementBudgetStrategy>, Integer, Hash)> project_management_budget_strategies_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Budget strategy
  data, status_code, headers = api_instance.project_management_budget_strategies_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementBudgetStrategy>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementBudgetStrategyApi->project_management_budget_strategies_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id of the budget strategy to delete |  |

### Return type

[**ProjectManagementBudgetStrategy**](ProjectManagementBudgetStrategy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_budget_strategies_id_get

> <ProjectManagementBudgetStrategy> project_management_budget_strategies_id_get(id)

Reads a single Budget strategy

Reads a single Budget strategy

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

api_instance = F::ProjectManagementBudgetStrategyApi.new
id = '1234' # String | Filter budget strategies by these ids

begin
  # Reads a single Budget strategy
  result = api_instance.project_management_budget_strategies_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementBudgetStrategyApi->project_management_budget_strategies_id_get: #{e}"
end
```

#### Using the project_management_budget_strategies_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementBudgetStrategy>, Integer, Hash)> project_management_budget_strategies_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Budget strategy
  data, status_code, headers = api_instance.project_management_budget_strategies_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementBudgetStrategy>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementBudgetStrategyApi->project_management_budget_strategies_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter budget strategies by these ids |  |

### Return type

[**ProjectManagementBudgetStrategy**](ProjectManagementBudgetStrategy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_management_budget_strategies_id_put

> <ProjectManagementBudgetStrategy> project_management_budget_strategies_id_put(id, opts)

Updates a Budget strategy

Updates a Budget strategy

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

api_instance = F::ProjectManagementBudgetStrategyApi.new
id = '1234' # String | Id of the budget strategy to update
opts = {
  project_management_budget_strategies_id_put_request: F::ProjectManagementBudgetStrategiesIdPutRequest.new({id: '1234'}) # ProjectManagementBudgetStrategiesIdPutRequest | 
}

begin
  # Updates a Budget strategy
  result = api_instance.project_management_budget_strategies_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementBudgetStrategyApi->project_management_budget_strategies_id_put: #{e}"
end
```

#### Using the project_management_budget_strategies_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementBudgetStrategy>, Integer, Hash)> project_management_budget_strategies_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Budget strategy
  data, status_code, headers = api_instance.project_management_budget_strategies_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementBudgetStrategy>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementBudgetStrategyApi->project_management_budget_strategies_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Id of the budget strategy to update |  |
| **project_management_budget_strategies_id_put_request** | [**ProjectManagementBudgetStrategiesIdPutRequest**](ProjectManagementBudgetStrategiesIdPutRequest.md) |  | [optional] |

### Return type

[**ProjectManagementBudgetStrategy**](ProjectManagementBudgetStrategy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## project_management_budget_strategies_post

> <ProjectManagementBudgetStrategy> project_management_budget_strategies_post(opts)

Creates a Budget strategy

Creates a Budget strategy

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

api_instance = F::ProjectManagementBudgetStrategyApi.new
opts = {
  project_management_budget_strategies_post_request: F::ProjectManagementBudgetStrategiesPostRequest.new({budget_strategy_type: 'project_fixed_cost', project_id: '1234'}) # ProjectManagementBudgetStrategiesPostRequest | 
}

begin
  # Creates a Budget strategy
  result = api_instance.project_management_budget_strategies_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ProjectManagementBudgetStrategyApi->project_management_budget_strategies_post: #{e}"
end
```

#### Using the project_management_budget_strategies_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectManagementBudgetStrategy>, Integer, Hash)> project_management_budget_strategies_post_with_http_info(opts)

```ruby
begin
  # Creates a Budget strategy
  data, status_code, headers = api_instance.project_management_budget_strategies_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectManagementBudgetStrategy>
rescue F::ApiError => e
  puts "Error when calling ProjectManagementBudgetStrategyApi->project_management_budget_strategies_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_management_budget_strategies_post_request** | [**ProjectManagementBudgetStrategiesPostRequest**](ProjectManagementBudgetStrategiesPostRequest.md) |  | [optional] |

### Return type

[**ProjectManagementBudgetStrategy**](ProjectManagementBudgetStrategy.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

