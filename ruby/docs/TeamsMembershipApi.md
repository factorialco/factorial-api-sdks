# F::TeamsMembershipApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**teams_memberships_get**](TeamsMembershipApi.md#teams_memberships_get) | **GET** /api/2026-07-01/resources/teams/memberships | Reads all Memberships |
| [**teams_memberships_id_delete**](TeamsMembershipApi.md#teams_memberships_id_delete) | **DELETE** /api/2026-07-01/resources/teams/memberships/{id} | Deletes a Membership |
| [**teams_memberships_id_get**](TeamsMembershipApi.md#teams_memberships_id_get) | **GET** /api/2026-07-01/resources/teams/memberships/{id} | Reads a single Membership |
| [**teams_memberships_id_put**](TeamsMembershipApi.md#teams_memberships_id_put) | **PUT** /api/2026-07-01/resources/teams/memberships/{id} | Updates a Membership |
| [**teams_memberships_post**](TeamsMembershipApi.md#teams_memberships_post) | **POST** /api/2026-07-01/resources/teams/memberships | Creates a Membership |


## teams_memberships_get

> <TeamsMembershipsGet200Response> teams_memberships_get(opts)

Reads all Memberships

Get all memberships.

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

api_instance = F::TeamsMembershipApi.new
opts = {
  ids: ['inner_example'], # Array<String> | Membership ids.
  lead: true, # Boolean | Whether the employee is a lead of the team or not
  team_ids: ['inner_example'], # Array<String> | Team ids.
  employee_ids: ['inner_example'] # Array<String> | Employee ids.
}

begin
  # Reads all Memberships
  result = api_instance.teams_memberships_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TeamsMembershipApi->teams_memberships_get: #{e}"
end
```

#### Using the teams_memberships_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TeamsMembershipsGet200Response>, Integer, Hash)> teams_memberships_get_with_http_info(opts)

```ruby
begin
  # Reads all Memberships
  data, status_code, headers = api_instance.teams_memberships_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TeamsMembershipsGet200Response>
rescue F::ApiError => e
  puts "Error when calling TeamsMembershipApi->teams_memberships_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | Membership ids. | [optional] |
| **lead** | **Boolean** | Whether the employee is a lead of the team or not | [optional] |
| **team_ids** | [**Array&lt;String&gt;**](String.md) | Team ids. | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | Employee ids. | [optional] |

### Return type

[**TeamsMembershipsGet200Response**](TeamsMembershipsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teams_memberships_id_delete

> <TeamsMembership> teams_memberships_id_delete(id)

Deletes a Membership

Delete the membership to remove the employee from the team.

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

api_instance = F::TeamsMembershipApi.new
id = '1' # String | Membership id.

begin
  # Deletes a Membership
  result = api_instance.teams_memberships_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TeamsMembershipApi->teams_memberships_id_delete: #{e}"
end
```

#### Using the teams_memberships_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TeamsMembership>, Integer, Hash)> teams_memberships_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Membership
  data, status_code, headers = api_instance.teams_memberships_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TeamsMembership>
rescue F::ApiError => e
  puts "Error when calling TeamsMembershipApi->teams_memberships_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Membership id. |  |

### Return type

[**TeamsMembership**](TeamsMembership.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teams_memberships_id_get

> <TeamsMembership> teams_memberships_id_get(id)

Reads a single Membership

Get all memberships.

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

api_instance = F::TeamsMembershipApi.new
id = '1' # String | Membership ids.

begin
  # Reads a single Membership
  result = api_instance.teams_memberships_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TeamsMembershipApi->teams_memberships_id_get: #{e}"
end
```

#### Using the teams_memberships_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TeamsMembership>, Integer, Hash)> teams_memberships_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Membership
  data, status_code, headers = api_instance.teams_memberships_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TeamsMembership>
rescue F::ApiError => e
  puts "Error when calling TeamsMembershipApi->teams_memberships_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Membership ids. |  |

### Return type

[**TeamsMembership**](TeamsMembership.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teams_memberships_id_put

> <TeamsMembership> teams_memberships_id_put(id, opts)

Updates a Membership

Update the membership to either make the employee a lead of the team or remove them as a lead.

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

api_instance = F::TeamsMembershipApi.new
id = '1' # String | Membership id.
opts = {
  teams_memberships_id_put_request: F::TeamsMembershipsIdPutRequest.new({id: '1'}) # TeamsMembershipsIdPutRequest | 
}

begin
  # Updates a Membership
  result = api_instance.teams_memberships_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TeamsMembershipApi->teams_memberships_id_put: #{e}"
end
```

#### Using the teams_memberships_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TeamsMembership>, Integer, Hash)> teams_memberships_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Membership
  data, status_code, headers = api_instance.teams_memberships_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TeamsMembership>
rescue F::ApiError => e
  puts "Error when calling TeamsMembershipApi->teams_memberships_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Membership id. |  |
| **teams_memberships_id_put_request** | [**TeamsMembershipsIdPutRequest**](TeamsMembershipsIdPutRequest.md) |  | [optional] |

### Return type

[**TeamsMembership**](TeamsMembership.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teams_memberships_post

> <TeamsMembership> teams_memberships_post(opts)

Creates a Membership

Assign an employee to a team, meaning create a membership.

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

api_instance = F::TeamsMembershipApi.new
opts = {
  teams_memberships_post_request: F::TeamsMembershipsPostRequest.new({team_id: '1', employee_id: '5'}) # TeamsMembershipsPostRequest | 
}

begin
  # Creates a Membership
  result = api_instance.teams_memberships_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TeamsMembershipApi->teams_memberships_post: #{e}"
end
```

#### Using the teams_memberships_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TeamsMembership>, Integer, Hash)> teams_memberships_post_with_http_info(opts)

```ruby
begin
  # Creates a Membership
  data, status_code, headers = api_instance.teams_memberships_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TeamsMembership>
rescue F::ApiError => e
  puts "Error when calling TeamsMembershipApi->teams_memberships_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **teams_memberships_post_request** | [**TeamsMembershipsPostRequest**](TeamsMembershipsPostRequest.md) |  | [optional] |

### Return type

[**TeamsMembership**](TeamsMembership.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

