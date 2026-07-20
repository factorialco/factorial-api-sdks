# F::IntegrationsSyncRunOutputApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**integrations_sync_run_outputs_post**](IntegrationsSyncRunOutputApi.md#integrations_sync_run_outputs_post) | **POST** /api/2026-07-01/resources/integrations/sync_run_outputs | Creates a Sync run output |


## integrations_sync_run_outputs_post

> <IntegrationsSyncRunOutput> integrations_sync_run_outputs_post(sync_run_id, file)

Creates a Sync run output

Creates a Sync run output

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

api_instance = F::IntegrationsSyncRunOutputApi.new
sync_run_id = 'sync_run_id_example' # String | Identifier of the sync run this output belongs to
file = File.new('/path/to/some/file') # File | The CSV file to upload as the sync run output

begin
  # Creates a Sync run output
  result = api_instance.integrations_sync_run_outputs_post(sync_run_id, file)
  p result
rescue F::ApiError => e
  puts "Error when calling IntegrationsSyncRunOutputApi->integrations_sync_run_outputs_post: #{e}"
end
```

#### Using the integrations_sync_run_outputs_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<IntegrationsSyncRunOutput>, Integer, Hash)> integrations_sync_run_outputs_post_with_http_info(sync_run_id, file)

```ruby
begin
  # Creates a Sync run output
  data, status_code, headers = api_instance.integrations_sync_run_outputs_post_with_http_info(sync_run_id, file)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <IntegrationsSyncRunOutput>
rescue F::ApiError => e
  puts "Error when calling IntegrationsSyncRunOutputApi->integrations_sync_run_outputs_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **sync_run_id** | **String** | Identifier of the sync run this output belongs to |  |
| **file** | **File** | The CSV file to upload as the sync run output |  |

### Return type

[**IntegrationsSyncRunOutput**](IntegrationsSyncRunOutput.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

