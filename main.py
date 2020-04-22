import requests
import json
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth

# Define variables used for authentication
client_id = '80521d35b9a15c72b39ea3009e826dca0b2a7f47d7fdb5d31315e8620e478112'
client_secret = 'ff60bbd4d610b9ece66bfd508112fa453f47eb88673f8f2a10850fb7a206b5c1'
domain_prefix = 'hemaa'
username = 'thergautam12@gatech.edu'
password = 'thisisapassword'
grant_type = 'password'
token_url = 'https://accounts.tidyhq.com/oauth/token'

# Store in dictionary to pass as parameters
data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'domain_prefix': domain_prefix,
    'username': username,
    'password': password,
    'grant_type': grant_type
}


def get_contact_emails(email):
    auth_response = requests.post(token_url, data=data)

    # Request access token
    access_token = auth_response.json()['access_token']
    params = {'access_token': access_token}

    # Pull all contacts from TidyHQ
    contacts = requests.get("https://api.tidyhq.com/v1/contacts", params=params).json()

    id_nums = [contact['id'] for contact in contacts if contact['email_address'] == email]

    return id_nums, params


def valid_email(email_address):
    id_nums, params = get_contact_emails(email_address)
    if len(id_nums) > 0:
        for id in id_nums:
            # Get member status from TidyHQ
            mem_status = requests.get("https://api.tidyhq.com/v1/contacts/" + str(id) + "/memberships",
                                      params=params)

            if mem_status.status_code == 200:
                statuses = mem_status.json()
                for state in statuses:
                    # Confirm if member is active
                    if state['state'] == 'activated':
                        return True
            else:
                return False

    else:
        return False

