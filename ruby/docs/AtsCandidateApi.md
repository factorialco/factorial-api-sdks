# F::AtsCandidateApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**ats_candidates_get**](AtsCandidateApi.md#ats_candidates_get) | **GET** /api/2026-07-01/resources/ats/candidates | Reads all Candidates |
| [**ats_candidates_id_delete**](AtsCandidateApi.md#ats_candidates_id_delete) | **DELETE** /api/2026-07-01/resources/ats/candidates/{id} | Deletes a Candidate |
| [**ats_candidates_id_get**](AtsCandidateApi.md#ats_candidates_id_get) | **GET** /api/2026-07-01/resources/ats/candidates/{id} | Reads a single Candidate |
| [**ats_candidates_id_put**](AtsCandidateApi.md#ats_candidates_id_put) | **PUT** /api/2026-07-01/resources/ats/candidates/{id} | Updates a Candidate |
| [**ats_candidates_post**](AtsCandidateApi.md#ats_candidates_post) | **POST** /api/2026-07-01/resources/ats/candidates | Creates a Candidate |


## ats_candidates_get

> <AtsCandidatesGet200Response> ats_candidates_get(opts)

Reads all Candidates

Fetches candidates data from Factorial. When using administrator-level API Credentials, all candidates associated with a company will be returned. When using non-admin level API credentials, only candidates that applied to a job for which the user is a hiring manager will be returned.

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

api_instance = F::AtsCandidateApi.new
opts = {
  ids: ['inner_example'], # Array<String> | list of candidate identifiers.
  emails: ['inner_example'], # Array<String> | list of candidate emails.
  team_ids: ['inner_example'], # Array<String> | list of team identifiers, refers to teams/teams endpoint.
  location_ids: ['inner_example'], # Array<String> | list of location identifiers, refers to locations/locations endpoint.
  source: ['inner_example'], # Array<String> | source of the candidate.
  remote: true, # Boolean | is the candidate remote?
  job_posting_ids: ['inner_example'], # Array<String> | list of job posting identifiers, refers to ats/job_postings endpoint.
  minimum_average_rating: 4, # Float | minimum average rating of the candidate.
  active: true, # Boolean | is the candidate active?
  talent_pool: true, # Boolean | is the candidate part of talent pool?
  archived: true # Boolean | is the candidate archived?
}

begin
  # Reads all Candidates
  result = api_instance.ats_candidates_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsCandidateApi->ats_candidates_get: #{e}"
end
```

#### Using the ats_candidates_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsCandidatesGet200Response>, Integer, Hash)> ats_candidates_get_with_http_info(opts)

```ruby
begin
  # Reads all Candidates
  data, status_code, headers = api_instance.ats_candidates_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsCandidatesGet200Response>
rescue F::ApiError => e
  puts "Error when calling AtsCandidateApi->ats_candidates_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | list of candidate identifiers. | [optional] |
| **emails** | [**Array&lt;String&gt;**](String.md) | list of candidate emails. | [optional] |
| **team_ids** | [**Array&lt;String&gt;**](String.md) | list of team identifiers, refers to teams/teams endpoint. | [optional] |
| **location_ids** | [**Array&lt;String&gt;**](String.md) | list of location identifiers, refers to locations/locations endpoint. | [optional] |
| **source** | [**Array&lt;String&gt;**](String.md) | source of the candidate. | [optional] |
| **remote** | **Boolean** | is the candidate remote? | [optional] |
| **job_posting_ids** | [**Array&lt;String&gt;**](String.md) | list of job posting identifiers, refers to ats/job_postings endpoint. | [optional] |
| **minimum_average_rating** | **Float** | minimum average rating of the candidate. | [optional] |
| **active** | **Boolean** | is the candidate active? | [optional] |
| **talent_pool** | **Boolean** | is the candidate part of talent pool? | [optional] |
| **archived** | **Boolean** | is the candidate archived? | [optional] |

### Return type

[**AtsCandidatesGet200Response**](AtsCandidatesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_candidates_id_delete

> <AtsCandidate> ats_candidates_id_delete(id)

Deletes a Candidate

Deletes a candidate from the ATS

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

api_instance = F::AtsCandidateApi.new
id = '1' # String | identifier of the candidate.

begin
  # Deletes a Candidate
  result = api_instance.ats_candidates_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsCandidateApi->ats_candidates_id_delete: #{e}"
end
```

#### Using the ats_candidates_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsCandidate>, Integer, Hash)> ats_candidates_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Candidate
  data, status_code, headers = api_instance.ats_candidates_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsCandidate>
rescue F::ApiError => e
  puts "Error when calling AtsCandidateApi->ats_candidates_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the candidate. |  |

### Return type

[**AtsCandidate**](AtsCandidate.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_candidates_id_get

> <AtsCandidate> ats_candidates_id_get(id)

Reads a single Candidate

Fetches candidates data from Factorial. When using administrator-level API Credentials, all candidates associated with a company will be returned. When using non-admin level API credentials, only candidates that applied to a job for which the user is a hiring manager will be returned.

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

api_instance = F::AtsCandidateApi.new
id = '1' # String | list of candidate identifiers.

begin
  # Reads a single Candidate
  result = api_instance.ats_candidates_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsCandidateApi->ats_candidates_id_get: #{e}"
end
```

#### Using the ats_candidates_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsCandidate>, Integer, Hash)> ats_candidates_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Candidate
  data, status_code, headers = api_instance.ats_candidates_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsCandidate>
rescue F::ApiError => e
  puts "Error when calling AtsCandidateApi->ats_candidates_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | list of candidate identifiers. |  |

### Return type

[**AtsCandidate**](AtsCandidate.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ats_candidates_id_put

> <AtsCandidate> ats_candidates_id_put(id, opts)

Updates a Candidate

Updates ATS Candidates data

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

api_instance = F::AtsCandidateApi.new
id = '1' # String | identifier of the candidate.
opts = {
  ats_candidates_id_put_request: F::AtsCandidatesIdPutRequest.new({id: '1'}) # AtsCandidatesIdPutRequest | 
}

begin
  # Updates a Candidate
  result = api_instance.ats_candidates_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsCandidateApi->ats_candidates_id_put: #{e}"
end
```

#### Using the ats_candidates_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsCandidate>, Integer, Hash)> ats_candidates_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Candidate
  data, status_code, headers = api_instance.ats_candidates_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsCandidate>
rescue F::ApiError => e
  puts "Error when calling AtsCandidateApi->ats_candidates_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | identifier of the candidate. |  |
| **ats_candidates_id_put_request** | [**AtsCandidatesIdPutRequest**](AtsCandidatesIdPutRequest.md) |  | [optional] |

### Return type

[**AtsCandidate**](AtsCandidate.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ats_candidates_post

> <AtsCandidate> ats_candidates_post(opts)

Creates a Candidate

Creates candidates related to a particular company in an ATS

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

api_instance = F::AtsCandidateApi.new
opts = {
  ats_candidates_post_request: F::AtsCandidatesPostRequest.new({first_name: 'Ana', last_name: 'Fernandez Perez', company_id: '1'}) # AtsCandidatesPostRequest | 
}

begin
  # Creates a Candidate
  result = api_instance.ats_candidates_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling AtsCandidateApi->ats_candidates_post: #{e}"
end
```

#### Using the ats_candidates_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AtsCandidate>, Integer, Hash)> ats_candidates_post_with_http_info(opts)

```ruby
begin
  # Creates a Candidate
  data, status_code, headers = api_instance.ats_candidates_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AtsCandidate>
rescue F::ApiError => e
  puts "Error when calling AtsCandidateApi->ats_candidates_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ats_candidates_post_request** | [**AtsCandidatesPostRequest**](AtsCandidatesPostRequest.md) |  | [optional] |

### Return type

[**AtsCandidate**](AtsCandidate.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

