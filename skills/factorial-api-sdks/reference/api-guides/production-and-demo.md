<!-- Vendored from https://apidoc.factorialhr.com/docs/production-and-demo.md -->

# Environments: production and demo

Learn about Factorial's environments

Currently Factorial has 2 environments: `production` and `demo`:

* [Production](https://app.factorialhr.com/) is where all the clients use Factorial and interact with their real data\
  **API Base URL**: `api.factorialhr.com`
* [Demo](https://app.demo.factorial.dev/) is a separate cluster of servers for testing purposes. All the information can be deleted at any moment

  **API Base URL**: `api.eu2.demo.factorial.dev`

Both environments share the same code. Updates are deployed to both environments at the same time. Everything that works in a demo environment should work in production

> 📘 Switch production / demo servers in Reference
>
> Note you can select which sever you can use at the right in the [Reference section](/reference)
>
> ![](https://files.readme.io/6ed82a7906e7b0a60c514e00aae45653129ccedf2c63766495a4888786685efe-image.png)

> 🚧 Please, check that your credentails match the right environment
>
> You should use demo credentials in the demo server and production credentials in the production server
>
> Otherwise, you will get empty responses

## Getting a sandbox / demo environment

A sandbox/demo environment is available for testing integrations via public API calls. Developers can request provisioning with full access to a demo company where to test code before actually interacting with a production environment.

Contact your account manager or account executive to request this environment and get Oauth credentials for generating tokens.

<Callout icon="🚧" theme="warn">
  This environment is a demo and all information could be deleted at any moment.
</Callout>

## Requirements

After provisioning you should receive the user credentials for the demo company, along with the server URL
