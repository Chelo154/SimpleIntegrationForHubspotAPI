from interfaces.ioauth import IOAuth
from adapters.oauth.oauth_hubspot_adapter import  OAuthHubspotAdapter


class OauthHandler:

    oauth: IOAuth = OAuthHubspotAdapter()

    @staticmethod
    def get_oauth():
        return OauthHandler.oauth


pass
