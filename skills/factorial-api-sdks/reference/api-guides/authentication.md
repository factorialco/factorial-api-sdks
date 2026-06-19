<!-- Vendored from https://apidoc.factorialhr.com/docs/authentication.md -->

# Authentication methods

The public API provides **two methods of authentication, API Keys and OAuth2**. The following sections provide information regarding each one and their intent.

## API Keys

API Key is the most straightforward method to start making requests to the public API

> ❗️ API Keys access is restricted to internal company developments
>
> **API Key usage for marketplace integrations is deprecated**.
>
> Marketplace integrations must use OAuth.
>
> Internal company integrations are still supported

<br />

## OAuth 2

OAuth2 is meant to make requests on behalf of a user or a company

> 📘 OAuth 2 is the required way to build marketplace integrations
>
> Contrary to API Keys, OAuth 2 brings a secure channel for company token exchange. Besides, it automatizes the UX, allowing company HR admins to grant access following a link
