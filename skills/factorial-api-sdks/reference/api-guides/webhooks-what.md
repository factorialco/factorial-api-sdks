<!-- Vendored from https://apidoc.factorialhr.com/docs/webhooks-what.md -->

# What are webhooks?

Webhooks are instant notifications sent from Factorial to another application when something specific happens.

<Callout icon="📘" theme="info">
  "Knock knock on X outside Factorial when Y happens inside Factorial"
</Callout>

> 🚧 Usage
>
> Webhooks can be used directly or via intermediary platforms or services. Using them directly requires technical knowledge.

Webhooks allow you to build or set up integrations, such as sync between platforms or perform an action after a specific event happens inside Factorial. **When one of those events is triggered, a HTTP POST payload will be sent to the webhook's configured URL**. Webhooks can be used to update an external LDAP, trigger processes, update another application, or even connect to another platform to perform other events. You're only limited by your imagination.

## Factorial Webhooks

Many things are constantly happening inside Factorial . We require knowing the moment these events happen and their related information. We will notify you in these cases.

> 📘 List of available webhooks
>
> All of Factorial's subscription types can be found at the [Webhooks](https://apidoc.factorialhr.com/reference/webhooks) section in the API Reference
>
> The information sent in the notification can be found in the `Callback payload` in each [Webhook](https://apidoc.factorialhr.com/reference/webhooks)

> 🚧 Url
>
> The same URL can be used to get notifications for all events or different ones per event. Notice that if the same url for receiving notifications is used for all events, then distinguishing an event from another might be an issue.

When an event occurs inside Factorial, a POST request is triggered to the associated event URL. If the request fails for any reason, a retry is performed shortly after. In the case of more failures, the subscription is marked as disabled.

## Webhook Subscriptions

Subscribing to webhooks is relatively straightforward. After obtaining an OAuth2 token or an API key, the next step is to create a **Webhook Subscription**.

Webhook Subscriptions manage and configure all of webhook functionalities. By registering a `target_url` for a specific `subscription_type` and including a `company_id` that refers to your company's ID, your application can receive instant updates whenever the associated events occur. When an event is triggered, Factorial's server sends an HTTP request to the `target_url`, often including a `challenge` token for verification. This allows the subscriber to securely process and respond to the notification.

## Webhook author headers

Webhook deliveries may include optional headers that identify who triggered the event.

### Headers

* `x-factorial-author-id`
* `x-factorial-author-type`

`x-factorial-author-type` will be `employee` or `company`.

The headers are only sent when the author can be safely exposed to the subscriber. If the author is not visible to the subscriber, the headers are omitted.

These headers are metadata only and do not change the webhook payload.
