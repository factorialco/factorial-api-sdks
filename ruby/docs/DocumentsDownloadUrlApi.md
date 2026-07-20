# F::DocumentsDownloadUrlApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**documents_download_urls_bulk_create_post**](DocumentsDownloadUrlApi.md#documents_download_urls_bulk_create_post) | **POST** /api/2026-07-01/resources/documents/download_urls/bulk_create | Bulk creates a Download url |


## documents_download_urls_bulk_create_post

> <Array<DocumentsDownloadUrl>> documents_download_urls_bulk_create_post(opts)

Bulk creates a Download url

This endpoint generate temporal urls for a list of documents. The urls let you download the documents.

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

api_instance = F::DocumentsDownloadUrlApi.new
opts = {
  documents_download_urls_bulk_create_post_request: F::DocumentsDownloadUrlsBulkCreatePostRequest.new # DocumentsDownloadUrlsBulkCreatePostRequest | 
}

begin
  # Bulk creates a Download url
  result = api_instance.documents_download_urls_bulk_create_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling DocumentsDownloadUrlApi->documents_download_urls_bulk_create_post: #{e}"
end
```

#### Using the documents_download_urls_bulk_create_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<DocumentsDownloadUrl>>, Integer, Hash)> documents_download_urls_bulk_create_post_with_http_info(opts)

```ruby
begin
  # Bulk creates a Download url
  data, status_code, headers = api_instance.documents_download_urls_bulk_create_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<DocumentsDownloadUrl>>
rescue F::ApiError => e
  puts "Error when calling DocumentsDownloadUrlApi->documents_download_urls_bulk_create_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **documents_download_urls_bulk_create_post_request** | [**DocumentsDownloadUrlsBulkCreatePostRequest**](DocumentsDownloadUrlsBulkCreatePostRequest.md) |  | [optional] |

### Return type

[**Array&lt;DocumentsDownloadUrl&gt;**](DocumentsDownloadUrl.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

