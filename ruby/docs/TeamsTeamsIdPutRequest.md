# F::TeamsTeamsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | id of the team |  |
| **name** | **String** | name of the team | [optional] |
| **description** | **String** | Description of the team | [optional] |
| **avatar** | **File** | Avatar of the team | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::TeamsTeamsIdPutRequest.new(
  id: 1,
  name: Engineering,
  description: Engineering team description,
  avatar: https://api.factorialhr.com/rails/active_storage/representations/redirect/bob.png
)
```

