<!-- Vendored from https://apidoc.factorialhr.com/docs/create-a-new-oauth-application.md -->

# Create an OAuth2 application

This page will help you create your first OAuth application

> 📘 Administrator permissions required
>
> In order to perform the following steps, you are gonna need to be logged in Factorial with an administrator account. Administrator permissions can be granted to multiple users from the [Company Settings](https://app.factorialhr.com/settings/users) section.

# Choose your environment

Steps might be different depending on [Environments: production and demo](https://apidoc.factorialhr.com/docs/production-and-demo)

## Demo / sandbox environment

1. Firstly, head over to your company repository of OAuth applications:

* [Demo link](https://api.eu2.demo.factorial.dev/oauth/applications)
* [Deprecated demo link](https://api.demo.factorial.dev/oauth/applications)

2. Click on `New application`and follow the creation process.

## Production environment

Developer partner or client?

**Clients can create their own OAuth application in production**. However, if you are **a developer partner,** or you want your integration to be used by more than one client, **you need to get the official OAuth application for production**

### Client - single company use

1. Firstly, head over to your company repository of OAuth applications:

* [Production](https://api.factorialhr.com/oauth/applications) (clients internal use only)

2. Click on `New application`and follow the creation process.

### Developer partners - multiple company use

<Callout icon="⚠️" theme="warn">
  **Factorial requires an official OAuth application for multi company use**

  However, please **[fill up the form](https://factorial.typeform.com/to/B2GJV4lT) to get the official OAuth application for production**

  You will find a more precise guide [**here**](https://apidoc.factorialhr.com/docs/oauth2-partner-guide)
</Callout>

# OAuth application details

## Redirect URI

The redirect URI the user will be redirected once it has granted permissions to your application to use information from Factorial's API.

> 🚧 Note about the Redirect URI
>
> Kindly note that the Redirect URI in the Oauth Application dashboard MUST correspond with the Redirect URI in the body of your request for a new access token

<Image border={false} src="https://files.readme.io/b57f611-Screenshot_2021-12-13_at_15.53.13.png" title="Screenshot 2021-12-13 at 15.53.13.png" />

## Confidentiality

Indicates whether you can keep the client secret secure and inaccessible to any malicious actor.

Web and mobile applications are not considered secure, as a malicious actor could use debuggers to discover the client secret. Server applications with secure firewalls and protected access are considered secure.

## Scopes

Scopes specify the exact level of access needed, ensuring OAuth tokens are restricted to only the required resources.

Here you should select the scopes your application will need to have access to. Refer to the [scopes documentation](https://apidoc.factorialhr.com/v2025-04-01/docs/scopes) to see the list of scopes available.
