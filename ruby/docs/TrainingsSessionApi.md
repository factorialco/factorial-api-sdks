# F::TrainingsSessionApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**trainings_sessions_get**](TrainingsSessionApi.md#trainings_sessions_get) | **GET** /api/2026-07-01/resources/trainings/sessions | Reads all Sessions |
| [**trainings_sessions_id_delete**](TrainingsSessionApi.md#trainings_sessions_id_delete) | **DELETE** /api/2026-07-01/resources/trainings/sessions/{id} | Deletes a Session |
| [**trainings_sessions_id_get**](TrainingsSessionApi.md#trainings_sessions_id_get) | **GET** /api/2026-07-01/resources/trainings/sessions/{id} | Reads a single Session |
| [**trainings_sessions_id_put**](TrainingsSessionApi.md#trainings_sessions_id_put) | **PUT** /api/2026-07-01/resources/trainings/sessions/{id} | Update training session |
| [**trainings_sessions_post**](TrainingsSessionApi.md#trainings_sessions_post) | **POST** /api/2026-07-01/resources/trainings/sessions | Create a new training session |


## trainings_sessions_get

> <TrainingsSessionsGet200Response> trainings_sessions_get(opts)

Reads all Sessions

Reads all Sessions

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

api_instance = F::TrainingsSessionApi.new
opts = {
  ids: ['inner_example'], # Array<String> | This field is used to filter those sessions whose id match with the given.
  training_ids: ['inner_example'], # Array<String> | This field is used to filter those sessions whose belong to these trainings.
  search: 'Session 1', # String | This field is used to filter those sessions whose name include some of the text written.
  start_after: '2024-01-05T00:00:00.000Z', # String | This field is used to filter those sessions whose starts date is after the given.
  start_before: '2025-06-05T00:00:00.000Z', # String | This field is used to filter those sessions whose starts date is before the given.
  access_id: 'access_id_example', # String | access_id associated to the employee, refers to employees/employees endpoint.
  employee_id: '20', # String | employee_id associated to the employee, refers to employees/employees endpoint.
  training_class_ids: ['inner_example'], # Array<String> | This field is used to filter those sessions whose belong to this training groups.
  _next: false, # Boolean | When this field is active, it filters and orders those sessions that are closest in time, with the first element being the closest.
  modality: 'inperson', # String | The mode the session will be handled, online, in person or hybrid.
  starts_at: ['inner_example'], # Array<String> | This field is used to filter the sessions that start at a given date.
  active: true # Boolean | When this field is active, filter by only active sessions
}

begin
  # Reads all Sessions
  result = api_instance.trainings_sessions_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionApi->trainings_sessions_get: #{e}"
end
```

#### Using the trainings_sessions_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsSessionsGet200Response>, Integer, Hash)> trainings_sessions_get_with_http_info(opts)

```ruby
begin
  # Reads all Sessions
  data, status_code, headers = api_instance.trainings_sessions_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsSessionsGet200Response>
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionApi->trainings_sessions_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | This field is used to filter those sessions whose id match with the given. | [optional] |
| **training_ids** | [**Array&lt;String&gt;**](String.md) | This field is used to filter those sessions whose belong to these trainings. | [optional] |
| **search** | **String** | This field is used to filter those sessions whose name include some of the text written. | [optional] |
| **start_after** | **String** | This field is used to filter those sessions whose starts date is after the given. | [optional] |
| **start_before** | **String** | This field is used to filter those sessions whose starts date is before the given. | [optional] |
| **access_id** | **String** | access_id associated to the employee, refers to employees/employees endpoint. | [optional] |
| **employee_id** | **String** | employee_id associated to the employee, refers to employees/employees endpoint. | [optional] |
| **training_class_ids** | [**Array&lt;String&gt;**](String.md) | This field is used to filter those sessions whose belong to this training groups. | [optional] |
| **_next** | **Boolean** | When this field is active, it filters and orders those sessions that are closest in time, with the first element being the closest. | [optional] |
| **modality** | **String** | The mode the session will be handled, online, in person or hybrid. | [optional] |
| **starts_at** | [**Array&lt;String&gt;**](String.md) | This field is used to filter the sessions that start at a given date. | [optional] |
| **active** | **Boolean** | When this field is active, filter by only active sessions | [optional] |

### Return type

[**TrainingsSessionsGet200Response**](TrainingsSessionsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_sessions_id_delete

> <TrainingsSession> trainings_sessions_id_delete(id)

Deletes a Session

Deletes a Session

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

api_instance = F::TrainingsSessionApi.new
id = '1' # String | 

begin
  # Deletes a Session
  result = api_instance.trainings_sessions_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionApi->trainings_sessions_id_delete: #{e}"
end
```

#### Using the trainings_sessions_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsSession>, Integer, Hash)> trainings_sessions_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Session
  data, status_code, headers = api_instance.trainings_sessions_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsSession>
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionApi->trainings_sessions_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**TrainingsSession**](TrainingsSession.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_sessions_id_get

> <TrainingsSession> trainings_sessions_id_get(id)

Reads a single Session

Reads a single Session

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

api_instance = F::TrainingsSessionApi.new
id = '1' # String | This field is used to filter those sessions whose id match with the given.

begin
  # Reads a single Session
  result = api_instance.trainings_sessions_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionApi->trainings_sessions_id_get: #{e}"
end
```

#### Using the trainings_sessions_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsSession>, Integer, Hash)> trainings_sessions_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Session
  data, status_code, headers = api_instance.trainings_sessions_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsSession>
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionApi->trainings_sessions_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | This field is used to filter those sessions whose id match with the given. |  |

### Return type

[**TrainingsSession**](TrainingsSession.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_sessions_id_put

> <TrainingsSession> trainings_sessions_id_put(id, opts)

Update training session

Update fields from a training session

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

api_instance = F::TrainingsSessionApi.new
id = '1' # String | The session id you want to update
opts = {
  trainings_sessions_id_put_request: F::TrainingsSessionsIdPutRequest.new({id: 'id_example', name: 'Session one'}) # TrainingsSessionsIdPutRequest | 
}

begin
  # Update training session
  result = api_instance.trainings_sessions_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionApi->trainings_sessions_id_put: #{e}"
end
```

#### Using the trainings_sessions_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsSession>, Integer, Hash)> trainings_sessions_id_put_with_http_info(id, opts)

```ruby
begin
  # Update training session
  data, status_code, headers = api_instance.trainings_sessions_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsSession>
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionApi->trainings_sessions_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The session id you want to update |  |
| **trainings_sessions_id_put_request** | [**TrainingsSessionsIdPutRequest**](TrainingsSessionsIdPutRequest.md) |  | [optional] |

### Return type

[**TrainingsSession**](TrainingsSession.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## trainings_sessions_post

> <TrainingsSession> trainings_sessions_post(opts)

Create a new training session

Create a new training session, do not forget to make it child from a training class if you want it to be displayed in the frontend application.

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

api_instance = F::TrainingsSessionApi.new
opts = {
  trainings_sessions_post_request: F::TrainingsSessionsPostRequest.new({name: 'Session one', training_id: 'training_id_example'}) # TrainingsSessionsPostRequest | 
}

begin
  # Create a new training session
  result = api_instance.trainings_sessions_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionApi->trainings_sessions_post: #{e}"
end
```

#### Using the trainings_sessions_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsSession>, Integer, Hash)> trainings_sessions_post_with_http_info(opts)

```ruby
begin
  # Create a new training session
  data, status_code, headers = api_instance.trainings_sessions_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsSession>
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionApi->trainings_sessions_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **trainings_sessions_post_request** | [**TrainingsSessionsPostRequest**](TrainingsSessionsPostRequest.md) |  | [optional] |

### Return type

[**TrainingsSession**](TrainingsSession.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

