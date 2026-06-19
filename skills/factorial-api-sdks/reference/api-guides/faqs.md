<!-- Vendored from https://apidoc.factorialhr.com/docs/faqs.md -->

# FAQs

In this section you will find the frequently asked questions about our API.

## Authentication

* **Who, and how, can we obtain the API KEY?**\
  The administrators are responsible for creating the API KEY in the UI. The steps:\
  Click on "Configuration" on the left sidebar > click on the API option > Create API KEY.
* **Can I customize the API KEY information in Factorial?\&#xA;**&#x4E;o, the API KEY grants access to all information inside the platform and cannot be customized. The alternative is OAuth 2 to access customized data.
* **Does the API KEY expire?**\
  No, the API KEY won't expire.
* **OAuth2: What happens when I get "null" information using OAuth 2 in certain properties?\&#xA;**&#x54;his is because in your permission group (in the Factorial interface) you don't have access to this information. This permission has to be granted by the admin of the company from the UI.

## Rate limit

* There is a limit of 200 requests per minute for POST requests

<br />

## Sandbox development

In case you need a Sandbox development, contact your Account Manager, who will provide a Demo environment in Factorial for testing purposes.\
[Learn more about Factorial environments ](/docs/production-and-demo)

<br />

## Open API Specification (aka Swagger) file

Our [Reference](https://apidoc.factorialhr.com/reference/)  is built from an Open API Specification file. You can access it at:

[https://api.factorialhr.com/oas/](https://api.factorialhr.com/oas/)

You can also get a specific version, using the version query parameter:

[https://api.factorialhr.com/oas/?version=2025-04-01](https://api.factorialhr.com/oas/?version=2025-04-01)

## API status

Is the API failing? You get 500 errors. Check the current Factorial API status at:

[https://status.factorialhr.com/](https://status.factorialhr.com/)
