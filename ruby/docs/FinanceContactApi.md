# F::FinanceContactApi

All URIs are relative to *https://api.factorialhr.com*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**finance_contacts_get**](FinanceContactApi.md#finance_contacts_get) | **GET** /api/2026-07-01/resources/finance/contacts | Reads all Contacts |
| [**finance_contacts_id_get**](FinanceContactApi.md#finance_contacts_id_get) | **GET** /api/2026-07-01/resources/finance/contacts/{id} | Reads a single Contact |
| [**finance_contacts_id_put**](FinanceContactApi.md#finance_contacts_id_put) | **PUT** /api/2026-07-01/resources/finance/contacts/{id} | Updates a Contact |
| [**finance_contacts_post**](FinanceContactApi.md#finance_contacts_post) | **POST** /api/2026-07-01/resources/finance/contacts | Creates a Contact |


## finance_contacts_get

> <FinanceContactsGet200Response> finance_contacts_get(opts)

Reads all Contacts

Reads all Contacts

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

api_instance = F::FinanceContactApi.new
opts = {
  ids: ['inner_example'], # Array<String> | List of Contact IDs to filter by.
  tax_ids: ['inner_example'], # Array<String> | List of Tax IDs to filter by.
  legal_name: 'Google', # String | Filter by partial match of a contact's legal name.
  name: 'Google', # String | The commercial name of the Contact.
  contact_type: 'client', # String | Type of the contact (defaults to Vendor).
  website: 'https://www.example.com', # String | The website of the Contact.
  email: 'contact@example.com', # String | The email of the Contact.
  phone_number: '+1234567890', # String | The phone number of the Contact.
  updated_from: '2025-01-01' # String | Start date for filtering Contacts records based on their last update.
}

begin
  # Reads all Contacts
  result = api_instance.finance_contacts_get(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceContactApi->finance_contacts_get: #{e}"
end
```

#### Using the finance_contacts_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceContactsGet200Response>, Integer, Hash)> finance_contacts_get_with_http_info(opts)

```ruby
begin
  # Reads all Contacts
  data, status_code, headers = api_instance.finance_contacts_get_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceContactsGet200Response>
rescue F::ApiError => e
  puts "Error when calling FinanceContactApi->finance_contacts_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ids** | [**Array&lt;String&gt;**](String.md) | List of Contact IDs to filter by. | [optional] |
| **tax_ids** | [**Array&lt;String&gt;**](String.md) | List of Tax IDs to filter by. | [optional] |
| **legal_name** | **String** | Filter by partial match of a contact&#39;s legal name. | [optional] |
| **name** | **String** | The commercial name of the Contact. | [optional] |
| **contact_type** | **String** | Type of the contact (defaults to Vendor). | [optional] |
| **website** | **String** | The website of the Contact. | [optional] |
| **email** | **String** | The email of the Contact. | [optional] |
| **phone_number** | **String** | The phone number of the Contact. | [optional] |
| **updated_from** | **String** | Start date for filtering Contacts records based on their last update. | [optional] |

### Return type

[**FinanceContactsGet200Response**](FinanceContactsGet200Response.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_contacts_id_get

> <FinanceContact> finance_contacts_id_get(id)

Reads a single Contact

Reads a single Contact

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

api_instance = F::FinanceContactApi.new
id = '123' # String | List of Contact IDs to filter by.

begin
  # Reads a single Contact
  result = api_instance.finance_contacts_id_get(id)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceContactApi->finance_contacts_id_get: #{e}"
end
```

#### Using the finance_contacts_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceContact>, Integer, Hash)> finance_contacts_id_get_with_http_info(id)

```ruby
begin
  # Reads a single Contact
  data, status_code, headers = api_instance.finance_contacts_id_get_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceContact>
rescue F::ApiError => e
  puts "Error when calling FinanceContactApi->finance_contacts_id_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | List of Contact IDs to filter by. |  |

### Return type

[**FinanceContact**](FinanceContact.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finance_contacts_id_put

> <FinanceContact> finance_contacts_id_put(id, opts)

Updates a Contact

Updates a Contact

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

api_instance = F::FinanceContactApi.new
id = '123' # String | ID of the Contact to update.
opts = {
  finance_contacts_id_put_request: F::FinanceContactsIdPutRequest.new({id: '123', address: {"city":"East Ariana","country_code":"SC","line1":"93402 Spencer Points","line2":"Apt. 555","postal_code":"61471","state":"Oklahoma"}}) # FinanceContactsIdPutRequest | 
}

begin
  # Updates a Contact
  result = api_instance.finance_contacts_id_put(id, opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceContactApi->finance_contacts_id_put: #{e}"
end
```

#### Using the finance_contacts_id_put_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceContact>, Integer, Hash)> finance_contacts_id_put_with_http_info(id, opts)

```ruby
begin
  # Updates a Contact
  data, status_code, headers = api_instance.finance_contacts_id_put_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceContact>
rescue F::ApiError => e
  puts "Error when calling FinanceContactApi->finance_contacts_id_put_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | ID of the Contact to update. |  |
| **finance_contacts_id_put_request** | [**FinanceContactsIdPutRequest**](FinanceContactsIdPutRequest.md) |  | [optional] |

### Return type

[**FinanceContact**](FinanceContact.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## finance_contacts_post

> <FinanceContact> finance_contacts_post(opts)

Creates a Contact

Creates a Contact

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

api_instance = F::FinanceContactApi.new
opts = {
  finance_contacts_post_request: F::FinanceContactsPostRequest.new({name: 'Google', address: {city=East Ariana, country_code=SC, line1=93402 Spencer Points, line2=Apt. 555, postal_code=61471, state=Oklahoma}}) # FinanceContactsPostRequest | 
}

begin
  # Creates a Contact
  result = api_instance.finance_contacts_post(opts)
  p result
rescue F::ApiError => e
  puts "Error when calling FinanceContactApi->finance_contacts_post: #{e}"
end
```

#### Using the finance_contacts_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FinanceContact>, Integer, Hash)> finance_contacts_post_with_http_info(opts)

```ruby
begin
  # Creates a Contact
  data, status_code, headers = api_instance.finance_contacts_post_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FinanceContact>
rescue F::ApiError => e
  puts "Error when calling FinanceContactApi->finance_contacts_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **finance_contacts_post_request** | [**FinanceContactsPostRequest**](FinanceContactsPostRequest.md) |  | [optional] |

### Return type

[**FinanceContact**](FinanceContact.md)

### Authorization

[apikey](../README.md#apikey), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

