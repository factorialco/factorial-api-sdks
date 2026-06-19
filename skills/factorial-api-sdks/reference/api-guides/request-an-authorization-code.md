<!-- Vendored from https://apidoc.factorialhr.com/docs/request-an-authorization-code.md -->

# Request an authorization code

This page will teach you how your users can authorize your integration to access Factorial's API

Once you have [your Oauth application in Factorial](https://apidoc.factorialhr.com/docs/create-a-new-oauth-application) you will be able to let your users grant your integration access to Factorial's API. In order to do that, you will need to redirect users of your integration URL

## Fetching your authorization code in your application code

Use this URL and change the parameters with your information

```text
https://api.factorialhr.com/oauth/authorize?client_id=<YOUR_CLIENT_ID>&redirect_uri=<YOUR_REDIRECT_URI>&response_type=code

YOUR_CLIENT_ID: OAuth2 Application Id
REDIRECT_URI: OAuth2 Redirect URL
```

> 📘 Which URL to use for production or demo?
>
> Use the following hosts:
>
> * `api.factorialhr.com`for requesting codes in the Production environment
> * `api.demo.factorial.dev` for requesting codes in the Demo environment
>
> Learn more about the [environments: production and demo](https://apidoc.factorialhr.com/docs/production-and-demo) and [how to create an OAuth2 application in both environments](https://apidoc.factorialhr.com/docs/create-a-new-oauth-application)

### `state` parameter

An optional query parameter called `state` can be added to the code generation url. Any string can be used and will be sent on the callback url.

Authorization protocols provide a `state` parameter that allows you to restore the previous state of your application. The state parameter preserves some state objects set by the client in the Authorization request and makes it available to the client in the response.

### `resource_owner_type` parameter

> 📘 User or company wide access token
>
> Use this parameter to retrive, either a user-scoped token, or a company-wide token

An optional query parameter called `resource_owner_type` can be set to `company` to get a company Oauth token. A company OAuth token avoids problems tied to user permissions and the company's employee continuity and besides, it never expires.

```
https://api.factorialhr.com/oauth/authorize?client_id=>\<YOUR_CLIENT_ID>&redirect_uri=\<YOUR_REDIRECT_URI>&response_type=code&resource_owner_type=company
```

## Fetching your authorization code via the dashboard

> 🚧 Only available in the OAuth app list
>
> This option is only available in demo and client OAuth applications. Check [Create an OAuth2 application](https://apidoc.factorialhr.com/docs/create-a-new-oauth-application) to learn about the differences.

If you need an authorization token and you don't have a full oauth flow setup in your application code, consider using the authorize button in the oauth applications dashboard. It may be quicker for your use case, to retrieve your authorization code. This is particularly useful in cases of integrations with a single user like an external API.

Note that this button will  only give you authorization for a user access token

![](https://files.readme.io/045ee48-Screenshot_2021-12-20_at_18.38.34.png "Screenshot 2021-12-20 at 18.38.34.png")

## Further information

All the information required to build this URL is available in your OAuth application page, which you can access from the [list of OAuth2 applications](https://apidoc.factorialhr.com/docs/create-a-new-oauth-application)

Once the access is granted and the authorization code has been displayed to the user. Your integration is in condition to request its first access token.
