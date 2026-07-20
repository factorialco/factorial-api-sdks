# F::TeamsTeamApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**teams_teams_get**](TeamsTeamApi.md#teams_teams_get) | **GET** /api/2026-07-01/resources/teams/teams | Reads all Teams |
| [**teams_teams_id_delete**](TeamsTeamApi.md#teams_teams_id_delete) | **DELETE** /api/2026-07-01/resources/teams/teams/{id} | Deletes a Team |
| [**teams_teams_id_get**](TeamsTeamApi.md#teams_teams_id_get) | **GET** /api/2026-07-01/resources/teams/teams/{id} | Reads a single Team |
| [**teams_teams_id_put**](TeamsTeamApi.md#teams_teams_id_put) | **PUT** /api/2026-07-01/resources/teams/teams/{id} | Updates a Team |
| [**teams_teams_post**](TeamsTeamApi.md#teams_teams_post) | **POST** /api/2026-07-01/resources/teams/teams | Creates a Team |


## teams_teams_get

> <TeamsTeamsGet200Response> teams_teams_get(opts)

Reads all Teams

Gets all the teams

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

api_instance = F::TeamsTeamApi.new
opts = {
  ids: ['inner_example'] # Array<String> | 
}

begin
  # Reads all Teams
  result = api_instance.teams_teams_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TeamsTeamApi->teams_teams_get: #{e}"
end
```

#### Using the teams_teams_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TeamsTeamsGet200Response>, Integer, Hash)> teams_teams_get_with_http_info(opts)

```ruby
begin
  # Reads all Teams
  data, status_code, headers = api_instance.teams_teams_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TeamsTeamsGet200Response>
rescue F::ApiError => e
  puts "Error when calling TeamsTeamApi->teams_teams_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) |  | [optional] |

### Return type

[**TeamsTeamsGet200Response**](TeamsTeamsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teams_teams_id_delete

> <TeamsTeam> teams_teams_id_delete(id)

Deletes a Team

Delete a team

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

api_instance = F::TeamsTeamApi.new
id = '1' # String | id of the team

begin
  # Deletes a Team
  result = api_instance.teams_teams_id_delete(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TeamsTeamApi->teams_teams_id_delete: #{e}"
end
```

#### Using the teams_teams_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TeamsTeam>, Integer, Hash)> teams_teams_id_delete_with_http_info(id)

```ruby
begin
  # Deletes a Team
  data, status_code, headers = api_instance.teams_teams_id_delete_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TeamsTeam>
rescue F::ApiError => e
  puts "Error when calling TeamsTeamApi->teams_teams_id_delete_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | id of the team |  |

### Return type

[**TeamsTeam**](TeamsTeam.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teams_teams_id_get

> <TeamsTeam> teams_teams_id_get(id)

Reads a single Team

Gets all the teams

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

api_instance = F::TeamsTeamApi.new
id = '1' # String | 

begin
  # Reads a single Team
  result = api_instance.teams_teams_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling TeamsTeamApi->teams_teams_id_get: #{e}"
end
```

#### Using the teams_teams_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TeamsTeam>, Integer, Hash)> teams_teams_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Team
  data, status_code, headers = api_instance.teams_teams_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TeamsTeam>
rescue F::ApiError => e
  puts "Error when calling TeamsTeamApi->teams_teams_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |

### Return type

[**TeamsTeam**](TeamsTeam.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teams_teams_id_put

> <TeamsTeam> teams_teams_id_put(id, opts)

Updates a Team

Update a team

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

api_instance = F::TeamsTeamApi.new
id = '1' # String | id of the team
opts = {
  teams_teams_id_put_request: F::TeamsTeamsIdPutRequest.new({id: '1'}) # TeamsTeamsIdPutRequest | 
}

begin
  # Updates a Team
  result = api_instance.teams_teams_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TeamsTeamApi->teams_teams_id_put: #{e}"
end
```

#### Using the teams_teams_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TeamsTeam>, Integer, Hash)> teams_teams_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Team
  data, status_code, headers = api_instance.teams_teams_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TeamsTeam>
rescue F::ApiError => e
  puts "Error when calling TeamsTeamApi->teams_teams_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | id of the team |  |
| **teams_teams_id_put_request** | [**TeamsTeamsIdPutRequest**](TeamsTeamsIdPutRequest.md) |  | [optional] |

### Return type

[**TeamsTeam**](TeamsTeam.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teams_teams_post

> <TeamsTeam> teams_teams_post(opts)

Creates a Team

Create a team with a given name

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

api_instance = F::TeamsTeamApi.new
opts = {
  teams_teams_post_request: F::TeamsTeamsPostRequest.new({name: 'Management'}) # TeamsTeamsPostRequest | 
}

begin
  # Creates a Team
  result = api_instance.teams_teams_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling TeamsTeamApi->teams_teams_post: #{e}"
end
```

#### Using the teams_teams_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TeamsTeam>, Integer, Hash)> teams_teams_post_with_http_info(opts)

```ruby
begin
  # Creates a Team
  data, status_code, headers = api_instance.teams_teams_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TeamsTeam>
rescue F::ApiError => e
  puts "Error when calling TeamsTeamApi->teams_teams_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **teams_teams_post_request** | [**TeamsTeamsPostRequest**](TeamsTeamsPostRequest.md) |  | [optional] |

### Return type

[**TeamsTeam**](TeamsTeam.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

