# F::HolidaysCompanyHolidayApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**holidays_company_holidays_get**](HolidaysCompanyHolidayApi.md#holidays_company_holidays_get) | **GET** /api/2026-07-01/resources/holidays/company_holidays | Reads all Company holidays |
| [**holidays_company_holidays_id_get**](HolidaysCompanyHolidayApi.md#holidays_company_holidays_id_get) | **GET** /api/2026-07-01/resources/holidays/company_holidays/{id} | Reads a single Company holiday |


## holidays_company_holidays_get

> <HolidaysCompanyHolidaysGet200Response> holidays_company_holidays_get(opts)

Reads all Company holidays

Retrieves company holidays

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

api_instance = F::HolidaysCompanyHolidayApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Company holiday ids
  location_ids: ['inner_example'], # Array<String> | Location ids
  team_ids: ['inner_example'], # Array<String> | Team ids
  employee_ids: ['inner_example'], # Array<String> | Filter by the default location of these employees
  start_at: '2024-12-01', # String | Start date
  end_at: '2024-12-31' # String | End date
}

begin
  # Reads all Company holidays
  result = api_instance.holidays_company_holidays_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling HolidaysCompanyHolidayApi->holidays_company_holidays_get: #{e}"
end
```

#### Using the holidays_company_holidays_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<HolidaysCompanyHolidaysGet200Response>, Integer, Hash)> holidays_company_holidays_get_with_http_info(opts)

```ruby
begin
  # Reads all Company holidays
  data, status_code, headers = api_instance.holidays_company_holidays_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <HolidaysCompanyHolidaysGet200Response>
rescue F::ApiError => e
  puts "Error when calling HolidaysCompanyHolidayApi->holidays_company_holidays_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Company holiday ids | [optional] |
| **location_ids** | [**Array&lt;String&gt;**](String.md) | Location ids | [optional] |
| **team_ids** | [**Array&lt;String&gt;**](String.md) | Team ids | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Filter by the default location of these employees | [optional] |
| **start_at** | **String** | Start date | [optional] |
| **end_at** | **String** | End date | [optional] |

### Return type

[**HolidaysCompanyHolidaysGet200Response**](HolidaysCompanyHolidaysGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## holidays_company_holidays_id_get

> <HolidaysCompanyHoliday> holidays_company_holidays_id_get(id)

Reads a single Company holiday

Retrieves company holidays

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

api_instance = F::HolidaysCompanyHolidayApi.new
id = '56' # String | Company holiday ids

begin
  # Reads a single Company holiday
  result = api_instance.holidays_company_holidays_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling HolidaysCompanyHolidayApi->holidays_company_holidays_id_get: #{e}"
end
```

#### Using the holidays_company_holidays_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<HolidaysCompanyHoliday>, Integer, Hash)> holidays_company_holidays_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Company holiday
  data, status_code, headers = api_instance.holidays_company_holidays_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <HolidaysCompanyHoliday>
rescue F::ApiError => e
  puts "Error when calling HolidaysCompanyHolidayApi->holidays_company_holidays_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Company holiday ids |  |

### Return type

[**HolidaysCompanyHoliday**](HolidaysCompanyHoliday.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

