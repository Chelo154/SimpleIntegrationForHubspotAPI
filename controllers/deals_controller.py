from handlers.repository_handler import RepositoryHandler
from handlers.deal_api_handler import DealAPIHandler
from usecases.get_deals import GetDeals
from serializers.deal import DealJSONSerializer
import json


class DealsController:

    def __init__(self):
        user_repo = RepositoryHandler.get_user_repo()
        deal_repo = RepositoryHandler.get_deal_repo()
        api = DealAPIHandler.get_api()

        self.usecase = GetDeals(user_repo,deal_repo,api)
        pass

    def get_deals(self, username):
        deals = self.usecase.get_user_deals(username)
        return json.dumps(deals, cls=DealJSONSerializer)


pass
