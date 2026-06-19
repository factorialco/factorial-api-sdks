<!-- Vendored from https://apidoc.factorialhr.com/docs/first-steps.md -->

# First steps

Head over to the [demo environment](https://demo.factorialhr.com) and login with the admin user credentials provided. Then, on the same browser tab, open [https://api.eu2.demo.factorial.dev/oauth/applications](https://api.eu2.demo.factorial.dev/oauth/applications)

Create your credentials

![](https://files.readme.io/5c29848-image.png)

Remember to place your redirect URI

![](https://files.readme.io/8577685-image.png)

Then, on the same browser tab open `https://api.demo.factorial.dev/oauth/authorize?client_id=CLIENT_ID&redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=code` to generate an Oauth2 code. Don't forget to replace `CLIENT_ID` with the Oauth Id provisioned. This will take you to a page where you authorise the Oauth2 protocol.

<Image align="center" alt={1424} src="https://files.readme.io/ed4cda2f26b7005b6b45ebfd6490189bdd593e1b67ea108e0ca21ce3a1f134c1-Captura_de_pantalla_2024-09-03_a_las_16.46.43.png" title="Screenshot 2021-10-20 at 08.42.54.png" />

Once you have authorized the application, you will have all your data available

Data available

<Image align="center" width="500px" src="https://files.readme.io/a8e4ab3-image.png" />

Now you are ready to create your token. You can follow these steps in the[ Create an access token section](/docs/request-an-access-token) (remember to change the URL to [https://api.demo.factorial.dev/](https://api.demo.factorial.dev/))

Take note of the `code` generated.\
The next step is creating a user token, this can be done with a simple curl request.

```curl
curl -X POST 'https://api.demo.factorial.dev/oauth/token' -d 'client_id=CLIENT_ID&client_secret=CLIENT_SECRET&code=CODE&grant_type=authorization_code&redirect_uri=urn:ietf:wg:oauth:2.0:oob'
```

Don't forget to replace CLIENT\_ID with provisioned OAuth2 Id, CLIENT\_SECRET with provisioned OAuth2 secret and the generated CODE!\
Finally retrieve the token from the response and you're ready to make API calls. In the next page you have code examples of how to make request with this token.

> 📘 Api Call Examples
>
> Notice the examples in the next page have the production domain. Don't forget to change them to `https://api.demo.factorial.dev`

## First API call

To test the token, a simple and easy request is retrieving the information of the token. To do so perform the following curl request. Don't forget to replace TOKEN.

> 📘 This endpoint will give you access to your token owner information

```curl
curl https://api.demo.factorial.dev/api/2024-10-01/resources/api_public/credentials -H 'Authentication: Bearer TOKEN'
```

## Conclusion

All endpoints available in this docs are also available in the sandbox environment.

> 🚧 Don't forget to check the domain URL in your requests
