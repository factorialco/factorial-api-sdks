<!-- Vendored from https://apidoc.factorialhr.com/docs/api-keys.md -->

# API Keys

API Keys are a single string of symbols that must be added as a custom header on the request. The header name must be **x-api-key** and the key must be the value without any prefixes.

API keys have TOTAL ACCESS to everything and never expire. It's the creator's responsibility to generate them and store them securely.

> ❗️ DISCLAIMER
>
> API Key management requires full admin permissions as the resource itself allows for full admin access to the entire platform on behalf of the company and not of a user, therefore operations are not linked to any user in particular.

## Generation

An administrator should generate the KEY from the user interface (Factorial platform) following this <a href="https://help.factorialhr.com/how-to-create-api-keys-in-factorial" target="_blank">guide</a>

## Usage

The API Key should be passed in the request header as **x-api-key**

For example

```curl
curl --location --request GET 'Base URL' --header 'x-api-key: YOUR-API-KEY'
```

* Base URL: You can get these endpoints from our API Reference

<Image title="caputa de apidoc 1.png" alt={630} align="center" width="smart" src="https://files.readme.io/f525e2e-caputa_de_apidoc_1.png" />
