<!-- Vendored from https://apidoc.factorialhr.com/docs/manage-webhooks.md -->

# Webhooks Subscriptions

Subscribing to webhooks is relatively straightforward. After obtaining an OAuth2 token or an API key, the next step is to create a **Webhook Subscription**.

Webhook Subscriptions manage and configure all of webhook functionalities. By registering a `target_url` for a specific `subscription_type` and including a `company_id` that refers to your company's ID, your application can receive instant updates whenever the associated events occur. When an event is triggered, Factorial's server sends an HTTP request to the `target_url`, often including a `challenge` token for verification. This allows the subscriber to securely process and respond to the notification.

> 📘 List of `subscription_type`
>
> All of Factorial's subscription types can be found at the [Webhooks](https://apidoc.factorialhr.com/reference/webhooks) section in the API Reference

## Create a Webhook Subscription

Use the [webhook subscription endpoint](https://apidoc.factorialhr.com/v2026-04-01/reference/post_api-2026-04-01-resources-api-public-webhook-subscriptions) to create your webhook.

> ❗️ Automatic subscription disabling
>
> Note that the subscription might be disabled automatically after some failed retries. Please, check the [Webhooks Polices](webhooks-policies) for further information.

### Example:

To subscribe to the candidate creation action, get the `subscription_type` from the [candidate webhook](https://apidoc.factorialhr.com/reference/post_webhooks-ats-candidate-creates).
Then use this value in the field `subscription_type` to create a Webhook Subscription:

```curl
curl --request POST \
     --url https://api.factorialhr.com/api/v2/resources/api_public/webhook_subscriptions \
     --header 'Accept: application/json' \
     --header 'Authorization: Bearer TOKEN' \
     --header 'Content-Type: application/json' \
     --data '
{
     "subscription_type": "ats/candidate/create",
     "target_url": "https://foo.com/webhooks/candidate_from_factorial",
     "name": "Webhook for a candidates creation"
     "challenge": "2zal4e6d"
     "company_id": 55
}
'
```

### Challenge

When a webhook challenge is created during the creation of a webhook. We send back that challenge in the header of the requests as `x-factorial-wh-challenge`

This allows various validation mechanisms to be used to ascertain that the request is originating from the subscription that was created earlier

## Enabling or disabling a subscription

To enable/disable a webhook subscription, simply do a PUT request with the webhook subscription's `{id}` param and the body `{enabled: true/false}`

By default, all subscriptions are created as enabled.

```curl
curl --request PUT \
     --url https://api.factorialhr.com/api/2024-10-01/resources/api_public/webhook_subscriptions/11303 \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'x-api-key: 12bddd1f5f0db6d16a476c66670eb0d545cd578cf45a0df674b4e52bca0ca6ad' \
     --data '{"enabled":false}'
```

<br />

## Unsubscribe

To delete a webhook or stop a subscription to an event, simply do a DELETE request with the webhook subscription's `{id}`.

```curl
curl --request DELETE \
     --url https://api.factorialhr.com/api/v2/resources/api_public/webhook_subscriptions/{id} \
     --header 'Accept: application/json' \
     --header 'Authorization: Bearer TOKEN' \
     --header 'Content-Type: application/json' \
```

## List subscriptions

To display current configured webhooks perform the following curl. (more info on the API documentation)

```curl
curl --request GET \
     --url https://api.factorialhr.com/api/v2/resources/api_public/webhook_subscriptions \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer TOKEN'
```
