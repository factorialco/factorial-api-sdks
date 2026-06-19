<!-- Vendored from https://apidoc.factorialhr.com/docs/request-an-access-token.md -->

# Request an access token

This page will teach you how to request an access token for your users

Once your user provides you with their authorization code, you can request their access token to Factorial. This is done via a POST request to the following URL:

> 🚧 Note
>
> Non-admin users can perform this action as long as they have the Oauth Application credentials

```curl
curl -X POST 'https://api.factorialhr.com/oauth/token' -d 'client_id=<YOUR_CLIENT_ID>&client_secret=<YOUR_CLIENT_SECRET>&code=<AUTHORIZATION_CODE>&grant_type=authorization_code&redirect_uri=<REDIRECT_URI>'

YOUR_CLIENT_ID: OAuth2 Application Id
YOUR_CLIENT_SECRET: OAuth2 Application Secret
AUTHORIZATION_CODE: OAuth2 CODE
REDIRECT_URI: OAuth2 Redirect URL
```

```text
https://api.factorialhr.com/oauth/token?client_id=<YOUR_CLIENT_ID>&client_secret=<YOUR_CLIENT_SECRET>&code=<AUTHORIZATION_CODE>&grant_type=authorization_code&redirect_uri=<REDIRECT_URI>

YOUR_CLIENT_ID: OAuth2 Application Id
YOUR_CLIENT_SECRET: OAuth2 Application Secret
AUTHORIZATION_CODE: OAuth2 CODE
REDIRECT_URI: OAuth2 Redirect URL
```

The `CLIENT_ID`, `CLIENT_SECRET` and `REDIRECT_URI` variables are available in the OAuth application page which can be accessed from your [repository of OAuth applications](https://api.factorialhr.com/oauth/applications).

The `AUTHORIZATION_CODE` should either be provided to you by your integration's users or, in case of single-user integrations, you should already have it as described in the [previous step of this guide](https://factorial.readme.io/docs/request-an-authorization-code).

The response to this request will have the following shape:

```json
{
 "access_token": "de6780bc506a0446309bd9362820ba8aed28aa506c71eedbe1c5c4f9dd350e54",
 "token_type": "Bearer", 
 "expires_in": 7200,
 "refresh_token": "8257e65c97202ed1726cf9571600918f3bffb2544b26e00a61df9897668c33a1",
 "scope": "read write",
 "created_at": 1680013957
}
```

Congratulations! With this token, your integration is now able to make requests to Factorial's API. You just need to pass the access token in the HTTP `Authorization` header as such: `Authorization: Bearer <ACCESS_TOKEN>`.

You can generate only one OAuth2 token with the same code, you should refresh your token.

Every time a new token is generated a refresh token is generated as well, so that you can use it as the OAuth2 Refresh Token, and an expiry date is also provided.

Now that you are authorized and authenticated to use Factorial's API, you might want to check out our [API reference](https://factorial.readme.io/reference). Happy hacking!

> ❗️ Access token expiration
>
> User access tokens are valid for a period of one hour. After this period has expired, you will need to request a new access token via a POST request providing the `REFRESH_TOKEN` that came with the expired access token. See how to do it [here](https://apidoc.factorialhr.com/docs/refreshing-an-access-token).

## Checking access token ownership

If you have a multi-company or multi-user integration, you will retrieve multiple access tokens

You will be interested in identifying which user or company granted access to their data in Factorial

> 📘 Identify you token access owner
>
> You can use the [Credentials](https://apidoc.factorialhr.com/reference/get_api-v2-resources-api-public-credentials) API endpoint to get information about the owner of a give token
