from handlers.oauth_handler import OauthHandler
from usecases.manage_oauth_flow import ManageOAuthFlow
from serializers.user import UserJsonEncoder
from handlers.repository_handler import RepositoryHandler
import json


class OAuthController:

    def __init__(self):
        oauth = OauthHandler.get_oauth()
        user_repo = RepositoryHandler.get_user_repo()
        self.use_case = ManageOAuthFlow(oauth, user_repo)
        pass

    def get_authorization_url(self):
        return self.use_case.get_authorization_url()

    def fill_user_data(self, user_code):
        user = self.use_case.fill_user_data(user_code)
        return json.dumps(user, cls=UserJsonEncoder)


pass
