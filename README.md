# Differences between oAuth1 and oAuth2 workflows

> These needs and steps may vary depending on the API you use

| oAuth1        | oAuth2       |
| ------------- | ------------ |
| **Needs:** CLIENT_KEY, CLIENT_SECRET, REQUEST_TOKEN_URL, BASE_AUTH_URL, ACCESS_TOKEN_URL | **Needs:** CLIENT_ID, CLIENT_SECRET, AUTHORIZATION_URL, REDIRECT_URI, TOKEN_URL |
| Create OAuth1Session instance using Client Key and Client Secret | Create OAuth2Session instance using Client Key and Redirect URI |
| Fetch Request Token to get a Key and Secret | |
| Extract OAuth/Request/Owner Token Key and OAuth/Request/Owner Token Secret | |
| Create Authorization URL | Create Authorization URL |
| Open the URL in browser, user gives permission | Open the URL in browser, user gives permission
| The API platform redirects to a URL (which contains the verifier code) or just displays a verifier code | The API platform redirects to a URL which contains the authorization response |
| Use the verifier code, client key, client secret, oAuth token key & oAuth token secret to regenerate OAuth1Session instance | |
| Fetch Access Token using ACCESS_TOKEN_URL | Fetch Token using Token URL, authorization response and client secret |
| Extract new OAuth/Request/Owner Token Key and OAuth/Request/Owner Token Secret | |
| In the end you have an oAuth1 session instance with Client Key, Client Secret, Token Key, Token Secret, Verifier | In the end you have an oAuth2 session instance with Access Token |

---

# Steps
> These instructions are intentionally vague. You will have to read the messages and troubleshoot.

1. Take *10 minutes* to skim through these pages, and find an interesting API 'endpoint' / data that you would like to get from this API. Make note of the permissions it requires.
    - https://developers.facebook.com/docs/graph-api/overview/
    - https://developers.facebook.com/docs/graph-api/reference

1. Take *10 mins* to look at the Facebook Login Flow Documentation:  https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow
    - What are your thoughts?
    - What do you think was important?

1. Look at the permissions document: https://developers.facebook.com/docs/facebook-login/permissions/
    - How does it connect to what you saw in graph-api reference?
    - *These are the values that you will use in `scope` variable to define what kind of private data access do you need from the user.*

1. In `facebook_oauth.py`, fill in values for `AUTHORIZATION_BASE_URL`, `TOKEN_URL`, `REDIRECT_URI` and `scope`, by either refering to the documentation or searching on Google. Note down what you just did.

1. Use `make_facebook_request` to make a request using Facebook's Graph API and retrieve this data

---

# More things to think about

1. How will you implement caching?
1. What will change in the code if you were to use it for other oAuth2 provider?
1. What will change in the code if you were to use an oAuth1 provider?
