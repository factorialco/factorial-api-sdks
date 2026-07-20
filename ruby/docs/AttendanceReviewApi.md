# F::AttendanceReviewApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**attendance_reviews_bulk_create_post**](AttendanceReviewApi.md#attendance_reviews_bulk_create_post) | **POST** /api/2026-07-01/resources/attendance/reviews/bulk_create | Bulk creates a Review |
| [**attendance_reviews_bulk_destroy_post**](AttendanceReviewApi.md#attendance_reviews_bulk_destroy_post) | **POST** /api/2026-07-01/resources/attendance/reviews/bulk_destroy | Bulk destroys a Review |
| [**attendance_reviews_get**](AttendanceReviewApi.md#attendance_reviews_get) | **GET** /api/2026-07-01/resources/attendance/reviews | Reads all Reviews |


## attendance_reviews_bulk_create_post

> <Array<AttendanceReview>> attendance_reviews_bulk_create_post(opts)

Bulk creates a Review

Bulk creates a Review

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

api_instance = F::AttendanceReviewApi.new
opts = {
  attendance_reviews_bulk_create_post_request: F::AttendanceReviewsBulkCreatePostRequest.new({employee_ids: ["1", "2", "3"], start_on: '2025-02-01', end_on: '2025-02-28', reviewed_by: '1'}) # AttendanceReviewsBulkCreatePostRequest | 
}

begin
  # Bulk creates a Review
  result = api_instance.attendance_reviews_bulk_create_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceReviewApi->attendance_reviews_bulk_create_post: #{e}"
end
```

#### Using the attendance_reviews_bulk_create_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<AttendanceReview>>, Integer, Hash)> attendance_reviews_bulk_create_post_with_http_info(opts)

```ruby
begin
  # Bulk creates a Review
  data, status_code, headers = api_instance.attendance_reviews_bulk_create_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<AttendanceReview>>
rescue F::ApiError => e
  puts "Error when calling AttendanceReviewApi->attendance_reviews_bulk_create_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_reviews_bulk_create_post_request** | [**AttendanceReviewsBulkCreatePostRequest**](AttendanceReviewsBulkCreatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;AttendanceReview&gt;**](AttendanceReview.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attendance_reviews_bulk_destroy_post

> <Array<AttendanceReview>> attendance_reviews_bulk_destroy_post(opts)

Bulk destroys a Review

Bulk destroys a Review

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

api_instance = F::AttendanceReviewApi.new
opts = {
  attendance_reviews_bulk_destroy_post_request: F::AttendanceReviewsBulkDestroyPostRequest.new({employee_ids: [1,  2,  3], start_on: '2025-01-01', end_on: '2025-01-02'}) # AttendanceReviewsBulkDestroyPostRequest | 
}

begin
  # Bulk destroys a Review
  result = api_instance.attendance_reviews_bulk_destroy_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceReviewApi->attendance_reviews_bulk_destroy_post: #{e}"
end
```

#### Using the attendance_reviews_bulk_destroy_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<AttendanceReview>>, Integer, Hash)> attendance_reviews_bulk_destroy_post_with_http_info(opts)

```ruby
begin
  # Bulk destroys a Review
  data, status_code, headers = api_instance.attendance_reviews_bulk_destroy_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<AttendanceReview>>
rescue F::ApiError => e
  puts "Error when calling AttendanceReviewApi->attendance_reviews_bulk_destroy_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **attendance_reviews_bulk_destroy_post_request** | [**AttendanceReviewsBulkDestroyPostRequest**](AttendanceReviewsBulkDestroyPostRequest.md) |  | [optional] |

### Return type

[**Array&lt;AttendanceReview&gt;**](AttendanceReview.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attendance_reviews_get

> <AttendanceReviewsGet200Response> attendance_reviews_get(employee_ids, start_on, end_on, reviewed_at)

Reads all Reviews

Reads all Reviews

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

api_instance = F::AttendanceReviewApi.new
employee_ids = ['inner_example'] # Array<String> | Employee identifiers
start_on = '2025-01-01' # String | Start date of the reviews
end_on = '2025-01-02' # String | End date of the reviews
reviewed_at = '2025-01-02T00:00:00.000Z' # String | Reviewed at date(ISO 8601 format string)

begin
  # Reads all Reviews
  result = api_instance.attendance_reviews_get(employee_ids, start_on, end_on, reviewed_at)
  p result
rescue F::ApiError => e
  puts "Error when calling AttendanceReviewApi->attendance_reviews_get: #{e}"
end
```

#### Using the attendance_reviews_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AttendanceReviewsGet200Response>, Integer, Hash)> attendance_reviews_get_with_http_info(employee_ids, start_on, end_on, reviewed_at)

```ruby
begin
  # Reads all Reviews
  data, status_code, headers = api_instance.attendance_reviews_get_with_http_info(employee_ids, start_on, end_on, reviewed_at)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AttendanceReviewsGet200Response>
rescue F::ApiError => e
  puts "Error when calling AttendanceReviewApi->attendance_reviews_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Employee identifiers |  |
| **start_on** | **String** | Start date of the reviews |  |
| **end_on** | **String** | End date of the reviews |  |
| **reviewed_at** | **String** | Reviewed at date(ISO 8601 format string) |  |

### Return type

[**AttendanceReviewsGet200Response**](AttendanceReviewsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

