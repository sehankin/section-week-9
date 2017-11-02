# This code is based on Steve Oney's example

from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix # special for Facebook!

import webbrowser
import json
from datetime import datetime

# for Facebook oAuth
APP_ID = ''
APP_SECRET = ''
AUTHORIZATION_BASE_URL = ''
TOKEN_URL = ''
REDIRECT_URI = ''
# REFRESH_URL = ''
scope = []

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
facebook_session = False

def make_facebook_request(url, params=None):
    # we use 'global' to tell python that we will be modifying this global variable
    global facebook_session

    if not facebook_session:
        start_facebook_session()

    if not params:
        params = {}

    return facebook_session.get(url, params=params)

def start_facebook_session():
    global facebook_session

    # 0 - get token from cache
    try:
        token = get_saved_token()
    except FileNotFoundError:
        token = None

    if token:
        facebook_initial_session = OAuth2Session(APP_ID, token=token)
        facebook_session = facebook_compliance_fix(facebook_initial_session)

    else:
        # 1 - session
        facebook_initial_session = OAuth2Session(APP_ID, redirect_uri=REDIRECT_URI, scope=scope)
        facebook_session = facebook_compliance_fix(facebook_initial_session)

        # 2 - authorization
        authorization_url, state = facebook_session.authorization_url(AUTHORIZATION_BASE_URL)
        print('Opening browser to {} for authorization'.format(authorization_url))
        webbrowser.open(authorization_url)

        # 3 - token
        redirect_response = input('Paste the full redirect URL here: ')
        token = facebook_session.fetch_token(TOKEN_URL, client_secret=APP_SECRET,
            authorization_response=redirect_response.strip())

        # 4 - save token
        save_token(token)

def get_saved_token():
    with open('token.json', 'r') as f:
        token_json = f.read()
        token_dict = json.loads(token_json)

        return token_dict

def save_token(token_dict):
    with open('token.json', 'w') as f:
        token_json = json.dumps(token_dict)
        f.write(token_json)


# TODO use make_facebook_request
