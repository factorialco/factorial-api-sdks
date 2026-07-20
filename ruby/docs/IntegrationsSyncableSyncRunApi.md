# F::IntegrationsSyncableSyncRunApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**integrations_syncable_sync_runs_id_put**](IntegrationsSyncableSyncRunApi.md#integrations_syncable_sync_runs_id_put) | **PUT** /api/2026-07-01/resources/integrations/syncable_sync_runs/{id} | Updates a Syncable sync run |


## integrations_syncable_sync_runs_id_put

> <IntegrationsSyncableSyncRun> integrations_syncable_sync_runs_id_put(id, opts)

Updates a Syncable sync run

Updates a Syncable sync run

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

api_instance = F::IntegrationsSyncableSyncRunApi.new
id = '1' # String | Identifier of the syncable sync run
opts = {
  integrations_syncable_sync_runs_id_put_request: F::IntegrationsSyncableSyncRunsIdPutRequest.new({id: '1', status: 'success'}) # IntegrationsSyncableSyncRunsIdPutRequest | 
}

begin
  # Updates a Syncable sync run
  result = api_instance.integrations_syncable_sync_runs_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling IntegrationsSyncableSyncRunApi->integrations_syncable_sync_runs_id_put: #{e}"
end
```

#### Using the integrations_syncable_sync_runs_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<IntegrationsSyncableSyncRun>, Integer, Hash)> integrations_syncable_sync_runs_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Syncable sync run
  data, status_code, headers = api_instance.integrations_syncable_sync_runs_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <IntegrationsSyncableSyncRun>
rescue F::ApiError => e
  puts "Error when calling IntegrationsSyncableSyncRunApi->integrations_syncable_sync_runs_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the syncable sync run |  |
| **integrations_syncable_sync_runs_id_put_request** | [**IntegrationsSyncableSyncRunsIdPutRequest**](IntegrationsSyncableSyncRunsIdPutRequest.md) |  | [optional] |

### Return type

[**IntegrationsSyncableSyncRun**](IntegrationsSyncableSyncRun.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

