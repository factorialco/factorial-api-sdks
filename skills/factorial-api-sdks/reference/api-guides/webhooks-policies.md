<!-- Vendored from https://apidoc.factorialhr.com/docs/webhooks-policies.md -->

# Webhooks Policies

## Notification and retries

To allow the service to recover from potential temporary errors on your end, we have implemented a retry policy of up to **20 attempts** over the **48 hours** following the event you
are subscribed to.

If the request is unsuccessful, in retries #1, #5, #10 and later, you will be notified of this issue via email.

After the maximum number of retries or the maximum allowed time has been reached, you will receive a final email notification, and the **subscription will be disabled.**
If the issue in your service is resolved, you can reactivate the subscription by following the instructions described in [Enabling or Disabling a
subscription](manage-webhooks#enabling-or-disabling-a-subscription).

### Email recipient resolution

Failure and disabling notifications are sent to the first available contact in this order:

1. **Partner email** — from the marketplace integration linked to the OAuth application
2. **OAuth application owner** — the user who owns the OAuth application that created the subscription
3. **Subscription author** — the user who originally created the webhook subscription
4. **Company admins** — if none of the above can be resolved, all company administrators with login rights are notified

If no recipient can be resolved at all, the notification is skipped and the event is logged internally.
