<!-- Vendored from https://apidoc.factorialhr.com/docs/webhook-attendance-clock-in.md -->

# Practical Example: Clock In a Shift

Get a notification when an user clocks in a shift inside Factorial

## When?

When the user clocks in a shift and starts the timer, this event is triggered.

<Image title="Screenshot 2021-10-29 at 13.49.22.png" alt={2054} align="center" src="https://files.readme.io/67b2beb-Screenshot_2021-10-29_at_13.49.22.png">
  Click on "Clock in" to trigger the event
</Image>

## How?

With the [Clocks in a shift webhook](https://apidoc.factorialhr.com/reference/post_webhooks-attendance-shift-clock-ins) get the `subscription_type` and the value:`attendance/shift/clock_in` in the [Creates a Webhook subscription](https://apidoc.factorialhr.com/reference/post_api-v2-resources-api-public-webhook-subscriptions) endpoint:

```curl
curl --request POST \
     --url https://api.factorialhr.com/api/v2/resources/api_public/webhook_subscriptions \
     --header 'Accept: application/json' \
     --header 'Authorization: Bearer TOKEN' \
     --header 'Content-Type: application/json' \
     --data '
{
     "subscription_type": "attendance/shift/clock_in",
     "target_url": "https://foo.com/webhooks/candidate_from_factorial",
     "name": "Webhook for a shift clock"
     "challenge": "2zal4e6d"
     "company_id": 55
}
'
```

## What data in sent in the notification?

```
{
  "employee_id": 1,
  "now": "2024-06-23T11:00:00.000+00:00",
  "latitude": 52.377956,
  "longitude": 4.89707,
  "accuracy": 5,
  "observations": "I clocked in 10 minutes before",
  "location_type": "business_trip",
  "workplace_id":5,
  "time_settings_break_configuration_id": 2,
  "project_worker_id": 3,
  "subproject_id": 4
}
```

<br />

## Why would I subscribe to this event??

* Do an action on an external application immediately when user clocks in.
* Sync shifts with external application.
