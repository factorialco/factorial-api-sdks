# F::ApiPublicWebhookSubscriptionsIdPutRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the webhook subscription |  |
| **target_url** | **String** | URL where the webhook payload will be sent | [optional] |
| **subscription_type** | **String** | Type of the webhook subscription | [optional] |
| **name** | **String** | Name of the webhook subscription | [optional] |
| **challenge** | **String** | String to verify the subscription | [optional] |
| **enabled** | **Boolean** | Boolean to enable/disable the subscription | [optional] |
| **api_version** | **String** | API version of the webhook subscription that determines the schema of the payload | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ApiPublicWebhookSubscriptionsIdPutRequest.new(
  id: 1,
  target_url: https://webhook.site/,
  subscription_type: ats/job_posting/create,
  name: Webhook subscription of a job posting created,
  challenge: 2bca4e6d-9aaf-4f11-9e5d,
  enabled: true,
  api_version: null
)
```

