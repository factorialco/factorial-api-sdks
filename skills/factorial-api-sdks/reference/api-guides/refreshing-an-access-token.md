<!-- Vendored from https://apidoc.factorialhr.com/docs/refreshing-an-access-token.md -->

# Refreshing an access token

User access tokens are valid for a period of one hour. After this period has expired, you will need to request a new access token with a POST request, providing the refresh token that came with the first access token.

> 🚧 Note
>
> Non-admin users can perform this action as long as they have the refresh token provided at time of first authentication.

> ❗️ Important
>
> The refresh access token will last 1 week. In case you are over one week, you will need to start the process all over again.

```curl
curl -X POST 'https://api.factorialhr.com/oauth/token' -d 'client_id=<YOUR_CLIENT_ID>&client_secret=<YOUR_CLIENT_SECRET>&refresh_token=<REFRESH_TOKEN>&grant_type=refresh_token'
```

```text
https://api.factorialhr.com/oauth/token?client_id=<YOUR_CLIENT_ID>&client_secret=<YOUR_CLIENT_SECRET>&refresh_token=<REFRESH_TOKEN>&grant_type=refresh_token
```
