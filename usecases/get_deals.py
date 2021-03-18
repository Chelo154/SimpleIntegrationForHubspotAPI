from interfaces.irepository import IRepository
from interfaces.idealconnector import IDealConnector
class GetDeals:

    user_repo: IRepository
    deals_repo: IRepository
    deals_api: IDealConnector

    def __init__(self, user_repo, deals_repo, deals_api):
        self.user_repo = user_repo
        self.deals_repo = deals_repo
        self.deals_api = deals_api

    def get_user_deals(self,username):

        user = self.user_repo.get_one(username)

        deals = self.deals_api.get_deals(user.access_token)

        self.deals_repo.insert_many(deals)

        return deals



pass

