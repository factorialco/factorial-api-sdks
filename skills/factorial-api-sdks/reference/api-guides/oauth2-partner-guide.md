<!-- Vendored from https://apidoc.factorialhr.com/docs/oauth2-partner-guide.md -->

# Partner guide - Company token

## Main advantages

* It won't expire (has unlimited time)
* Anyone can use it (in case the company provides permission to connect with it)
* Has all permissions enabled (like an API KEY)

## Step 1 - Factorial creates an OAuth App for the partner

The whole process can be tested in a demo environment as well. So if this is your purpose, you can create your OAuth App in a demo environment [here](https://api.demo.factorial.dev/oauth/applications).

Production environment URL:  **`https://api.factorialhr.com`**

Demo environment URL:  **`https://api.demo.factorialhr.dev`**

In this initial step, Factorial will create your OAuth Application (only for production). To accomplish this, we require the partner to provide us with a **`redirect_uri`** to facilitate the OAuth App creation process. This `redirect_uri` is the endpoint in which the partner will receive the authorization code (this will be described in next step).

For Factorial to create your OAuth Application in Production, you can fill [this form](https://factorial.typeform.com/to/B2GJV4lT)

Upon creation of the OAuth App, we will share to the partner via Keeper the following information:

* `client_id`: The unique identifier for the app
* `client_secret`: The confidential code for secure communication

You will receive a link of Keeper that will get you to a page similar to the image below. If you want more info about the way about how Keeper so it you can visit this [link](https://docs.keeper.io/en/v/user-guides/one-time-share)

<Image align="center" width="300px" src="https://files.readme.io/132e862907a6dfba7f77e7d1d55a553e62aad94eca1cae9021d9a5d6f40af99d-image.png" />

## **Step 2 - Request authorization code:**

As part of the OAuth 2 protocol, the action should be started by the **Factorial user**. As we are asking a `company_token`, it is important that before clicking it a F**actorial admin is logged**. The link you should provide to your client is:

**`https://api.factorialhr.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&resource_owner_type=company`**

⚠️ **NOTE:** Before this initiative, Factorial already allowed users OAuth tokens. Right now the difference is that you will request a company token with this last parameter: **`resource_owner_type=company`**\
Without this parameter, you will request a user one.

Before granting an authorization code, the admin should authorize the permissions needed for your app.

The following picture is an example of how the grant screen displays:

![](https://files.readme.io/089e15aeae85ef23bf5d18bab8daa3a60d6169533ab2c719ea35bb7c3311ff37-image.png)

Upon clicking "Authorize," the user will be redirected to the **`redirect_uri`** with the generated code. An example of the resulting URL is as follows:

`https://embeddedapp.com?code=examplecode123`

Then the Partner app receives the code and initiates the process of obtaining an access token.

## Final Step:

To get a company access token from the partner app server you will need to do a POST request with the following parameters:

* `client_id` = the one we sent you when creating the OAuth App
* `client_secret` = the one we sent you when creating the OAuth App
* `code` = (the one you received previously with the GET request = codeexample123)
* `redirect_uri` = the one you sent us for us to create the OAuth App
* `grant_type` = authorization\_code

So it would look like the following url:\
`POST - https://api.factorialhr.com/oauth/token?client_id={client_id}&client_secret={client_secret}&code={code}&redirect_uri={redirect_uri}&grant_type=authorization_code`

And you will get a response like in the following picture:

![](https://files.readme.io/1f375e16b95dda8faef4e477d41f90b518422ed5ae5ce155861b3d02410cf589-image.png)

## Good Job!

Following these steps, you should now be able to make requests to our [API](https://apidoc.factorialhr.com/reference) using the **`access_token`** as a Bearer token for authorization.

Make your first request to the [credentials](https://apidoc.factorialhr.com/reference/get_api-2025-04-01-resources-api-public-credentials) endpoint to get information about the company which refers to the obtained token.

You will only had to add a header in your requests like this:

`Authorization: ‘Bearer {access-token}`

The following picture illustrates an example of how we use the credentials endpoint to retrieve information about the company with which we are authenticated through the token we got before:

![](https://files.readme.io/a4a250052a536e448cd32c9ae60ecce3c577d0ee692eff842ff82c22985e78b8-image.png)

Note: You can still use both API Keys and OAuth company token until you finish your migration and switch everyone to OAuth.

## Diagram flow

![](https://files.readme.io/32a00a4641778f4c20c22e37d317332f713e35bca0e1de227f9b8ec3f1edbf4b-image.png)
