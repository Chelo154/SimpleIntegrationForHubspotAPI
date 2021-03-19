from interfaces.irepository import IRepository
from adapters.database.mongo_deal_adapter import MongoDealAdapter
from adapters.database.mongo_user_adapter import MongoUserAdapter


class RepositoryHandler:

    user_repo = MongoUserAdapter()

    deal_repo = MongoDealAdapter()

    @staticmethod
    def get_user_repo():
        return RepositoryHandler.user_repo

    @staticmethod
    def get_deal_repo():
        return RepositoryHandler.deal_repo


pass
