<!-- Vendored from https://apidoc.factorialhr.com/docs/oauth-2.md -->

# OAuth 2

[OAuth](https://oauth.net/) is the de facto standard for authorization in our industry

OAuth in Factorial brings 2 types of access: user and company

### User tokens

In case of user tokens, all actions are authored on behalf of the user that creates the token. This means, is to be used mainly to submit actions the actual user is performing on an alternative interface or for.

In other words, the user needs to meet certain requirements to use OAuth 2:

* The user needs to be an employee inside Factorial interface
* The user needs to be on a permission group with the correspondent access to Factorial information. For example, if the user shouldn't see the contracts of other employees, their set of permissions should reflect this.
* Only admin users can access OAuth 2 repository and change the configuration

> ⚠️ User token live-time
>
> User tokens last from 1 hour. You will need to [refresh an user access token](https://apidoc.factorialhr.com/docs/refreshing-an-access-token)

### Company tokens

On the other hand, in case of company tokens, all actions are authored on behalf of the user's company. This kind of token is mainly used for sharing data without the user interaction.

> 👍 Company token live-time
>
> Company tokens don't expire. However, they can be [revoked](https://apidoc.factorialhr.com/docs/revoking-an-access-token) if needed

> 📘 Getting a user or company token?
>
> Learn how to retrive a user or company token at the [Request an OAuth 2 authorization code](https://apidoc.factorialhr.com/docs/request-an-authorization-code) section

## Steps to set up your OAuth 2 authentication

1. [Create a new OAuth application](/docs/create-a-new-oauth-application) and follow the creation process.

2. [Generate the OAuth 2 Authorization Code](/docs/request-an-authorization-code) in order to generate an OAuth2 Token.

3. [You will request an Access token ](/docs/request-an-access-token)

4. [Refresh an access token (in case you need it) ](/docs/refreshing-an-access-token)

## OAuth 2 token usage

The generated token is the credential for performing authenticated requests to Factorial. This token should be included in the `Authorization` header prefixed with the word `Bearer` and a separating space.\
Check the details on how to use your access token at [Request an access token](https://apidoc.factorialhr.com/docs/request-an-access-token)
