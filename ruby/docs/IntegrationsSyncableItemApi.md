# F::IntegrationsSyncableItemApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**integrations_syncable_items_get**](IntegrationsSyncableItemApi.md#integrations_syncable_items_get) | **GET** /api/2026-07-01/resources/integrations/syncable_items | Reads all Syncable items |


## integrations_syncable_items_get

> <IntegrationsSyncableItemsGet200Response> integrations_syncable_items_get(sync_run_id)

Reads all Syncable items

Reads all Syncable items

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

api_instance = F::IntegrationsSyncableItemApi.new
sync_run_id = '1' # String | Identifier of the sync run

begin
  # Reads all Syncable items
  result = api_instance.integrations_syncable_items_get(sync_run_id)
  p result
rescue F::ApiError => e
  puts "Error when calling IntegrationsSyncableItemApi->integrations_syncable_items_get: #{e}"
end
```

#### Using the integrations_syncable_items_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<IntegrationsSyncableItemsGet200Response>, Integer, Hash)> integrations_syncable_items_get_with_http_info(sync_run_id)

```ruby
begin
  # Reads all Syncable items
  data, status_code, headers = api_instance.integrations_syncable_items_get_with_http_info(sync_run_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <IntegrationsSyncableItemsGet200Response>
rescue F::ApiError => e
  puts "Error when calling IntegrationsSyncableItemApi->integrations_syncable_items_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **sync_run_id** | **String** | Identifier of the sync run |  |

### Return type

[**IntegrationsSyncableItemsGet200Response**](IntegrationsSyncableItemsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

