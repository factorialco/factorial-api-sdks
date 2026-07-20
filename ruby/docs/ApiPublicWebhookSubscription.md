# F::ApiPublicWebhookSubscription

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Identifier of the webhook subscription |  |
| **target_url** | **String** | URL where the webhook payload will be sent |  |
| **type** | **String** | Type of the webhook subscription |  |
| **company_id** | **String** | Company identifier of the webhook subscription |  |
| **name** | **String** | Name of the webhook subscription | [optional] |
| **challenge** | **String** | String to verify the subscription | [optional] |
| **enabled** | **Boolean** | Boolean to enable/disable the subscription |  |
| **api_version** | **String** | API version of the webhook subscription that determines the schema of the payload |  |

## Example

```ruby
require 'factorial_api'

instance = F::ApiPublicWebhookSubscription.new(
  id: 1,
  target_url: https://webhook.site/,
  type: ats/job_posting/create,
  company_id: 1,
  name: Webhook subscription of a job posting created,
  challenge: 2bca4e6d-9aaf-4f11-9e5d,
  enabled: true,
  api_version: 2026-07-01
)
```

