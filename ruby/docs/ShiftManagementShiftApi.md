# F::ShiftManagementShiftApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**shift_management_shifts_bulk_create_post**](ShiftManagementShiftApi.md#shift_management_shifts_bulk_create_post) | **POST** /api/2026-07-01/resources/shift_management/shifts/bulk_create | Bulk creates a Shift |
| [**shift_management_shifts_bulk_delete_post**](ShiftManagementShiftApi.md#shift_management_shifts_bulk_delete_post) | **POST** /api/2026-07-01/resources/shift_management/shifts/bulk_delete | Bulk deletes a Shift |
| [**shift_management_shifts_get**](ShiftManagementShiftApi.md#shift_management_shifts_get) | **GET** /api/2026-07-01/resources/shift_management/shifts | Reads all Shifts |
| [**shift_management_shifts_id_delete**](ShiftManagementShiftApi.md#shift_management_shifts_id_delete) | **DELETE** /api/2026-07-01/resources/shift_management/shifts/{id} | Deletes a Shift |
| [**shift_management_shifts_id_get**](ShiftManagementShiftApi.md#shift_management_shifts_id_get) | **GET** /api/2026-07-01/resources/shift_management/shifts/{id} | Reads a single Shift |
| [**shift_management_shifts_post**](ShiftManagementShiftApi.md#shift_management_shifts_post) | **POST** /api/2026-07-01/resources/shift_management/shifts | Creates a Shift |


## shift_management_shifts_bulk_create_post

> <Array<ShiftManagementShift>> shift_management_shifts_bulk_create_post(opts)

Bulk creates a Shift

Bulk creates a Shift

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

api_instance = F::ShiftManagementShiftApi.new
opts = {
  shift_management_shifts_bulk_create_post_request: F::ShiftManagementShiftsBulkCreatePostRequest.new({shifts: [3.56]}) # ShiftManagementShiftsBulkCreatePostRequest | 
}

begin
  # Bulk creates a Shift
  result = api_instance.shift_management_shifts_bulk_create_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ShiftManagementShiftApi->shift_management_shifts_bulk_create_post: #{e}"
end
```

#### Using the shift_management_shifts_bulk_create_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<ShiftManagementShift>>, Integer, Hash)> shift_management_shifts_bulk_create_post_with_http_info(opts)

```ruby
begin
  # Bulk creates a Shift
  data, status_code, headers = api_instance.shift_management_shifts_bulk_create_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<ShiftManagementShift>>
rescue F::ApiError => e
  puts "Error when calling ShiftManagementShiftApi->shift_management_shifts_bulk_create_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **shift_management_shifts_bulk_create_post_request** | [**ShiftManagementShiftsBulkCreatePostRequest**](ShiftManagementShiftsBulkCreatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;ShiftManagementShift&gt;**](ShiftManagementShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## shift_management_shifts_bulk_delete_post

> <Array<ShiftManagementShift>> shift_management_shifts_bulk_delete_post(opts)

Bulk deletes a Shift

Bulk deletes a Shift

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

api_instance = F::ShiftManagementShiftApi.new
opts = {
  shift_management_shifts_bulk_delete_post_request: F::ShiftManagementShiftsBulkDeletePostRequest.new({author_id: '1781'}) # ShiftManagementShiftsBulkDeletePostRequest | 
}

begin
  # Bulk deletes a Shift
  result = api_instance.shift_management_shifts_bulk_delete_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ShiftManagementShiftApi->shift_management_shifts_bulk_delete_post: #{e}"
end
```

#### Using the shift_management_shifts_bulk_delete_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<ShiftManagementShift>>, Integer, Hash)> shift_management_shifts_bulk_delete_post_with_http_info(opts)

```ruby
begin
  # Bulk deletes a Shift
  data, status_code, headers = api_instance.shift_management_shifts_bulk_delete_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<ShiftManagementShift>>
rescue F::ApiError => e
  puts "Error when calling ShiftManagementShiftApi->shift_management_shifts_bulk_delete_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **shift_management_shifts_bulk_delete_post_request** | [**ShiftManagementShiftsBulkDeletePostRequest**](ShiftManagementShiftsBulkDeletePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;ShiftManagementShift&gt;**](ShiftManagementShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## shift_management_shifts_get

> <ShiftManagementShiftsGet200Response> shift_management_shifts_get(opts)

Reads all Shifts

Reads all Shifts

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

api_instance = F::ShiftManagementShiftApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Filter shifts by their unique identifiers. Returns only shifts matching the provided IDs. If an empty array is provided, returns no results
  without_ids: ['inner_example'], # Array<String> | Exclude shifts with these identifiers from the results. Useful for filtering out specific shifts while keeping others
  employee_ids: ['inner_example'], # Array<String> | Filter shifts by employee identifiers. Returns only shifts assigned to the specified employees. If not provided, returns shifts for all accessible employees
  location_ids: ['inner_example'], # Array<String> | Filter shifts by location identifiers. Returns shifts that occur at the specified locations. Can be combined with employee_ids for more precise filtering
  start_at: '2020-01-01', # String | Filter shifts that end on or after this date. Only the date (calendar day) is used; the time part is ignored (treated as start of day, 00:00:00). Shifts are included if their end time is at or after the start of the specified day
  end_at: '2020-12-31', # String | Filter shifts that start before this date. Only the date (calendar day) is used; the time part is ignored (treated as end of day, 23:59:59). Shifts are included if their start time is before the end of the specified day
  only_published: false, # Boolean | When true, returns only shifts with state 'published' (visible to employees). When false, returns shifts in all states (draft, published, backup) based on your permissions
  only_states: ['inner_example'], # Array<String> | Filter shifts by their state. Provide an array of states ('draft', 'published', 'backup') to include. Can be combined with other filters for precise control
  split_overnight_shifts: false # Boolean | When true, shifts that span across midnight (overnight shifts) are split into two separate shift objects - one for each calendar day. This makes it easier to display shifts in day-based views
}

begin
  # Reads all Shifts
  result = api_instance.shift_management_shifts_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ShiftManagementShiftApi->shift_management_shifts_get: #{e}"
end
```

#### Using the shift_management_shifts_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ShiftManagementShiftsGet200Response>, Integer, Hash)> shift_management_shifts_get_with_http_info(opts)

```ruby
begin
  # Reads all Shifts
  data, status_code, headers = api_instance.shift_management_shifts_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ShiftManagementShiftsGet200Response>
rescue F::ApiError => e
  puts "Error when calling ShiftManagementShiftApi->shift_management_shifts_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Filter shifts by their unique identifiers. Returns only shifts matching the provided IDs. If an empty array is provided, returns no results | [optional] |
| **without_ids** | [**Array&lt;String&gt;**](String.md) | Exclude shifts with these identifiers from the results. Useful for filtering out specific shifts while keeping others | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Filter shifts by employee identifiers. Returns only shifts assigned to the specified employees. If not provided, returns shifts for all accessible employees | [optional] |
| **location_ids** | [**Array&lt;String&gt;**](String.md) | Filter shifts by location identifiers. Returns shifts that occur at the specified locations. Can be combined with employee_ids for more precise filtering | [optional] |
| **start_at** | **String** | Filter shifts that end on or after this date. Only the date (calendar day) is used; the time part is ignored (treated as start of day, 00:00:00). Shifts are included if their end time is at or after the start of the specified day | [optional] |
| **end_at** | **String** | Filter shifts that start before this date. Only the date (calendar day) is used; the time part is ignored (treated as end of day, 23:59:59). Shifts are included if their start time is before the end of the specified day | [optional] |
| **only_published** | **Boolean** | When true, returns only shifts with state &#39;published&#39; (visible to employees). When false, returns shifts in all states (draft, published, backup) based on your permissions | [optional] |
| **only_states** | [**Array&lt;String&gt;**](String.md) | Filter shifts by their state. Provide an array of states (&#39;draft&#39;, &#39;published&#39;, &#39;backup&#39;) to include. Can be combined with other filters for precise control | [optional] |
| **split_overnight_shifts** | **Boolean** | When true, shifts that span across midnight (overnight shifts) are split into two separate shift objects - one for each calendar day. This makes it easier to display shifts in day-based views | [optional] |

### Return type

[**ShiftManagementShiftsGet200Response**](ShiftManagementShiftsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## shift_management_shifts_id_delete

> <ShiftManagementShift> shift_management_shifts_id_delete(id)

Deletes a Shift

Deletes a Shift

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

api_instance = F::ShiftManagementShiftApi.new
id = '1' # String | Shift identifier to delete

begin
  # Deletes a Shift
  result = api_instance.shift_management_shifts_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ShiftManagementShiftApi->shift_management_shifts_id_delete: #{e}"
end
```

#### Using the shift_management_shifts_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ShiftManagementShift>, Integer, Hash)> shift_management_shifts_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Shift
  data, status_code, headers = api_instance.shift_management_shifts_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ShiftManagementShift>
rescue F::ApiError => e
  puts "Error when calling ShiftManagementShiftApi->shift_management_shifts_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Shift identifier to delete |  |

### Return type

[**ShiftManagementShift**](ShiftManagementShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## shift_management_shifts_id_get

> <ShiftManagementShift> shift_management_shifts_id_get(id)

Reads a single Shift

Reads a single Shift

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

api_instance = F::ShiftManagementShiftApi.new
id = '1' # String | Filter shifts by their unique identifiers. Returns only shifts matching the provided IDs. If an empty array is provided, returns no results

begin
  # Reads a single Shift
  result = api_instance.shift_management_shifts_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling ShiftManagementShiftApi->shift_management_shifts_id_get: #{e}"
end
```

#### Using the shift_management_shifts_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ShiftManagementShift>, Integer, Hash)> shift_management_shifts_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Shift
  data, status_code, headers = api_instance.shift_management_shifts_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ShiftManagementShift>
rescue F::ApiError => e
  puts "Error when calling ShiftManagementShiftApi->shift_management_shifts_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Filter shifts by their unique identifiers. Returns only shifts matching the provided IDs. If an empty array is provided, returns no results |  |

### Return type

[**ShiftManagementShift**](ShiftManagementShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## shift_management_shifts_post

> <ShiftManagementShift> shift_management_shifts_post(opts)

Creates a Shift

Creates a Shift

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

api_instance = F::ShiftManagementShiftApi.new
opts = {
  shift_management_shifts_post_request: F::ShiftManagementShiftsPostRequest.new({start_at: '2020-09-07T06:00:00.000+00:00', end_at: '2020-09-07T15:00:00.000+00:00', employee_id: '1', company_id: '1'}) # ShiftManagementShiftsPostRequest | 
}

begin
  # Creates a Shift
  result = api_instance.shift_management_shifts_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling ShiftManagementShiftApi->shift_management_shifts_post: #{e}"
end
```

#### Using the shift_management_shifts_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ShiftManagementShift>, Integer, Hash)> shift_management_shifts_post_with_http_info(opts)

```ruby
begin
  # Creates a Shift
  data, status_code, headers = api_instance.shift_management_shifts_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ShiftManagementShift>
rescue F::ApiError => e
  puts "Error when calling ShiftManagementShiftApi->shift_management_shifts_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **shift_management_shifts_post_request** | [**ShiftManagementShiftsPostRequest**](ShiftManagementShiftsPostRequest.md) |  | [optional] |

### Return type

[**ShiftManagementShift**](ShiftManagementShift.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

