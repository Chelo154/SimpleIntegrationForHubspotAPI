from interfaces.ioauth import IOAuth
import requests


class OAuthHubspotAdapter(IOAuth):


    def __init__(self):
        self.url = 'https://app.hubspot.com/oauth/authorize'
        self.tokens_url = 'https://api.hubapi.com/oauth/v1/token'
        self.client_id = 'a0fa566f-6a52-4379-96af-d4e56e59f417'
        self.scope = 'contacts'
        self.redirect_uri = 'https://71d450ef4a37.ngrok.io/api/oauth/callback'
        self.client_secret = '51f551f9-a0b2-4a2f-a2e7-483b6155c146'

    def get_oauth_url(self):
        url = "{url}?client_id={client_id}&scope={scope}&redirect_uri={redirect_uri}"\
            .format(url=self.url, client_id=self.client_id, scope=self.scope, redirect_uri=self.redirect_uri)
        print(url)
        return url
        pass

    def get_tokens(self, code):

        form_data = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri' : self.redirect_uri,
            'code' : code
        }

        response = requests.post(url=self.tokens_url, data=form_data)

        response = response.json()

        print(response)

        refresh_token, access_token = response['refresh_token'], response['access_token']

        return access_token, refresh_token

    def refresh_token(self):
        pass

    def get_username(self, access_token):
        metadata_url = 'https://api.hubapi.com/oauth/v1/access-tokens/'

        complete_url = f'{metadata_url}{access_token}'

        response = requests.get(complete_url)

        response = response.json()

        username = response['user']

        return username


pass
