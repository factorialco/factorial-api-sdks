# F::BookkeepersManagementIncidenceApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**bookkeepers_management_incidences_get**](BookkeepersManagementIncidenceApi.md#bookkeepers_management_incidences_get) | **GET** /api/2026-07-01/resources/bookkeepers_management/incidences | Reads all Incidences |
| [**bookkeepers_management_incidences_id_get**](BookkeepersManagementIncidenceApi.md#bookkeepers_management_incidences_id_get) | **GET** /api/2026-07-01/resources/bookkeepers_management/incidences/{id} | Reads a single Incidence |
| [**bookkeepers_management_incidences_id_put**](BookkeepersManagementIncidenceApi.md#bookkeepers_management_incidences_id_put) | **PUT** /api/2026-07-01/resources/bookkeepers_management/incidences/{id} | Updates an Incidence |


## bookkeepers_management_incidences_get

> <BookkeepersManagementIncidencesGet200Response> bookkeepers_management_incidences_get(opts)

Reads all Incidences

Reads all Incidences

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

api_instance = F::BookkeepersManagementIncidenceApi.new
opts = {
  ids: ['inner_example'], # Array<String> | A list of incidence identifiers.
  legal_entities_ids: ['inner_example'], # Array<String> | A list of legal entities identifiers.
  status: ['inner_example'], # Array<String> | A list of statuses.
  starts_on: '2020-01-01', # String | Get the incidence (aka employee update) that start safter this date (included).
  ends_on: '2020-01-01', # String | Get the incidence (aka employee update) that ends before this date (included).
  type: ['inner_example'], # Array<String> | A list of types. It can be any of the following address, bank, cost_center, contract, gender, hiring, id, irpf, legal_entity, manual_incidence, name, nationality, parental, phone_number, sick, tax_id, termination, workplace
  sort_by: 'effective_date', # String | Field to sort by. It can be any of the following employee_first_name, employee_last_name, type, legal_entity_name, effective_date, status.
  direction: 'desc', # String | Sort direction. It can be 'asc' or 'desc'.
  search: 'Hellen', # String | Filter the result by the name of the employee.
  employee_ids: ['inner_example'], # Array<String> | A list of employee identifiers.
  contains_message: true, # Boolean | Boolean that filters incidences that does or does not contains messages.
  message_from: 'bookkeeper', # String | Filter by message sender.
  custom_leave_name: ['inner_example'] # Array<String> | A list of custom leave names.
}

begin
  # Reads all Incidences
  result = api_instance.bookkeepers_management_incidences_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling BookkeepersManagementIncidenceApi->bookkeepers_management_incidences_get: #{e}"
end
```

#### Using the bookkeepers_management_incidences_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BookkeepersManagementIncidencesGet200Response>, Integer, Hash)> bookkeepers_management_incidences_get_with_http_info(opts)

```ruby
begin
  # Reads all Incidences
  data, status_code, headers = api_instance.bookkeepers_management_incidences_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BookkeepersManagementIncidencesGet200Response>
rescue F::ApiError => e
  puts "Error when calling BookkeepersManagementIncidenceApi->bookkeepers_management_incidences_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | A list of incidence identifiers. | [optional] |
| **legal_entities_ids** | [**Array&lt;String&gt;**](String.md) | A list of legal entities identifiers. | [optional] |
| **status** | [**Array&lt;String&gt;**](String.md) | A list of statuses. | [optional] |
| **starts_on** | **String** | Get the incidence (aka employee update) that start safter this date (included). | [optional] |
| **ends_on** | **String** | Get the incidence (aka employee update) that ends before this date (included). | [optional] |
| **type** | [**Array&lt;String&gt;**](String.md) | A list of types. It can be any of the following address, bank, cost_center, contract, gender, hiring, id, irpf, legal_entity, manual_incidence, name, nationality, parental, phone_number, sick, tax_id, termination, workplace | [optional] |
| **sort_by** | **String** | Field to sort by. It can be any of the following employee_first_name, employee_last_name, type, legal_entity_name, effective_date, status. | [optional] |
| **direction** | **String** | Sort direction. It can be &#39;asc&#39; or &#39;desc&#39;. | [optional] |
| **search** | **String** | Filter the result by the name of the employee. | [optional] |
| **employee_ids** | [**Array&lt;String&gt;**](String.md) | A list of employee identifiers. | [optional] |
| **contains_message** | **Boolean** | Boolean that filters incidences that does or does not contains messages. | [optional] |
| **message_from** | **String** | Filter by message sender. | [optional] |
| **custom_leave_name** | [**Array&lt;String&gt;**](String.md) | A list of custom leave names. | [optional] |

### Return type

[**BookkeepersManagementIncidencesGet200Response**](BookkeepersManagementIncidencesGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bookkeepers_management_incidences_id_get

> <BookkeepersManagementIncidence> bookkeepers_management_incidences_id_get(id)

Reads a single Incidence

Reads a single Incidence

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

api_instance = F::BookkeepersManagementIncidenceApi.new
id = '1' # String | A list of incidence identifiers.

begin
  # Reads a single Incidence
  result = api_instance.bookkeepers_management_incidences_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling BookkeepersManagementIncidenceApi->bookkeepers_management_incidences_id_get: #{e}"
end
```

#### Using the bookkeepers_management_incidences_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BookkeepersManagementIncidence>, Integer, Hash)> bookkeepers_management_incidences_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Incidence
  data, status_code, headers = api_instance.bookkeepers_management_incidences_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BookkeepersManagementIncidence>
rescue F::ApiError => e
  puts "Error when calling BookkeepersManagementIncidenceApi->bookkeepers_management_incidences_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | A list of incidence identifiers. |  |

### Return type

[**BookkeepersManagementIncidence**](BookkeepersManagementIncidence.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bookkeepers_management_incidences_id_put

> <BookkeepersManagementIncidence> bookkeepers_management_incidences_id_put(id, opts)

Updates an Incidence

Updates an Incidence

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

api_instance = F::BookkeepersManagementIncidenceApi.new
id = '1' # String | incidence (aka employee update) identifier to update.
opts = {
  bookkeepers_management_incidences_id_put_request: F::BookkeepersManagementIncidencesIdPutRequest.new({id: '1'}) # BookkeepersManagementIncidencesIdPutRequest | 
}

begin
  # Updates an Incidence
  result = api_instance.bookkeepers_management_incidences_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling BookkeepersManagementIncidenceApi->bookkeepers_management_incidences_id_put: #{e}"
end
```

#### Using the bookkeepers_management_incidences_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BookkeepersManagementIncidence>, Integer, Hash)> bookkeepers_management_incidences_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates an Incidence
  data, status_code, headers = api_instance.bookkeepers_management_incidences_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BookkeepersManagementIncidence>
rescue F::ApiError => e
  puts "Error when calling BookkeepersManagementIncidenceApi->bookkeepers_management_incidences_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | incidence (aka employee update) identifier to update. |  |
| **bookkeepers_management_incidences_id_put_request** | [**BookkeepersManagementIncidencesIdPutRequest**](BookkeepersManagementIncidencesIdPutRequest.md) |  | [optional] |

### Return type

[**BookkeepersManagementIncidence**](BookkeepersManagementIncidence.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

