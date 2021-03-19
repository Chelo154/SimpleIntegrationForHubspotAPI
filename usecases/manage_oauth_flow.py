from interfaces.ioauth import IOAuth
from interfaces.irepository import IRepository
from domain.user import User


class ManageOAuthFlow:

    oauth: IOAuth
    user_repo: IRepository

    def __init__(self, oauth: IOAuth, user_repo: IRepository):
        self.oauth = oauth
        self.user_repo = user_repo
        pass

    def get_authorization_url(self):
        url = self.oauth.get_oauth_url()
        return url

    def fill_user_data(self, user_code):

        access_token, refresh_token = self.oauth.get_tokens(user_code)

        username = self.oauth.get_username(access_token)

        new_user = User(user_code, username, access_token, refresh_token)

        ok = self.user_repo.insert(new_user)

        if ok:
            return new_user
        else:
            return None

    def refresh_token(self,username):

        user = self.user_repo.get_one(username)

        access_token = self.oauth.refresh_token(user.refresh_token)

        self.user_repo.update(username, {'access_token': access_token})


pass

