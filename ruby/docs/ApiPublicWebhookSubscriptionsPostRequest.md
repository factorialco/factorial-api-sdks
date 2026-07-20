# F::ApiPublicWebhookSubscriptionsPostRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **subscription_type** | **String** | Type of the webhook subscription |  |
| **target_url** | **String** | URL where the webhook payload will be sent |  |
| **name** | **String** | Name of the webhook subscription | [optional] |
| **challenge** | **String** | String to verify the subscription | [optional] |
| **company_id** | **String** | Company identifier of the webhook subscription |  |
| **enabled** | **Boolean** | Boolean to enable/disable the subscription | [optional] |
| **api_version** | **String** | API version of the webhook subscription that determines the schema of the payload | [optional] |

## Example

```ruby
require 'factorial_api'

instance = F::ApiPublicWebhookSubscriptionsPostRequest.new(
  subscription_type: ats/job_posting/create,
  target_url: https://webhook.site/,
  name: Webhook subscription of a job posting created,
  challenge: 2bca4e6d-9aaf-4f11-9e5d,
  company_id: 1,
  enabled: true,
  api_version: null
)
```

