from interfaces.ioauth import IOAuth


class OauthHandler:

    oauth: IOAuth = None

    @staticmethod
    def set_oauth(oauth: IOAuth):
        OauthHandler.oauth = oauth

    @staticmethod
    def get_oauth():
        return OauthHandler.oauth


pass
