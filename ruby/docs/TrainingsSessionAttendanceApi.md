# F::TrainingsSessionAttendanceApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**trainings_session_attendances_bulk_update_post**](TrainingsSessionAttendanceApi.md#trainings_session_attendances_bulk_update_post) | **POST** /api/2026-07-01/resources/trainings/session_attendances/bulk_update | Bulk update session attendances |
| [**trainings_session_attendances_get**](TrainingsSessionAttendanceApi.md#trainings_session_attendances_get) | **GET** /api/2026-07-01/resources/trainings/session_attendances | Reads all Session attendances |
| [**trainings_session_attendances_id_get**](TrainingsSessionAttendanceApi.md#trainings_session_attendances_id_get) | **GET** /api/2026-07-01/resources/trainings/session_attendances/{id} | Reads a single Session attendance |


## trainings_session_attendances_bulk_update_post

> <Array<TrainingsSessionAttendance>> trainings_session_attendances_bulk_update_post(opts)

Bulk update session attendances

Updates the status or completed duration of multiple session attendances. When status is set to completed, completed_duration is automatically set to session duration. When only completed_duration is provided, attendances must already be in completed status.

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

api_instance = F::TrainingsSessionAttendanceApi.new
opts = {
  trainings_session_attendances_bulk_update_post_request: F::TrainingsSessionAttendancesBulkUpdatePostRequest.new({ids: ["1"]}) # TrainingsSessionAttendancesBulkUpdatePostRequest | 
}

begin
  # Bulk update session attendances
  result = api_instance.trainings_session_attendances_bulk_update_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionAttendanceApi->trainings_session_attendances_bulk_update_post: #{e}"
end
```

#### Using the trainings_session_attendances_bulk_update_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<TrainingsSessionAttendance>>, Integer, Hash)> trainings_session_attendances_bulk_update_post_with_http_info(opts)

```ruby
begin
  # Bulk update session attendances
  data, status_code, headers = api_instance.trainings_session_attendances_bulk_update_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<TrainingsSessionAttendance>>
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionAttendanceApi->trainings_session_attendances_bulk_update_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **trainings_session_attendances_bulk_update_post_request** | [**TrainingsSessionAttendancesBulkUpdatePostRequest**](TrainingsSessionAttendancesBulkUpdatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;TrainingsSessionAttendance&gt;**](TrainingsSessionAttendance.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## trainings_session_attendances_get

> <TrainingsSessionAttendancesGet200Response> trainings_session_attendances_get(opts)

Reads all Session attendances

Reads all Session attendances

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

api_instance = F::TrainingsSessionAttendanceApi.new
opts = {
  session_id: 'session_id_example', # String | 
  id: 'id_example', # String | 
  ids: ['inner_example'], # Array<String> | 
  session_access_membership_ids: ['inner_example'], # Array<String> | 
  access_ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Session attendances
  result = api_instance.trainings_session_attendances_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionAttendanceApi->trainings_session_attendances_get: #{e}"
end
```

#### Using the trainings_session_attendances_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsSessionAttendancesGet200Response>, Integer, Hash)> trainings_session_attendances_get_with_http_info(opts)

```ruby
begin
  # Reads all Session attendances
  data, status_code, headers = api_instance.trainings_session_attendances_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsSessionAttendancesGet200Response>
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionAttendanceApi->trainings_session_attendances_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **session_id** | **String** |  | [optional] |
| **id** | **String** |  | [optional] |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **session_access_membership_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |
| **access_ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**TrainingsSessionAttendancesGet200Response**](TrainingsSessionAttendancesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainings_session_attendances_id_get

> <TrainingsSessionAttendance> trainings_session_attendances_id_get(id)

Reads a single Session attendance

Reads a single Session attendance

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

api_instance = F::TrainingsSessionAttendanceApi.new
id = '1' # String | 

begin
  # Reads a single Session attendance
  result = api_instance.trainings_session_attendances_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionAttendanceApi->trainings_session_attendances_id_get: #{e}"
end
```

#### Using the trainings_session_attendances_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TrainingsSessionAttendance>, Integer, Hash)> trainings_session_attendances_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Session attendance
  data, status_code, headers = api_instance.trainings_session_attendances_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TrainingsSessionAttendance>
rescue F::ApiError => e
  puts "Error when calling TrainingsSessionAttendanceApi->trainings_session_attendances_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**TrainingsSessionAttendance**](TrainingsSessionAttendance.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

